docker stop rendered_by_playwright_project
docker rm  rendered_by_playwright_project
docker build -t rendered_by_playwright .
docker run -itd --name rendered_by_playwright_project -p 9001:9001 rendered_by_playwright /bin/bash