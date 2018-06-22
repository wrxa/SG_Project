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
    initChimneyCalculate();
    $('#submitData').bind('click', submitChimneyCalculate);
    
     // 点击选择模块
     $('.left-select').bind('click', function(){
        // 当前页面所有模块list
        listModule = ["q-1", "q-2", "q-3", "q-4", "q-5", "q-6", "q-7", "q-8", "q-9", "q-10", "q-11", "q-12", "q-13"];
        var moduleName = $(this).attr("id");
        // 切换页面右侧内容
        changeModule(listModule, moduleName);
    })
    
    createLabelBind("ccppChimneyCalculateForm", oldFormData);
});

function initChimneyCalculate() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './initChimneyCalculate',
        async: false,
        error: function (request) {
            messageToast('error', '发生异常！',3000);
        },
        success: function (data) {
            assignmentForm(data.chimneyCalculateData, "ccppChimneyCalculateForm");
            var dataformInit = $("#ccppChimneyCalculateForm").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
        }
    });
}


// 提交保存页面所有表单数据
function submitChimneyCalculate() {
    $.ajax({
        cache: true,
        type: "POST",
        url: './formChimneyCalculate',
        data: $('#ccppChimneyCalculateForm').serialize(),
        async: false,
        error: function (request) {
            messageToast('error', '发生异常，保存失败！',3000);
        },
        success: function (data) {
            if(data.newDatas == null){
                messageToast('info', data.message, 3000);
                return;
            }
            messageToast('success', '燃气蒸汽联合循环-烟囱数据保存成功！',3000);
            assignmentForm(data.newDatas, "ccppChimneyCalculateForm");
            var dataformInit = $("#ccppChimneyCalculateForm").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
            createLabelBind("ccppChimneyCalculateForm", oldFormData);
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

