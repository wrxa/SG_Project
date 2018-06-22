var oldFormData;

$(document).ready(function () {
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
    init();
    hiddenUnit();
    bool_input = false;

    //unlockMeunBiomassCHP();

    // 回热级数必须为数字
    $("[name='s_hh_grade']").keypress(function (e) {
        if (!String.fromCharCode(e.keyCode).match(/[0-2\.]/)) {
            return false;
        }
    });

    $("[name='s_lh_grade']").keypress(function (e) {
        if (!String.fromCharCode(e.keyCode).match(/[1-3\.]/)) {
            return false;
        }
    });

    //选择不同的汽轮机型式，下列项目显示不同的值
    $("#steamType").change(function () {
        var id = $(this).val();
        $("#e_steam_pressure").attr("readOnly",true);
        $("#e_steam_temperature").attr("readOnly",true);

        switch (id)
        {
            //空白
            case "0":
                //主蒸汽  压力
                $("#e_steam_pressure").val("");
                //主蒸汽  温度
                $("#e_steam_temperature").val("");
                break;
            //低压
            case "1":
                //主蒸汽  压力
                $("#e_steam_pressure").val("1.27");
                //主蒸汽  温度
                $("#e_steam_temperature").val("340");
                break;
            //次中压
            case "2":
                //主蒸汽  压力
                $("#e_steam_pressure").val("2.35");
                //主蒸汽  温度
                $("#e_steam_temperature").val("390");
                break;
            //中压
            case "3":
                //主蒸汽  压力
                $("#e_steam_pressure").val("3.43");
                //主蒸汽  温度
                $("#e_steam_temperature").val("435");
                break;
            //次高压
            case "4":
                //主蒸汽  压力
                $("#e_steam_pressure").val("4.90");
                //主蒸汽  温度
                $("#e_steam_temperature").val("435");
                break;
            //高压
            case "5":
                //主蒸汽  压力
                $("#e_steam_pressure").val("8.8");
                //主蒸汽  温度
                $("#e_steam_temperature").val("535");
                break;
            //其他
            case "6":
                //主蒸汽  压力
                $("#e_steam_pressure").val("");
                //主蒸汽  温度
                $("#e_steam_temperature").val("");
                $("#e_steam_pressure").attr("readOnly",false);
                $("#e_steam_temperature").attr("readOnly",false);
                $("#e_steam_pressure").focus();
                break;
        }
    });

    //选择不同的除氧器温度压力，下列项目显示不同的值
    $("#s_temperature_pressure").change(function () {
        var id = $(this).val();
        switch (id)
        {
         //空白
        case "0":
            //除氧器温度
            $("#d_water_temperature").val("");
            //除氧器压力
            $("#d_work_pressure").val("");
            break;
        //大气式
        case "1":
            //除氧器温度
            $("#d_water_temperature").val("104");
            //除氧器压力
            $("#d_work_pressure").val("0.02");
            break; 
        //中压
        case "2":
            //除氧器温度
            $("#d_water_temperature").val("130");
            //除氧器压力
            $("#d_work_pressure").val("0.3");
            break;  
         //高压
        case "3":
            //除氧器温度
            $("#d_water_temperature").val("158");
            //除氧器压力
            $("#d_work_pressure").val("0.588");
            break;
        }
    });


    // 获得汽轮机（背压）页面初期数据
    initSteamTurbine();

    // 给保存按钮绑定事件
   $('#submitData').bind('click', submitSteamTurbine);

   // 根据压力查询温度
   $('#by_pressure').bind('click', byPressure);

   // 根据压力和熵查询温度
   $('#by_pressure_entropy').bind('click', byPressureEntropy);

   $('#by_temperature_back').bind('click', byTemperatureBack);
   $('#by_pressure_back').bind('click', byPressureBack);

   $('#by_pressure_entropy_back').bind('click', byPressureEntropyBack);
   $('#by_temperature_entropy_back').bind('click', byTemperatureEntropyBack);
   $('.left-select').bind('click', function(){
    // 当前页面所有模块list
    listModule = ["t-1", "t-2", "t-3", "t-4"];
    var moduleName = $(this).attr("id");
    // 切换页面右侧内容
    changeModule(listModule, moduleName);
    });
   createLabelBind("biomasschpSteamTurbine", oldFormData);

    $("#info1").on("click", function () {
        $("#showInfo").modal('show');
        $("#infoContent").html("<img class='img-responsive center-block' src='static/img/BiomassCHP/steamtype.png'/>");
    });
});


//除尘除灰页面信息初期化
function initSteamTurbine() {
    planId = $('#planId').val();
    $.ajax({
        cache: true,
        type: "POST",
        url: './coalinitSteamTurbine',
        data: { "planId": planId },
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，页面初期化失败！',3000);
        },
        success: function (data) {
            assignmentForm(data.steamturbine);

            var dataformInit = $("#biomasschpSteamTurbine").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
        }
    });
}

// 给页面中所有表单赋值
function assignmentForm(datas){
    var elements = getElements();
    notvalidcolumname = [];
    var tempInput;
    for (var i = 0; i < elements.length; i++) {
        tempInput = elements[i];
        if(datas[tempInput] != "" || datas[tempInput] == "0") {
            $("input[name='"+tempInput+"']").val(datas[tempInput]);
        }
        valid(tempInput, notvalidcolumname);
    }

    // if(datas['s_temperature_pressure'] == '1') {
    //    $("#d_water_temperature").val("104");
    //    $("#d_work_pressure").val("0.02");
    // }

    // if(datas['s_temperature_pressure'] == '2') {
    //    $("#d_water_temperature").val("130");
    //    $("#d_work_pressure").val("0.3");
    // }

    // if(datas['s_temperature_pressure'] == '3') {
    //    $("#d_water_temperature").val("158");
    //    $("#d_work_pressure").val("0.588");
    // }

    $("#steamType").val(datas['e_steam_type']);
    $("#h_assume").val(datas['h_assume']);

    $("#s_steam_type_test").val(datas['s_steam_type_test']);
    $("#s_temperature_pressure").val(datas['s_temperature_pressure']);

}


//获取form中的所有的<input>对象  
function getElements() {  
    var tagElements = $("#biomasschpSteamTurbine input");  
    var elements = new Array();  
    for (var j = 0; j < tagElements.length; j++){ 
        elements.push(tagElements[j].name); 
    }
    return elements;  
}

//提交表单信息
function submitSteamTurbine() {

    if ($("[name='s_steam_type_test']").val() == '0' || $("[name='s_steam_type_test']").val() == null)
    {
        messageToast('info', '请选择汽轮机类型！',4000);

    } else if($("[name='s_temperature_pressure']").val() == '0' || $("[name='s_temperature_pressure']").val() == null){
        messageToast('info', '请选择除氧器温度和压力！',4000);
    
    } else if(($("[name='s_hh_grade']").val() != "0" &&  $("[name='s_hh_grade']").val() != "1" && $("[name='s_hh_grade']").val() != "2") ){
        messageToast('info', '请输入高加级数0~2！',4000);
        $("[name='s_hh_grade']").focus();

    } else if(($("[name='s_lh_grade']").val() != "1" && $("[name='s_lh_grade']").val() != "2" && $("[name='s_lh_grade']").val() != "3")){
        messageToast('info', '请输入低加级数1~3！',4000);
        $("[name='s_lh_grade']").focus();
        
    } else {

    $.ajax({
        cache: true,
        type: "POST",
        url: './coalFormDataSteamTurbine',
        data: $('#biomasschpSteamTurbine').serialize(),
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，保存失败！',3000);
        },
        success: function (data) {

            messageToast('success', '燃煤热电联产-汽轮机计算数据保存成功！',3000);
            // 刷新页面
            initSteamTurbine();
            var dataformInit = $("#biomasschpSteamTurbine").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
            createLabelBind("biomasschpSteamTurbine", oldFormData);
            window.location.href="/coalSteamTurbine"
        }
    });
    }
}


function byPressure() {
    if ($("[name='e_exhaust_point_pressure']").val() == null || $("[name='e_exhaust_point_pressure']").val() == "")
    {
        messageToast('info', '请输入压力值！',4000);

    } else {
    $.ajax({
        cache: true,
        type: "POST",
        url: './biomassByPressure',
        data: $('#biomasschpSteamTurbine').serialize(),
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，保存失败！',3000);
        },
        success: function (data) {
             $("[name='e_exhaust_point_temperature']").val(data.temperature.temperature.toFixed(2));
        }
    });  
    }
}

function byPressureEntropy() {
    if ($("[name='e_exhaust_point_pressure']").val() == null || $("[name='e_exhaust_point_pressure']").val() == "")
    {
        messageToast('info', '请输入压力值！',4000);

    } else if($("[name='e_exhaust_point_entropy']").val() == null || $("[name='e_exhaust_point_entropy']").val() == "") {
        messageToast('info', '请输入熵值！',4000);
    } else {
    $.ajax({
        cache: true,
        type: "POST",
        url: './byPressureEntropy',
        data: $('#biomasschpSteamTurbine').serialize(),
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，保存失败！',3000);
        },
        success: function (data) {
             $("[name='e_exhaust_point_temperature']").val(data.temperature.temperature.toFixed(2));
        }
    });  
    }
}

function byTemperatureBack() {
    if ($("[name='e_backpressure_temperature']").val() == null || $("[name='e_backpressure_temperature']").val() == "")
    {
        messageToast('info', '请输入温度值！',4000);

    } else {
    $.ajax({
        cache: true,
        type: "POST",
        url: './byTemperatureBack',
        data: $('#biomasschpSteamTurbine').serialize(),
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，保存失败！',3000);
        },
        success: function (data) {
             $("[name='e_backpressure_pressure']").val(data.pressure.pressure.toFixed(3));
        }
    });  
    }
}

function byPressureBack() {
    if ($("[name='e_backpressure_pressure']").val() == null || $("[name='e_backpressure_pressure']").val() == "")
    {
        messageToast('info', '请输入压力值！',4000);

    } else {
    $.ajax({
        cache: true,
        type: "POST",
        url: './byPressureBack',
        data: $('#biomasschpSteamTurbine').serialize(),
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，保存失败！',3000);
        },
        success: function (data) {
             $("[name='e_backpressure_temperature']").val(data.temperature.temperature.toFixed(2));
        }
    });  
    }
}

function byPressureEntropyBack() {
    if ($("[name='e_backpressure_pressure']").val() == null || $("[name='e_backpressure_pressure']").val() == "")
    {
        messageToast('info', '请输入压力值！',4000);

    } else if($("[name='e_exhaust_after_entropy']").val() == null || $("[name='e_exhaust_after_entropy']").val() == "") {
        messageToast('info', '请先计算抽汽后熵值！',4000);
    } else {
    $.ajax({
        cache: true,
        type: "POST",
        url: './byPressureEntropyBack',
        data: $('#biomasschpSteamTurbine').serialize(),
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，保存失败！',3000);
        },
        success: function (data) {
             $("[name='e_backpressure_enthalpy']").val(data.enthalpy.enthalpy.toFixed(2));
        }
    });  
    }
}

function byTemperatureEntropyBack() {
    if ($("[name='e_backpressure_temperature']").val() == null || $("[name='e_backpressure_temperature']").val() == "")
    {
        messageToast('info', '请输入温度值！',4000);

    } else if($("[name='e_exhaust_after_entropy']").val() == null || $("[name='e_exhaust_after_entropy']").val() == "") {
        messageToast('info', '请先计算抽汽后熵值！',4000);
    } else {
    $.ajax({
        cache: true,
        type: "POST",
        url: './byTemperatureEntropyBack',
        data: $('#biomasschpSteamTurbine').serialize(),
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，保存失败！',3000);
        },
        success: function (data) {
             $("[name='e_backpressure_enthalpy']").val(data.enthalpy.enthalpy.toFixed(2));
        }
    });  
    }
}