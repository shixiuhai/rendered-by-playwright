import sys
sys.path.append("..")
import uvicorn
import asyncio
from rendered_by_playwright.utils.log import rendered_logger
from rendered_by_playwright.api.rendered_api import app
from rendered_by_playwright.action_by_js.implementation_class import ImplementationClass
from rendered_by_playwright.settings import API_WORKERS
from rendered_by_playwright.action_by_js.create_browser import Browser

async def create_a():
    b = Browser()
    await b.create()
    c = Browser()
    await c.create()
if __name__ == "__main__":
    
    asyncio.run(create_a())