from playwright.async_api import async_playwright
from rendered_by_playwright.settings import HEADLESS
import platform
import asyncio
os_name = platform.system()
if os_name == "Windows":
    HEADLESS = False

class Browser:
    chromium = None
    firefox = None
    webkit = None

    async def create(self):
            if Browser.chromium is None:
                Browser.chromium = await self.create_chromium_browser()
            if not Browser.chromium.is_connected():
                Browser.chromium = await self.create_chromium_browser()
            
            if Browser.firefox is None:
                Browser.firefox = await self.create_firefox_browser()
            if not Browser.firefox.is_connected():
                Browser.firefox = await self.create_firefox_browser()
            
            if Browser.webkit is None:
                Browser.webkit = await self.create_webkit_browser()
            if not Browser.webkit.is_connected():
                Browser.webkit = await self.create_webkit_browser()
        
    async def create_chromium_browser(self):
        p = await async_playwright().start()  # 初始化 Playwright
        browser_options = {
            'headless': HEADLESS,
            'args': ['--no-sandbox', '--disable-gpu'],
            # 'timeout': 10000
            # 'slow_mo': 50,
            # 'devtools': True,
            # 'ignore_default_args': True,
            # 'device': 'iPhone 8'  # 模拟 iPhone 8
        }
        return await p.chromium.launch(**browser_options) # 启动 Chromium 浏览器
        # context = await Browser.chromium.new_context()
        # page = await context.new_page()
        # await page.goto("http://www.baidu.com")
        # await asyncio.sleep(10)
    
    async def create_firefox_browser(self):
        p = await async_playwright().start()  # 初始化 Playwright
        browser_options = {
            'headless': HEADLESS,
            'args': ['--no-sandbox', '--disable-gpu'],
            # 'timeout': self.timeout*1000
            # 'slow_mo': 50,
            # 'devtools': True,
            # 'ignore_default_args': True,
            # 'device': 'iPhone 8'  # 模拟 iPhone 8
        }
        return await p.firefox.launch(**browser_options) # 启动 firefox 浏览器
        
    async def create_webkit_browser(self):
        p = await async_playwright().start()  # 初始化 Playwright
        browser_options = {
            'headless': HEADLESS,
            'args': ['--no-sandbox', '--disable-gpu'],
            # 'timeout': self.timeout*1000
            # 'slow_mo': 50,
            # 'devtools': True,
            # 'ignore_default_args': True,
            # 'device': 'iPhone 8'  # 模拟 iPhone 8
        }
        return await p.webkit.launch(**browser_options) # 启动 webkit 浏览器

