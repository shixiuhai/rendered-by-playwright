from rendered_by_playwright.action_by_js.interface_class import InterfaceClass
from playwright_stealth import stealth_async
from rendered_by_playwright.enum_class.browser_type_enum import BrowserTypeEnum
from rendered_by_playwright.enum_class.return_type_enum import ReturnTypeEnum
from rendered_by_playwright.utils.log import rendered_logger
import platform
import asyncio
import re
from rendered_by_playwright.action_by_js.create_browser import Browser
from rendered_by_playwright.settings import CLOSED_WINDOWS
from rendered_by_playwright.utils.parse_rule import parse_regular, parse_replace
from rendered_by_playwright.utils.custom_error import CustomException

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
        创建一个 上下文本对象, 页面对象， 实现反扒配置，初始化窗口大小, 设置页面超时
        (browser, context, page)
        Returns:
            (object,object,object): _description_
        """
       
        browser_object = Browser()
        await browser_object.create()
        
        if self.browser_type == BrowserTypeEnum.CHROMIUM.value:
            browser = browser_object.chromium
        
        if self.browser_type == BrowserTypeEnum.FIREFOX.value:
            browser = browser_object.firefox
        
        if self.browser_type == BrowserTypeEnum.WEBKIT.value:
            browser = browser_object.webkit
    
        context_options = {
            "viewport": {"width": self.view_window_width, "height": self.view_window_height},
            "device_scale_factor":1, 
            "bypass_csp":True
        }
        if self.proxy:
            context_options['proxy'] = {'server': self.proxy}    
        if self.user_agent:
            context_options['user_agent'] = self.user_agent
        
        self.context = await browser.new_context(**context_options) # 创建上下文
        rendered_logger.info(f"======{self.url}请求开启了浏览器上下文======")
        await self.add_cookies_to_context() # 给上下文对象添加cookies

        self.page = await self.context.new_page() # 在这里执行其他操作，例如打开页面、截图等
        await self.add_anti_detection_js_to_page() # 注入反扒js
    
        self.page.set_default_timeout(self.timeout*1000) # 设置page超时
        
    async def add_anti_detection_js_to_page(self)->None:
        """_summary_
        给页面添加反爬取js
        Args:
            page (object): _description_
        Returns:
            None: _description_
        """
        await self.page.evaluate("""
            () => {
                Object.defineProperty(navigator, 'webdriver', {
                    get: () => false,
                });
            }
        """)
        await stealth_async(self.page)
    
    async def add_cookies_to_context(self)->None:
        """_summary_
        给页面添加cookies
        Args:
            context (object): _description_
            cookies (object): _description_
        Returns:
            None: _description_
        cookies [
            {"name":"a", "value":"b", "path":"c","domain":"d"},
            {"name":"a1", "value":"b1", "path":"c1","domain":"d1"}
        ]
        name: str
        value: str
        url: Optional[str] = None
        domain: Optional[str]
        path: Optional[str]
        expires: Optional[float] = None
        httpOnly: Optional[bool] = None
        secure: Optional[bool] = None
        sameSite: Optional[Literal["Lax", "None", "Strict"]] = None
        
        下面两个值必须同时出现
        sameSite 设置为 "None"。
        secure 设置为 true，即 cookies 只在使用 HTTPS 连接时发送。
        """
        
        if self.cookies:
            cookies_list = []
            for item in self.cookies:
                cookies_item = {}
                if item.name:
                    cookies_item["name"] = item.name
                if item.value:
                    cookies_item["value"] = item.value
                if item.url:
                    cookies_item["url"] = item.url
                if item.domain:
                    cookies_item["domain"] = item.domain
                if item.path:
                    cookies_item["path"] = item.path
                if item.expires:
                    cookies_item["expires"] = item.expires
                if item.httpOnly:
                    cookies_item["httpOnly"] = item.httpOnly
                if item.secure:
                    cookies_item["secure"] = item.secure
                if item.sameSite:
                    cookies_item["sameSite"] = item.sameSite
                cookies_list.append(cookies_item)
            await self.context.add_cookies(cookies_list)
    
    async def execute_js_to_page_after(self)->None:
        """_summary_
        将js注入到访问url后
        Args:
            page (object): _description_
        Returns:
            None: _description_
        """
        if self.js_script_after_page:
            rendered_logger.info(self.js_script_after_page)
            self.execut_js_response_after_page =  await self.page.evaluate(self.js_script_after_page) # 访问页面后执行js后，js返回的结果
          
    async def execute_js_to_page_before(self)->None:
        """_summary_
        将js注入到访问url前
        Args:
            page (object): _description_
        Returns:
            None: _description_
        """
        if self.js_script_before_page:
            await self.page.evaluate(self.js_script_before_page)
            
    async def goto_page(self)->None:
        """_summary_
        请求页面
        Args:
            page (object): _description_
            url (str): _description_
        """
        if self.url:
            if self.handle_xhr_path:
                self.page.on('response', self.handle_page_xhr_url) # 开启xhrl监听
            await self.page.goto(self.url, wait_until = self.wait_until) # 完全加载
            if self.after_page_load_delay:
                await asyncio.sleep(self.after_page_load_delay)
            self.is_handle_page_xhr_text_list_sucess = True # xhrl加载全部完成
    
    async def handle_page_xhr_url(self, response)->None:
        """_summary_
        勾取xhr请求
        Args:
            page (object): _description_
        """
        if self.handle_xhr_path:
            if self.handle_xhr_path in response.url and response.status==200:
                item_text = await response.text()
                self.handle_page_xhr_text_list.append(item_text)
    
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
    
    async def get_page_cookies(self)->list:
        """_summary_
        获取页面cookies
        Args:
            page (object): _description
        Returns:
            list: _description_
        """
        page_cookies = await self.context.cookies()
        return page_cookies
    
        
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
            await self.context.route(re.compile(r"(\.mp4)|(\.flv)|(\.m3u8)"), lambda route: route.abort())
    
    async def block_context_image(self)->None:
        """_summary_
        屏蔽页面图片加载
        Args:
            context (object): _description_
        Returns:
            None: _description_
        """
        if self.is_block_image:
            await self.context.route(re.compile(r"(\.png)|(\.jpg)|(webp)"), lambda route: route.abort())
            
    async def block_context_audio(self)->None:
        """_summary_
        屏蔽页面音频加载
        Args:
            context (object): _description_
        Returns:
            None: _description_
        """
        if self.is_block_audio:
            await self.context.route(re.compile(r"(\.wav)|(\.mp3)"), lambda route: route.abort())
    
    async def close_context(self)->None:
        """_summary_
            关闭context对象
            Args:
                context (object): _description_
            Returns:
                None: _description_
        """
        if self.context:
            await self.context.close()
            rendered_logger.info(f"成功关闭浏览器上下文: {self.url}")
        else:
            rendered_logger.warning("上下文对象不存在或已经关闭")
        
        
    async def main_requests(self, 
                            url:str, 
                            cookies:list, 
                            is_block_image:bool, 
                            is_block_video:bool,
                            is_block_audio:bool,  
                            js_script_after_page:str, 
                            js_script_before_page:str,
                            user_agent:str, 
                            timeout:int, 
                            max_retry_times:int, 
                            browser_type:str, 
                            return_type:str, 
                            view_window_width:int,
                            view_window_height:int, 
                            proxy:str, 
                            handle_xhr_path:str, 
                            wait_until:str, 
                            after_page_load_delay:float,
                            parse_by_regular:str,
                            parse_by_replace:str,
                            is_return_cookies:bool):
        """_summary_
        定义一个汇总请求方法
        url:str
        cookies:Optional[List[CookiesItem]] = None # cookies
        is_block_image:Optional[bool] = False # 是否屏蔽图片加载
        is_block_video:Optional[bool] = False # 是否屏蔽视频加载
        is_block_audio:Optional[bool] = False # 是否屏蔽音频加载
        js_script_after_page:Optional[str] = None # 访问页面后执行的js脚本
        js_script_before_page:Optional[str] = None # 访问页面前执行的js脚本
        user_agent:Optional[str] = None # 设置请求设备
        timeout:Optional[int] = 10 # 请求页面的超时时间
        max_retry_times:Optional[int] = 1 # 请求失败重试次数
        browser_type:Optional[str] = BrowserTypeEnum.CHROMIUM.value # 浏览器类型
        return_type:Optional[str] = ReturnTypeEnum.TEXT.value # 请求返回类型
        view_window_width:Optional[int] = 1920 # 默认开启浏览器的窗口宽
        view_window_height:Optional[int] = 1080 # 默认开启浏览器的窗口高
        proxy:Optional[str] = None # 浏览器代理
        handle_xhr_path:Optional[str] = None # 筛选动态页面加载xhr接口返回数据
        wait_until:Optional[str] = "load" # 页面完成加载的结拜
        after_page_load_delay:Optional[float] = None # 页面加载完成后延时时间
        parse_by_regular:Optional[str] = None # 正则对返回内容进行处理 传入方式 "*a|*b"
        parse_by_replace:Optional[str] = None # 通过replace对返回内容进行处理 "(a,b)|(c,d)"
        is_return_cookies:Optional[bool] = False # 设置是否在请求接口后返回tokens
        """
        self.url = url
        self.cookies = cookies
        self.is_block_image = is_block_image
        self.is_block_video = is_block_video
        self.is_block_audio = is_block_audio
        self.js_script_after_page = js_script_after_page
        self.js_script_before_page = js_script_before_page
        self.user_agent = user_agent
        self.timeout = timeout
        self.max_retry_times = max_retry_times
        self.browser_type = browser_type
        self.return_type = return_type
        self.view_window_width = view_window_width
        self.view_window_height = view_window_height
        self.proxy = proxy
        self.handle_xhr_path = handle_xhr_path
        self.wait_until = wait_until
        self.after_page_load_delay = after_page_load_delay
        self.parse_by_regular = parse_by_regular
        self.parse_by_replace = parse_by_replace
        self.is_return_cookies = is_return_cookies
        try:
            await self.create_browser_context_page() # 创建一个 浏览器对象, 上下文本对象, 页面对象， 实现反扒配置，初始化窗口大小
            await self.block_context_image() # 屏蔽上下文图片加载
            await self.block_context_video() # 屏蔽上下文视频加载
            await self.block_context_audio() # 屏蔽上下文音频加载
            await self.execute_js_to_page_before() # 在访问页面前执行js
            await self.goto_page() # 请求页面url
            await self.execute_js_to_page_after() # 在访问页面后执行js
            
            if self.return_type == ReturnTypeEnum.TEXT.value:
                result = await self.get_page_text()
                if self.parse_by_replace:
                    result = parse_replace(self.parse_by_replace, result)
                if self.parse_by_regular:
                    result = parse_regular(self.parse_by_regular, result)
                
            if self.return_type == ReturnTypeEnum.SCREENSHOT.value:
                result = await self.get_page_screenshot()
            
            if self.return_type == ReturnTypeEnum.HANDLEXHR.value:
                while self.is_handle_page_xhr_text_list_sucess is False:
                    await asyncio.sleep(0.15)
                result = self.handle_page_xhr_text_list
                if self.parse_by_replace:
                    for i in range(len(result)):
                        result[i] = parse_replace(self.parse_by_replace, result[i])
                if self.parse_by_regular:
                    for i in range(len(result)):
                        result[i]  = parse_regular(self.parse_by_regular, result[i])
                
            if self.return_type == ReturnTypeEnum.COOKIES.value:
                result = await self.get_page_cookies()
                
            if self.return_type == ReturnTypeEnum.JSRESPONSE.value:
                result = self.execut_js_response_after_page
                if self.parse_by_replace:
                    result = parse_replace(self.parse_by_replace, result)
                if self.parse_by_regular:
                    result = parse_regular(self.parse_by_regular, result)
            
            # 判断是否返回cookies
            if self.is_return_cookies:
                cookies = await self.get_page_cookies()
                return {
                    "code": 200,
                    "result": result,
                    "cookies": cookies
                }
            else:
                return {
                    "code": 200,
                    "result": result
                }
            
        except Exception as error:
            rendered_logger.error(f"请求出现错误,出现的错误是: {error}")
            return {
                "code":500,
                "result":error
            }
        finally:
            if CLOSED_WINDOWS:
                rendered_logger.info(f"======{self.url}请求关闭了浏览器上下文======")
                await self.close_context()

   
        
        
        

    
        
        
    