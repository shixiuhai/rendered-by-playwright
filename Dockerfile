FROM robd003/python3.10
# 创建工作文件夹
WORKDIR /rendered-by-playwright/rendered_by_playwright
# 把当前目录rendered_by_playwright copy到/rendered-by-playwright/rendered_by_playwright
COPY  ./rendered_by_playwright /rendered-by-playwright/rendered_by_playwright
RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install
RUN chmod +x start.sh
# 使用 ENTRYPOINT 设置启动脚本
ENTRYPOINT ["bash", "./start.sh"]