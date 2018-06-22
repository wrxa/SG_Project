var oldFormData;

$(document).ready(function () {
    init();
    //unlockMeunBiomassCHP();
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
    //选择不同的锅炉，点火方式不同
    $("#boilerType").change(function () {
        var id = $(this).val();
        switch (id)
        {
            //空白
            case "0":
                $("#fireWay").val("");
                $("." + "o-2").addClass('hide');
                break;
            //层燃炉
            case "1":
                $("#fireWay").val("人工点火（即床上火把点火）");
                $("." + "o-2").addClass('hide');
                break;
            //循环流化床锅炉
            case "2":
                $("#fireWay").val("0#轻柴油点火（一般为床下点火）");
                $("." + "o-2").removeClass('hide');
                break;
        }
    });

    $("#steamParameter, #steamVolumn").change(function () {
        $("#furnaceType").val("");
    });

    //燃料类型选定后，关联得出锅炉型号
    $("#fuelType").change(function () {
        var id = $(this).val();
        var steamParameter = $("#steamParameter").val();
        var steamVolumn = $("#steamVolumn").val();

		//额定蒸发量数值
		var steamVolumn_text;
		switch(steamVolumn)
		{
		    case "0":
		        steamVolumn_text = "";
		        break;
		    case "1":
		        steamVolumn_text = "2";
		        break;
		    case "2":
		        steamVolumn_text = "4";
		        break;
		    case "3":
		        steamVolumn_text = "6";
		        break;
		}

		//额定蒸汽参数数值
		var steamParameterPressure;//压力
		var steamParameterTemperature;//温度
		switch(steamParameter)
		{
		    case "0":
		        steamParameterPressure = "";
		        steamParameterTemperature = "";
		        break;
		    case "1":
		        steamParameterPressure = "0.7";
		        steamParameterTemperature = "170";
		        break;
		    case "2":
		        steamParameterPressure = "1.0";
		        steamParameterTemperature = "184";
		        break;
		    case "3":
		        steamParameterPressure = "1.25";
		        steamParameterTemperature = "194";
		        break;
		    case "4":
		        steamParameterPressure = "1.6";
		        steamParameterTemperature = "204";
		        break;
		}

        var furnaceType;
        switch (id)
        {
            case "0":
		        furnaceType = "";
                $("#furnaceType").val(furnaceType);
		        break;
		    case "1":
		        furnaceType = "DZL" + steamVolumn_text + "-" + steamParameterPressure + "/" + steamParameterTemperature;
                $("#furnaceType").val(furnaceType);
		        break;
		    case "2":
		        furnaceType = "WNS" + steamVolumn_text + "-" + steamParameterPressure + "/" + steamParameterTemperature;
                $("#furnaceType").val(furnaceType);
		        break;
        }
        

    });

    // 获得公用工程页面初期数据
    initOfficial();


    if($("#boilerType").val() == "2") {
        $("." + "o-2").removeClass('hide');
    }

    // 给保存按钮绑定事件
    $('#submitData').bind('click', submitOfficial);

    // 给清空按钮绑定事件
    $('#clearData').bind('click', clearOfficial);

    // 点击选择模块
    $('.left-select').bind('click', function(){
        // 当前页面所有模块list
        listModule = ["o-1", "o-3"];
        var moduleName = $(this).attr("id");
        // 切换页面右侧内容
        changeModule(listModule, moduleName);

        if(moduleName == 'o-3') {
            $("." + "o-2").addClass('hide');
        }
        // 获得公用工程页面初期数据
        initOfficial();

        if($("#boilerType").val() == "2" && moduleName == 'o-1') {
            $("." + "o-2").removeClass('hide');
        }

    });

    // if($("#boilerType").val() == "2") {
    //     $("." + "o-2").removeClass('hide');
    // }


    createLabelBind("biomasschpOfficial", oldFormData);
});

//锅炉辅机页面信息初期化
function initOfficial() {
    planId = $('#planId').val();
    $.ajax({
        cache: true,
        type: "POST",
        url: './biomassinitOfficial',
        data: { "planId": planId },
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，页面初期化失败！',3000);
        },
        success: function (data) {
            assignmentForm(data.official);
            var dataformInit = $("#biomasschpOfficial").serializeArray();  
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

    // 给下拉列表[锅炉类型，点火方式，燃料类型]赋值
    $("#boilerType").val(datas['o_boiler_type']);
    $("#fireWay").val(datas['o_fire_way']);
    $("#fuelType").val(datas['o_fuel_type']);
    $("#steamParameter").val(datas['o_steam_parameter']);
    $("#steamVolumn").val(datas['o_steam_volumn']);
    $("#o_furnace_type").val(datas['o_furnace_type']);

    //计算供油泵的出力Q（单台）
    if(datas['o_oil_pump'] == ''){
       oilPumpCal();
    } 

    if(datas['o_install_way'] == '' || datas['o_install_way'] == null){
        $("input[name='o_install_way']").val("快装式");
    }

}


//获取form中的所有的<input>对象  
function getElements() {  
    var tagElements = $("#biomasschpOfficial input");  
    var elements = new Array();  
    for (var j = 0; j < tagElements.length; j++){ 
        elements.push(tagElements[j].name); 
    }
    return elements;  
}

//提交表单信息
function submitOfficial() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './biomassFormDataOfficial',
        data: $('#biomasschpOfficial').serialize(),
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，保存失败！',3000);
        },
        success: function (data) {
            messageToast('success', '生物质热电联产-公用工程数据保存成功！',3000);
            // 刷新页面
            initOfficial();
            var dataformInit = $("#biomasschpOfficial").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
            createLabelBind("biomasschpOfficial", oldFormData);
        }
    });
}

// 清空表单中的值
function clearOfficial(datas){
    var elements = getElements();
    var tempInput;
    for (var i = 0; i < elements.length; i++) {
        tempInput = elements[i];
        $("input[name='"+tempInput+"']").val("");
    }

    $("#boilerType").val("");
    $("#fireWay").val("");
    $("#fuelType").val("");
}

function oilPumpCal(){
    planId = $('#planId').val();
    $.ajax({
        cache: true,
        type: "POST",
        url: './biomassOilPumpCal',
        data: { "planId": planId },
        async: false,
        error: function (request) {
            alert("Connection error1");
        },
        success: function (data) {
            var low_calorific_value_estimation = data.oilPumpData['c_low_calorific_value_estimation_design'];
            var boiler_consumption = data.oilPumpData['f_boiler_consumption_design'];
            var oilPump_value = low_calorific_value_estimation*boiler_consumption*0.15/10000/4.1868/1000;
            
            if(oilPump_value  != 0){
                $("input[name='o_oil_pump']").val(oilPump_value);
            }
        }
    });
}