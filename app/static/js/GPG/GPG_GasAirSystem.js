var oldFormData;

$(document).ready(function () {
    init();
    
    getGasAirDataByPlanId();

    $('#submitGasAir').bind('click', submitGasAir);
    // 定义面包屑个数
    var breakCount = 12
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
        listModule = ["q-1", "q-2", "q-3", "q-4", "q-5", "q-6", "q-7", "q-8", "q-9", "q-10", "q-11", "q-12", "q-13", "q-14", "q-15"];
        var moduleName = $(this).attr("id");
        // 切换页面右侧内容
        changeModule(listModule, moduleName);
    })

    $('#s2c_condition_temperature_air').bind('keyup', function(){
        $('#blower_air_temperature').val($(this).val());
        $('#coldwind_tube_medium_temperature').val($(this).val());
    });

    $('#s2c_condition_temperature_smoke').bind('keyup', function(){
        $('#induced_smoke_temperature').val($(this).val());
    });

    $('#s2c_condition_temperature_gas').bind('keyup', function(){
        $('#gas_tube_medium_temperature').val($(this).val());
    });

    $("#info1").on("click", function () {
        $("#showInfo").modal('show');
        $("#infoContent").html("<img class='img-responsive center-block' src='static/img/GPG/GPG_GasAirSystem/windSpeed.png'/>");
    });

    $("#info2").on("click", function () {
        $("#showInfo").modal('show');
        $("#infoContent").html("<img class='img-responsive center-block' src='static/img/GPG/GPG_GasAirSystem/7-28.png'/>");
    });

    $("#info3").on("click", function () {
        $("#showInfo").modal('show');
        $("#infoContent").html("<img class='img-responsive center-block' src='static/img/GPG/GPG_GasAirSystem/4-18-2.png'/>");
    });

    $("#info4").on("click", function () {
        $("#showInfo").modal('show');
        $("#infoContent").html("<img class='img-responsive center-block' src='static/img/GPG/GPG_GasAirSystem/4-18-1.png'/>");
    });

    createLabelBind("GPG_GasAirSystemForm", oldFormData);
});

function getGasAirDataByPlanId() {
    planId = $('#GPGCurrentPlanId').val();
    $.ajax({
        cache: true,
        type: "POST",
        url: './getGasAirDataByPlanId',
        data: { "planId": planId },
        async: false,
        error: function (request) {
            messageToast('error', '发生异常！',3000);
        },
        success: function (data) {
            assignmentForm(data.GasAirJson, "GPG_GasAirSystemForm");
            var dataformInit = $("#GPG_GasAirSystemForm").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
        }
    });
}

function submitGasAir() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './GPG_SaveGasAirData',
        data: $('#GPG_GasAirSystemForm').serialize(),
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
                assignmentForm(data.newDatas, "GPG_GasAirSystemForm");
                var dataformInit = $("#GPG_GasAirSystemForm").serializeArray();  
                oldFormData = JSON.stringify({ dataform: dataformInit });
                createLabelBind("GPG_GasAirSystemForm", oldFormData);
                messageToast('success', '煤气发电-烟风系统数据保存成功！',2000);
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
    var tagElements = $("#GPG_GasAirSystemForm input");
    var elements = new Array();
    for (var j = 0; j < tagElements.length; j++) {
        elements.push(tagElements[j].name);
    }
    return elements;
}
*/
