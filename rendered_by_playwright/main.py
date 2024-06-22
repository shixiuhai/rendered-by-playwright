import sys
sys.path.append("..")
import uvicorn
from rendered_by_playwright.utils.log import rendered_logger
from rendered_by_playwright.settings import API_WORKERS
if __name__ == "__main__":
    rendered_logger.info("渲染框架启动")
    uvicorn.run("rendered_by_playwright.api.rendered_api:app", host="0.0.0.0", port=9001, workers=API_WORKERS)

