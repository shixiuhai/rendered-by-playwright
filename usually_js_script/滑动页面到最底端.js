// 代码结构化数据，借用GPT实现的合并
async () => {
    await new Promise((resolve) => {
      const getRandomValue = (min, max) => Math.random() * (max - min) + min;
  
      // 随机滑动距离和延迟
      const distance = getRandomValue(200, 500);
      const delay = getRandomValue(100, 300);
  
      // 超时时间
      const timeout = 7000;
  
      // 记录开始时间
      let startTime = Date.now();
  
      function scroll() {
        const currentTime = Date.now();
        const elapsedTime = currentTime - startTime;
  
        // 获取滚动位置和页面高度
        const scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
        const scrollHeight = Math.max(document.documentElement.scrollHeight, document.body.scrollHeight);
  
        // 判断是否滚动到底部或超时
        if (scrollTop + window.innerHeight >= scrollHeight || elapsedTime >= timeout) {
          resolve();
        } else {
          // 滚动并设置下一次滚动的延迟
          window.scrollBy(0, distance);
          setTimeout(scroll, delay);
        }
      }
  
      // 初始调用滚动函数
      scroll();
    });
  };
  

// 代码合并成一行的数据, 请求复制这个字符串 有一定概率死循环，已经弃用
//async () => { await new Promise((resolve) => { const distance = 300; const delay = 200; function scrollToBottom() { const scrollTop = document.documentElement.scrollTop || document.body.scrollTop; const scrollHeight = Math.max(document.documentElement.scrollHeight, document.body.scrollHeight); if (scrollTop + window.innerHeight >= scrollHeight) { resolve(); } else { window.scrollBy(0, distance); setTimeout(scrollToBottom, delay); } } scrollToBottom(); }); }

// v2.0版本  timeout = 7000表示7秒钟后自动结束推出,防止js卡死在死循环
async () => { await new Promise((resolve) => { const getRandomValue = (min, max) => Math.random() * (max - min) + min; const distance = getRandomValue(200, 500), delay = getRandomValue(100, 300), timeout = 7000; let startTime = Date.now(); function scroll() { const currentTime = Date.now(); const elapsedTime = currentTime - startTime; const t = document.documentElement.scrollTop || document.body.scrollTop, e = Math.max(document.documentElement.scrollHeight, document.body.scrollHeight); t + window.innerHeight >= e || elapsedTime >= timeout ? resolve() : (window.scrollBy(0, distance), setTimeout(scroll, delay)); } scroll(); }); };

