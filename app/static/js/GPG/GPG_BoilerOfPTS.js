$(document).ready(function () {
    unlockMenuGPG();

    getBoilerDataByPlanId();

    $('#submitBoiler').bind('click', submitBoiler);
});

function getBoilerDataByPlanId() {
    planId = $('#GPGCurrentPlanId').val();
    $.ajax({
        cache: true,
        type: "POST",
        url: './getBoilerByPlanId',
        data: { "planId": planId },
        async: false,
        error: function (request) {
            alert("Connection error");
        },
        success: function (data) {
            assignmentForm(data.BoilerJson);
        }
    });
}

// 提交锅炉页面所有表单数据
function submitBoiler() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './GPG_SaveBoilerOfPTS',
        data: $('#GPG_BoilerForm').serialize(),
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
    var tagElements = $("#GPG_BoilerForm input");
    var elements = new Array();
    for (var j = 0; j < tagElements.length; j++) {
        elements.push(tagElements[j].name);
    }
    return elements;
}
