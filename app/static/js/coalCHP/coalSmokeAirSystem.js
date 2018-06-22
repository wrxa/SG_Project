var oldFormData;

$(document).ready(function () {
    init();
    hiddenUnit();
    // 给保存按钮绑定事件
    initSmokeAirSystem();
    $('#submitData').bind('click', submitSmokeAirSystem);
    // 烟风流量
    changeSmokeAirFlow();
    // 点击选择模块
    $('.left-select').bind('click', function(){
        // 当前页面所有模块list
        listModule = ["s-1", "s-2", "s-3", "s-4", "s-5", "s-6"];
        var moduleName = $(this).attr("id");
        // 切换页面右侧内容
        changeModule(listModule, moduleName);
    });
    createLabelBind("coalSmokeAirSystemForm", oldFormData);
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

function initSmokeAirSystem() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './initSmokeAirSystem',
        // data: { "planId": planId },
        async: false,
        error: function (request) {
            messageToast('error', '发生异常！',3000);
        },
        success: function (data) {
            assignmentForm(data.smokeAirSystem, "coalSmokeAirSystemForm");
            var dataformInit = $("#coalSmokeAirSystemForm").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
        }
    });
}


// 提交保存页面所有表单数据
function submitSmokeAirSystem() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './formSmokeAirSystem',
        data: $('#coalSmokeAirSystemForm').serialize(),
        async: false,
        error: function (request) {
            messageToast('error', '发生异常！',3000);
        },
        success: function (data) {
            assignmentForm(data.newDatas, "coalSmokeAirSystemForm");
            var dataformInit = $("#coalSmokeAirSystemForm").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
            createLabelBind("coalSmokeAirSystemForm", oldFormData);
            messageToast('success', '燃煤热电联产-烟风系统数据保存成功！',3000);
        }
    });

}

function assignmentForm(datas, formName) {
    var notvalidcolumname = ["f_lectotype", "s_lectotype", "i_lectotype", "r_lectotype"];
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

// 烟风流量
function changeSmokeAirFlow() {
    // 一次风机烟风流量计算
    $("[name='f_wind_Proportion'], [name='f_count'], [name='p_operational_point_flow_f']").change(function () {
        var f_wind_Proportion = Number($("[name='f_wind_Proportion']").val());
        var f_count = Number($("[name='f_count']").val());
        var p_operational_point_flow_f = Number($("[name='p_operational_point_flow_f']").val());
        if (f_wind_Proportion != '' && f_count != '' && p_operational_point_flow_f != ''){
        $("[name='f_smoke_flow_rate_condition']").val(
            (f_wind_Proportion*p_operational_point_flow_f/f_count).toFixed(2)
        );
    }
    });

    // 二次风烟风流量机计算
    $("[name='s_count'], [name='p_operational_point_flow_s']").change(function () {
        var s_count = Number($("[name='s_count']").val());
        var p_operational_point_flow_s = Number($("[name='p_operational_point_flow_s']").val());
        if (s_count != '' && p_operational_point_flow_s != ''){
        $("[name='s_smoke_flow_rate_condition']").val(
            (p_operational_point_flow_s/s_count).toFixed(2)
        );
    }
    });

    // 引风机烟风流量计算
    $("[name='i_count'], [name='p_operational_point_flow_t']").change(function () {
        var i_count = Number($("[name='i_count']").val());
        var p_operational_point_flow_t = Number($("[name='p_operational_point_flow_t']").val());
        if (i_count != '' && p_operational_point_flow_t != ''){
        $("[name='i_smoke_flow_rate_condition']").val(
            (p_operational_point_flow_t/i_count).toFixed(2)
        );
    }
    });

    var dataformInit = $("#coalSmokeAirSystemForm").serializeArray();  
    oldFormData = JSON.stringify({ dataform: dataformInit });
    createLabelBind("coalSmokeAirSystemForm", oldFormData);
}

function fomatFloat(src,pos){   
    return Math.round(src*Math.pow(10, pos))/Math.pow(10, pos);   
 } 