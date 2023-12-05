from playwright.async_api import async_playwright
from playwright_stealth import stealth_async
import time
import asyncio
async def aa():
    p = await async_playwright().start()  # 初始化 Playwright
            
    launch_options = {
        'headless': False,
        'args': ['--no-sandbox', '--disable-gpu'],
        # 'timeout': self.timeout*1000
        # 'slow_mo': 50,
        # 'devtools': True,
        # 'ignore_default_args': True,
        # 'device': 'iPhone 8'  # 模拟 iPhone 8
    }
    t1 = time.time()
    browser = await p.chromium.launch(**launch_options) # 启动 Chromium 浏览器
    t2 = time.time()
    print(f"打开浏览器耗费时间{t2-t1}")
    context1 = await browser.new_context()
    t3 = time.time()
    print(f"打开页面context1耗费时间{t3-t2}")
    context2 = await browser.new_context()
    t4 = time.time()
    print(f"打开页面context2耗费时间{t4-t3}")
    page = await context1.new_page()
    page1 = await context2.new_page()
    t5 = time.time()
    print(f"打开页面page耗费时间{t5-t4}")
    await page.goto("http://www.taobao.com")
    t6 = time.time()
    await browser.close()
    print(f"访问页面耗费时间{t6-t5}")
    await asyncio.sleep(1000)

if __name__ == "__main__":
    asyncio.run(aa())
    
    