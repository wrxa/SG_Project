$(document).ready(function () {
    unlockMenuGPG();

    getSmokeAirCalculateDataByPlanId();

    $('#submitSmokeAirCalculateData').bind('click', submitSmokeAirCalculateData);
});

function getSmokeAirCalculateDataByPlanId() {
    planId = $('#GPGCurrentPlanId').val();
    $.ajax({
        cache: true,
        type: "POST",
        url: './getSmokeAirCalculateDataByPlanId',
        data: { "planId": planId },
        async: false,
        error: function (request) {
            alert("Connection error");
        },
        success: function (data) {
            assignmentForm(data.SmokeAirCalculateJson);
        }
    });
}

function submitSmokeAirCalculateData() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './GPG_SaveSmokeAirCalculateData',
        data: $('#GPG_SmokeAirCalculateForm').serialize(),
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
}


//获取form中的所有的<input>对象
function getElements() {
    var tagElements = $("#GPG_SmokeAirCalculateForm input");
    var elements = new Array();
    for (var j = 0; j < tagElements.length; j++) {
        elements.push(tagElements[j].name);
    }
    return elements;
}
