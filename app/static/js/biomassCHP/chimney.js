var oldFormData;

$(document).ready(function () {
    init();
    getBiomassChimneyData();
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
    $('#submitChimney').bind('click', submitChimney);
    // 点击选择模块
    $('.left-select').bind('click', function(){
        // 当前页面所有模块list
        listModule = ["c-1", "c-2", "c-3", "c-4"];
        var moduleName = $(this).attr("id");
        // 切换页面右侧内容
        changeModule(listModule, moduleName);
    });

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
});

function getBiomassChimneyData() {
    planId = $('#planId').val();
    $.ajax({
        cache: true,
        type: "POST",
        url: './getBiomassChimneyData',
        data: { "planId": planId },
        async: false,
        error: function (request) {
            messageToast('error', '发生异常！',3000);
        },
        success: function (data) {
            assignmentForm(data.ChimneyJson, "biomassChimenyForm");
            var dataformInit = $("#biomassChimenyForm").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
            createLabelBind("biomassChimenyForm", oldFormData);

            $('#biomass15').attr('onclick', "messageToast('info', '正在进行出图处理，请稍候！',16000);")
        }
    });
}

function submitChimney() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './BiomassSaveChimneyData',
        data: $('#biomassChimenyForm').serialize(),
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，保存失败！',3000);
        },
        success: function (data) {
            assignmentForm(data.newDatas, "biomassChimenyForm");
            var dataformInit = $("#biomassChimenyForm").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
            createLabelBind("biomassChimenyForm", oldFormData);
            messageToast('success', '生物质热电联产-烟囱数据保存成功！',3000);
        }
    });
}
