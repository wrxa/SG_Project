$(document).ready(function () {
    init();

    // 获得主要技术经济指标页面初期数据
    initEconomic();

    // 给保存按钮绑定事件
    $('#submitData').bind('click', submitEconomic);
    $('.left-select').bind('click', function(){
        // 当前页面所有模块list
        listModule = ["e-1", "e-2"];
        var moduleName = $(this).attr("id");
        // 切换页面右侧内容
        changeModule(listModule, moduleName);
    });
    createLabelBind("coalchpEconomic", oldFormData);
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


//主要技术经济指标页面信息初期化
function initEconomic() {
    planId = $('#planId').val();
    $.ajax({
        cache: true,
        type: "POST",
        url: '/coalInitEconomic',
        data: { "planId": planId },
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，页面初期化失败！',3000);
        },
        success: function (data) {
            assignmentForm(data.economic);
            var dataformInit = $("#coalchpEconomic").serializeArray();  
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
        valid(tempInput, notvalidcolumname);
    }

}


//获取form中的所有的<input>对象  
function getElements() {  
    var tagElements = $("#coalchpEconomic input");  
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
        url: './coalFormDataEconomic',
        data: $('#coalchpEconomic').serialize(),
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，保存失败！',3000);
        },
        success: function (data) {
            messageToast('success', '生物质热电联产-主要技术经济指标保存成功！',3000);
            // 刷新页面
            initEconomic();

            var dataformInit = $("#coalchpEconomic").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
            createLabelBind("coalchpEconomic", oldFormData);

        }
    });
}

