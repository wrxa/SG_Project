var oldFormData;

$(document).ready(function () {
    init();
    
    getBoilerAuxiliariesDataByPlanId();

    //calculateWaterSupplyAll();

    $('#submitBoilerAuxiliaries').bind('click', submitBoilerAuxiliaries);

    // 点击选择模块
    $('.left-select').bind('click', function(){
        // 当前页面所有模块list
        listModule = ["q-1", "q-2", "q-3", "q-4", "q-5", "q-6", "q-7", "q-8", "q-9"];
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
    createLabelBind("GPG_BoilerAuxiliariesForm", oldFormData);
});

function calculateWaterSupplyAll(){
    var m_boiler_desalted_work_cycle = $('#m_boiler_desalted_work_cycle').val();
    var m_boiler_desalted_rebirth_time = $('#m_boiler_desalted_rebirth_time').val();
    var m_boiler_max_watersupply  = $('#m_boiler_max_watersupply').val();

    if(m_boiler_desalted_work_cycle != null && m_boiler_desalted_work_cycle !=''
        && m_boiler_desalted_rebirth_time != null && m_boiler_desalted_rebirth_time !=''
        && m_boiler_max_watersupply != null && m_boiler_max_watersupply !=''){
        
        $('#m_boiler_watersupply_all').val(
            (parseInt(m_boiler_desalted_work_cycle) +
                parseInt(m_boiler_desalted_rebirth_time)) * m_boiler_max_watersupply
                / m_boiler_desalted_work_cycle
        );

        $.ajax({
            cache: true,
            type: "POST",
            url: './GPG_SaveBoilerAuxiliariesData',
            data: $('#GPG_BoilerAuxiliariesForm').serialize(),
            async: false,
            error: function (request) {
            },
            success: function (data) {
                assignmentForm(data.newDatas, "GPG_BoilerAuxiliariesForm");
                var dataformInit = $("#GPG_BoilerAuxiliariesForm").serializeArray();  
                oldFormData = JSON.stringify({ dataform: dataformInit });
                createLabelBind("GPG_BoilerAuxiliariesForm", oldFormData);
            }
        });
    }
}

function getBoilerAuxiliariesDataByPlanId() {
    planId = $('#GPGCurrentPlanId').val();
    $.ajax({
        cache: true,
        type: "POST",
        url: './getBoilerAuxiliariesDataByPlanId',
        data: { "planId": planId },
        async: false,
        error: function (request) {
            messageToast('error', '发生异常！',3000);
        },
        success: function (data) {
            assignmentForm(data.BoilerAuxiliariesJson, "GPG_BoilerAuxiliariesForm");
            if(data.BoilerAuxiliariesJson['desalted_water_tech_type'] == 2){
                $("#desalted_water_tech_type").val("2");
            }else{
                $("#desalted_water_tech_type").val("1");
            }
            var dataformInit = $("#GPG_BoilerAuxiliariesForm").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
        }
    });
}


function submitBoilerAuxiliaries() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './GPG_SaveBoilerAuxiliariesData',
        data: $('#GPG_BoilerAuxiliariesForm').serialize(),
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
                messageToast('error', '数据有误，可能出现了除0情况!', 3000);
            }else{
                assignmentForm(data.newDatas, "GPG_BoilerAuxiliariesForm");
                calculateWaterSupplyAll();

                var dataformInit = $("#GPG_BoilerAuxiliariesForm").serializeArray();  
                oldFormData = JSON.stringify({ dataform: dataformInit });
                createLabelBind("GPG_BoilerAuxiliariesForm", oldFormData);
                messageToast('success', '煤气发电-锅炉辅机系统数据保存成功！',2000);
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
    var tagElements = $("#GPG_BoilerAuxiliariesForm input");
    var elements = new Array();
    for (var j = 0; j < tagElements.length; j++) {
        elements.push(tagElements[j].name);
    }
    return elements;
}*/
