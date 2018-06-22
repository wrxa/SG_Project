var oldFormData;

$(document).ready(function () {
    init();
    //unlockMeunBiomassCHP();
    // 获得脱硫脱销页面初期数据
    initDesulDenit();
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
    $('#submitData').bind('click', submitDesulDenit);

    // 给清空按钮绑定事件
    $('#clearData').bind('click', clearDesulDenit);
    // 点击选择模块
    $('.left-select').bind('click', function(){
        // 当前页面所有模块list
        listModule = ["d-1", "d-2", "d-3", "d-4", "d-5"];
        var moduleName = $(this).attr("id");
        // 切换页面右侧内容
        changeModule(listModule, moduleName);
    });
    createLabelBind("biomasschpDesulDenit", oldFormData);
});


//脱硫脱销页面信息初期化
function initDesulDenit() {
    planId = $('#planId').val();
    $.ajax({
        cache: true,
        type: "POST",
        url: './biomassInitDesulDenit',
        data: { "planId": planId },
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，页面初期化失败！',3000);
        },
        success: function (data) {
            assignmentForm(data.desuldenit);
            var dataformInit = $("#biomasschpDesulDenit").serializeArray();  
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
    var tagElements = $("#biomasschpDesulDenit input");  
    var elements = new Array();  
    for (var j = 0; j < tagElements.length; j++){ 
        elements.push(tagElements[j].name); 
    }
    return elements;  
}

//提交表单信息
function submitDesulDenit() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './biomassFormDataDesulDenit',
        data: $('#biomasschpDesulDenit').serialize(),
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，保存失败！',3000);
        },
        success: function (data) {          
            // 刷新页面
            initDesulDenit();
            var dataformInit = $("#biomasschpDesulDenit").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
            createLabelBind("biomasschpDesulDenit", oldFormData);
            messageToast('success', '生物质热电联产-脱硫脱销系统数据保存成功！',3000);
        }
    });
}

// 清空表单中的值
function clearDesulDenit(datas){
    var elements = getElements();
    var tempInput;
    for (var i = 0; i < elements.length; i++) {
        tempInput = elements[i];
        $("input[name='"+tempInput+"']").val("");
    }
    var dataformInit = $("#biomasschpDesulDenit").serializeArray();  
    oldFormData = JSON.stringify({ dataform: dataformInit });
    createLabelBind("biomasschpDesulDenit", oldFormData);
}