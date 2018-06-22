var oldFormData;

$(document).ready(function () {
    init();
    //unlockMeunBiomassCHP();
    update_flg = false;
    
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
                $("#f_unburned_loss_design").val("1");
                $("#f_unburned_loss_check").val("1");
                $("#prompt2").attr("data-content","0.5~2%");
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
                $("#f_unburned_loss_design").val("1");
                $("#f_unburned_loss_check").val("1");
                $("#prompt2").attr("data-content","0.5~2%");
                $("#d_ash_share_design").val("0.9");
                $("#d_ash_share_check").val("0.9");
                $("#d_dust_share_design").val("0.1");
                $("#d_dust_share_check").val("0.1");
                break;
            //联合炉排炉
            case "3":
                $("#f_boiler_efficiency_design").val("86");
                $("#f_boiler_efficiency_check").val("86");
                $("#f_unburned_loss_design").val("2");
                $("#f_unburned_loss_check").val("2");
                $("#prompt2").attr("data-content","2~4%");
                $("#d_ash_share_design").val("0.6");
                $("#d_ash_share_check").val("0.6");
                $("#d_dust_share_design").val("0.4");
                $("#d_dust_share_check").val("0.4");
                break;
            //水冷振动炉排炉
            case "4":
                $("#f_boiler_efficiency_design").val("87");
                $("#f_boiler_efficiency_check").val("87");
                $("#f_unburned_loss_design").val("2");
                $("#f_unburned_loss_check").val("2");
                $("#prompt2").attr("data-content","2~4%");
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
                $("#prompt").attr("data-content","210,220");
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
                $("#prompt").attr("data-content","150,104");
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
                $("#prompt").attr("data-content","158,104");
                break;
        }
    });

    // 获得锅炉页面初期数据
    initFurnace();
    // 给保存按钮绑定事件
    $('#submitData').bind('click', submitFurnace);

    // 给清空按钮绑定事件
    $('#clearData').bind('click', clearFurnace);
    // 点击选择模块
    $('.left-select').bind('click', function(){
        // 当前页面所有模块list
        listModule = ["f-1", "f-2", "f-3", "f-4", "f-5", "f-6", "f-7", "f-8", "f-9", "f-10"];
        var moduleName = $(this).attr("id");
        // 切换页面右侧内容
        changeModule(listModule, moduleName);
    });
    createLabelBind("biomassFurnaceForm", oldFormData);
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
});

//锅炉页面信息初期化
function initFurnace() {
    planId = $('#planId').val(); 

    $.ajax({
        cache: true,
        type: "POST",
        url: './biomassInitFurnace',
        data: { "planId": planId },
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，页面初期化失败！',3000);
        },
        success: function (data) {
            furnaceData = data.furnace;          
            assignmentForm(data.furnace);
        }
    });

    //给水温度的推荐值
    if($("#f_water_temperature_design").val() == "215") {
        $("#prompt").attr("data-content","210,220");
    }

    if($("#f_water_temperature_design").val() == "158") {
        $("#prompt").attr("data-content","150,104");
    }

    if($("#f_water_temperature_design").val() == "150") {
        $("#prompt").attr("data-content","158,104");
    }

    //机械未燃烧损失的推荐值
    if($("#f_unburned_loss_design").val() == "1") {
        $("#prompt2").attr("data-content","0.5~2%");
    }

    if($("#f_unburned_loss_design").val() == "2") {
        $("#prompt2").attr("data-content","2~4%");
    }
    var dataformInit = $("#biomassFurnaceForm").serializeArray();  
    oldFormData = JSON.stringify({ dataform: dataformInit });

    $('#biomass15').attr('onclick', "messageToast('info', '正在进行出图处理，请稍候！',16000);")
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
            messageToast('error', '发生异常，保存失败！',3000);
        },
        success: function (data) {
            messageToast('success', '生物质热电联产-锅炉计算数据保存成功！',3000);
            update_flg = true;
            // 刷新页面
            initFurnace();
            var dataformInit = $("#biomassFurnaceForm").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
            createLabelBind("biomassFurnaceForm", oldFormData);
        }
    });
}

// 给页面中所有表单赋值
function assignmentForm(datas) {
    var notvalidcolumname = [];
    var elements = getElements();
    var tempInput;
    var boolFlg_design = false;
    var boolFlg_check = false;
    var sQuantityDesign = $('#quantity_design').val();
    var sQuantityCheck = $('#quantity_check').val();

    for (var i = 0; i < elements.length; i++) {
        tempInput = elements[i];
        if(datas[tempInput] != "" || datas[tempInput] == "0") {
            $("input[name='" + tempInput + "']").val(datas[tempInput]);
        }
        // valid(tempInput, notvalidcolumname);
    }
    // 给下拉列表[锅炉类型，温度压力]赋值
    $("#boilerType").val(datas['boiler_type']);
    $("#pressureType").val(datas['pressure_temperature']);

    //若需求调研表中，设计燃料收到基水分＞30%，校核燃料收到基水分＞40%，
    //则需对燃料收到基低位发热量按标准水分进行修正计算
    if(datas['c_water_content_received_design'] > 30 && datas['c_base_heat_received_user_design'] != "" && sQuantityDesign == datas['c_base_heat_received_user_design']){
        //重新计算收到基低位发热量
        dBaseHeatCal(datas['c_water_content_received_design'],datas['c_base_heat_received_user_design']);
        dBaseHeatCal2(datas['c_water_content_received_design'],datas['c_base_heat_received_user_design']);
        boolFlg_design = true;
    }
    if(datas['c_water_content_received_check'] > 40 && datas['c_base_heat_received_user_check'] != "" && sQuantityCheck == datas['c_base_heat_received_user_check']){
        //重新计算收到基低位发热量
        cBaseHeatCal(datas['c_water_content_received_check'],datas['c_base_heat_received_user_check']);
        cBaseHeatCal2(datas['c_water_content_received_check'],datas['c_base_heat_received_user_check']);
        boolFlg_check = true;
    }

    if(update_flg == false) {
        if(boolFlg_design == true && boolFlg_check == true) {
           messageToast('info_long', '需求调研表中，设计燃料收到基水分＞30%，校核燃料收到基水分＞40%，则需对燃料收到基低位发热量按标准水分进行修正计算',4000); 
        } else if(boolFlg_design == true) {
           messageToast('info_long', '需求调研表中设计燃料收到基水分＞30%，对设计燃料收到基低位发热量按标准水分30%进行修正计算！',4000);
        } else if(boolFlg_check == true) {
           messageToast('info_long', '需求调研表中校核燃料收到基水分＞40%，对校核燃料收到基低位发热量按标准水分40%进行修正计算！',4000);
        } else {

        }
    }
    update_flg = false;
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

// 清空表单中的值
function clearFurnace(datas){
    var elements = getElements();
    var tempInput;
    for (var i = 0; i < elements.length; i++) {
        tempInput = elements[i];
        $("input[name='"+tempInput+"']").val("");
    }
    $("#boilerType").val("");
    $("#pressureType").val("");
}

function dBaseHeatCal(water,heat){
    base_value=heat-(30-water)*193.4;
    $("input[name='c_base_heat_received_user_design']").val(base_value);
    var dataformInit = $("#biomassFurnaceForm").serializeArray();  
    oldFormData = JSON.stringify({ dataform: dataformInit });
    createLabelBind("biomassFurnaceForm", oldFormData);
}

function cBaseHeatCal(water,heat){
    base_value=heat-(40-water)*193.4;
    $("input[name='c_base_heat_received_user_check']").val(base_value);
    var dataformInit = $("#biomassFurnaceForm").serializeArray();  
    oldFormData = JSON.stringify({ dataform: dataformInit });
    createLabelBind("biomassFurnaceForm", oldFormData);
}

function dBaseHeatCal2(water,heat){
    base_value=(heat-(30-water)*193.4)/4.1868;
    $("input[name='c_base_heat_received_calculation_design']").val(base_value);
    var dataformInit = $("#biomassFurnaceForm").serializeArray();  
    oldFormData = JSON.stringify({ dataform: dataformInit });
    createLabelBind("biomassFurnaceForm", oldFormData);
}

function cBaseHeatCal2(water,heat){
    base_value=(heat-(40-water)*193.4)/4.1868;
    $("input[name='c_base_heat_received_calculation_check']").val(base_value);
    var dataformInit = $("#biomassFurnaceForm").serializeArray();  
    oldFormData = JSON.stringify({ dataform: dataformInit });
    createLabelBind("biomassFurnaceForm", oldFormData);
}
