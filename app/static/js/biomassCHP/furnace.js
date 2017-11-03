$(document).ready(function () {
    unlockMeunBiomassCHP();

    //选择不同的锅炉，下列项目显示不同的值
    $("#boilerType").change(function () {
        var id = $(this).val();
        switch (id)
        {
            //空白
            case "0":
                //锅炉效率
                $("#f_boiler_efficiency_design").val("");
                $("#f_boiler_efficiency_check").val("");
                //机械未燃烧损失
                $("#f_unburned_loss_design").val("");
                $("#f_unburned_loss_check").val("");
                //飞灰份额
                $("#d_ash_share_design").val("");
                $("#d_ash_share_check").val("");
                //底渣份额
                $("#d_dust_share_design").val("");
                $("#d_dust_share_check").val("");
                break;
            //常规循环流化床锅炉（CFB）
            case "1":
                //锅炉效率
                $("#f_boiler_efficiency_design").val("90");
                $("#f_boiler_efficiency_check").val("90");
                //机械未燃烧损失
                $("#f_unburned_loss_design").val("4");
                $("#f_unburned_loss_check").val("4");
                //飞灰份额
                $("#d_ash_share_design").val("0.9");
                $("#d_ash_share_check").val("0.9");
                //底渣份额
                $("#d_dust_share_design").val("0.1");
                $("#d_dust_share_check").val("0.1");
                break;
            //高低差速循环流化床锅炉（ICFB）
            case "2":
                $("#f_boiler_efficiency_design").val("89");
                $("#f_boiler_efficiency_check").val("89");
                $("#f_unburned_loss_design").val("4");
                $("#f_unburned_loss_check").val("4");
                $("#d_ash_share_design").val("0.9");
                $("#d_ash_share_check").val("0.9");
                $("#d_dust_share_design").val("0.1");
                $("#d_dust_share_check").val("0.1");
                break;
            //联合炉排炉
            case "3":
                $("#f_boiler_efficiency_design").val("86");
                $("#f_boiler_efficiency_check").val("86");
                $("#f_unburned_loss_design").val("1");
                $("#f_unburned_loss_check").val("1");
                $("#d_ash_share_design").val("0.6");
                $("#d_ash_share_check").val("0.6");
                $("#d_dust_share_design").val("0.4");
                $("#d_dust_share_check").val("0.4");
                break;
            //水冷振动炉排炉
            case "4":
                $("#f_boiler_efficiency_design").val("87");
                $("#f_boiler_efficiency_check").val("87");
                $("#f_unburned_loss_design").val("1");
                $("#f_unburned_loss_check").val("1");
                $("#d_ash_share_design").val("0.6");
                $("#d_ash_share_check").val("0.6");
                $("#d_dust_share_design").val("0.4");
                $("#d_dust_share_check").val("0.4");
                break;
        }
    });

    //选择不同的温度压力，下列项目显示不同的值
    $("#pressureType").change(function () {
        var id = $(this).val();
        switch (id)
        {
            //空白
            case "0":
                //过热蒸汽出口压力
                $("#f_steam_pressure_design").val("");
                $("#f_steam_pressure_check").val("");
                //过热蒸汽温度
                $("#f_steam_temperature_design").val("");
                $("#f_steam_temperature_check").val("");
                //给水温度
                $("#f_water_temperature_design").val("");
                $("#f_water_temperature_check").val("");
                break;
            //高温高压
            case "1":
                //过热蒸汽出口压力
                $("#f_steam_pressure_design").val("9.81");
                $("#f_steam_pressure_check").val("9.81");
                //过热蒸汽温度
                $("#f_steam_temperature_design").val("540");
                $("#f_steam_temperature_check").val("540");
                //给水温度
                $("#f_water_temperature_design").val("215");
                $("#f_water_temperature_check").val("215");
                break;
            //次高温次高压
            case "2":
                //过热蒸汽出口压力
                $("#f_steam_pressure_design").val("5.3");
                $("#f_steam_pressure_check").val("5.3");
                //过热蒸汽温度
                $("#f_steam_temperature_design").val("485");
                $("#f_steam_temperature_check").val("485");
                //给水温度
                $("#f_water_temperature_design").val("158");
                $("#f_water_temperature_check").val("158");
                break;
            //中温中压
            case "3":
                //过热蒸汽出口压力
                $("#f_steam_pressure_design").val("3.82");
                $("#f_steam_pressure_check").val("3.82");
                //过热蒸汽温度
                $("#f_steam_temperature_design").val("450");
                $("#f_steam_temperature_check").val("450");
                //给水温度
                $("#f_water_temperature_design").val("150");
                $("#f_water_temperature_check").val("150");
                break;
        }
    });

    // 获得锅炉页面初期数据
    initFurnace();
    // 给保存按钮绑定事件
    $('#submitData').bind('click', submitFurnace);
});

//锅炉页面信息初期化
function initFurnace() {
    planId = $('#biomassCHPCurrentPlanId').val();
    $.ajax({
        cache: true,
        type: "POST",
        url: './biomassInitFurnace',
        data: { "planId": planId },
        async: false,
        error: function (request) {
            alert("Connection error1");
        },
        success: function (data) {
            assignmentForm(data.furnace);
        }
    });
}

// 提交锅炉页面所有表单数据
function submitFurnace() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './biomassFormDataFurnace',
        data: $('#biomassFurnaceForm').serialize(),
        async: false,
        error: function (request) {
            alert("Connection error2");
        },
        success: function (data) {
            alert("成功！！！" + data.coalSort['flag']);
        }
    });
}

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
    $("#boilerType").val(datas['boiler_type']);
    $("#pressureType").val(datas['pressure_temperature']);
}


//获取form中的所有的<input>对象
function getElements() {
    var tagElements = $("#biomassFurnaceForm input");
    var elements = new Array();
    for (var j = 0; j < tagElements.length; j++) {
        elements.push(tagElements[j].name);
    }
    return elements;
}