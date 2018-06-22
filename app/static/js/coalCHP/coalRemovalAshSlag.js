var oldFormData;

$(document).ready(function () {
    init();
    hiddenUnit();
    // 给保存按钮绑定事件
    initRemovalAshSlag();
    $('#submitData').bind('click', submitRemovalAshSlag);
    $('.left-select').bind('click', function(){
        // 当前页面所有模块list
        listModule = ["r-1", "r-2", "r-4"];
        var moduleName = $(this).attr("id");
        // 切换页面右侧内容
        changeModule(listModule, moduleName);
    });
    createLabelBind("coalRemovalAshSlagForm", oldFormData);
    $("#info6").on("click", function () {
        $("#showInfo").modal('show');
        $("#infoContent").html("<img class='img-responsive center-block' src='static/img/CoalCHP/removeAshSlag.png'/>");
    });
    // 定义面包屑个数
    var breakCount = 17;
    // 定义面包屑上id的模块类型
    var moduleName = "coalchp";
    initPreNext(moduleName, breakCount);
    // 上一页
    $('.pre').bind('click', function(){
        clickPre(breakCount, moduleName);
    });
    // 下一页
    $('.next').bind('click', function(){
        clickNext(breakCount, moduleName);
    });
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
            var dataformInit = $("#coalRemovalAshSlagForm").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
        }
    });
}

function assignmentForm(datas, formName) {
    var notvalidcolumname = [];
    var elements = getElements(formName);
    var tempInput;
    for (var i = 0; i < elements.length; i++) {
        tempInput = elements[i];
        if (datas[tempInput] != "" || datas[tempInput] == "0") {
            $("input[name='" + tempInput + "']").val(datas[tempInput]);
            $("input[name='" + tempInput + "']").removeClass("default-color");
        }
        valid(tempInput, notvalidcolumname);
    }
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
            var dataformInit = $("#coalRemovalAshSlagForm").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
            createLabelBind("coalRemovalAshSlagForm", oldFormData);
            messageToast('success', '燃煤热电联产-除灰除渣系统数据保存成功！',3000);
        }
    });

}

