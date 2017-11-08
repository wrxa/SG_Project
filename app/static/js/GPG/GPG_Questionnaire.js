$(document).ready(function () {
    var sorts = ['s_carbon', 's_hydrogen', 's_oxygen', 's_nitrogen', 's_sulfur', 's_water',
        's_grey', 's_daf', 's_grindability', 's_low'];

    // 煤质分析设计煤种选择
    $("#coalDesign").change(function () {
        // 选择其他项时清空当前所有煤质分析值
        var id = $(this).val();
        if (id == "others") {
            for (var i = 0; i < sorts.length; i++) {
                $("#" + sorts[i] + "_design").val("");
            }
        } else {
            $.ajax({
                url: './coalSort',
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
                    alert("异常！");
                }
            });
        }
    });

    // 煤质分析校核煤种选择
    $("#coalCheck").change(function () {
        // 选择其他项时清空当前所有煤质分析值
        var id = $(this).val();
        if (id == "others") {
            for (var i = 0; i < sorts.length; i++) {
                $("#s_" + sorts[i] + "_check").val("");
            }
        } else {
            $.ajax({
                url: './coalSort',
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
                    alert("异常！");
                }
            });
        }
    });


    // 给选择已知方案下拉框绑定事件
    $("#knownPlan").bind('change', updatePlanData);

    // 给保存按钮绑定事件
    $('#GPG_SaveQuestionnaire').bind('click', GPG_SaveQuestionnaire);
});

// 提交保存页面所有表单数据
function GPG_SaveQuestionnaire() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './GPG_SaveQuestionnaire',
        data: $('#GPG_questionnaire').serialize(),
        async: false,
        error: function (request) {
            alert("Connection error");
        },
        success: function (data) {
            unlockMenuGPG();
            alert("保存成功！！！");
        }
    });

}

// 选择已知方案时动态变更所有输入框内值
function updatePlanData() {
    var planId = $(this).val();
    if (planId != 0) {
        $.ajax({
            cache: true,
            type: "POST",
            url: './selectPlan',
            data: { "planId": planId },
            async: false,
            error: function (request) {
                alert("Connection error");
            },
            success: function (data) {
                assignmentForm(data.questionnaire);
                unlockMenuGPG();
            }
        });
    }else{
        // 清空页面所有表单值
        $("#GPG_questionnaire input").val("");
        //lockMeunGPG();
    }
}

// 给页面中所有表单赋值
function assignmentForm(datas) {
    var elements = getElements("GPG_questionnaire");
    var tempInput;
    for (var i = 0; i < elements.length; i++) {
        tempInput = elements[i];
        $("input[name='" + tempInput + "']").val(datas[tempInput]);
    }
    if(datas['project_approval_eia'] == true){
        $("#project_approval_eia_yes").attr("checked", true);
        $("#project_approval_eia_no").attr("checked", false);
    }else{
        $("#project_approval_eia_yes").attr("checked", false);
        $("#project_approval_eia_no").attr("checked", true);
    }
}

