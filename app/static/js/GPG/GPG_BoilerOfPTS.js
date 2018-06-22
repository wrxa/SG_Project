var oldFormData;

$(document).ready(function () {
    init();
    
    getBoilerDataByPlanId();

    $('#submitBoiler').bind('click', submitBoiler);

    // 点击选择模块
    $('.left-select').bind('click', function(){
        // 当前页面所有模块list
        listModule = ["q-1", "q-2", "q-3", "q-4", "q-5", "q-6", "q-7"];
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
    createLabelBind("GPG_BoilerForm", oldFormData);
});

function getBoilerDataByPlanId() {
    planId = $('#GPGCurrentPlanId').val();
    $.ajax({
        cache: true,
        type: "POST",
        url: './getBoilerByPlanId',
        data: { "planId": planId },
        async: false,
        error: function (request) {
            messageToast('error', '发生异常！',3000);
        },
        success: function (data) {
            assignmentForm(data.BoilerJson, "GPG_BoilerForm");
            var dataformInit = $("#GPG_BoilerForm").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
        }
    });
}

// 提交锅炉页面所有表单数据
function submitBoiler() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './GPG_SaveBoilerOfPTS',
        data: $('#GPG_BoilerForm').serialize(),
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，保存失败！',2000);
        },
        success: function (data) {
            if(data.newDatas == null){
                messageToast('error', '输入数据有误，转换发生异常!', 2000);
            }else if(data.newDatas == "-1"){
                messageToast('error', '输入数据有误，出现除0情况!', 2000);
            }else{
                assignmentForm(data.newDatas, "GPG_BoilerForm");
                var dataformInit = $("#GPG_BoilerForm").serializeArray();  
                oldFormData = JSON.stringify({ dataform: dataformInit });       
                createLabelBind("GPG_BoilerForm", oldFormData);
                messageToast('success', '煤气发电-锅炉计算数据保存成功！',2000);
            }
            
        }
    });
}