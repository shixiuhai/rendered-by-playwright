//  过淘宝滑块滑动js
// 获取滑块元素的函数
// https://www.cnblogs.com/yizhiyan/p/11286028.html js过淘宝
function getSliderElement() {
    return document.evaluate('//*[@id="nc_1_n1z"]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
}

// 模拟鼠标移动的函数
async function simulateMouseMovement(startX, startY, distances) {
    const sliderElement = getSliderElement();

    for (let i = 0; i < distances.length; i++) {
        const distance = distances[i];

        startX += distance;

        sliderElement.dispatchEvent(
            new MouseEvent('mousemove', { clientX: startX, clientY: startY, bubbles: true, cancelable: true, composed: true })
        );

        // Use await with setTimeout inside the loop
        await new Promise(resolve => setTimeout(resolve, 2000)); // Adding a 2-second delay
    }
}

// 执行滑块移动的函数
async function moveSlider() {
    const sliderElement = getSliderElement();
    const sliderRect = sliderElement.getBoundingClientRect();
    const startX = sliderRect.x + sliderRect.width / 2;
    const startY = sliderRect.y + sliderRect.height / 2;

    // 定义滑动比例
    const ratios = [3, 2, 1, 3, 1];

    // 计算滑动距离
    const totalDistance = 300;
    const distances = ratios.map(ratio => (ratio / ratios.reduce((a, b) => a + b, 0)) * totalDistance);

    // 开始滑动
    sliderElement.dispatchEvent(new MouseEvent('mousedown', { bubbles: true, cancelable: true, composed: true })); // 按下鼠标左键
    await simulateMouseMovement(startX, startY, distances);
    sliderElement.dispatchEvent(new MouseEvent('mouseup', { bubbles: true, cancelable: true, composed: true })); // 放下鼠标左键
}

// 执行滑块移动的过程
moveSlider();




// 第二部分
const iframe = document.querySelector('//*[@id="sufei-dialog-content"]');
const iframeContent = iframe.contentDocument || iframe.contentWindow.document;

// 在加载前刷新页面
// location.reload(true);

// 获取滑块元素的函数
function getSliderElement() {
    return iframeContent.evaluate('//*[@id="nc_1_n1z"]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
}

// 模拟鼠标移动的函数
async function simulateMouseMovement(startX, startY, distances) {
    const sliderElement = getSliderElement();

    for (let i = 0; i < distances.length; i++) {
        const distance = distances[i];

        startX += distance;

        sliderElement.dispatchEvent(
            new MouseEvent('mousemove', { clientX: startX, clientY: startY, bubbles: true, cancelable: true, composed: true })
        );
        console.log("滑动一次" + (i + 1));

        // Use await with setTimeout inside the loop
        await new Promise(resolve => setTimeout(resolve, 600)); // Adding a 2-second delay
    }
}

// 执行滑块移动的函数
async function moveSlider() {
    const sliderElement = getSliderElement();
    const sliderRect = sliderElement.getBoundingClientRect();
    const startX = 0;
    const startY = 0;
    console.log("开始滑动坐标" + startX);
    console.log("结束滑动坐标" + startY);

    // 定义滑动比例
    const ratios = [1, 3, 2, 1, 4, 5, 2]; // 请根据实际情况调整

    // 计算滑动距离
    const totalDistance = 310;
    const distances = ratios.map(ratio => (ratio / ratios.reduce((a, b) => a + b, 0)) * totalDistance);
    console.log(distances);

    // 开始滑动
    sliderElement.dispatchEvent(new MouseEvent('mousedown', { bubbles: true, cancelable: true, composed: true })); // 按下鼠标左键
    await simulateMouseMovement(startX, startY, distances);
    sliderElement.dispatchEvent(new MouseEvent('mouseup', { bubbles: true, cancelable: true, composed: true })); // 放下鼠标左键
}

// 执行滑块移动的过程
await moveSlider();

