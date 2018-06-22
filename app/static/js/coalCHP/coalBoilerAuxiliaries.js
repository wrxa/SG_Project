var oldFormData;

$(document).ready(function () {
    init();
    hiddenUnit();
    // 给保存按钮绑定事件
    initBoilerAuxiliaries();
    $('#submitData').bind('click', submitBoilerAuxiliaries);
    // 点击选择模块
    $('.left-select').bind('click', function(){
    // 当前页面所有模块list
    listModule = ["b-1", "b-2", "b-3", "b-4", "b-5", "b-6"];
    var moduleName = $(this).attr("id");
    // 切换页面右侧内容
    changeModule(listModule, moduleName);
});
    createLabelBind("coalBoilerAuxiliariesForm", oldFormData);
    $("#info1").on("click", function () {
        $("#showInfo").modal('show');
        $("#infoContent").html("<img class='img-responsive center-block' src='static/img/CoalCHP/boilerAuxiliaries_1.png'/>");
    });
    
    $("#info2").on("click", function () {
        $("#showInfo").modal('show');
        $("#infoContent").html("<img class='img-responsive center-block' src='static/img/CoalCHP/boilerAuxiliaries_2.png'/>");
    });

    $("#info3").on("click", function () {
        $("#showInfo").modal('show');
        $("#infoContent").html("<img class='img-responsive center-block' src='static/img/CoalCHP/boilerAuxiliaries_3.png'/>");
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
            var dataformInit = $("#coalBoilerAuxiliariesForm").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
        }
    });
}

function assignmentForm(datas, formName) {
    var notvalidcolumname = ["r_specifications", "c_specifications", "p_specifications"];
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
            var dataformInit = $("#coalBoilerAuxiliariesForm").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
            createLabelBind("coalBoilerAuxiliariesForm", oldFormData);
            messageToast('success', '燃煤热电联产-锅炉辅机系统数据保存成功！',3000);
        }
    });

}

