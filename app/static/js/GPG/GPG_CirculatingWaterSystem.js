var oldFormData;
$(document).ready(function () {
    init();
    
    getCirculatingWaterDataByPlanId();

    $('#submitCirculatingWaterData').bind('click', submitCirculatingWaterData);

    // 点击选择模块
    $('.left-select').bind('click', function(){
        // 当前页面所有模块list
        listModule = ["q-1", "q-2", "q-3", "q-4", "q-5", "q-6", "q-7", "q-8", "q-9", "q-10", "q-11", "q-12"];
        var moduleName = $(this).attr("id");
        // 切换页面右侧内容
        changeModule(listModule, moduleName);
    })
    // 定义面包屑个数
    var breakCount = 12;
    // 定义面包屑上id的模块类型
    var moduleName = "gpg";
    initPreNext(moduleName, breakCount);
    // 上一页
    $('.pre').bind('click', function(){
        clickPre(breakCount, moduleName);
    });
    // 下一页
    $('.next').bind('click', function(){
        clickNext(breakCount, moduleName);
    });
    $("#cooling_tower_selected_type").change(function(){
        var id = $(this).val();
        switch(id){
            case "1":
                $("#cooling_tower1")[0].style.display='block';
                $("#cooling_tower2")[0].style.display='none';
                break;
            case "2":
                $("#cooling_tower1")[0].style.display='none';
                $("#cooling_tower2")[0].style.display='block';
                break;
        }
    });

    $("#info1").on("click", function () {
        $("#showInfo").modal('show');
        $("#infoContent").html("<img class='img-responsive center-block' src='static/img/GPG/GPG_CirculatingWaterSystem/5.6.1.png'/>");
    });

    createLabelBind("GPG_CirculatingWaterSystemForm", oldFormData);
});

function getCirculatingWaterDataByPlanId() {
    planId = $('#GPGCurrentPlanId').val();
    $.ajax({
        cache: true,
        type: "POST",
        url: './getCirculatingWaterDataByPlanId',
        data: { "planId": planId },
        async: false,
        error: function (request) {
            messageToast('error', '发生异常！',3000);
        },
        success: function (data) {
            assignmentForm(data.CirculatingWaterJson, "GPG_CirculatingWaterSystemForm");
            if(data.CirculatingWaterJson['cooling_tower_selected_type'] == 1){
                $("#cooling_tower_selected_type").val("1");
                $("#cooling_tower1")[0].style.display='block';
                $("#cooling_tower2")[0].style.display='none';
            }else{
                $("#cooling_tower_selected_type").val("2");
                $("#cooling_tower1")[0].style.display='none';
                $("#cooling_tower2")[0].style.display='block';
            }
            var dataformInit = $("#GPG_CirculatingWaterSystemForm").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
        }
    });
}

function submitCirculatingWaterData() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './GPG_SaveCirculatingWaterData',
        data: $('#GPG_CirculatingWaterSystemForm').serialize(),
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，保存失败！',3000);
        },
        success: function (data) {
            if(data.newDatas == null){
                messageToast('error', '输入数据有误，转换发生异常!', 3000);
            }else if(data.newDatas == "-1"){
                messageToast('error', '输入数据有误，出现除0情况!', 3000);
            }else if(data.newDatas == "0"){
                messageToast('error', '数据有误，数据库计算中可能出现了除0情况!', 3000);
            }else{
                assignmentForm(data.newDatas, "GPG_CirculatingWaterSystemForm");
                var dataformInit = $("#GPG_CirculatingWaterSystemForm").serializeArray();  
                oldFormData = JSON.stringify({ dataform: dataformInit });
                createLabelBind("GPG_CirculatingWaterSystemForm", oldFormData);
                messageToast('success', '煤气发电-循环水系统数据保存成功！',2000);
            }
            
        }
    });
}

/*
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
    var tagElements = $("#GPG_CirculatingWaterSystemForm input");
    var elements = new Array();
    for (var j = 0; j < tagElements.length; j++) {
        elements.push(tagElements[j].name);
    }
    return elements;
}*/
