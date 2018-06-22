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
    initCirculatingWater();
    $('#submitData').bind('click', submitCirculatingWater);
    $('.left-select').bind('click', function(){
        // 当前页面所有模块list
        listModule = ["w-1", "w-2", "w-3", "w-4", "w-5"];
        var moduleName = $(this).attr("id");
        // 切换页面右侧内容
        changeModule(listModule, moduleName);
    });
    $("#info1").on("click", function () {
        $("#showInfo").modal('show');
        $("#infoContent").html("<img class='img-responsive center-block' src='/static/img/ccpp/circulatingWater.png'/>");
    });
    createLabelBind("coalCirculatingWaterForm", oldFormData);
});

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


// 提交保存页面所有表单数据
function submitCirculatingWater() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './formCirculatingWater',
        data: $('#coalCirculatingWaterForm').serialize(),
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，保存失败！',3000);
        },
        success: function (data) {
            if(data.newDatas != null){
                assignmentForm(data.newDatas, "coalCirculatingWaterForm");
                var dataformInit = $("#coalCirculatingWaterForm").serializeArray();  
                oldFormData = JSON.stringify({ dataform: dataformInit });
                createLabelBind("coalCirculatingWaterForm", oldFormData);         
                messageToast('success', '燃气蒸汽联合循环-循环水系统数据保存成功！',3000);
            }else{
                messageToast('info', '数据输入有误！',3000);
            }
        }
    });

}

function assignmentForm(datas, formName) {
    var elements = getElements(formName);
    var tempInputName;
    for (var i = 0; i < elements.length; i++) {
        tempInputName = elements[i];
        if (datas[tempInputName] != "" || datas[tempInputName] == "0") {
            $("input[name='" + tempInputName + "']").val(datas[tempInputName]);
            $("input[name='" + tempInputName + "']").removeClass("default-color");
        }
        valid(tempInputName, []);
    }
}
