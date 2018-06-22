var oldFormData;

$(document).ready(function () {
    init();
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
    //冷却塔选型
    $("#pSelect").change(function () {
        var id = $(this).val();
        switch (id)
        {
            //空白
            case "0":   
                $("." + "w-2").addClass('hide');
                $("." + "w-3").addClass('hide');             
                break;
            //双曲线自然通风冷却塔
            case "1":                
                $("." + "w-2").removeClass('hide');
                $("." + "w-3").addClass('hide');
                break;
            //逆流式机械通风冷却塔
            case "2":
                $("." + "w-3").removeClass('hide');
                $("." + "w-2").addClass('hide');
                break;
        }
    });

    // 给保存按钮绑定事件
    initCirculatingWater();
    $('#submitData').bind('click', submitCirculatingWater);
    // 点击选择模块
    $('.left-select').bind('click', function(){
        // 当前页面所有模块list
        listModule = ["w-1", "w-2", "w-3", "w-4", "w-5"];
        var moduleName = $(this).attr("id");  
        // 切换页面右侧内容
        // 获得公用工程页面初期数据
        initCirculatingWater();

        changeModule(listModule, moduleName);

        if($("#pSelect").val() == "1" && moduleName == 'w-5') {
            $("." + "w-2").removeClass('hide');
        }

        if($("#pSelect").val() == "2" && moduleName == 'w-5') {
            $("." + "w-3").removeClass('hide');
        }
       
    });
    createLabelBind("biomassCirculatingWaterForm", oldFormData);

    $("#info1").on("click", function () {
        $("#showInfo").modal('show');
        $("#infoContent").html("<img class='img-responsive center-block' src='static/img/CoalCHP/circulatingWater.png'/>");
    });
});

function initCirculatingWater() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './biomassinitCirculatingWater',
        async: false,
        error: function (request) {
            messageToast('error', '发生异常！',3000);
        },
        success: function (data) {
            assignmentForm(data.circulatingWaterData);
            var dataformInit = $("#biomassCirculatingWaterForm").serializeArray();  
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

    $("#pSelect").val(datas['p_select']);

}


//获取form中的所有的<input>对象  
function getElements() {  
    var tagElements = $("#biomassCirculatingWaterForm input");  
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
        url: './biomassFormCirculatingWater',
        data: $('#biomassCirculatingWaterForm').serialize(),
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，保存失败！',3000);
        },
        success: function (data) {
            assignmentForm(data.newDatas);
            var dataformInit = $("#biomassCirculatingWaterForm").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
            createLabelBind("biomassCirculatingWaterForm", oldFormData);
            messageToast('success', '生物质热电联产-循环水系统数据保存成功！',3000);
        }
    });

}

