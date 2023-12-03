# 获取网页请求js
import requests

url = "http://127.0.0.1:9001/rendered_by_playwright/requests"

payload = {
    "url": "https://item.taobao.com/item.htm?spm=a21bo.jianhua.201876.1.5af92a89EP5tnC&id=36903311829&scm=1007.40986.276750.0&pvid=24189f20-0708-421d-980f-730cd37cfc05",
    "return_type": "screenshot",
    "is_block_image": False,
    "browser_type": "chromium",
    "timeout": 15,
    "cookies": [
        {
            "domain": ".taobao.com",
            "expiry": 1717156841,
            "name": "tfstk",
            "path": "/",
            "value": "e-3yXr4pQULrKk5s4o4U78c4pG48JPp6T2wQtXc3N82oVXV38xDBw8GHevuUnx5WeJt-LkkIHkDQdb1-DAGGP4t8Rwz8Jyv6CFT_wbUL-2WwSTlJnLJ4odT65bc8Jyv6CQHI83SiEw0n87xay1lr1w3bauyNR-7F8BNz4Rcu3SFxueEzIb2V8gJOpSbOg2nPKMruMSy6gIyMXbwAyMYteMIL2mF4CQdRvMEuMSy6gISdvuUTgROJw"
        },
        {
            "domain": ".taobao.com",
            "expiry": 1717156840,
            "name": "l",
            "path": "/",
            "value": "fBr0RUTqPHM1d7WbBOfaFurza77OSIRYYuPzaNbMi9fP9_1B5cfcW1EKGuT6C3GVF6-HR3SebziDBeYBqQAonxv9w8VMULkmndLHR35.."
        },
        {
            "domain": ".taobao.com",
            "expiry": 1717156839,
            "name": "isg",
            "path": "/",
            "sameSite": "None",
            "value": "BLGxbNKYcCxSJdw4bq3bWXrkwD1LniUQHFarNJPGrXiXutEM2-414F_Y2E7cab1I"
        },
        {
            "domain": ".taobao.com",
            "name": "cookie17",
            "path": "/",
            "sameSite": "None",
            "value": "UNQyQxMqUdx1nQ=="
        },
        {
            "domain": ".taobao.com",
            "name": "cookie1",
            "path": "/",
            "sameSite": "None",
            "value": "U+GWz3AsFiX+Qb4KVw17j51DAUP9jxfiN9Dd/omAUJ8="
        },
        {
            "domain": ".taobao.com",
            "name": "uc1",
            "path": "/",
            "sameSite": "None",
            "value": "cookie14=UoYelDaUBzi4aQ==&cookie15=U+GCWk/75gdr5Q==&pas=0&cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw==&existShop=false&cookie21=U+GCWk/7p4mBoUyS4E9C"
        },
        {
            "domain": ".taobao.com",
            "name": "_samesite_flag_",
            "path": "/",
            "sameSite": "None",
            "value": "true"
        },
        {
            "domain": ".taobao.com",
            "name": "_nk_",
            "path": "/",
            "sameSite": "None",
            "value": "tb80111606"
        },
        {
            "domain": ".taobao.com",
            "expiry": 1704225636,
            "name": "uc3",
            "path": "/",
            "sameSite": "None",
            "value": "id2=UNQyQxMqUdx1nQ==&lg2=VFC/uZ9ayeYq2g==&vt3=F8dD3CQ86yWj1Y1xLYc=&nk2=F5RNZTse5XZpwA=="
        },
        {
            "domain": ".taobao.com",
            "name": "sg",
            "path": "/",
            "sameSite": "None",
            "value": "641"
        },
        {
            "domain": ".taobao.com",
            "name": "_l_g_",
            "path": "/",
            "sameSite": "None",
            "value": "Ug=="
        },
        {
            "domain": ".taobao.com",
            "name": "cookie2",
            "path": "/",
            "sameSite": "None",
            "value": "107b800532eecbfa58297aa1b150eaa5"
        },
        {
            "domain": ".taobao.com",
            "expiry": 1704225636,
            "name": "uc4",
            "path": "/",
            "sameSite": "None",
            "value": "id4=0@UgP5GPE5h/vopPV87xcz+yFEcyRI&nk4=0@FY4GsvRHfRNKE+deKV5sJktJib8B"
        },
        {
            "domain": ".taobao.com",
            "expiry": 1733169636,
            "name": "tracknick",
            "path": "/",
            "sameSite": "None",
            "value": "tb80111606"
        },
        {
            "domain": ".taobao.com",
            "name": "existShop",
            "path": "/",
            "sameSite": "None",
            "value": "MTcwMTYwNDgzNg=="
        },
        {
            "domain": ".taobao.com",
            "name": "skt",
            "path": "/",
            "sameSite": "None",
            "value": "ef7bbcd14e3cba6e"
        },
        {
            "domain": ".taobao.com",
            "expiry": 1733169636,
            "name": "_cc_",
            "path": "/",
            "sameSite": "None",
            "value": "UtASsssmfA=="
        },
        {
            "domain": ".taobao.com",
            "expiry": 1704225636,
            "name": "lgc",
            "path": "/",
            "sameSite": "None",
            "value": "tb80111606"
        },
        {
            "domain": ".taobao.com",
            "name": "dnk",
            "path": "/",
            "sameSite": "None",
            "value": "tb80111606"
        },
        {
            "domain": ".taobao.com",
            "expiry": 1733169636,
            "name": "sgcookie",
            "path": "/",
            "sameSite": "None",
            "value": "E100ILy5qGW/gljD/XKs5neSdgHpFCtkMgpZjBLl5ISDXNZpWf16CW0TPM9kjQQukCJsOEdPC5bN98lkBZS2/c5dbHwnROOVjhmj/hWOf8IrOSgeGp9zWl4ki1AEAQkZTsoX"
        },
        {
            "domain": ".taobao.com",
            "name": "csg",
            "path": "/",
            "sameSite": "None",
            "value": "2e63aa70"
        },
        {
            "domain": ".taobao.com",
            "expiry": 1701864027,
            "name": "xlly_s",
            "path": "/",
            "sameSite": "None",
            "value": "1"
        },
        {
            "domain": ".taobao.com",
            "name": "cancelledSubSites",
            "path": "/",
            "sameSite": "None",
            "value": "empty"
        },
        {
            "domain": ".taobao.com",
            "expiry": 1709409636,
            "name": "t",
            "path": "/",
            "sameSite": "None",
            "value": "5471f2842b1f235c29cc326ce81f3dfa"
        },
        {
            "domain": ".taobao.com",
            "name": "unb",
            "path": "/",
            "sameSite": "None",
            "value": "3451510054"
        },
        {
            "domain": ".taobao.com",
            "expiry": 2332324824,
            "name": "cna",
            "path": "/",
            "sameSite": "None",
            "value": "11vzHZqQkVgCASe6tKSHLPTd"
        },
        {
            "domain": ".taobao.com",
            "name": "_tb_token_",
            "path": "/",
            "sameSite": "None",
            "value": "35515518b3feb"
        }
    ]
}
headers = {"content-type": "application/json"}

response = requests.request("POST", url, json=payload, headers=headers)

with open("page.png","wb") as f:
    f.write(response.content)