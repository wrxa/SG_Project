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
    var sorts = ['width', 'coefficient'];

    $("#beltWidth").change(function () {

        var id = $(this).val();
            $.ajax({
                url: './beltSort',
                data: { "id": id },
                type: 'post',
                cache: false,
                dataType: 'json',
                success: function (data) {
                    $("#belt_coefficient").val(data.beltSort.coefficient);
                    var dataformInit = $("#biomasschpStorTran").serializeArray();  
                    oldFormData = JSON.stringify({ dataform: dataformInit });
                    createLabelBind("biomasschpStorTran", oldFormData);
                },
                error: function () {
                    alert("异常！");
                }
            });

    });

    // 根据锅炉类型，获得锅炉年利用时间
    getAnnualHours();

     // 过热蒸汽额定流量，设定双螺旋给料机组数的默认值
    getDuplexNumber();
    
    // 获得燃料运输页面初期数据
    initSortTran();

    // 给保存按钮绑定事件
    $('#submitData').bind('click', submitSortTran);

    // 给清空按钮绑定事件
    $('#clearData').bind('click', clearSortTran);
    // 点击选择模块
    $('.left-select').bind('click', function(){
        // 当前页面所有模块list
        listModule = ["fs-1", "fs-2", "fs-3", "fs-4", "fs-5", "fs-6", "fs-7", "fs-8", "fs-9"];
        var moduleName = $(this).attr("id");
        // 切换页面右侧内容
        changeModule(listModule, moduleName);
    });
    createLabelBind("biomasschpStorTran", oldFormData);
});

//获得锅炉年利用时间
function getAnnualHours() {
    planId = $('#planId').val();
    $.ajax({
        cache: true,
        type: "POST",
        url: './biomassGetAnnualHours',
        data: { "planId": planId },
        async: false,
        error: function (request) {
            alert("Connection error1");
        },
        success: function (data) {
            var boiler_type = data.boilerType;     
            switch (boiler_type)
            {
                //常规循环流化床锅炉（CFB）,高低差速循环流化床锅炉（ICFB）
                case "1":case "2":
                    $("#b_annual_use_hours_design").val('7200');
                    $("#b_annual_use_hours_check").val('7200');
                    break;
                //联合炉排炉
                case "3":
                    $("#b_annual_use_hours_design").val('7500');
                    $("#b_annual_use_hours_check").val('7500');
                    break;
                //水冷振动炉排炉
                case "4":
                    $("#b_annual_use_hours_design").val('8000');
                    $("#b_annual_use_hours_check").val('8000');
                    break;
                default:
                    break;
            }
            var dataformInit = $("#biomasschpStorTran").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
            createLabelBind("biomasschpStorTran", oldFormData);
        }
    });
}

//设定双螺旋给料机组数的默认值
function getDuplexNumber() {
    planId = $('#planId').val();
    $.ajax({
        cache: true,
        type: "POST",
        url: './biomassGetDuplexNumber',
        data: { "planId": planId },
        async: false,
        error: function (request) {
            alert("Connection error1");
        },
        success: function (data) {
            var steam_flow = data.steamFlow;
            //过热蒸汽额定流量≤65t/h，则此项默认值自动取2
            if(parseInt(steam_flow) <= 65) {
                $("#s_duplex_number_design").val('2');
                $("#s_duplex_number_check").val('2');
            //过热蒸汽额定流量>65t/h，则此项默认值自动取4
            } else {
                $("#s_duplex_number_design").val('4');
                $("#s_duplex_number_check").val('4');
            }  
            var dataformInit = $("#biomasschpStorTran").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
            createLabelBind("biomasschpStorTran", oldFormData);
        }
    });
}

//燃料运输页面信息初期化
function initSortTran() {
    planId = $('#planId').val();
    $.ajax({
        cache: true,
        type: "POST",
        url: './biomassInitSortTran',
        data: { "planId": planId },
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，页面初期化失败！',3000);
        },
        success: function (data) {
            assignmentForm(data.sorttran);
            var dataformInit = $("#biomasschpStorTran").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
            createLabelBind("biomasschpStorTran", oldFormData);

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
    // 给下拉列表[皮带宽度]赋值
    if(datas['f_belt_width'] != "") {
        $("#beltWidth").val(datas['f_belt_width']);
    }
    
}


//获取form中的所有的<input>对象  
function getElements() {  
    var tagElements = $("#biomasschpStorTran input");  
    var elements = new Array();  
    for (var j = 0; j < tagElements.length; j++){ 
        elements.push(tagElements[j].name); 
    }
    return elements;  
}

function submitSortTran() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './biomassFormDataStorTran',
        data: $('#biomasschpStorTran').serialize(),
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，保存失败！',3000);
        },
        success: function (data) {           
             // 刷新页面
            initSortTran();
            var dataformInit = $("#biomasschpStorTran").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
            createLabelBind("biomasschpStorTran", oldFormData);
            messageToast('success', '生物质热电联产-燃料存储及输送系统数据保存成功！',3000);
        }
    });
}

// 清空表单中的值
function clearSortTran(datas){
    var elements = getElements();
    var tempInput;
    for (var i = 0; i < elements.length; i++) {
        tempInput = elements[i];
        $("input[name='"+tempInput+"']").val("");
    }
    $("#beltWidth").val('');
    var dataformInit = $("#biomasschpStorTran").serializeArray();  
    oldFormData = JSON.stringify({ dataform: dataformInit });
    createLabelBind("biomasschpStorTran", oldFormData);
}