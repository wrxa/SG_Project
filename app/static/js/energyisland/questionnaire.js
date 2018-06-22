var oldFormData;

$(document).ready(function () {
    init();

    // 给保存按钮绑定事件
    $('#submitData').bind('click', submitQuestionnaire);

    // 点击选择模块
    $('.left-select').bind('click', function(){
        // 当前页面所有模块list
        listModule = ["q-1", "q-2", "q-3", "q-4", "q-5", "q-6", "q-7", "q-8", "q-9", "q-10", "q-11", "q-12", "q-13", "q-14", "q-15", "q-16", "q-17", "q-18"];
        var moduleName = $(this).attr("id");
        // 切换页面右侧内容
        changeModule(listModule, moduleName);
    })

    // input框添加name属性
    listModule = ["q-1", "q-2", "q-3", "q-4", "q-5", "q-6", "q-7", "q-8", "q-9", "q-10", "q-11", "q-12", "q-13", "q-14", "q-15", "q-16", "q-17", "q-18"]
    listModule.forEach(function(question_id) {
        $('.' + question_id).find('input').each(function(index, element) {
            $(element).attr('name', $(element).attr('id'))
        })
        $('.' + question_id).find('select').each(function(index, element) {
            $(element).attr('name', $(element).attr('id'))
        })
    })

    initQuestionnaire()

    var dataformInit = $("#energyisland_questionnaireForm").serializeArray();  
    oldFormData = JSON.stringify({ dataform: dataformInit });
    createLabelBind("energyisland_questionnaireForm", oldFormData);

    //选择不同的典型日，显示不同的典型日内容
    $("#typicalDay").change(function () {
        var id = $(this).val();
        for (var j = 1; j < 5; j++) {
            if(j == id) {
                $("#typicalSeason" + j).removeClass('hide');
                $("#typicalTime"  + j).removeClass('hide');
            } else {
                $("#typicalSeason" + j).addClass('hide');
                $("#typicalTime"  + j).addClass('hide');
            }
        }
    });

    $("#coldTypicalDay").change(function () {
        var id = $(this).val();
        for (var j = 1; j < 5; j++) {
            if(j == id) {
                $("#coldTypicalDay" + j).removeClass('hide');
            } else {
                $("#coldTypicalDay" + j).addClass('hide');
            }
        }
    });

    $("#steamTypicalDay").change(function () {
        var id = $(this).val();
        for (var j = 1; j < 5; j++) {
            if(j == id) {
                $("#steamTypicalDay" + j).removeClass('hide');
            } else {
                $("#steamTypicalDay" + j).addClass('hide');
            }
        }
    });

    $("#eleTypicalDay").change(function () {
        var id = $(this).val();
        for (var j = 1; j < 5; j++) {
            if(j == id) {
                $("#eleTypicalDay" + j).removeClass('hide');
            } else {
                $("#eleTypicalDay" + j).addClass('hide');
            }
        }
    });

    $("#hotTypicalDay").change(function () {
        var id = $(this).val();
        for (var j = 1; j < 5; j++) {
            if(j == id) {
                $("#hotTypicalDay" + j).removeClass('hide');
            } else {
                $("#hotTypicalDay" + j).addClass('hide');
            }
        }
    });

    $("#airTypicalDay").change(function () {
        var id = $(this).val();
        for (var j = 1; j < 5; j++) {
            if(j == id) {
                $("#airTypicalDay" + j).removeClass('hide');
            } else {
                $("#airTypicalDay" + j).addClass('hide');
            }
        }
    });
});

// 提交保存页面所有表单数据
function submitQuestionnaire() {
    $.ajax({
        cache: true,
        type: "POST",
        url: '../formDataEnergyIslandQuestionnaire',
        data: $('#energyisland_questionnaireForm').serialize(),
        async: false,
        beforeSend: checkInput,
        error: function (request) {
            messageToast('info', "数据采集异常！", 3000);
        },
        success: function (data) {
            var dataformInit = $("#energyisland_questionnaireForm").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
            createLabelBind("energyisland_questionnaireForm", oldFormData);
            messageToast('success', "数据采集成功！", 3000);
        }
    });

}

// 选择已知方案时动态变更所有输入框内值
var initQuestionnaire = function() {
    $.ajax({
        cache: true,
        type: "POST",
        url: '/energyIsland/initQuestionnaire',
        data: {},
        async: false,
        error: function (request) {
            messageToast('error', '检索发生异常！', 3000);
        },
        success: function (data) {
            assignmentForm(data.questionnaire);
            assignmentSelect(data.questionnaire)
            // unlockMeun();
        }
    });
}

// 给页面中所有表单赋值
var assignmentForm = function(datas) {
    if(datas != null){
        var elements = getFormElements();
        var tempInput;
        for (var i = 0; i < elements.length; i++) {
            tempInput = elements[i];
            $("input[name='" + tempInput + "']").val(datas[tempInput]);
        }
         $("#surf_internet_flage").val(datas['surf_internet_flage']);
         $("#isolated_network_operation_flage").val(datas['isolated_network_operation_flage']);
    }
}


//获取form中的所有的<input>对象
var getFormElements = function() {
    var tagElements = $('.module-content').find('input')
    var elements = new Array();
    for (var j = 0; j < tagElements.length; j++) {
        elements.push(tagElements[j].name);
    }
    return elements;
}

// 给页面中所有下拉框赋值
var assignmentSelect = function(datas) {
    if(datas != null){
        var elements = getSelectElements();
        var tempInput;
        for (var i = 0; i < elements.length; i++) {
            tempInput = elements[i];
            $("select[name='" + tempInput + "']").val(datas[tempInput]);
        }
         $("#surf_internet_flage").val(datas['surf_internet_flage']);
         $("#isolated_network_operation_flage").val(datas['isolated_network_operation_flage']);
    }
    $("#eir_work_year_maintain").val(datas['eir_work_year_maintain']);
    $("#eir_available_steam_boiler_fuel_1_unit").val(datas['eir_available_steam_boiler_fuel_1_unit']);
    $("#eir_available_steam_boiler_fuel_2_unit").val(datas['eir_available_steam_boiler_fuel_2_unit']);
}


//获取所有的<select>对象
var getSelectElements = function() {
    var tagElements = $('.module-content').find('select')
    var elements = new Array();
    for (var j = 0; j < tagElements.length; j++) {
        elements.push(tagElements[j].id);
    }
    return elements;
}

// 检查输入
function checkInput() {
}

