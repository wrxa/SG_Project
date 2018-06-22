var oldFormData;
$(document).ready(function () {
    init();
    //unlockMeunBiomassCHP();
    // 获得除尘除灰页面初期数据
    initDASRemove();
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
    $('#submitData').bind('click', submitDASRemove);

    // 给清空按钮绑定事件
    $('#clearData').bind('click', clearDASRemove);
    // 点击选择模块
    $('.left-select').bind('click', function(){
        // 当前页面所有模块list
        listModule = ["r-1", "r-2", "r-3", "r-4", "r-5"];
        var moduleName = $(this).attr("id");
        // 切换页面右侧内容
        changeModule(listModule, moduleName);
    });
    createLabelBind("biomasschpDASRemove", oldFormData);

    $("#info1").on("click", function () {
        $("#showInfo").modal('show');
        $("#infoContent").html("除灰渣系统的工艺原则：灰渣分除、干湿分排方案。<br>1、除灰系统：省煤器和旋风除尘器＋布袋除尘器干灰采用正压浓相气力输送方式清除；<br>2、除渣系统：锅炉底渣采用干式机械除渣方式清除。 ");
    });

});


//除尘除灰页面信息初期化
function initDASRemove() {
    planId = $('#planId').val();
    $.ajax({
        cache: true,
        type: "POST",
        url: './biomassinitDASRemove',
        data: { "planId": planId },
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，页面初期化失败！',3000);
        },
        success: function (data) {
            assignmentForm(data.dasremove);
            var dataformInit = $("#biomasschpDASRemove").serializeArray();  
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
    var tagElements = $("#biomasschpDASRemove input");  
    var elements = new Array();  
    for (var j = 0; j < tagElements.length; j++){ 
        elements.push(tagElements[j].name); 
    }
    return elements;  
}

//提交表单信息
function submitDASRemove() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './biomassFormDataDASRemove',
        data: $('#biomasschpDASRemove').serialize(),
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，保存失败！',3000);
        },
        success: function (data) {           
            // 刷新页面
            initDASRemove();
            var dataformInit = $("#biomasschpDASRemove").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
            createLabelBind("biomasschpDASRemove", oldFormData);
            messageToast('success', '生物质热电联产-除尘除灰除渣系统数据保存成功！',3000);
        }
    });
}

// 清空表单中的值
function clearDASRemove(datas){
    var elements = getElements();
    var tempInput;
    for (var i = 0; i < elements.length; i++) {
        tempInput = elements[i];
        $("input[name='"+tempInput+"']").val("");
    }
    var dataformInit = $("#biomasschpDASRemove").serializeArray();  
    oldFormData = JSON.stringify({ dataform: dataformInit });
    createLabelBind("biomasschpDASRemove", oldFormData);
}