var oldFormData;

$(document).ready(function () {
    init();
    hiddenUnit();
    $("[name='company_name']").focus();
    var sorts = ['s_carbon', 's_hydrogen', 's_oxygen', 's_nitrogen', 's_sulfur', 's_water',
        's_grey', 's_daf', 's_grindability', 's_low'];

    // 初始化需求调查表数据
    initQuestionnaire();
    // 煤质分析设计煤种选择
    $("#coalDesign").change(function () {
        // 选择其他项时清空当前所有煤质分析值
        var id = $(this).val();
        if (id == "-1") {
            for (var i = 0; i < sorts.length; i++) {
                $("#" + sorts[i] + "_design").val("");
            }
        } else {
            $.ajax({
                url: '/coalSort',
                data: { "id": id },
                type: 'post',
                cache: false,
                dataType: 'json',
                success: function (data) {
                    var temp;
                    for (var i = 0; i < sorts.length; i++) {
                        temp = sorts[i];
                        $("#" + sorts[i] + "_design").val(data.coalSort[temp]);
                    }
                },
                error: function () {
                    messageToast('error', '发生异常！',3000);
                }
            });
        }
    });

    // 煤质分析校核煤种选择
    $("#coalCheck").change(function () {
        // 选择其他项时清空当前所有煤质分析值
        var id = $(this).val();
        if (id == "-1") {
            for (var i = 0; i < sorts.length; i++) {
                $("#" + sorts[i] + "_check").val("");
            }
        } else {
            $.ajax({
                url: '/coalSort',
                data: { "id": id },
                type: 'post',
                cache: false,
                dataType: 'json',
                success: function (data) {
                    var temp;
                    for (var i = 0; i < sorts.length; i++) {
                        temp = sorts[i];
                        $("#" + sorts[i] + "_check").val(data.coalSort[temp]);
                    }
                },
                error: function () {
                    messageToast('error', '发生异常！',3000);
                }
            });
        }
    });

    // 给选择已知方案下拉框绑定事件
    // $("#knownPlan").bind('change', updatePlanData);

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



    // 给保存按钮绑定事件
    $('#submitData').bind('click', submitQuestionnaire);
    // 点击选择模块
    $('.left-select').bind('click', function(){
        // 当前页面所有模块list
        listModule = ["q-1", "q-2", "q-3", "q-4", "q-5"];
        var moduleName = $(this).attr("id");
        // 切换页面右侧内容
        changeModule(listModule, moduleName);
    });
    createLabelBind("coalchpQuestionnaire", oldFormData);
});

/**
 * 提交保存页面所有表单数据
 */
function submitQuestionnaire() {

    if ($("[name='company_name']").val() == ""){
        messageToast('info', '公司名是唯一区别方案的标识，不能为空！',4000);
    }
    else {
        $.ajax({
            cache: true,
            type: "POST",
            url: '/formData',
            data: $('#coalchpQuestionnaire').serialize(),
            async: false,
            error: function (request) {
                messageToast('error', '发生异常，保存失败！',3000);
            },
            success: function (data) {
                if (data.state == "0") {
                    messageToast('info', '新增方案失败，该单位方案已存在，请修改单位名称作为区分！',4000);
                    $("[name='company_name']").focus();
                }else{
                    unlockBreadcrumb();
                    $("[name='company_name']").attr("readonly", true);
                    messageToast('success', '燃煤热电联产-需求调查表数据保存成功！',3000);
                    window.location.reload();
                }

                var dataformInit = $("#coalchpQuestionnaire").serializeArray();  
                oldFormData = JSON.stringify({ dataform: dataformInit });   
                createLabelBind("coalchpQuestionnaire", oldFormData);            
            }
        });
    }
}

/**
 * 选择已知方案时动态变更所有输入框内值
 */
// function updatePlanData() {
//     var planId = $(this).val();
//     if (planId != 0) {
//         $.ajax({
//             cache: true,
//             type: "POST",
//             url: '/findPlan',
//             data: { "planId": planId },
//             async: false,
//             error: function (request) {
//                 $("#ajax_message").html("异常！");
//                 $("#modal_info").modal('show');
//             },
//             success: function (data) {
//                 assignmentForm(data.questionnaire);
//                 unlockBreadcrumb();
//             }
//         });
//     }else{
//         // 清空页面所有表单值
//         $("#coalchpQuestionnaire input").val("");
//         $("#coalCheck, #coalDesign").val("-1");
//     }
// }

/**
 * 给页面中所有表单赋值
 * @param {后台传回来的值} datas 
 */
function assignmentForm(datas) {
    var elements = getElements("coalchpQuestionnaire");
    var notvalidcolumname = ["ihl_steam_time_value", "hhl_heating_occasions_type_value","os_local_water_condition_value", "oe_is_internet_access_value", "oe_is_isolated_network_value", "od_use_desulfurization_form_value", "od_use_denitration_form_value",  "plan_name", "company_name", "company_location"]
    var tempInput;
    for (var i = 0; i < elements.length; i++) {
        tempInput = elements[i];
        if (datas[tempInput] != "" || datas[tempInput] == "0") {
            $("input[name='" + tempInput + "']").val(datas[tempInput]);
            $("input[name='" + tempInput + "']").removeClass("default-color");
        }
        valid(tempInput, notvalidcolumname);
    }
    // 给select框赋值
    if (datas['s_fuel_check'] != ""){
        $("#coalCheck").val(datas['s_fuel_check']);
    }else{
        $("#coalCheck").val("-1");
    }
    if (datas['s_fuel_design'] != ""){
        $("#coalDesign").val(datas['s_fuel_design']);
    }else{
        $("#coalDesign").val("-1");
    }
    

    var dataformInit = $("#coalchpQuestionnaire").serializeArray();  
    oldFormData = JSON.stringify({ dataform: dataformInit });
}

function initQuestionnaire() {
    $.ajax({
        cache: true,
        type: "POST",
        url: '/initQuestionnaire',
        async: false,
        error: function (request) {
            messageToast('error', '发生异常！',3000);
        },
        success: function (data) {
            if (data.questionnaire != "null") {
                assignmentForm(data.questionnaire, "coalchpQuestionnaire");
            }
            var dataformInit = $("#coalchpQuestionnaire").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
        }
    });
}