var oldFormData;

$(document).ready(function () {
    init();
    //unlockMeunBiomassCHP();
    // 获得锅炉辅机页面初期数据
    initAuxiliaries();
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
    // 给保存按钮绑定事件
    $('#submitData').bind('click', submitAuxiliaries);

    // 给清空按钮绑定事件
    $('#clearData').bind('click', clearAuxiliaries);
    // 点击选择模块
    $('.left-select').bind('click', function(){
        // 当前页面所有模块list
        listModule = ["b-1", "b-2", "b-3", "b-4", "b-5", "b-6", "b-7", "b-8", "b-9", "b-10", "b-11", "b-12", "b-13", "b-14"];
        var moduleName = $(this).attr("id");
        // 切换页面右侧内容
        changeModule(listModule, moduleName);
    });
    

    $("#info1").on("click", function () {
        $("#showInfo").modal('show');
        $("#infoContent").html("<img class='img-responsive center-block' src='static/img/BiomassCHP/atmosphere.png'/>");
    });

    $("#info2").on("click", function () {
        $("#showInfo").modal('show');
        $("#infoContent").html("<img class='img-responsive center-block' src='static/img/BiomassCHP/regular.png'/>");
    });

    $("#info3").on("click", function () {
        $("#showInfo").modal('show');
        $("#infoContent").html("<img class='img-responsive center-block' src='static/img/BiomassCHP/continuous.png'/>");
    });

});


//锅炉辅机页面信息初期化
function initAuxiliaries() {
    planId = $('#planId').val();
    $.ajax({
        cache: true,
        type: "POST",
        url: './biomassinitAuxiliaries',
        data: { "planId": planId },
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，页面初期化失败！',3000);
        },
        success: function (data) {
            assignmentForm(data.auxiliaries);
            var dataformInit = $("#biomasschpAuxiliaries").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
            createLabelBind("biomasschpAuxiliaries", oldFormData);

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

    // 没有大气压的场合,用海拔（不为空）计算大气压
    if(datas['a_atmosphere'] == "" && datas['a_altitude'] != ""){
        var atmosphere = atmosphereCal(datas['a_altitude']);
        $("input[name='a_atmosphere']").val(atmosphere);
        messageToast('info', '需求调研表中无当地历年平均气压数据，已按公式重新计算大气压！',4000);
    }
}


//获取form中的所有的<input>对象  
function getElements() {  
    var tagElements = $("#biomasschpAuxiliaries input");  
    var elements = new Array();  
    for (var j = 0; j < tagElements.length; j++){ 
        elements.push(tagElements[j].name); 
    }
    return elements;  
}

//提交表单信息
function submitAuxiliaries() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './biomassFormDataAuxiliaries',
        data: $('#biomasschpAuxiliaries').serialize(),
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，保存失败！',3000);
        },
        success: function (data) {           
            // 刷新页面
            initAuxiliaries();

            var dataformInit = $("#biomasschpAuxiliaries").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
            createLabelBind("biomasschpAuxiliaries", oldFormData);

            messageToast('success', '生物质热电联产-锅炉辅机数据保存成功！',3000);
        }
    });
}

// 清空表单中的值
function clearAuxiliaries(datas){
    var elements = getElements();
    var tempInput;
    for (var i = 0; i < elements.length; i++) {
        tempInput = elements[i];
        $("input[name='"+tempInput+"']").val("");
    }
    var dataformInit = $("#biomasschpAuxiliaries").serializeArray();  
    oldFormData = JSON.stringify({ dataform: dataformInit });
    createLabelBind("biomasschpAuxiliaries", oldFormData);
}

//计算大气压
function atmosphereCal(altitude){
    var atmosphere = Math.round(1013.25*Math.pow((1-altitude/44330),5.255)*100);
    return atmosphere;
}