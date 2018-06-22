$(document).ready(function () {

    getWindResistanceDataByPlanId();

    $('#submitWindResistance').bind('click', submitWindResistance);
});

function getWindResistanceDataByPlanId() {
    planId = $('#GPGCurrentPlanId').val();
    $.ajax({
        cache: true,
        type: "POST",
        url: './getWindResistanceByPlanId',
        data: { "planId": planId },
        async: false,
        error: function (request) {
            alert("Connection error");
        },
        success: function (data) {
            assignmentForm(data.WindResistanceJson);
        }
    });
}

function submitWindResistance() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './GPG_SaveWindResistanceData',
        data: $('#GPG_WindResistanceForm').serialize(),
        async: false,
        error: function (request) {
            alert("Connection error");
        },
        success: function (data) {
            alert("成功！！！");
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
    //$("#boilerType").val(datas['boiler_type']);
    //$("#pressureType").val(datas['pressure_temperature']);
}


//获取form中的所有的<input>对象
function getElements() {
    var tagElements = $("#GPG_WindResistanceForm input");
    var elements = new Array();
    for (var j = 0; j < tagElements.length; j++) {
        elements.push(tagElements[j].name);
    }
    return elements;
}
