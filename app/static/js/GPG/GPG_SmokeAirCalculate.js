var oldFormData;

$(document).ready(function () {
    init();
    
    getSmokeAirCalculateDataByPlanId();

    $('#submitSmokeAirCalculateData').bind('click', submitSmokeAirCalculateData);
    // 定义面包屑个数
    var breakCount = 12;
    // 定义面包屑上id的模块类型
    var moduleName = "gpg";
    initPreNext(moduleName, breakCount);
    // 上一页
    $('.pre').bind('click', function(){
        clickPre(breakCount, moduleName);
    });
    // 下一页
    $('.next').bind('click', function(){
        clickNext(breakCount, moduleName);
    });
    // 点击选择模块
    $('.left-select').bind('click', function(){
        // 当前页面所有模块list
        listModule = ["q-1", "q-2", "q-3", "q-4", "q-5", "q-6", "q-7"];
        var moduleName = $(this).attr("id");
        // 切换页面右侧内容
        changeModule(listModule, moduleName);
    })

    $("#component_c2h4").val("0");
    $("#component_c3h8").val("0");
    $("#component_c4h10").val("0");

    $("#hl_h2").val("10.79");
    $("#hl_co").val("12.64");
    $("#hl_ch4").val("35.906");
    $("#hl_c2h4").val("59.477");
    $("#hl_c3h8").val("93.24");
    $("#hl_c4h10").val("123.6");
    $("#hl_n2").val("0");
    $("#hl_o2").val("0");
    $("#hl_co2").val("0");
    $("#hl_h2s").val("23.38");
    $("#hl_cmhn").val("87.67");

    $("#hh_h2").val("12.75");
    $("#hh_co").val("12.64");
    $("#hh_ch4").val("39.842");
    $("#hh_c2h4").val("63.438");
    $("#hh_c3h8").val("101.27");
    $("#hh_c4h10").val("133.9");
    $("#hh_n2").val("0");
    $("#hh_o2").val("0");
    $("#hh_co2").val("0");
    $("#hh_h2s").val("85.36");
    $("#hh_cmhn").val("93.67");

    var dataformInit = $("#GPG_SmokeAirCalculateForm").serializeArray();  
    oldFormData = JSON.stringify({ dataform: dataformInit });
    createLabelBind("GPG_SmokeAirCalculateForm", oldFormData);
});

function getSmokeAirCalculateDataByPlanId() {
    planId = $('#GPGCurrentPlanId').val();
    $.ajax({
        cache: true,
        type: "POST",
        url: './getSmokeAirCalculateDataByPlanId',
        data: { "planId": planId },
        async: false,
        error: function (request) {
            messageToast('error', '发生异常！',3000);
        },
        success: function (data) {
            assignmentForm(data.SmokeAirCalculateJson, "GPG_SmokeAirCalculateForm");
            var dataformInit = $("#GPG_SmokeAirCalculateForm").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
        }
    });
}

function submitSmokeAirCalculateData() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './GPG_SaveSmokeAirCalculateData',
        data: $('#GPG_SmokeAirCalculateForm').serialize(),
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，保存失败！',3000);
        },
        success: function (data) {
            if(data.newDatas == null){
                messageToast('error', '输入数据有误，转换发生异常!', 3000);
            }else if(data.newDatas == "-1"){
                messageToast('error', '输入数据有误，出现除0情况!', 3000);
            }else if(data.newDatas == "0"){
                messageToast('error', '数据有误，数据库计算中可能出现了除0情况!', 3000);
            }else{
                assignmentForm(data.newDatas, "GPG_SmokeAirCalculateForm");
                var dataformInit = $("#GPG_SmokeAirCalculateForm").serializeArray();  
                oldFormData = JSON.stringify({ dataform: dataformInit });
                createLabelBind("GPG_SmokeAirCalculateForm", oldFormData);
                messageToast('success', '煤气发电-烟,风量计算数据保存成功！',2000);
            }           
        }
    });
}

/*
// 给页面中所有表单赋值
function assignmentForm(datas) {
    var elements = getElements();
    var tempInput;
    for (var i = 0; i < elements.length; i++) {
        tempInput = elements[i];
        if(datas[tempInput] != "") {
            $("input[name='" + tempInput + "']").val(datas[tempInput]);
        }
    }
}


//获取form中的所有的<input>对象
function getElements() {
    var tagElements = $("#GPG_SmokeAirCalculateForm input");
    var elements = new Array();
    for (var j = 0; j < tagElements.length; j++) {
        elements.push(tagElements[j].name);
    }
    return elements;
}
*/
