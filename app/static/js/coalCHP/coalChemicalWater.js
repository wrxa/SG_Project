var oldFormData;

$(document).ready(function () {
    init();
    hiddenUnit();
    // 给保存按钮绑定事件
    initChemicalWater();
    $('#submitData').bind('click', submitchemicalWater);
    $('.left-select').bind('click', function(){
        // 当前页面所有模块list
        listModule = ["c-1"];
        var moduleName = $(this).attr("id");
        // 切换页面右侧内容
        changeModule(listModule, moduleName);
    });
    createLabelBind("coalChemicalWaterForm", oldFormData);
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

function initChemicalWater() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './initChemicalWater',
        async: false,
        error: function (request) {
            messageToast('error', '发生异常！',3000);
        },
        success: function (data) {
            assignmentForm(data.chemicalWater, "coalChemicalWaterForm");
            $("#processRoute").val(data.chemicalWater['m_process_route']);
            var dataformInit = $("#coalChemicalWaterForm").serializeArray();  
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
function submitchemicalWater() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './chemicalWaterData',
        data: $('#coalChemicalWaterForm').serialize(),
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，保存失败！',3000);
        },
        success: function (data) {
            assignmentForm(data.newDatas, "coalChemicalWaterForm");
            $("#processRoute").val(data.newDatas['m_process_route']);
            var dataformInit = $("#coalChemicalWaterForm").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
            createLabelBind("coalChemicalWaterForm", oldFormData);
            messageToast('success', '燃煤热电联产-化学水系统数据保存成功！',3000);
        }
    });

}

