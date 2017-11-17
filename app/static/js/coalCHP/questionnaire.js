$(document).ready(function () {
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
                $("#s_" + sorts[i] + "_check").val("");
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
    $("#knownPlan").bind('change', updatePlanData);

    // 给保存按钮绑定事件
    $('#submitData').bind('click', submitQuestionnaire);
});

/**
 * 提交保存页面所有表单数据
 */
function submitQuestionnaire() {
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
            unlockBreadcrumb();
            messageToast('success', '燃煤热电联产-需求调查表数据保存成功！',3000);
        }
    });

}

/**
 * 选择已知方案时动态变更所有输入框内值
 */
function updatePlanData() {
    var planId = $(this).val();
    if (planId != 0) {
        $.ajax({
            cache: true,
            type: "POST",
            url: '/findPlan',
            data: { "planId": planId },
            async: false,
            error: function (request) {
                $("#ajax_message").html("异常！");
                $("#modal_info").modal('show');
            },
            success: function (data) {
                assignmentForm(data.questionnaire);
                unlockBreadcrumb();
            }
        });
    }else{
        // 清空页面所有表单值
        $("#coalchpQuestionnaire input").val("");
        $("#coalCheck, #coalDesign").val("others");
    }
}

/**
 * 给页面中所有表单赋值
 * @param {后台传回来的值} datas 
 */
function assignmentForm(datas) {
    var elements = getElements("coalchpQuestionnaire");
    var tempInput;
    for (var i = 0; i < elements.length; i++) {
        tempInput = elements[i];
        $("input[name='" + tempInput + "']").val(datas[tempInput]);
    }
    // 给select框赋值
    $("#coalCheck").val(datas['s_fuel_check']);
    $("#coalDesign").val(datas['s_fuel_design']);
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
            
        }
    });
}