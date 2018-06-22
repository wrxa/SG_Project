var oldFormData;

$(function() {
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
    // 提交保存页面所有表单数据
    $("#submitData").click(function(){
        $("#ccpptargethtml").val("ccpppararesearch")
        $.ajax({
            cache: false,
            type: "POST",
            url: './submitCalculateform',
            data: $('#ccppCalculateform').serialize(),
            async: false,
            error: function (request) {
                messageToast('error', '检索发生异常！', 3000);
            },
            success: function (data) {
                if(data.state == 1){
                    messageToast('info', data.message, 3000);
                }else{
                    messageToast('success', data.message, 3000);
                }
                var dataformInit = $("#ccppCalculateform").serializeArray();  
                oldFormData = JSON.stringify({ dataform: dataformInit });
                createLabelBind("ccppCalculateform", oldFormData);
            }
        });
    })

    data = initInputData();
    initData(data)
    
    $("#info1").on("click", function () {
        $("#showInfo").modal('show');
        $("#infoContent").html("<img class='img-responsive center-block' src='/static/img/ccpp/ccppcalculate/ccpp-t-1.PNG'/>");
    });

    //选择锅型
    $("#selectSingDouble").change(function(){
        var pottype = $(this).val();
        if(pottype == 'singlepot'){
            $("#doublepot input").val("")
            $('#doublepot').hide();
            $('#singlepot').show();
            assignmentForm($("#singlepot input"), data.ccppinputdata, data.permissiondata, data.defaultvaluedata);

            $('#selectSingDouble').val("singlepot")
            setInputdisable($("#doublepot input"), true);
        }else if(pottype == 'doublepot'){
            $("#singlepot input").val("")
            $('#singlepot').hide();
            $('#doublepot').show();
            $('#selectSingDouble').val("doublepot")
            assignmentForm($("#doublepot input"), data.ccppinputdata, data.permissiondata, data.defaultvaluedata);
            setInputdisable($("#singlepot input"), true);
        }else{
            $("#doublepot input").val("")
            $("#singlepot input").val("")
            $('#doublepot').hide();
            $('#singlepot').hide();
            $('#selectSingDouble').val("-1")
            setInputdisable($("#singlepot input"), true);
            setInputdisable($("#doublepot input"), true);
        }
    })

    var dataformInit = $("#ccppCalculateform").serializeArray();  
    oldFormData = JSON.stringify({ dataform: dataformInit });

    // 点击选择模块
    $('.left-select').bind('click', function(){
        // 当前页面所有模块list
        listModule = ["q-1", "q-2", "q-3", "q-4", "q-5", "q-6", "q-7", "q-8", "q-9", "q-10", "q-11", "q-12", "q-13"];
        var moduleName = $(this).attr("id");
        // 切换页面右侧内容
        changeModule(listModule, moduleName);
    })
    
    createLabelBind("ccppCalculateform", oldFormData);
});


function setInputdisable(elements, flg){
    for (var i = 0; i < elements.length; i++) {
            tempInput = elements[i];
            tempInput.readOnly=flg;
    }
}

function initData(data){
    datas = data.ccppinputdata
    permissiondata = data.permissiondata
    defaultvaluedata = data.defaultvaluedata
    assignmentForm($("#ccppCalculateform input"), datas, permissiondata, defaultvaluedata);
    $('#engine_id_design').val(datas['engine_id_design'])
    var pottype = datas['boiler_single_or_dula_pressure_design'];
    if(pottype == 'singlepot'){
        $('#doublepot').hide();
        $('#singlepot').show();
        $('#selectSingDouble').val("singlepot")
        setInputdisable($("#doublepot input"), true);
    }else if(pottype == 'doublepot'){
        $('#doublepot').show();
        $('#singlepot').hide();
        $('#selectSingDouble').val("doublepot")
        setInputdisable($("#singlepot input"), true);
    }else{
        $('#doublepot').hide();
        $('#singlepot').hide();
        $('#selectSingDouble').val("-1")
        setInputdisable($("#singlepot input"), true);
        setInputdisable($("#doublepot input"), true);
    }
}
//获取ccpp计算页面数据并显示
function initInputData() {
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
function assignmentForm(elements, datas, permissiondata, defaultvaluedata) {
    var tempInputName;
    for (var i = 0; i < elements.length; i++) {
        tempInputName = elements[i].name;
        if((datas[tempInputName] != "" || datas[tempInputName] == '0') && datas[tempInputName] != null){
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