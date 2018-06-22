var oldFormData;

$(document).ready(function () {
    init();
    
    getTurbineAuxiliaryDataByPlanId();

    $('#submitTurbineAuxiliary').bind('click', submitTurbineAuxiliary);

    // 点击选择模块
    $('.left-select').bind('click', function(){
        // 当前页面所有模块list
        listModule = ["q-1", "q-2", "q-3", "q-4", "q-5", "q-6", "q-7", "q-8", "q-9", "q-10", "q-11", "q-12"];
        var moduleName = $(this).attr("id");
        // 切换页面右侧内容
        changeModule(listModule, moduleName);
    });
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

    createLabelBind("GPG_TurbineAuxiliarySystemForm", oldFormData);
});

function getTurbineAuxiliaryDataByPlanId() {
    planId = $('#GPGCurrentPlanId').val();
    $.ajax({
        cache: true,
        type: "POST",
        url: './getTurbineAuxiliaryByPlanId',
        data: { "planId": planId },
        async: false,
        error: function (request) {
            messageToast('error', '发生异常！',3000);
        },
        success: function (data) {
            assignmentForm(data.TurbineAuxiliaryJson, "GPG_TurbineAuxiliarySystemForm");
            var dataformInit = $("#GPG_TurbineAuxiliarySystemForm").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
        }
    });
}

function submitTurbineAuxiliary() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './GPG_SaveTurbineAuxiliaryData',
        data: $('#GPG_TurbineAuxiliarySystemForm').serialize(),
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
                assignmentForm(data.newDatas, "GPG_TurbineAuxiliarySystemForm");
                var dataformInit = $("#GPG_TurbineAuxiliarySystemForm").serializeArray();  
                oldFormData = JSON.stringify({ dataform: dataformInit });
                createLabelBind("GPG_TurbineAuxiliarySystemForm", oldFormData);
                messageToast('success', '煤气发电-汽机辅机系统数据保存成功！',2000);
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
}


//获取form中的所有的<input>对象
function getElements() {
    var tagElements = $("#GPG_TurbineAuxiliarySystemForm input");
    var elements = new Array();
    for (var j = 0; j < tagElements.length; j++) {
        elements.push(tagElements[j].name);
    }
    return elements;
}
*/
