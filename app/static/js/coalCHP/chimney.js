var oldFormData;

$(document).ready(function () {
    init();
    getCoalChimneyData();

    $('#submitChimney').bind('click', submitChimney);
    // 点击选择模块
    $('.left-select').bind('click', function(){
        // 当前页面所有模块list
        listModule = ["c-1", "c-2", "c-3", "c-4"];
        var moduleName = $(this).attr("id");
        // 切换页面右侧内容
        changeModule(listModule, moduleName);
    });
    createLabelBind("coalChimenyForm", oldFormData);

    $("#info1").on("click", function () {
        $("#showInfo").modal('show');
        $("#infoContent").html("<img class='img-responsive center-block' src='static/img/BiomassCHP/BiomassChimney/4-18-1.jpg'/>");
    });

    $("#info2").on("click", function () {
        $("#showInfo").modal('show');
        $("#infoContent").html("<img class='img-responsive center-block' src='static/img/BiomassCHP/BiomassChimney/4-18-2.jpg'/>");
    });

    $("#info3").on("click", function () {
        $("#showInfo").modal('show');
        $("#infoContent").html("<img class='img-responsive center-block' src='static/img/BiomassCHP/BiomassChimney/windSpeed.png'/>");
    });

    $("#info4").on("click", function () {
        $("#showInfo").modal('show');
        $("#infoContent").html("<img class='img-responsive center-block' src='static/img/BiomassCHP/BiomassChimney/7-28.png'/>");
    });
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
});

function getCoalChimneyData() {
    planId = $('#planId').val();
    $.ajax({
        cache: true,
        type: "POST",
        url: './getcoalChimneyData',
        data: { "planId": planId },
        async: false,
        error: function (request) {
            messageToast('error', '发生异常！',3000);
        },
        success: function (data) {
            assignmentForm(data.ChimneyJson, "coalChimenyForm");
            var dataformInit = $("#coalChimenyForm").serializeArray();  
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

function submitChimney() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './coalSaveChimneyData',
        data: $('#coalChimenyForm').serialize(),
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，保存失败！',3000);
        },
        success: function (data) {
            assignmentForm(data.newDatas, "coalChimenyForm");
            var dataformInit = $("#coalChimenyForm").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
            createLabelBind("coalChimenyForm", oldFormData);
            messageToast('success', '燃煤热电联产-烟囱数据保存成功！',3000);
        }
    });
}
