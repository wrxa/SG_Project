$(document).ready(function () {
    unlockMeunCoalCHP();
    // 给保存按钮绑定事件
    // initFurnace();
    // $('#submitData').bind('click', submitFurnace);
});

function initFurnace() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './initFurnace',
        // data: { "planId": planId },
        async: false,
        error: function (request) {
            alert("Connection error");
        },
        success: function (data) {
            assignmentForm(data.furnace, "coalFurnaceForm");
        }
    });
}


// 提交保存页面所有表单数据
function submitFurnace() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './formDataFurnace',
        data: $('#coalFurnaceForm').serialize(),
        async: false,
        error: function (request) {
            alert("Connection error");
        },
        success: function (data) {
            assignmentForm(data.newDatas, "coalFurnaceForm");
            alert("成功！！！");
        }
    });

}

