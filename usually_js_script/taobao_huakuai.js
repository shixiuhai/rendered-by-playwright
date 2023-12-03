//  淘宝滑块滑动js
// 获取滑块元素的函数
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

        await new Promise(resolve => setTimeout(resolve, 2000)); // 添加 1 秒的延迟
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
    sliderElement.dispatchEvent(new MouseEvent('mousedown', { bubbles: true, cancelable: true, composed: true }));
    await simulateMouseMovement(startX, startY, distances);
    sliderElement.dispatchEvent(new MouseEvent('mouseup', { bubbles: true, cancelable: true, composed: true }));
}

// 执行滑块移动的过程
moveSlider();
