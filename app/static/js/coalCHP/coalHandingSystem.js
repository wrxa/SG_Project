var oldFormData;

$(document).ready(function () {
    init();
    hiddenUnit();
    // 给保存按钮绑定事件
    initHandingSystem();
    $('#submitData').bind('click', submitHandingSystem);
    // 点击选择模块
    $('.left-select').bind('click', function(){
        // 当前页面所有模块list
        listModule = ["h-1", "h-2", "h-3", "h-4", "h-5", "h-6"];
        var moduleName = $(this).attr("id");
        // 切换页面右侧内容
        changeModule(listModule, moduleName);
    });
    createLabelBind("coalchpHandingSystem", oldFormData);


    // s_belt_width_design
    // 选择带宽，断面系数变化
    $("#s_belt_width_design").change(function () {
        // 选择其他项时清空当前所有煤质分析值
        var count = $(this).val();
        var section_coefficients = [{ "belt_width": "500", "section_coefficient": "340" },
         { "belt_width": "650", "section_coefficient": "365" }, 
         { "belt_width": "800", "section_coefficient": "380" }, 
         { "belt_width": "1000", "section_coefficient": "400" }, 
         { "belt_width": "1200", "section_coefficient": "410" }, 
         { "belt_width": "1400", "section_coefficient": "415" }, 
         { "belt_width": "1600", "section_coefficient": "420" },
         { "belt_width": "1800", "section_coefficient": "425" },
         { "belt_width": "2000", "section_coefficient": "430" }];
         for (var j = 0; j < section_coefficients.length; j++) {
             if (section_coefficients[j].belt_width == count){
                $("#s_section_coefficient_design").val(section_coefficients[j].section_coefficient);
             }
         }
    });

    $("#info4").on("click", function () {
        $("#showInfo").modal('show');
        $("#infoContent").html("<img class='img-responsive center-block' src='static/img/CoalCHP/coalHandingSystem/1-13.png'/></br><img class='img-responsive center-block' src='static/img/CoalCHP/coalHandingSystem/ck2.png'/>");
    });

    $("#info5").on("click", function () {
        $("#showInfo").modal('show');
        $("#infoContent").html("<img class='img-responsive center-block' src='static/img/CoalCHP/coalHandingSystem/10-9.png'/></br><img class='img-responsive center-block' src='static/img/CoalCHP/coalHandingSystem/10.2.1.png'/>");
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

function initHandingSystem() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './initHandingSystem',
        async: false,
        error: function (request) {
            messageToast('error', '发生异常！',3000);
        },
        success: function (data) {
            assignmentForm(data.handingSystem, "coalchpHandingSystem");
            var dataformInit = $("#coalchpHandingSystem").serializeArray();
            oldFormData = JSON.stringify({ dataform: dataformInit });
        }
    });
}


// 提交保存页面所有表单数据
function submitHandingSystem() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './formDataHandingSystem',
        data: $('#coalchpHandingSystem').serialize(),
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，保存失败！',3000);
        },
        success: function (data) {
            assignmentForm(data.newDatas, "coalchpHandingSystem");
            var dataformInit = $("#coalchpHandingSystem").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
            createLabelBind("coalchpHandingSystem", oldFormData);
            messageToast('success', '燃煤热电联产-输煤系统数据保存成功！',3000);
        }
    });

}

/**
 * 给页面中所有表单赋值
 * @param {后台传回来的值} datas 
 */
function assignmentForm(datas) {
    var notvalidcolumname = [];
    var elements = getElements("coalchpHandingSystem");
    var tempInput;
    for (var i = 0; i < elements.length; i++) {
        tempInput = elements[i];
        if (datas[tempInput] != "" || datas[tempInput] == "0") {
            $("input[name='" + tempInput + "']").val(datas[tempInput]);
            $("input[name='" + tempInput + "']").removeClass("default-color");
        }
        valid(tempInput, notvalidcolumname);
    }
    
    // 给select框赋值
    $("#s_belt_width_design").val(datas['s_belt_width_design']);

    var dataformInit = $("#coalchpHandingSystem").serializeArray();  
    oldFormData = JSON.stringify({ dataform: dataformInit });
}


