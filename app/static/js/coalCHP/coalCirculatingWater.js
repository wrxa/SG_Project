$(document).ready(function () {
    unlockMeunCoalCHP();
    // 给保存按钮绑定事件
    initCirculatingWater();
    $('#submitData').bind('click', submitCirculatingWater);
});

function initCirculatingWater() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './initCirculatingWater',
        async: false,
        error: function (request) {
            messageToast('error', '发生异常！',3000);
        },
        success: function (data) {
            assignmentForm(data.circulatingWater, "coalCirculatingWaterForm");
        }
    });
}


// 提交保存页面所有表单数据
function submitCirculatingWater() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './formCirculatingWater',
        data: $('#coalCirculatingWaterForm').serialize(),
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，保存失败！',3000);
        },
        success: function (data) {
            assignmentForm(data.newDatas, "coalCirculatingWaterForm");
            messageToast('success', '燃煤热电联产-循环水系统数据保存成功！',3000);
        }
    });

}

