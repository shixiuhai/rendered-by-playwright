# https://playwright.dev/docs/docker
FROM mcr.microsoft.com/playwright:v1.40.0-jammy
# 设置时区
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
# 创建工作文件夹
WORKDIR /rendered-by-playwright/rendered_by_playwright
# 把当前目录rendered_by_playwright里面内容 copy到/rendered-by-playwright/rendered_by_playwright文件夹内
COPY  ./rendered_by_playwright /rendered-by-playwright/rendered_by_playwright
# RUN apt update && apt install libnss3 libnspr4 libatk1.0-0 libatk-bridge2.0-0 libcups2 libdrm2 libxkbcommon0 libatspi2.0-0 libxcomposite1 libxdamage1 libxfixes3 libxrandr2 libgbm1 libasound2 -y
RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install
RUN chmod +x start.sh
# 使用 ENTRYPOINT 设置启动脚本
ENTRYPOINT ["bash", "./start.sh"]
