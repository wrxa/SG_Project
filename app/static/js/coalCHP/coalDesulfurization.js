$(document).ready(function () {
    unlockMeunCoalCHP();
    // 给保存按钮绑定事件
    initDesulfurization();
    $('#submitData').bind('click', submitDesulfurization);
});

function initDesulfurization() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './initDesulfurization',
        // data: { "planId": planId },
        async: false,
        error: function (request) {
            messageToast('error', '发生异常！',3000);
        },
        success: function (data) {
            assignmentForm(data.desulfurization, "coalDesulfurizationForm");
        }
    });
}


// 提交保存页面所有表单数据
function submitDesulfurization() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './formDesulfurization',
        data: $('#coalDesulfurizationForm').serialize(),
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，保存失败！',3000);
        },
        success: function (data) {
            assignmentForm(data.newDatas, "coalDesulfurizationForm");
            messageToast('success', '燃煤热电联产-脱硫脱硝数据保存成功！',3000);
        }
    });

}

