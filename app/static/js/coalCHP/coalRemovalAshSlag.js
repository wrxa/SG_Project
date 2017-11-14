$(document).ready(function () {
    unlockMeunCoalCHP();
    // 给保存按钮绑定事件
    initRemovalAshSlag();
    $('#submitData').bind('click', submitRemovalAshSlag);
});

function initRemovalAshSlag() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './initRemovalAshSlag',
        // data: { "planId": planId },
        async: false,
        error: function (request) {
            messageToast('error', '发生异常！',3000);
        },
        success: function (data) {
            // alert(data.removalAshSlag)
            assignmentForm(data.removalAshSlag, "coalRemovalAshSlagForm");
        }
    });
}


// 提交保存页面所有表单数据
function submitRemovalAshSlag() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './formRemovalAshSlag',
        data: $('#coalRemovalAshSlagForm').serialize(),
        async: false,
        error: function (request) {
            messageToast('error', '发生异常, 保存失败！',3000);
        },
        success: function (data) {
            assignmentForm(data.newDatas, "coalRemovalAshSlagForm");
            messageToast('success', '燃煤热电联产-除灰除渣系统数据保存成功！',3000);
        }
    });

}

