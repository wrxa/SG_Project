var oldFormData;

$(document).ready(function () {
    init();
    // 定义面包屑个数
    var breakCount = 14;
    // 定义面包屑上id的模块类型
    var moduleName = "ccpp";
    initPreNext(moduleName, breakCount);
    // 上一页
    $('.pre').bind('click', function(){
        clickPre(breakCount, moduleName);
    });
    // 下一页
    $('.next').bind('click', function(){
        clickNext(breakCount, moduleName);
    });
    // 给保存按钮绑定事件
    initCirculatingWater();
    $('#submitData').bind('click', submitCirculatingWater);
    // 点击选择模块
    $('.left-select').bind('click', function(){
        // 当前页面所有模块list
        listModule = ["t-1", "t-2", "t-3", "t-4", "t-5"];
        var moduleName = $(this).attr("id");
        // 切换页面右侧内容
        changeModule(listModule, moduleName);
    });
    createLabelBind("biomassTurbineAuxiliary", oldFormData);

    $("#info1").on("click", function () {
        $("#showInfo").modal('show');
        $("#infoContent").html("<img class='img-responsive center-block' src='/static/img/ccpp/tb.png'/>");
    });
});

function initCirculatingWater() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './biomassinitTurbineAuxiliary',
        async: false,
        error: function (request) {
            messageToast('error', '发生异常！',3000);
        },
        success: function (data) {
            assignmentForm(data.turbineAuxiliaryData);
            var dataformInit = $("#biomassTurbineAuxiliary").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
        }
    });
}

// 给页面中所有表单赋值
function assignmentForm(datas){
    var elements = getElements();
    var tempInput;
    for (var i = 0; i < elements.length; i++) {
        tempInput = elements[i];
        if(datas[tempInput] != "" || datas[tempInput] == "0") {
            $("input[name='"+tempInput+"']").val(datas[tempInput]);
        }
    }
}


//获取form中的所有的<input>对象  
function getElements() {  
    var tagElements = $("#biomassTurbineAuxiliary input");  
    var elements = new Array();  
    for (var j = 0; j < tagElements.length; j++){ 
        elements.push(tagElements[j].name); 
    }
    return elements;  
}

// 提交保存页面所有表单数据
function submitCirculatingWater() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './biomassFormTurbineAuxiliary',
        data: $('#biomassTurbineAuxiliary').serialize(),
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，保存失败！',3000);
        },
        success: function (data) {
            assignmentForm(data.newDatas);
            var dataformInit = $("#biomassTurbineAuxiliary").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
            createLabelBind("biomassTurbineAuxiliary", oldFormData);
            messageToast('success', '燃气蒸汽联合循环-汽机辅机数据保存成功！',3000);
        }
    });

}

