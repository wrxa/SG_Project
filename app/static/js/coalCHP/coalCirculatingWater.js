var oldFormData;

$(document).ready(function () {
    init();
    hiddenUnit();
    // 给保存按钮绑定事件
    initCirculatingWater();
    $('#submitData').bind('click', submitCirculatingWater);
    $('.left-select').bind('click', function(){
        // 当前页面所有模块list
        listModule = ["w-1", "w-2", "w-3"];
        var moduleName = $(this).attr("id");
        // 切换页面右侧内容
        changeModule(listModule, moduleName);
    });
    createLabelBind("coalCirculatingWaterForm", oldFormData);
    $("#info1").on("click", function () {
        $("#showInfo").modal('show');
        $("#infoContent").html("<img class='img-responsive center-block' src='static/img/CoalCHP/circulatingWater.png'/>");
    });
    // 选择循环水系统配置方式
    $("#circleWaterSelect").change(function () {
        var methodId = $(this).val();
        loadMethod(methodId);
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

/**
 * 根据选择加载对应的方式
 */
function loadMethod(methodId){
    if (methodId == "1") {
        if($("#method1").hasClass('hide')) {
         $("#method1").removeClass('hide');
         }
         if(!$("#method2").hasClass('hide')) {
         $("#method2").addClass('hide');
         }
     } else if (methodId == "2") {
         if($("#method2").hasClass('hide')) {
             $("#method2").removeClass('hide');
         }
         if(!$("#method1").hasClass('hide')) {
             $("#method1").addClass('hide');
         }
     }else{
        if(!$("#method1").hasClass('hide')) {
            $("#method1").addClass('hide');
        }
        if(!$("#method2").hasClass('hide')) {
            $("#method2").addClass('hide');
     }
    }
}

function initCirculatingWater() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './initCirculatingWater',
        async: false,
        error: function (request) {
            messageToast('error', '发生异常！',3000);
        },
        success: function (data) {
            assignmentForm(data.circulatingWater, "coalCirculatingWaterForm");
            // 给select赋值
            $("#circleWaterSelect").val(data.circulatingWater['circleWaterSelect']);
            loadMethod(data.circulatingWater['circleWaterSelect']);
            var dataformInit = $("#coalCirculatingWaterForm").serializeArray();
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
function submitCirculatingWater() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './formCirculatingWater',
        data: $('#coalCirculatingWaterForm').serialize(),
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，保存失败！',3000);
        },
        success: function (data) {
            assignmentForm(data.newDatas, "coalCirculatingWaterForm");
            // 给select赋值
            $("#circleWaterSelect").val(data.newDatas['circleWaterSelect']);
            loadMethod(data.newDatas['circleWaterSelect']);
            var dataformInit = $("#coalCirculatingWaterForm").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
            createLabelBind("coalCirculatingWaterForm", oldFormData);
            messageToast('success', '燃煤热电联产-循环水系统数据保存成功！',3000);
        }
    });

}

