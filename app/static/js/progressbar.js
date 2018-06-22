var i = 0;
function mainFunc(){
    //把i发送到浏览器的js引擎线程里
    postMessage(1);
}
setTimeout(mainFunc,100);
// setInterval(mainFunc,10);