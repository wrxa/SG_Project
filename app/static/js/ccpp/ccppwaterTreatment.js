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
    // 获得化学水处理页面初期数据
    initWater();
    $("#info1").on("click", function () {
        $("#showInfo").modal('show');
        $("#infoContent").html("<img class='img-responsive center-block' src='/static/img/ccpp/hxsck.PNG'/>");
    }); 

    // 给保存按钮绑定事件
    $('#submitData').bind('click', submitWater);
    // 点击选择模块
    $('.left-select').bind('click', function(){
        // 当前页面所有模块list
        listModule = ["c-1", "c-2", "c-3"];
        var moduleName = $(this).attr("id");
        // 切换页面右侧内容
        changeModule(listModule, moduleName);
    });
    createLabelBind("biomasschpWater", oldFormData);
});

//化学水处理页面信息初期化
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
            assignmentForm(data.water);
            var dataformInit = $("#biomasschpWater").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
        }
    });
}

// 给页面中所有表单赋值
function assignmentForm(datas){
    var elements = getElements();
    var tempInputName;
    for (var i = 0; i < elements.length; i++) {
        tempInputName = elements[i];
        if(datas[tempInputName] != "" || datas[tempInputName] == "0") {
            $("input[name='"+tempInputName+"']").val(datas[tempInputName]);
        }
        valid(tempInputName, []);
    }

    $("#processRoute").val(datas['o_process_route']);
    
    if(datas['o_boiler_water_system'] != "") {
        $("[name='o_boiler_water_system']").val(datas['o_boiler_water_system'].toFixed(0));
    }
}


//获取form中的所有的<input>对象  
function getElements() {  
    var tagElements = $("#biomasschpWater input");  
    var elements = new Array();  
    for (var j = 0; j < tagElements.length; j++){ 
        elements.push(tagElements[j].name); 
    }
    return elements;  
}

//提交表单信息
function submitWater() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './biomassFormDataWater',
        data: $('#biomasschpWater').serialize(),
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，保存失败！',3000);
        },
        success: function (data) {
            if(data.flag == "fail"){
                messageToast('info', data.info, 3000);
                return;
            }
            messageToast('success', '燃气蒸汽联合循环-化学水处理数据保存成功！',3000);
            // 刷新页面
            initWater();
            var dataformInit = $("#biomasschpWater").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
            createLabelBind("biomasschpWater", oldFormData);

        }
    });
}

