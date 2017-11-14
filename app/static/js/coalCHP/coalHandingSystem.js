$(document).ready(function () {
    unlockMeunCoalCHP();
    // 给保存按钮绑定事件
    initHandingSystem();
    $('#submitData').bind('click', submitHandingSystem);
});

function initHandingSystem() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './initHandingSystem',
        async: false,
        error: function (request) {
            messageToast('error', '发生异常！',3000);
        },
        success: function (data) {
            assignmentForm(data.handingSystem, "coalchpHandingSystem");
        }
    });
}


// 提交保存页面所有表单数据
function submitHandingSystem() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './formDataHandingSystem',
        data: $('#coalchpHandingSystem').serialize(),
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，保存失败！',3000);
        },
        success: function (data) {
            assignmentForm(data.newDatas, "coalchpHandingSystem");
            messageToast('success', '燃煤热电联产-输煤系统数据保存成功！',3000);
        }
    });

}

