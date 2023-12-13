from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse,StreamingResponse
from pydantic import BaseModel
from typing import List, Literal, Optional
from rendered_by_playwright.action_by_js.implementation_class import ImplementationClass
from rendered_by_playwright.utils.log import rendered_logger
from rendered_by_playwright.enum_class.browser_type_enum import BrowserTypeEnum
from rendered_by_playwright.enum_class.return_type_enum import ReturnTypeEnum
from io import BytesIO

class CookiesItem(BaseModel):
    name: str
    value: str
    url: Optional[str] = None
    domain: Optional[str]
    path: Optional[str]
    expires: Optional[float] = None
    httpOnly: Optional[bool] = None
    secure: Optional[bool] = None
    sameSite: Optional[Literal["Lax", "None", "Strict"]] = None

class ResquestsData(BaseModel):
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
    
    
app = FastAPI()
# 创建一个路由，接受 POST 请求
@app.post("/rendered_by_playwright/requests",  response_model=None)
async def requests(data: ResquestsData):
    """
    接收一个包含在请求体中的 JSON 数据
    :param data: 一个字典，包含 JSON 数据
    :return: 返回接收到的数据
    """
    try:
        url = data.url
        cookies = data.cookies
        is_block_image = data.is_block_image
        is_block_video = data.is_block_video
        is_block_audio = data.is_block_audio
        js_script_after_page = data.js_script_after_page
        js_script_before_page = data.js_script_before_page
        user_agent = data.user_agent
        timeout = data.timeout
        max_retry_times = data.timeout
        browser_type = data.browser_type
        return_type = data.return_type
        view_window_width = data.view_window_width
        view_window_height = data.view_window_height
        proxy = data.proxy
        handle_xhr_path = data.handle_xhr_path
        wait_until = data.wait_until
        after_page_load_delay = data.after_page_load_delay
        parse_by_regular = data.parse_by_regular
        parse_by_replace = data.parse_by_replace
        
        implementation_class = ImplementationClass()
        
        result = await implementation_class.\
            main_requests(
                            url=url, 
                            cookies=cookies,
                            is_block_image=is_block_image,
                            is_block_video=is_block_video, 
                            is_block_audio=is_block_audio,
                            js_script_after_page=js_script_after_page,
                            js_script_before_page=js_script_before_page,
                            user_agent=user_agent, 
                            timeout=timeout,
                            max_retry_times=max_retry_times, 
                            browser_type=browser_type,
                            return_type=return_type, 
                            view_window_width=view_window_width, 
                            view_window_height=view_window_height,
                            proxy=proxy,
                            handle_xhr_path=handle_xhr_path,
                            wait_until=wait_until,
                            after_page_load_delay=after_page_load_delay,
                            parse_by_regular=parse_by_regular,
                            parse_by_replace=parse_by_replace)
            
        rendered_logger.info(f"动态渲染请求成功,请求的url是: {data.url}")
        if return_type == ReturnTypeEnum.TEXT.value:
            return JSONResponse(
                content={
                            "code": 200,
                            "message":"成功",
                            f"{ReturnTypeEnum.TEXT.value}":result
                })
        
        if return_type == ReturnTypeEnum.HANDLEXHR.value:
            return JSONResponse(
                content={
                            "code": 200,
                            "message":"成功",
                            f"{ReturnTypeEnum.HANDLEXHR.value}":result
                })
            
        if return_type == ReturnTypeEnum.COOKIES.value:
            return JSONResponse(
                content={
                            "code": 200,
                            "message":"成功",
                            f"{ReturnTypeEnum.COOKIES.value}":result
                })
            
        if return_type == ReturnTypeEnum.SCREENSHOT.value:
            return StreamingResponse(BytesIO(result), media_type="image/png")
        
        if return_type == ReturnTypeEnum.JSRESPONSE.value:
            return JSONResponse(
                content={
                            "code": 200,
                            "message":"成功",
                            f"{ReturnTypeEnum.JSRESPONSE.value}":result
                })
    
    except Exception as error:
        rendered_logger.error(f"动态渲染请求出现错误, 请求的url是: {data.url}, 错误内容是{error}")
        return JSONResponse(
                content={
                            "code": 500,
                            "message": error
                })
        
       
        
   
# if __name__ == "__main__":
#     pass
#     # rendered_logger.info("你好") # 日志打印测试
#     uvicorn.run(app, host="127.0.0.1", port=9001)


