var oldFormData;

$(document).ready(function () {
    init();
    initInputData();
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
    $('#submitData').bind('click', submitEconomicdata);
    $('.repayment_plan_refer').bind('click', function(){
        window.open("/ccpp/ccpprepayrefer");
    });
    // 点击选择模块
    $('.left-select').bind('click', function(){
        // 当前页面所有模块list
        listModule = ["q-1", "q-2", "q-3", "q-4", "q-5", "q-6", "q-7", "q-8", "q-9", "q-10", "q-11", "q-12", "q-13"];
        var moduleName = $(this).attr("id");
        // 切换页面右侧内容
        changeModule(listModule, moduleName);
    }) 
    $('.tax-rate').bind('blur', function(){
        name = $(this).attr("name");
        
     })
    $('.incomeyear').bind('blur', function(){
       id = $(this).attr("id");
       curryeararr = id.split("_");
       curryear = curryeararr[curryeararr.length -1]
       curryear = parseInt(curryear)
       fz(id, "energy_supply_for_heating", curryear, curryear + 1, 20)
       fz(id, "power_supply_capacity", curryear, curryear + 1, 20)
       fz(id, "energy_supply_heating", curryear, curryear + 1, 20)
       fz(id, "energy_supply_for_cooling", curryear, curryear + 1, 20)
       fz(id, "vapour_production", curryear, curryear + 1, 20)
       fz(id, "income_other", curryear, curryear + 1, 20)
       fz(id, "income_otherother", curryear, curryear + 1, 20)
    })
    $('.costyear').bind('blur', function(){
        id = $(this).attr("id");
        curryeararr = id.split("_");
        curryear = curryeararr[curryeararr.length -1]
        curryear = parseInt(curryear)
        fz(id, "gas_consumption", curryear, curryear + 1, 20)
        fz(id, "coal_consumption", curryear, curryear + 1, 20)
        fz(id, "power_consumption", curryear, curryear + 1, 20)
        fz(id, "water_consumption", curryear, curryear + 1, 20)
        fz(id, "material_cost", curryear, curryear + 1, 20)
        fz(id, "maintenance_cost", curryear, curryear + 1, 20)
        fz(id, "artificial_cost", curryear, curryear + 1, 20)
        fz(id, "otherincluding_rent_capacity", curryear, curryear + 1, 20)
     })
     $('.targeyear').bind('blur', function(){
        id = $(this).attr("id");
        curryeararr = id.split("_");
        curryear = curryeararr[curryeararr.length -1]
        curryear = parseInt(curryear)
        fz(id, "bank_interest", curryear, curryear + 1, 20)
     })
    
    
    var dataformInit = $("#ccppEconomic").serializeArray();  
    oldFormData = JSON.stringify({ dataform: dataformInit });
    createLabelBind("ccppEconomic", oldFormData);

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

function fz(id1, id2, curryear, startyear, endyear){
    if(id1 == ""+id2+"_"+curryear+""){
        for(var i=startyear; i<=endyear; i++){
            $("#"+id2+"_"+i+"").val($("#"+id2+"_"+curryear+"").val())
        }
    }
}

function onblurtbdata2(){
    id = $(this).attr("id")
    fz(id, "energy_supply_for_heating", 2, 3, 20)
    fz(id, "power_supply_capacity", 2, 3, 20)
    fz(id, "energy_supply_heating", 2, 3, 20)
    fz(id, "energy_supply_for_cooling", 2, 3, 20)
    fz(id, "vapour_production", 2, 3, 20)
    fz(id, "income_other", 2, 3, 20)
    fz(id, "income_otherother", 2, 3, 20)
}

// 提交保存页面所有表单数据
function submitEconomicdata() {
    $.ajax({
        cache: false,
        type: "POST",
        url: './submitEconomicform',
        data: $('#ccppEconomic').serialize(),
        async: false,
        error: function (request) {
            messageToast('error', '检索发生异常！', 3000);
        },
        success: function (data) {
            if(data.state == 0){
                messageToast('info', data.message, 3000);
            }else{              
                unlockBreadcrumb();
                messageToast('success', data.message, 3000);
                datas = data.ccppinputdata
                permissiondata = data.permissiondata
                defaultvaluedata = data.defaultvaluedata
                assignmentAllForm($("#ccppEconomic input"), datas, permissiondata, defaultvaluedata);
                var dataformInit = $("#ccppEconomic").serializeArray();  
                oldFormData = JSON.stringify({ dataform: dataformInit });
                createLabelBind("ccppEconomic", oldFormData);              
            }
        }
    });
}


//获取ccpp计算页面数据并显示
function initInputData() {
    $.ajax({
        cache: true,
        type: "POST",
        url: '/ccpp/initEconomicInputData',
        data: {},
        async: false,
        error: function (request) {
            messageToast('error', '检索发生异常！', 3000);
        },
        success: function (data) {
            assignmentForm(data.economicInputData);
        }
    });
}

// 给页面中所有表单赋值
function assignmentForm(datas) {
    if(datas != null){
        var elements = getElements();
        var tempInputName;
        for (var i = 0; i < elements.length; i++) {
            tempInputName = elements[i];
            if((datas[tempInputName] != "" || datas[tempInputName] === 0) && datas[tempInputName] != null){
                $("input[name='" + tempInputName + "']").val(datas[tempInputName]);
            }
            $("input[name='" + tempInputName + "']").keypress(function (e) {
                return (/[\d.]/.test(String.fromCharCode(event.keyCode)))
            });
            $("input[name='" + tempInputName + "']").blur(function () {
                numvar = $(this).val()
                if(!isNumber(numvar)){
                    // messageToast('info', '输入有误，请重新输入！', 500);
                    $(this).val("")
                }
            });
            $("input[name='" + tempInputName + "']").css("style", "ime-mode:Disabled");
        }
        
    }
}
// 给页面中所有表单赋值
function assignmentAllForm(elements, datas, permissiondata, defaultvaluedata) {
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
        valid(tempInputName, []);
    }
}


//获取form中的所有的<input>对象
function getElements() {
    var tagElements = $("#ccppEconomic input");
    var elements = new Array();
    for (var j = 0; j < tagElements.length; j++) {
        elements.push(tagElements[j].name);
    }
    return elements;
}