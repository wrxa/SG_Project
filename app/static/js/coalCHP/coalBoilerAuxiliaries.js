$(document).ready(function () {
    unlockMeunCoalCHP();
    // 给保存按钮绑定事件
    initBoilerAuxiliaries();
    $('#submitData').bind('click', submitBoilerAuxiliaries);
});

function initBoilerAuxiliaries() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './initBoilerAuxiliaries',
        // data: { "planId": planId },
        async: false,
        error: function (request) {
            messageToast('error', '发生异常！',3000);
        },
        success: function (data) {
            assignmentForm(data.boilerAuxiliaries, "coalBoilerAuxiliariesForm");
        }
    });
}


// 提交保存页面所有表单数据
function submitBoilerAuxiliaries() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './formDataBoilerAuxiliaries',
        data: $('#coalBoilerAuxiliariesForm').serialize(),
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，保存失败！',3000);
        },
        success: function (data) {
            assignmentForm(data.newDatas, "coalBoilerAuxiliariesForm");
            messageToast('success', '燃煤热电联产-输煤系统数据保存成功！',3000);
        }
    });

}

