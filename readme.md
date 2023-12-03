## rendered-by-playwright项目
### api接口文档
* https://console-docs.apipost.cn/preview/73fc7c6d53b316e0/6bf3e4ff47acf074
### 项目docker部署到ubuntu
* linux系统安装docker
* git拉取项目 
* 运行 cd rendered_by_playwright && bash build.sh
### 1. 项目初衷
* 实现一个类似splash动态渲染通过api接口实现
* 实现一个类似selenium将逐步操作方法通过接口请求实现
* 实现基于docker分布式部署
* 实现无头模式的高效率渲染
### 2. 内联相关技术
* api接口通过fastapi实现
* 分布式部署基于docker实现
* 自动化框架选择playwright
### 3. 接口相关
* 接口通过apiPost实现描述
### 4. 接口类型
* 第一类类似splash可以直接通过接口进行动态页面的渲染返回渲染页面文本, 可以通过提交js脚本实现一系列内置操作流程，最终返回页面文本，添加一个类似splash的调试页面(已开发)

* 第二类类似selenium可以通过接口传递创建窗口，通过接口发送xpath和css选择器操作，简言之封装了playwright常用操作方法基于接口实现的方式(构思考虑中)

