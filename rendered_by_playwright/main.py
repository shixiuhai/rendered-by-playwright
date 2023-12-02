import sys
sys.path.append("..")
import uvicorn
import asyncio
from rendered_by_playwright.utils.log import rendered_logger
from rendered_by_playwright.api.rendered_api import app
from rendered_by_playwright.action_by_js.implementation_class import ImplementationClass

if __name__ == "__main__":
    pass
    # rendered_logger.info("你好") # 日志打印测试
    uvicorn.run(app, host="127.0.0.1", port=9001)
    # asyncio.run(main())
    