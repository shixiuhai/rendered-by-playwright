import requests
import json
url = "http://127.0.0.1:9001/rendered_by_playwright/requests"

payload = {
    "url": "https://www.xiaohongshu.com/explore/654ed925000000001b00c2bc",
    "browser_type": "chromium",
    "timeout": 8,
    "return_type": "handle_xhr",
    "handle_xhr_path": "/api/sns/web/v2/comment/page",
    "after_page_load_delay": 1
}
headers = {"content-type": "application/json"}

handle_xhr_response_json = requests.request("POST", url, json=payload, headers=headers).json()["handle_xhr"]

if len(handle_xhr_response_json)>0:
    resp_text = handle_xhr_response_json[0]
    resp_text = resp_text.replace("true","True").replace("false","False") # 将接口json数据中的 true和false转换为python可以解释的True和False
    resp_json = eval(resp_text)
    cursor=resp_json["data"]["cursor"]
    print(cursor)
    