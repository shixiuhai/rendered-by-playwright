import requests
import json
url = "http://127.0.0.1:9001/rendered_by_playwright/requests"

def request_test():
    payload = {
        "url": "https://www.xiaohongshu.com/explore/6562c575000000001b00dd80",
        "browser_type": "chromium",
        "timeout": 6,
        "return_type": "handle_xhr",
        "handle_xhr_path": "/api/sns/web/v2/comment/page",
        "after_page_load_delay": 2
    }
    headers = {"content-type": "application/json"}

    result_json = requests.request("POST", url, json=payload, headers=headers).json()
    if result_json["code"] == 200:
        handle_xhr_response_json=result_json["handle_xhr"]
        if len(handle_xhr_response_json)>0:
            resp_text = handle_xhr_response_json[0]
            resp_text = resp_text.replace("true","True").replace("false","False") # 将接口json数据中的 true和false转换为python可以解释的True和False
            resp_json = eval(resp_text)
            # cursor=resp_json["data"]["cursor"] # 方法1
            cursor=resp_json.get("data","").get("cursor","")# 方法2 方法2可以配置默认值
            
            print(cursor)
    
if __name__ == "__main__":
    while True:
        request_test()