from abc import abstractclassmethod, ABCMeta
from rendered_by_playwright.enum_class.browser_type_enum import BrowserTypeEnum
from rendered_by_playwright.enum_class.return_type_enum import ReturnTypeEnum
import base64

class InterfaceClass(metaclass=ABCMeta):
    """_summary_
    定义一下需要实现的方法
    Args:
        metaclass (_type_, optional): _description_. Defaults to ABCMeta.
    """
    def __init__(self) -> None:
        self.browser = None
        self.context = None
        self.page = None
        self.url = None
        self.cookies = None
        self.is_block_image = False
        self.is_block_video = False
        self.is_block_audio = False
        self.user_agent = None
        self.js_script = None
        self.timeout = 20
        self.max_retry_times = 1
        self.browser_type = BrowserTypeEnum.CHROMIUM.value
        self.return_type = ReturnTypeEnum.TEXT.value
        self.view_window_width = 1920
        self.view_window_height = 1080
        self.proxy = None
        self.handle_xhr_path = None
        self.handle_page_xhr_text_list = []
        self.is_handle_page_xhr_text_list_sucess = False
        
    
    @abstractclassmethod
    async def create_browser_context_page(self):
        """_summary_
        创建一个 浏览器对象, 上下文本对象, 页面对象
        (browser, context, page)
        Returns:
            (object,object,object): _description_
        """
        pass
    
    @abstractclassmethod
    async def add_anti_detection_js_to_context(self)->None:
        """_summary_
        给上下文添加反爬取js
        Args:
            context (object): _description_
        Returns:
            None: _description_
        """
        pass
    
    @abstractclassmethod
    async def add_anti_detection_js_to_page(self)->None:
        """_summary_
        给页面添加反爬取js
        Args:
            page (object): _description_
        Returns:
            None: _description_
        """
        pass
    
    @abstractclassmethod
    async def add_cookies_to_context(self)->None:
        """_summary_
        给页面添加cookies
        Args:
            context (object): _description_
            cookies (object): _description_
        Returns:
            None: _description_
        """
        pass
    
    @abstractclassmethod
    async def execute_js_to_page(self)->None:
        """_summary_
        将js注入到页面执行
        Args:
            page (object): _description_
        Returns:
            None: _description_
        """
        pass
    
    @abstractclassmethod
    async def goto_page(self)->None:
        """_summary_
        请求页面
        Args:
            page (object): _description_
            url (str): _description_
        """
        
    @abstractclassmethod
    async def handle_page_xhr_url(self)->None:
        """_summary_
        勾取xhr请求
        Args:
            page (object): _description_
        """
    
    @abstractclassmethod
    async def get_page_text(self)->str:
        """_summary_
        获取页面文本
        Args:
            page (object): _description
        Returns:
            str: _description_
        """
        pass
    
    @abstractclassmethod
    async def get_page_screenshot(self)->bytes:
        """_summary_
        获取页面截图
        Args:
            page (object): _description_

        Returns:
            bytes: _description_
        """
        pass
    
    @abstractclassmethod
    async def block_context_video(self)->None:
        """_summary_
        屏蔽页面视频加载
        Args:
            context (object): _description_
        Returns:
            None: _description_
        """
        pass
    
    @abstractclassmethod
    async def block_context_image(self)->None:
        """_summary_
        屏蔽页面图片加载
        Args:
            context (object): _description_
        Returns:
            None: _description_
        """
        pass
    
    @abstractclassmethod
    async def block_context_audio(self)->None:
        """_summary_
        屏蔽页面音频加载
        Args:
            context (object): _description_
        Returns:
            None: _description_
        """
        pass
    
    @abstractclassmethod
    async def close_browser(self)->None:
        """_summary_
        关闭浏览器对象
        Args:
            page (object): _description_
        Returns:
            None: _description_
        """
        pass
    
    # @abstractclassmethod
    # def add_page_attributes(self, page:object)->None:
    #     """_summary_
    #     给页面添加基础属性
    #     Args:
    #         page (object): _description_
    #     Returns:
    #         None: _description_
    #     """
    #     pass
        
    