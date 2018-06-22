var oldFormData;

var sorts = ['carbon', 'hydrogen', 'oxygen', 'nitrogen', 'sulfur', 'water',
        'daf', 'grey', 'grindability', 'low'];

$(document).ready(function () {

    initFuel();
    // 选择燃料
    $("#fuelDesign").change(function () {
        // 选择其他项时清空当前所有煤质分析值
        var id = $(this).val();
        if (id == "-1") {
            for (var i = 0; i < sorts.length; i++) {
                $("#" + sorts[i] + "_design").val("");
            }
        } else {
            $.ajax({
                url: '/fuelSort',
                data: { "id": id },
                type: 'post',
                cache: false,
                dataType: 'json',
                success: function (data) {
                    var temp;
                    for (var i = 0; i < sorts.length; i++) {
                        temp = sorts[i];
                        $("#" + sorts[i]).val(data.fuelSort[temp]);
                    }
                },
                error: function () {
                    messageToast('error', '发生异常！',3000);
                }
            });
        }
    });

    // 新增燃料时，页面上输入项全部置为空
    $("#fuelNew").focus(function () {
        $("#fuelDesign").val("");

        var elements = getElements();
        var tempInput;
        for (var i = 0; i < elements.length; i++) {
            tempInput = elements[i];
            $("input[name='"+tempInput+"']").val("");

        }
    });

    // 给保存按钮绑定事件
    $('#submitData').bind('click', submitFuel);

});

//页面信息初期化
function initFuel() {
	$.ajax({
	    url: '/initFuel',
	    type: 'post',
	    cache: false,
	    dataType: 'json',
	    success: function (data) {
	        var temp;
	        for (var i = 0; i < sorts.length; i++) {
	            temp = sorts[i];
	            $("#" + sorts[i]).val(data.fuelInit[temp]);
	        }
            $("[name='s_fuel_design']").val("1");
	    },
	    error: function () {
	        messageToast('error', '发生异常！',3000);
	    }
	});
    // $.ajax({
    //     cache: true,
    //     type: "POST",
    //     url: './biomassinitHeat',
    //     data: { "planId": planId },
    //     async: false,
    //     error: function (request) {
    //         messageToast('error', '发生异常，页面初期化失败！',3000);
    //     },
    //     success: function (data) {
    //         assignmentForm(data.heat);
    //         //$("[name='o_boiler_water_system']").val(data.water.o_boiler_water_system.toFixed(0));
    //         var dataformInit = $("#biomasschpHeat").serializeArray();  
    //         oldFormData = JSON.stringify({ dataform: dataformInit });
    //     }
    // });
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
}


//获取form中的所有的<input>对象  
function getElements() {  
    var tagElements = $("#fuelMaintain input");  
    var elements = new Array();  
    for (var j = 0; j < tagElements.length; j++){ 
        elements.push(tagElements[j].name); 
    }
    return elements;  
}

//提交表单信息
function submitFuel() {
    if ($("[name='s_fuel_design']").val() == null && $("[name='s_fuel_new']").val() == '')
    {
        messageToast('info', '请选择或输入燃料名称！',4000);
    } else {

    $.ajax({
        cache: true,
        type: "POST",
        url: './biomassFuelMaintainSave',
        data: $('#fuelMaintain').serialize(),
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，保存失败！',3000);
        },
        success: function (data) {
            messageToast('success', '生物质热电联产-燃料数据保存成功！',3000);
            // 刷新页面
            initFuel();
            $("[name='s_fuel_new']").val("");
            window.location.href="./biomassFuelMaintain"
            // var dataformInit = $("#fuelMaintain").serializeArray();  
            // oldFormData = JSON.stringify({ dataform: dataformInit });
            // createLabelBind("fuelMaintain", oldFormData);
        }
    });
    }
}

