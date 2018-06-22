var oldFormData;

$(document).ready(function () {
    init();
    // 给选择已知方案下拉框绑定事件
    //$("#knownPlan").bind('change', updatePlanData);

    // 给保存按钮绑定事件
    $('#GPG_SaveQuestionnaire').bind('click', GPG_SaveQuestionnaire);

    /*
    $('#breadcrumbDiv a').each(function(){
        var id = $(this).attr('id');
        var href = $(this).attr('href');
        if(href !="#"){
            $(this).bind('click', {labelID: id}, isDataModified);
        }
    });

    $('#sidebar-nav a').each(function(){
        var id = $(this).attr('id');
        var href = $(this).attr('href');
        if(id !="coalMean" && id !="biomassMean" && id !="ccppMean" && id !="gaspowerMean" && id !="energyislandMean"){
            $('#' + id)[0].setAttribute("onclick",'return false;');
            $(this).bind('click', {labelID: id}, isDataModified);
        }
    });
    */ 
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
    // 初始化需求调查表数据
    initGPGQuestionnaire();

    $('#project_approval_eia_yes').bind('click', project_approval_eia_yes);
    $('#project_approval_eia_no').bind('click', project_approval_eia_no);

    // 点击选择模块
    $('.left-select').bind('click', function(){
        // 当前页面所有模块list
        listModule = ["q-1", "q-2", "q-3", "q-4", "q-5", "q-6", "q-7"];
        var moduleName = $(this).attr("id");
        // 切换页面右侧内容
        changeModule(listModule, moduleName);
    });

    createLabelBind("GPG_questionnaire", oldFormData);
});

// function isDataModified(event){
//     isModified(event.data.labelID, "GPG_questionnaire", oldFormData);
// }

function project_approval_eia_yes(){
    $("#project_approval_eia_yes").attr("checked", true);
    $("#project_approval_eia_no").attr("checked", false);
    $('#project_approval_eia').val("true"); 
}

function project_approval_eia_no(){
    $("#project_approval_eia_yes").attr("checked", false);
    $("#project_approval_eia_no").attr("checked", true);
    $('#project_approval_eia').val("false"); 
}

function initGPGQuestionnaire() {
    $.ajax({
        cache: true,
        type: "POST",
        url: '/initGPGQuestionnaire',
        async: false,
        error: function (request) {
            messageToast('error', '发生异常！',3000);
        },
        success: function (data) {
            if (data.questionnaireJson != "null") {
                assignmentForm(data.questionnaireJson);
            }
            var dataformInit = $("#GPG_questionnaire").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
        }
    });
}

// 提交保存页面所有表单数据
function GPG_SaveQuestionnaire() {
    if ($("[name='company_name']").val() == ""){
        messageToast('info', '公司名是唯一区别方案的标识，不能为空！',4000);
    } else{
        $.ajax({
            cache: true,
            type: "POST",
            url: '/GPG_SaveQuestionnaire',
            data: $('#GPG_questionnaire').serialize(),
            async: false,
            error: function (request) {
                messageToast('error', '发生异常，保存失败！',3000);
            },
            success: function (data) {
                unlockBreadcrumb();
                messageToast('success', '煤气发电-需求调查表数据保存成功！',3000);
                window.location.reload();
                var dataformInit = $("#GPG_questionnaire").serializeArray();  
                oldFormData = JSON.stringify({ dataform: dataformInit });
                createLabelBind("GPG_questionnaire", oldFormData);
            }
        });
    }
}

// 选择已知方案时动态变更所有输入框内值
function updatePlanData() {
    var planId = $(this).val();
    if (planId != 0) {
        $.ajax({
            cache: true,
            type: "POST",
            url: '/selectPlan',
            data: { "planId": planId },
            async: false,
            error: function (request) {
                ("#ajax_message").html("异常！");
                $("#modal_info").modal('show');
            },
            success: function (data) {
                assignmentForm(data.questionnaireJson);
                unlockBreadcrumb();
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
        if (datas[tempInput] != "" || datas[tempInput] == "0") {
            $("input[name='" + tempInput + "']").val(datas[tempInput]);
        }
    }
    if(datas['project_approval_eia'] == true){
        $("#project_approval_eia_yes").attr("checked", true);
        $("#project_approval_eia_no").attr("checked", false);
    }else{
        $("#project_approval_eia_yes").attr("checked", false);
        $("#project_approval_eia_no").attr("checked", true);
    }
}

