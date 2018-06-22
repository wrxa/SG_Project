var oldFormData;

$(document).ready(function () {
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
    
    bool_input = false;
    // 汽轮机
    initTurbineData();
    
    //化学水
    initWater();

    //ccpp计算
    data = initInputDataccpp();
    initDataccpp(data)

    //循环水
    initCirculatingWater();
    
    var offset = 300,
    offset_opacity = 1200,
    scroll_top_duration = 700,
    $back_to_top = $('.cd-top');
    $(window).scroll(function(){
        ( $(this).scrollTop() > offset ) ? $back_to_top.addClass('cd-is-visible') : $back_to_top.removeClass('cd-is-visible cd-fade-out');
        if( $(this).scrollTop() > offset_opacity ) { 
            $back_to_top.addClass('cd-fade-out');
        }
    });

    $back_to_top.on('click', function(event){
        event.preventDefault();
        $('body,html').animate({
            scrollTop: 0 ,
            }, scroll_top_duration
        );
    });
});


//汽轮机
function initTurbineData() {
    //planId = $('#GPGCurrentPlanId').val();
    $.ajax({
        cache: true,
        type: "POST",
        url: './initTurbineData',
        //data: { "planId": planId },
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，页面初期化失败！',3000);
        },
        success: function (data) {
            assignmentFormTurbine(data.steamturbine);

            if(data.steamturbine.s_parameter_flg == '1') {
                bool_input = true;
            }
            var dataformInit = $("#ccppTurbineForm").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
        }
    });
}
// 给页面中所有表单赋值
function assignmentFormTurbine(datas){
    var elements = getElementsTurbine();
    var tempInput;
    for (var i = 0; i < elements.length; i++) {
        tempInput = elements[i];
        if(datas[tempInput] != "" || datas[tempInput] == "0") {
            $("input[name='"+tempInput+"']").val(datas[tempInput]);
        }
    }

    // if(datas['s_temperature_pressure'] == '1') {
    //    $("#d_water_temperature").val("104");
    //    $("#d_work_pressure").val("0.02");
    // }

    // if(datas['s_temperature_pressure'] == '2') {
    //    $("#d_water_temperature").val("130");
    //    $("#d_work_pressure").val("0.3");
    // }

    // if(datas['s_temperature_pressure'] == '3') {
    //    $("#d_water_temperature").val("158");
    //    $("#d_work_pressure").val("0.588");
    // }

    $("#steamType").val(datas['e_steam_type']);
    $("#h_assume").val(datas['h_assume']);

    $("#s_steam_type_test").val(datas['s_steam_type_test']);
    $("#s_temperature_pressure").val(datas['s_temperature_pressure']);
}
//获取form中的所有的<input>对象  
function getElementsTurbine() {  
    var tagElements = $("#ccppTurbineForm input");  
    var elements = new Array();  
    for (var j = 0; j < tagElements.length; j++){ 
        elements.push(tagElements[j].name); 
    }
    return elements;  
}



//化学水
function initWater() {
    planId = $('#planId').val();
    $.ajax({
        cache: true,
        type: "POST",
        url: './biomassinitWater',
        data: { "planId": planId },
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，页面初期化失败！',3000);
        },
        success: function (data) {
            biomassassignmentForm(data.water);
            var dataformInit = $("#biomasschpWater").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
        }
    });
}
// 给页面中所有表单赋值
function biomassassignmentForm(datas){
    var elements = biomassgetElements();
    var tempInput;
    for (var i = 0; i < elements.length; i++) {
        tempInput = elements[i];
        if(datas[tempInput] != "" || datas[tempInput] == "0") {
            $("input[name='"+tempInput+"']").val(datas[tempInput]);
        }
    }

    $("#processRoute").val(datas['o_process_route']);
    
    if(datas['o_boiler_water_system'] != "") {
        $("[name='o_boiler_water_system']").val(datas['o_boiler_water_system'].toFixed(0));
    }
}
//获取form中的所有的<input>对象  
function biomassgetElements() {  
    var tagElements = $("#biomasschpWater input");  
    var elements = new Array();  
    for (var j = 0; j < tagElements.length; j++){ 
        elements.push(tagElements[j].name); 
    }
    return elements;  
}


//ccpp计算
function initDataccpp(data){
    datas = data.ccppinputdata
    permissiondata = data.permissiondata
    defaultvaluedata = data.defaultvaluedata
    assignmentFormccpp($("#ccppCalculateform input"), datas, permissiondata, defaultvaluedata);
    $('#engine_id_design').val(datas['engine_id_design'])
    var pottype = datas['boiler_single_or_dula_pressure_design'];
    if(pottype == 'singlepot'){
        $('#selectSingDouble').val("singlepot")
        setInputdisableccpp($("#singlepot input"), true);
        setInputdisableccpp($("#doublepot input"), true);
    }else if(pottype == 'doublepot'){
        $('#selectSingDouble').val("doublepot")
        setInputdisableccpp($("#singlepot input"), true);
        setInputdisableccpp($("#doublepot input"), true);
    }else{
        $('#selectSingDouble').val("-1")
        setInputdisableccpp($("#singlepot input"), true);
        setInputdisableccpp($("#doublepot input"), true);
    }
        // $('#selectSingDouble').val(datas['boiler_single_or_dula_pressure_design'])
    
}
//获取ccpp计算页面数据并显示
function initInputDataccpp() {
    var datajson = null;
    $.ajax({
        cache: true,
        type: "POST",
        url: './initInputData',
        data: {},
        async: false,
        error: function (request) {
            messageToast('error', '检索发生异常！', 3000);
        },
        success: function (data) {
            datajson = data
        }
    });
    return datajson;
}

// 给页面中所有表单赋值
function assignmentFormccpp(elements, datas, permissiondata, defaultvaluedata) {
    var tempInputName;
    for (var i = 0; i < elements.length; i++) {
        tempInputName = elements[i].name;
        if((datas[tempInputName] != "" || datas[tempInputName] === 0) && datas[tempInputName] != null){
            $("input[name='" + tempInputName + "']").val(datas[tempInputName]);
        }else{
            //存放默认值
            $("input[name='" + tempInputName + "']").val(defaultvaluedata[tempInputName]);
        }
        if(permissiondata[tempInputName] == "true"){
            elements[i].readOnly = false;
        }
    }
}

//为input设置disable属型
function setInputdisableccpp(elements, flg){
    for (var i = 0; i < elements.length; i++) {
            tempInput = elements[i];
            // 修改对象的readonly属性
            tempInput.readOnly=flg;
    }
}

//循环水
function initCirculatingWater() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './initCirculatingWater',
        async: false,
        error: function (request) {
            messageToast('error', '发生异常！',3000);
        },
        success: function (data) {
            assignmentForm(data.circulatingWater, "coalCirculatingWaterForm");
            var dataformInit = $("#coalCirculatingWaterForm").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });           
        }
    });
}