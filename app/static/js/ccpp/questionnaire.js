var oldFormData;

$(document).ready(function () {
    init();
    hiddenUnit();
    // 定义面包屑个数
    var breakCount = 14;
    // 定义面包屑上id的模块类型
    var moduleName = "ccpp";
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

    $('#add_pressure').bind('click', function(){
        if($("#Industrialheatin").is(':hidden')){
            $("#Industrialheatin").show();
            return
        }else{
            $("#industrialheatlow").show();
            $("#Industrialheatin").show();
        }
    });

    $('#del_pressure').bind('click', function(){
        if($("#industrialheatlow").is(':visible')){
            $("#industrialheatlow").hide();
            $("#steam_pressure_level_3").val("")
            $("#steam_temperature_level_3").val("")
            $("#use_steam_time_3").val("")
            $("#forward_steam_flow_range_3").val("")
            $("#rrcw_3").val("")
            $("#icicw_3").val("")
            $("#steam_price_3").val("")
            return
        }else{
            $("#Industrialheatin").hide();
            $("#steam_pressure_level_2").val("")
            $("#steam_temperature_level_2").val("")
            $("#use_steam_time_2").val("")
            $("#forward_steam_flow_range_2").val("")
            $("#rrcw_2").val("")
            $("#icicw_2").val("")
            $("#steam_price_2").val("")
        }
    });

    initQuestionnaire()
    // 判断是否显示二三级压力等级
    panduanshow()

    // 点击选择模块
    $('.left-select').bind('click', function(){
        // 当前页面所有模块list
        listModule = ["q-1", "q-2", "q-3", "q-4", "q-5", "q-6", "q-7", "q-8", "q-9", "q-10", "q-11", "q-12", "q-13"];
        var moduleName = $(this).attr("id");
        // 切换页面右侧内容
        changeModule(listModule, moduleName);
    })
    $('#surf_internet_flage').bind('change', function(){
        var surf_internet_flage = $('#surf_internet_flage').val()
        if(surf_internet_flage == 0){
            $('#isolated_network_operation_flage').val(1)
        }else if(surf_internet_flage == 1){
            $('#isolated_network_operation_flage').val(0)
        }
    })
    $('#isolated_network_operation_flage').bind('change', function(){
        var isolated_network_operation_flage = $('#isolated_network_operation_flage').val()
        if(isolated_network_operation_flage == 0){
            $('#surf_internet_flage').val(1)
        }else if(isolated_network_operation_flage == 1){
            $('#surf_internet_flage').val(0)
        }
    })
    
    var dataformInit = $("#ccppQuestionnaire").serializeArray();  
    oldFormData = JSON.stringify({ dataform: dataformInit });
    createLabelBind("ccppQuestionnaire", oldFormData);
});


// 提交保存页面所有表单数据
function submitQuestionnaire() {
    if ($("[name='company_name']").val() == ""){
        messageToast('info', '公司名是唯一区别方案的标识，不能为空！',4000);
    }
    else {
        $.ajax({
            cache: false,
            type: "POST",
            url: '/ccpp/submitQuestionnaire',
            data: $('#ccppQuestionnaire').serialize(),
            async: false,
            error: function (request) {
                messageToast('error', '检索发生异常！', 3000);
            },
            success: function (data) {
                if(data.state == 0){
                    messageToast('info', data.message, 3000);
                }else{              
                    unlockBreadcrumb();
                    $("#total_design").val(data.total_design)
                    $("[name='company_name']").attr("readonly", true);
                    messageToast('success', data.message, 3000);
                    window.location.reload();         
                }
                var dataformInit = $("#ccppQuestionnaire").serializeArray();  
                oldFormData = JSON.stringify({ dataform: dataformInit });
                createLabelBind("ccppQuestionnaire", oldFormData);  
            }
        });
    }
}

// 选择已知方案时动态变更所有输入框内值
function initQuestionnaire() {
    $.ajax({
        cache: true,
        type: "POST",
        url: '/ccpp/initQuestionnaire',
        data: {},
        async: false,
        error: function (request) {
            messageToast('error', '检索发生异常！', 3000);
        },
        success: function (data) {
            assignmentForm(data.questionnaire);
            // unlockMeun();
        }
    });
}

// 给页面中所有表单赋值
function assignmentForm(datas) {
    var notvalidcolumname = ["denitration_form", "urea_ammonia_water_supply", "plan_name", "company_name", "company_location"]
    if(datas != null){
        var elements = getElements();
        var tempInputName;
        for (var i = 0; i < elements.length; i++) {
            tempInputName = elements[i];
            $("input[name='" + tempInputName + "']").val(datas[tempInputName]);
            valid(tempInputName, notvalidcolumname);
        }
        $("#surf_internet_flage").val(datas['surf_internet_flage']);
        $("#isolated_network_operation_flage").val(datas['isolated_network_operation_flage']); 
    }
}


//获取form中的所有的<input>对象
function getElements() {
    var tagElements = $("#ccppQuestionnaire input");
    var elements = new Array();
    for (var j = 0; j < tagElements.length; j++) {
        elements.push(tagElements[j].name);
    }
    return elements;
}

// 判断是否显示二三级压力等级
function panduanshow(){
    if($("#steam_pressure_level_2").val() == '' && $("#steam_temperature_level_2").val() == '' &&
    $("#use_steam_time_2").val() == '' && $("#forward_steam_flow_range_2").val() == '' &&
    $("#rrcw_2").val() == '' && $("#icicw_2").val() == '' && $("#steam_price_2").val() == ''){
        $("#Industrialheatin").hide();
        
    }
    if($("#steam_pressure_level_3").val() == '' && $("#steam_temperature_level_3").val() == '' &&
    $("#use_steam_time_3").val() == '' && $("#forward_steam_flow_range_3").val() == '' &&
    $("#rrcw_3").val() == '' && $("#icicw_3").val() == '' && $("#steam_price_3").val() == ''){
        $("#industrialheatlow").hide();
    }
}
