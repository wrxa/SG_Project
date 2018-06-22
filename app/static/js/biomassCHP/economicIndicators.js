$(document).ready(function () {
    init();
    // 根据锅炉类型，确定厂用电率的初期值
    initElectricityConsumption();

    // 获得主要技术经济指标页面初期数据
    initEconomic();
    // 定义面包屑个数
    var breakCount = 16;
    // 定义面包屑上id的模块类型
    var moduleName = "biomass";
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
    $('#submitData').bind('click', submitEconomic);
    // 点击选择模块
    $('.left-select').bind('click', function(){
        // 当前页面所有模块list
        listModule = ["e-1", "e-2"];
        var moduleName = $(this).attr("id");
        // 切换页面右侧内容
        changeModule(listModule, moduleName);
    });
    createLabelBind("biomasschpEconomic", oldFormData);
});

//确定厂用电率的初期值
function initElectricityConsumption() {
    planId = $('#planId').val();
    $.ajax({
        cache: true,
        type: "POST",
        url: '/biomassGetBoilerType',
        data: { "planId": planId },
        async: false,
        error: function (request) {
            alert("Connection error1");
        },
        success: function (data) {
            var boiler_type = data.boilerType;     
            switch (boiler_type)
            {
                //常规循环流化床锅炉（CFB）,高低差速循环流化床锅炉（ICFB）
                case "1":case "2":
                    $("input[name='plant_electricity_consumption']").val('11');
                    break;
                //联合炉排炉,水冷振动炉排炉
                case "3":case "4":
                    $("input[name='plant_electricity_consumption']").val('9');
                    break;
                default:
                    break;
            }
            var dataformInit = $("#biomasschpEconomic").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
            createLabelBind("biomasschpEconomic", oldFormData);

            $('#biomass15').attr('onclick', "messageToast('info', '正在进行出图处理，请稍候！',16000);")
        }
    });
}

//主要技术经济指标页面信息初期化
function initEconomic() {
    planId = $('#planId').val();
    $.ajax({
        cache: true,
        type: "POST",
        url: '/biomassInitEconomic',
        data: { "planId": planId },
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，页面初期化失败！',3000);
        },
        success: function (data) {
            assignmentForm(data.economic);
            var dataformInit = $("#biomasschpEconomic").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
        }
    });
}

// 给页面中所有表单赋值
function assignmentForm(datas){
    var notvalidcolumname = [];
    var elements = getElements();
    var tempInput;
    for (var i = 0; i < elements.length; i++) {
        tempInput = elements[i];
        if(datas[tempInput] != "" || datas[tempInput] == "0") {
            $("input[name='"+tempInput+"']").val(datas[tempInput]);
        }
        // valid(tempInput, notvalidcolumname);
    }

}


//获取form中的所有的<input>对象  
function getElements() {  
    var tagElements = $("#biomasschpEconomic input");  
    var elements = new Array();  
    for (var j = 0; j < tagElements.length; j++){ 
        elements.push(tagElements[j].name); 
    }
    return elements;  
}

//提交表单信息
function submitEconomic() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './biomassFormDataEconomic',
        data: $('#biomasschpEconomic').serialize(),
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，保存失败！',3000);
        },
        success: function (data) {
            messageToast('success', '生物质热电联产-主要技术经济指标保存成功！',3000);
            // 刷新页面
            initEconomic();

            var dataformInit = $("#biomasschpEconomic").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
            createLabelBind("biomasschpEconomic", oldFormData);

        }
    });
}

