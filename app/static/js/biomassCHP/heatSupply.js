var oldFormData;

$(document).ready(function () {
    init();
    // 获得采暖供热系统页面初期数据
    initHeat();
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
    $('#submitData').bind('click', submitHeat);
    // 点击选择模块
    $('.left-select').bind('click', function(){
        // 当前页面所有模块list
        listModule = ["h-1", "h-2", "h-3"];
        var moduleName = $(this).attr("id");
        // 切换页面右侧内容
        changeModule(listModule, moduleName);
    });
    createLabelBind("biomasschpHeat", oldFormData);

    $("#info1").on("click", function () {
        $("#showInfo").modal('show');
        $("#infoContent").html("<img class='img-responsive center-block' src='static/img/BiomassCHP/heatsupply.png'/>");
    });
});

//采暖供热系统页面信息初期化
function initHeat() {
    planId = $('#planId').val();
    $.ajax({
        cache: true,
        type: "POST",
        url: './biomassinitHeat',
        data: { "planId": planId },
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，页面初期化失败！',3000);
        },
        success: function (data) {
            assignmentForm(data.heat);
            //$("[name='o_boiler_water_system']").val(data.water.o_boiler_water_system.toFixed(0));
            var dataformInit = $("#biomasschpHeat").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });

            $('#biomass15').attr('onclick', "messageToast('info', '正在进行出图处理，请稍候！',16000);")
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
    var tagElements = $("#biomasschpHeat input");  
    var elements = new Array();  
    for (var j = 0; j < tagElements.length; j++){ 
        elements.push(tagElements[j].name); 
    }
    return elements;  
}

//提交表单信息
function submitHeat() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './biomassFormDataHeat',
        data: $('#biomasschpHeat').serialize(),
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，保存失败！',3000);
        },
        success: function (data) {
            messageToast('success', '生物质热电联产-采暖供热系统数据保存成功！',3000);
            // 刷新页面
            initHeat();
            var dataformInit = $("#biomasschpHeat").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
            createLabelBind("biomasschpHeat", oldFormData);
        }
    });
}

