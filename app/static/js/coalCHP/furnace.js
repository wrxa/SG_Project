var oldFormData;

$(document).ready(function () {
    init();
    hiddenUnit();
    // 给保存按钮绑定事件
    initFurnace();
    $('#submitData').bind('click', submitFurnace);

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

   //选择不同的温度压力，下列项目显示不同的值
   $("#pressureType").change(function () {
        var id = $(this).val();
        switch (id){
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
    // 点击选择模块
    $('.left-select').bind('click', function(){
        // 当前页面所有模块list
        listModule = ["f-1", "f-2", "f-3", "f-4", "f-7", "f-8", "f-9", "f-10", "f-11"];
        var moduleName = $(this).attr("id");
        // 切换页面右侧内容
        changeModule(listModule, moduleName);
    });
    createLabelBind("coalFurnaceForm", oldFormData);
});

function initFurnace() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './initFurnace',
        async: false,
        error: function (request) {
            messageToast('error', '发生异常！',3000);
        },
        success: function (data) {
            assignmentForm(data.furnace, "coalFurnaceForm");
            if (data.furnace.boiler_params_select == "") {
                $("#pressureType").val(0);
            }
            else{
                $("#pressureType").val(data.furnace.boiler_params_select);
            }
            var dataformInit = $("#coalFurnaceForm").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
        }
    });
}

function assignmentForm(datas, formName) {
    var notvalidcolumname = ["p_heater_type_design", "p_heater_type_check"];
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
function submitFurnace() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './formDataFurnace',
        data: $('#coalFurnaceForm').serialize(),
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，保存失败！',3000);
        },
        success: function (data) {
            assignmentForm(data.newDatas, "coalFurnaceForm");
            $("#pressureType").val(data.newDatas.boiler_params_select);
            var dataformInit = $("#coalFurnaceForm").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
            createLabelBind("coalFurnaceForm", oldFormData);
            messageToast('success', '燃煤热电联产-锅炉本体计算数据保存成功！',3000);
        }
    });
}

