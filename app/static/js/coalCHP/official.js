var oldFormData;

$(document).ready(function () {
    init();
    //unlockMeunBiomassCHP();
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


    //选择不同的锅炉，点火方式不同
    // $("#boilerType").change(function () {
    //     var id = $(this).val();
    //     switch (id)
    //     {
    //         //空白
    //         case "0":
    //             $("#fireWay").val("");
    //             $("." + "o-2").addClass('hide');
    //             break;
    //         //层燃炉
    //         case "1":
    //             $("#fireWay").val("人工点火（即床上火把点火）");
    //             $("." + "o-2").addClass('hide');
    //             break;
    //         //循环流化床锅炉
    //         case "2":
    //             $("#fireWay").val("0#轻柴油点火（一般为床下点火）");
    //             $("." + "o-2").removeClass('hide');
    //             break;
    //     }
    // });

    // 获得公用工程页面初期数据
    initOfficial();

    // if($("#boilerType").val() == "2") {
    //     $("." + "o-2").removeClass('hide');
    // }

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

        // if(moduleName == 'o-3') {
        //     $("." + "o-2").addClass('hide');
        // }
        // // 获得公用工程页面初期数据
        initOfficial();

        // if($("#boilerType").val() == "2" && moduleName == 'o-1') {
        //     $("." + "o-2").removeClass('hide');
        // }

    });

    // if($("#boilerType").val() == "2") {
    //     $("." + "o-2").removeClass('hide');
    // }


    createLabelBind("coalchpOfficial", oldFormData);
});

//锅炉辅机页面信息初期化
function initOfficial() {
    planId = $('#planId').val();
    $.ajax({
        cache: true,
        type: "POST",
        url: './coalinitOfficial',
        data: { "planId": planId },
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，页面初期化失败！',3000);
        },
        success: function (data) {
            assignmentForm(data.official);
            var dataformInit = $("#coalchpOfficial").serializeArray();  
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


// 给页面中所有表单赋值
function assignmentForm(datas){
    var elements = getElements();
    var tempInput;
    for (var i = 0; i < elements.length; i++) {
        tempInput = elements[i];
        if(datas[tempInput] != "" || datas[tempInput] == "0") {
            $("input[name='"+tempInput+"']").val(datas[tempInput]);
        }
    }

    // 给下拉列表[锅炉类型，点火方式，燃料类型]赋值
    if(datas['o_boiler_type'] == '' || datas['o_boiler_type'] == null){
        $("input[name='o_boiler_type']").val("循环流化床锅炉");
    }
    if(datas['o_fire_way'] == '' || datas['o_fire_way'] == null){
        $("input[name='o_fire_way']").val("0#轻柴油点火（一般为床下点火）");
    }
    $("#fuelType").val(datas['o_fuel_type']);

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
    var tagElements = $("#coalchpOfficial input");  
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
        url: './coalFormDataOfficial',
        data: $('#coalchpOfficial').serialize(),
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，保存失败！',3000);
        },
        success: function (data) {
            messageToast('success', '燃煤热电联产-公用工程数据保存成功！',3000);
            // 刷新页面
            initOfficial();
            var dataformInit = $("#coalchpOfficial").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
            createLabelBind("coalchpOfficial", oldFormData);
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

    // $("#boilerType").val("");
    // $("#fireWay").val("");
    // $("#fuelType").val("");
}

function oilPumpCal(){
    planId = $('#planId').val();
    $.ajax({
        cache: true,
        type: "POST",
        url: './coalOilPumpCal',
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