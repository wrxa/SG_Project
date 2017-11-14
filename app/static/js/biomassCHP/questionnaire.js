$(document).ready(function () {

    // 给选择已知方案下拉框绑定事件
    $("#knownPlan").bind('change', updatePlanData);

    // 给保存按钮绑定事件
    $('#submitData').bind('click', submitQuestionnaire);

    // 给清空按钮绑定事件
    $('#clearData').bind('click', clearQuestionnaire);

});

// 提交保存页面所有表单数据
function submitQuestionnaire(){
    $.ajax({
        cache: true,
        type: "POST",
        url:'./biomassFormData',
        data:$('#biomasschpQuestionnaire').serialize(),
        async: false,
        error: function(request) {
            alert("Connection error");
        },
        success: function(data) {
            unlockMeunBiomassCHP();
            alert("成功！！！" );
        }
    });
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
        url:'./biomassFindPlan',
        data: { "planId": planId },
        async: false,
        error: function(request) {
            alert("Connection error");
        },
        success: function(data) {
            unlockMeunBiomassCHP();
            assignmentForm(data.questionnaire);
        }
    });

}

// 给页面中所有表单赋值
function assignmentForm(datas){
    var elements = getElements();
    var tempInput;
    for (var i = 0; i < elements.length; i++) {
        tempInput = elements[i];
        $("input[name='"+tempInput+"']").val(datas[tempInput]);
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