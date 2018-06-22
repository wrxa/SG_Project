var oldFormData;

$(document).ready(function () {
    init();
    var sorts = ['s_carbon', 's_hydrogen', 's_oxygen', 's_nitrogen', 's_sulfur', 's_water',
        's_daf', 's_grey', 's_grindability', 's_low'];

   // 初始化需求调查表数据
    initBiomassQuestionnaire();

    // 选择设计和校核燃料
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
                        temp = sorts[i].substring(2);
                        if(temp == "water") {
                            $("#s_total_moisture_design").val(data.fuelSort[temp])
                        } else if(temp == "low") {
                            $("#s_quantity_design").val(data.fuelSort[temp])
                        } else {
                            $("#" + sorts[i] + "_design").val(data.fuelSort[temp]);
                        }
                            
                    }
                },
                error: function () {
                    messageToast('error', '发生异常！',3000);
                }
            });
        }
    });

    // 煤质分析校核煤种选择
    $("#fuelCheck").change(function () {
        // 选择其他项时清空当前所有煤质分析值
        var id = $(this).val();
        if (id == "-1") {
            for (var i = 0; i < sorts.length; i++) {
                $("#" + sorts[i] + "_check").val("");
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
                        temp = sorts[i].substring(2);
                        if(temp == "water") {
                            $("#s_total_moisture_check").val(data.fuelSort[temp])
                        } else if(temp == "low") {
                            $("#s_quantity_check").val(data.fuelSort[temp])
                        } else {
                            $("#" + sorts[i] + "_check").val(data.fuelSort[temp]);
                        }
                    }
                },
                error: function () {
                    messageToast('error', '发生异常！',3000);
                }
            });
        }
    });

    // 给选择已知方案下拉框绑定事件
    $("#knownPlan").bind('change', updatePlanData);

    // 给保存按钮绑定事件
    $('#submitData').bind('click', submitQuestionnaire);

    // 给清空按钮绑定事件
    $('#clearData').bind('click', clearQuestionnaire);
    // 点击选择模块
    $('.left-select').bind('click', function(){
        // 当前页面所有模块list
        listModule = ["q-1", "q-2", "q-3", "q-4", "q-5","q-6"];
        var moduleName = $(this).attr("id");
        // 切换页面右侧内容
        changeModule(listModule, moduleName);
    });
    createLabelBind("biomasschpQuestionnaire", oldFormData);
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
});

// 提交保存页面所有表单数据
function submitQuestionnaire(){
    if ($("[name='company_name']").val() == "")
    {
        messageToast('info', '公司名是唯一区别方案的标识，不能为空！',4000);
    } else {

    $.ajax({
        cache: true,
        type: "POST",
        url:'/biomassFormData',
        data:$('#biomasschpQuestionnaire').serialize(),
        async: false,
        error: function(request) {
            messageToast('error', '发生异常，保存失败！',3000);
        },
        success: function(data) {
            unlockBreadcrumb();
            messageToast('success', '生物质热电联产-需求调查表数据保存成功！',3000);
            
            window.location.reload();
            var dataformInit = $("#biomasschpQuestionnaire").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
            createLabelBind("biomasschpQuestionnaire", oldFormData);

        }
    });
}
}

// 清空表单中的值
function clearQuestionnaire(datas){
    var elements = getElements();
    var tempInput;
    for (var i = 0; i < elements.length; i++) {
        tempInput = elements[i];
        $("input[name='"+tempInput+"']").val("");
    }
    $("#knownPlan").val("");
}

// 选择已知方案时动态变更所有输入框内值
function updatePlanData(){
    var planId = $(this).val();
    $.ajax({
        cache: true,
        type: "POST",
        url:'/biomassFindPlan',
        data: { "planId": planId },
        async: false,
        error: function(request) {
            messageToast('error', '发生异常，选择方案失败！',3000);
        },
        success: function(data) {
            unlockBreadcrumb();
            assignmentForm(data.questionnaire);
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
        if (datas[tempInput] != "" || datas[tempInput] == "0") {
            $("input[name='"+tempInput+"']").val(datas[tempInput]);
        }
        // valid(tempInput, notvalidcolumname);
    }

    // 给select框赋值
    if(datas['s_fuel_check'] != null){
        $("#fuelCheck").val(datas['s_fuel_check']);
    }
    if(datas['s_fuel_design'] != null){
        $("#fuelDesign").val(datas['s_fuel_design']);
    }
}


//获取form中的所有的<input>对象  
function getElements() {  
    var tagElements = $("#biomasschpQuestionnaire input");  
    var elements = new Array();  
    for (var j = 0; j < tagElements.length; j++){ 
        elements.push(tagElements[j].name); 
    }
    return elements;  
}

function initBiomassQuestionnaire() {
    $.ajax({
        cache: true,
        type: "POST",
        url: '/initBiomassQuestionnaire',
        async: false,
        error: function (request) {
            messageToast('error', '发生异常！',3000);
        },
        success: function (data) {
            if (data.questionnaire != "null") {
                assignmentForm(data.questionnaire);
            }
            var dataformInit = $("#biomasschpQuestionnaire").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
            
            $('#biomass15').attr('onclick', "messageToast('info', '正在进行出图处理，请稍候！',16000);")
        }
    });
}