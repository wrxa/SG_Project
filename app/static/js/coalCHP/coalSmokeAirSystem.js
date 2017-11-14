$(document).ready(function () {
    unlockMeunCoalCHP();
    // 给保存按钮绑定事件
    initSmokeAirSystem();
    $('#submitData').bind('click', submitSmokeAirSystem);
});

function initSmokeAirSystem() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './initSmokeAirSystem',
        // data: { "planId": planId },
        async: false,
        error: function (request) {
            messageToast('error', '发生异常！',3000);
        },
        success: function (data) {
            assignmentForm(data.smokeAirSystem, "coalSmokeAirSystemForm");
        }
    });
}


// 提交保存页面所有表单数据
function submitSmokeAirSystem() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './formSmokeAirSystem',
        data: $('#coalSmokeAirSystemForm').serialize(),
        async: false,
        error: function (request) {
            messageToast('error', '发生异常！',3000);
        },
        success: function (data) {
            assignmentForm(data.newDatas, "coalSmokeAirSystemForm");
            messageToast('success', '燃煤热电联产-烟风系统数据保存成功！',3000);
        }
    });

}

