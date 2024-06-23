# https://playwright.dev/docs/docker
FROM mcr.microsoft.com/playwright:v1.44.1-jammy
# 设置时区
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
# 创建工作文件夹
WORKDIR /rendered-by-playwright/rendered_by_playwright
# 把当前目录rendered_by_playwright里面内容 copy到/rendered-by-playwright/rendered_by_playwright文件夹内
COPY  ./rendered_by_playwright /rendered-by-playwright/rendered_by_playwright
RUN apt update && apt install python3-pip -y
# RUN mkdir -p /root/.pip && \
#     printf "[global]\nindex-url = https://mirrors.aliyun.com/pypi/simple/\n" > /root/.pip/pip.conf
RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install
RUN chmod +x start.sh
# 使用 ENTRYPOINT 设置启动脚本
ENTRYPOINT ["bash", "./start.sh"]
