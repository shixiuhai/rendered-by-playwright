from rendered_by_playwright.action_by_js.interface_class import InterfaceClass
from playwright.async_api import async_playwright
from rendered_by_playwright.enum_class.browser_type_enum import BrowserTypeEnum
from rendered_by_playwright.enum_class.return_type_enum import ReturnTypeEnum
from rendered_by_playwright.utils.log import rendered_logger
import asyncio
import tempfile
import base64

class ImplementationClass(InterfaceClass):
    """_summary_
    实现上面抽象类定义的方法
    Args:
        InterfaceClass (_type_): _description_
    """
    def __init__(self) -> None:
        super().__init__()
    
    async def create_browser_context_page(self):
        """_summary_
        创建一个 浏览器对象, 上下文本对象, 页面对象， 实现反扒配置，初始化窗口大小, 设置页面超时
        (browser, context, page)
        Returns:
            (object,object,object): _description_
        """
        p = await async_playwright().start()  # 初始化 Playwright
        

        if self.browser_type == BrowserTypeEnum.CHROMIUM.value:
            self.browser = await p.chromium.launch(headless=False) # 启动 Chromium 浏览器
        if self.browser_type == BrowserTypeEnum.FIREFOX.value:
            self.browser = await p.firefox.launch(headless=True) # 启动 firefox 浏览器
        if self.browser_type == BrowserTypeEnum.WEBKIT.value:
            self.browser = await p.webkit.launch(headless=True) # 启动 webkit 浏览器
    
        self.context = await self.browser.new_context() # 创建新的上下文
        # await self.add_anti_detection_js_to_context(self.context) # 添加反爬取js

        self.page = await self.context.new_page() # 在这里执行其他操作，例如打开页面、截图等
        await self.add_anti_detection_js_to_page()
        await self.page.set_viewport_size({"width": self.view_window_width, "height": self.view_window_height})
        self.page.set_default_timeout(self.timeout*1000) # 设置page超时
            
            
    
    async def add_anti_detection_js_to_context(self)->None:
        """_summary_
        给页面添加反爬取js
        Args:
            context (object): _description_
        Returns:
            None: _description_
        """
        await self.context.add_init_script("""
            () => {
                Object.defineProperty(navigator, 'webdriver', {
                    get: () => false,
                });
            }
        """)
        
    async def add_anti_detection_js_to_page(self)->None:
        """_summary_
        给页面添加反爬取js
        Args:
            page (object): _description_
        Returns:
            None: _description_
        """
        self.page.evaluate("""
            () => {
                Object.defineProperty(navigator, 'webdriver', {
                    get: () => false,
                });
            }
        """)
    
    async def add_cookies_to_context(self)->None:
        """_summary_
        给页面添加cookies
        Args:
            context (object): _description_
            cookies (object): _description_
        Returns:
            None: _description_
        cookies [
            {"name":"a", "value":"b", "path":"c"},
            {"name":"a1", "value":"b1", "path":"c1"}
        ]
        """
        if self.cookies:
            await self.context.add_cookies(self.cookies)
    
    async def execute_js_to_page(self)->None:
        """_summary_
        将js注入到页面执行
        Args:
            page (object): _description_
        Returns:
            None: _description_
        """
        if self.js_script:
            await self.page.evaluate(self.js_script)
            
    async def goto_page(self)->None:
        """_summary_
        请求页面
        Args:
            page (object): _description_
            url (str): _description_
        """
        if self.url:
            await self.page.goto(self.url, wait_until='load')
        
    async def get_page_text(self)->str:
        """_summary_
        获取页面文本
        Args:
            page (object): _description_
        Returns:
            str: _description_
        """
        page_content = await self.page.content()
        return page_content
    
    async def set_context_user_agent(self)->None:
        if self.user_agent:
            extra_headers = {
                "User-Agent": self.user_agent
            }
            self.context.set_extra_http_headers(extra_headers) 
        
    async def get_page_screenshot(self)->bytes:
        """_summary_
        获取页面截图
        Args:
            page (object): _description_

        Returns:
            bytes: _description_
        """
        screenshot_data = await self.page.screenshot() # 截取页面截图
        return screenshot_data
        # base64_image = base64.b64encode(screenshot_data).decode('utf-8') # base64编码
        # return base64_image
        # # 创建临时文件
        # with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
        #     temp_file.write(screenshot_data)
        # # 获取临时文件的路径
        # temp_file_path = temp_file.name

    
    async def block_context_video(self)->None:
        """_summary_
        屏蔽页面视频加载
        Args:
            context (object): _description_
        Returns:
            None: _description_
        """
        if self.is_block_video:
            self.context.route('**/*.flv', lambda route: route.abort())
            self.context.route('**/*.m3u8', lambda route: route.abort())
            self.context.route('**/*.mp4', lambda route: route.abort())
    
    async def block_context_image(self)->None:
        """_summary_
        屏蔽页面图片加载
        Args:
            context (object): _description_
        Returns:
            None: _description_
        """
        if self.is_block_image:
            self.context.route('**/*.png', lambda route: route.abort())
            self.context.route('**/*.jpg', lambda route: route.abort())
            self.context.route('**/*.jpeg', lambda route: route.abort())
        # self.context.route('**/*.{png,jpg,jpeg}', lambda route: route.abort())
        
    async def block_context_audio(self)->None:
        """_summary_
        屏蔽页面音频加载
        Args:
            context (object): _description_
        Returns:
            None: _description_
        """
        if self.is_block_audio:
            self.context.route('**/*.mp3', lambda route: route.abort())
            self.context.route('**/*.wav', lambda route: route.abort())
       
    async def close_browser(self)->None:
        """_summary_
        关闭浏览器对象
        Args:
            page (object): _description_
        Returns:
            None: _description_
        """
        await self.browser.close() # 关闭浏览器对象 
        
    async def main_requests(self, url:str, cookies:list, is_block_image:bool, is_block_video:bool,
                            is_block_audio:bool,  js_script:str, user_agent:str, timeout:int, 
                            max_retry_times:int, browser_type:str, return_type:str, view_window_width:int,
                            view_window_height:int):
        """_summary_
        定义一个汇总请求方法
        url:str
        cookies:Optional[List[CookiesItem]] = None # cookies
        is_block_image:Optional[bool] = False # 是否屏蔽图片加载
        is_block_video:Optional[bool] = False # 是否屏蔽视频加载
        is_block_audio:Optional[bool] = False # 是否屏蔽音频加载
        js_script:Optional[str] = None # 执行的js脚本
        user_agent:Optional[str] = None # 设置请求设备
        timeout:Optional[int] = 20 # 请求页面的超时时间
        max_retry_times:Optional[int] = 1 # 请求失败重试次数
        browser_type:Optional[str] = "chromium" # 浏览器类型
        return_type:Optional[str] = "text" # 请求返回类型
        view_window_width:Optional[int] = 1920 # 默认开启浏览器的窗口宽
        view_window_height:Optional[int] = 1080 # 默认开启浏览器的窗口高
        """
        self.url = url
        self.cookies = cookies
        self.is_block_image = is_block_image
        self.is_block_video = is_block_video
        self.is_block_audio = is_block_audio
        self.js_script = js_script
        self.user_agent = user_agent
        self.timeout = timeout
        self.max_retry_times = max_retry_times
        self.browser_type = browser_type
        self.return_type = return_type
        self.view_window_width = view_window_width
        self.view_window_height = view_window_height
        try:
            await self.create_browser_context_page() # 创建一个 浏览器对象, 上下文本对象, 页面对象， 实现反扒配置，初始化窗口大小
            # return (self.browser, self.context, self.page)
            await self.block_context_image() # 屏蔽上下文图片加载
            await self.block_context_video() # 屏蔽上下文视频加载
            await self.block_context_audio() # 屏蔽上下文音频加载
            # await self.add_cookies_to_context() # 给上下文对象添加cookies
            await self.goto_page() # 请求页面url
            if self.return_type == ReturnTypeEnum.TEXT.value:
                result = await self.get_page_text()
            if self.return_type == ReturnTypeEnum.IMAGE.value:
                result = await self.get_page_screenshot()
            return result
        except Exception as error:
            rendered_logger.error(f"请求出现错误,出现的错误是: {error}")
        finally:
            pass
            # await self.close_browser()
   
        
        
        

    
        
        
    