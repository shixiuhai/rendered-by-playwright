// 代码结构化数据，借用GPT实现的合并
async () => {
    await new Promise((resolve) => {
        const distance = 300;  // 每次滚动的距离
        const delay = 200;  // 滚动之间的延迟时间

        function scrollToBottom() {
            const scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
            const scrollHeight = Math.max(document.documentElement.scrollHeight, document.body.scrollHeight);
            if (scrollTop + window.innerHeight >= scrollHeight) {
                resolve();
            } else {
                window.scrollBy(0, distance);
                setTimeout(scrollToBottom, delay);
            }
        }

        scrollToBottom();
    });
}

// 代码合并成一行的数据, 请求复制这个字符串
async () => { await new Promise((resolve) => { const distance = 300; const delay = 200; function scrollToBottom() { const scrollTop = document.documentElement.scrollTop || document.body.scrollTop; const scrollHeight = Math.max(document.documentElement.scrollHeight, document.body.scrollHeight); if (scrollTop + window.innerHeight >= scrollHeight) { resolve(); } else { window.scrollBy(0, distance); setTimeout(scrollToBottom, delay); } } scrollToBottom(); }); }

