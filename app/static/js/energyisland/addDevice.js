var oldFormData;

$(document).ready(function () {
    init();
    
    var dataformInit = $("#energyisland_addDeviceForm").serializeArray();  
    oldFormData = JSON.stringify({ dataform: dataformInit });

    // 点击选择模块
    $('.left-select').bind('click', function(){
        // 当前页面所有模块list
        listModule = ["q-1", "q-2", "q-3", "q-4", "q-5", "q-6", "q-7", "q-8", "q-9", "q-10", "q-11", "q-12"];
        var moduleName = $(this).attr("id");
        // 切换页面右侧内容
        changeModule(listModule, moduleName);
    })

    $("#device_class").change(function(){
        $("#device_type").find("option:selected").text("");
        $("#device_type").empty();
        var id = $(this).val();
        switch(id){
            case "1":
                $("#device_type").append("<option value='1'>蒸汽型溴化锂机组</option>");
                $("#device_type").append("<option value='2'>高温水大温差型  HDC系列</option>");
                $("#device_type").append("<option value='3'>低温水大温差型  LCC-**DH系列</option>");
                $("#device_type").append("<option value='4'>低温水型  LCC系列</option>");
                $("#device_type").append("<option value='5'>高温水型  HCC系列</option>");
                $("#device_type").append("<option value='6'>烟气热水补燃型溴化锂吸收式冷温水机</option>");
                $("#device_type").append("<option value='7'>烟气热水型溴化锂吸收式冷温水机</option>");
                $("#device_type").append("<option value='8'>烟气双效型溴化锂吸收式冷温水机</option>");
                $("#device_type").append("<option value='9'>烟气补燃型溴化锂吸收式冷温水机</option>");
                $("#device_type").append("<option value='10'>溴化锂吸收式直燃三用机</option>");
                break;
            case "2":
                $("#device_type").append("<option value='1'>LG系列螺杆制冷压缩机</option>");
                break;
            case "3":
                $("#device_type").append("<option value='1'>地源热泵</option>");
                $("#device_type").append("<option value='2'>空气源热泵</option>");
                break;
            case "4":
                $("#device_type").append("<option value='1'>燃气轮机</option>");
                break;
            case "5":
                $("#device_type").append("<option value='1'>内燃机</option>");
                break;
            case "6":
                $("#device_type").append("<option value='1'>光伏</option>");
                break;
            case "7":
                $("#device_type").append("<option value='1'>空压站</option>");
                break;
            case "9":
                $("#device_type").append("<option value='1'>并网模式</option>");
                $("#device_type").append("<option value='1'>离网模式</option>");
                break;
            case "12":
                $("#device_type").append("<option value='1'>风电</option>");
                break;
            case "13":
                $("#device_type").append("<option value='1'>污水</option>");
                break;
        }

        $(".device_property tbody").empty();
        $("#addDeviceBtn").attr("disabled","disabled")
        $("#confirmDeviceType").removeAttr("disabled"); 
    });

    $("#device_type").change(function(){
        $(".device_property tbody").empty();
        $("#addDeviceBtn").attr("disabled","disabled")
        $("#confirmDeviceType").removeAttr("disabled"); 
    });

    $("#confirmDeviceType").bind('click', confirmDeviceType);

    $("#addDeviceBtn").bind('click', addDevice);

    $("#displayDevice").bind('click', displayDevice);

    createLabelBind("energyisland_addDeviceForm", oldFormData);
});

function displayDevice(){
    $("#deviceListDiv").show();
    $("#addDeviceDiv").hide();
    $("#addDeviceBtn").attr("disabled","disabled")
     $("#confirmDeviceType").removeAttr("disabled");
     $("#deviceID").text("");

    //  $("#energyisland_addDeviceForm").find("input,textarea").each(function(){
    //     this.value ="";
    //  });

    var deviceClass = $("#device_class").val();
    var deviceType = $("#device_type").val();

    $.ajax({
        url: '/getDeviceList',
        data: { "deviceClass": deviceClass,  "deviceType": deviceType},
        type: 'post',
        cache: false,
        dataType: 'json',
        success: function (data) {
            drawDeviceList(data);
        },
        error: function () {
            messageToast('error', '发生异常！',3000);
        }
    });
}

//动态画页面
function drawDeviceList(data){
    var deviceCount = data.props_json_list.length;
    var devicePropertyLength = $.parseJSON(data.props_json_list[0]).prop_name.length;
    $(".device_list thead").empty();
    $(".device_list tbody").empty();
    var theadString = "";
    var tbodyString = "";

    theadString += "<tr>";
    theadString += "<th><div style='width:50px' align='center'></div></th>";
    for(var i = 0; i < devicePropertyLength; i++){
        theadString += "<th><div style='width:150px' align='center'>" + $.parseJSON(data.props_json_list[0]).prop_name[i];

        //判断“单位”是否为空
        if($.parseJSON(data.props_json_list[0]).prop_unit[i] != null && $.parseJSON(data.props_json_list[0]).prop_unit[i] != ""){
            theadString += "(" + $.parseJSON(data.props_json_list[0]).prop_unit[i] + ")";
        }

        theadString += "</div></th>";
    }
    theadString += "</tr>";

    for(var j = 0; j < deviceCount; j++){
        tbodyString += "<tr class='alert alert-success alert-dismissible' role='alert'>";
        tbodyString += "<td><div style='width:100px' align='center'>"
            + "<button type='button' class='btn-danger' attr_id='" + data.id_list[j] + "' onClick='deleteDevice(this)'>删除</button>"
            + " <button type='button' class='btn-primary' attr_id='" + data.id_list[j] + "' onClick='modifyDevice(this)'>编辑</button>" 
            + "</div></td>";

        for(var k = 0; k < devicePropertyLength; k++){
            tbodyString +="<td align='center'>"
            + $.parseJSON(data.props_json_list[j]).prop_value[k]
            +"</td>";
        }
        tbodyString +="</tr>";
    }

    $(".device_list thead").append(theadString);
    $(".device_list tbody").append(tbodyString);
}

//编辑该条设备
function modifyDevice(obj){
    var deviceId = $(obj).attr("attr_id");
    $("#deviceListDiv").hide();
    $("#addDeviceDiv").show();
    $("#deviceID").text(deviceId);

    $.ajax({
        url: '/getDeviceByID',
        data: { "deviceId": deviceId },
        type: 'post',
        cache: false,
        dataType: 'json',
        success: function (data) {
            var length = $.parseJSON(data.props_json).prop_name.length;
            $(".device_property tbody").empty();
            var theadString = "";
            var tbodyString = "";

            for (var i = 0; i < length; i++) {
                tbodyString += "<tr><td style='width:30%'>"
                    + "<span class='input-group-addon show-primary width-size'>" + $.parseJSON(data.props_json).prop_name[i] + "</span>"
                    + "</td>";
                tbodyString += "<td style='width:70%'><input class='form-control' type='text' name='device_property_" + i 
                    + "' value=" + $.parseJSON(data.props_json).prop_value[i] + "></td>";
                tbodyString += "</tr>";
            }
            $(".device_property tbody").append(tbodyString);

            $("#addDeviceBtn").removeAttr("disabled");     
            // $("#confirmDeviceType").attr("disabled","disabled");      
        },
        error: function () {
            messageToast('error', '发生异常！',3000);
        }
    });
}

//删除该条设备
function deleteDevice(obj) {
    var deviceId = $(obj).attr("attr_id");
    //alert(deviceId);

    $.ajax({
        url: '/deleteDevice',
        data: { "deviceId": deviceId },
        type: 'post',
        cache: false,
        dataType: 'json',
        success: function (data) {
            messageToast('success', '删除设备成功',2000);
            drawDeviceList(data);
        },
        error: function () {
            messageToast('error', '发生异常！',2000);
        }
    });
}

function addDevice(){
    var deviceId = $("#deviceID").text();
    var run = true;
    $("input[type=text]").each(function(){
        var inputName = this.name;
        if(inputName != null && inputName !="" && inputName.indexOf("device_property_") > -1){
            var value = $(this).val();
            if(value == null || $.trim(value) == ''){
                run = false;
                messageToast('error', '请填入全部数值',2000);
            }
        }        
    });

    if(run == true){
        var deviceClass = $("#device_class").val();
        var deviceType = $("#device_type").val();

        if(deviceId != null && deviceId !=""){
            $.ajax({
                url: '/editDevice',
                data: { "deviceId": deviceId, "formData": $('#energyisland_addDeviceForm').serialize()},
                type: 'post',
                cache: false,
                dataType: 'json',
                success: function (data) {
                    if(data.state == 'success'){
                        messageToast('success', '修改设备参数成功',2000);
                    }else{
                        messageToast('error', '修改设备参数失败',2000);
                    }
                },
                error: function () {
                    messageToast('error', '发生异常！',2000);
                }
            });
        }else{
            $.ajax({
                url: '/addDevice',
                //data: { "test": "test",  "form": $('#energyisland_addDeviceForm').serialize()},
                data: { "formData": $('#energyisland_addDeviceForm').serialize()},
                //data: $('#energyisland_addDeviceForm').serialize(),
                type: 'post',
                cache: false,
                dataType: 'json',
                success: function (data) {
                    if(data.state == 'success'){
                        messageToast('success', '添加设备成功',2000);
                    }else{
                        messageToast('error', '添加设备失败',2000);
                    }
                },
                error: function () {
                    messageToast('error', '发生异常！',2000);
                }
            });
        }
    }  
}

function confirmDeviceType(){
    $("#deviceListDiv").hide();
    $("#addDeviceDiv").show();
    $("#deviceID").text("");

    var deviceClass = $("#device_class").val();
    var deviceType = $("#device_type").val();

    $.ajax({
        url: '/getPropertyByDeviceType',
        data: { "deviceClass": deviceClass,  "deviceType": deviceType},
        type: 'post',
        cache: false,
        dataType: 'json',
        success: function (data) {
            var length = data.prop_name.length;
            $(".device_property tbody").empty();
            var theadString = "";
            var tbodyString = "";

            for (var i = 0; i < length; i++) {
                tbodyString += "<tr><td style='width:30%'>"
                    + "<span class='input-group-addon show-primary width-size'>" + data.prop_name[i] + "</span>"
                    + "</td>";
                tbodyString += "<td style='width:70%'><input class='form-control' type='text' name='device_property_" + i 
                    + "'></td>";
                tbodyString += "</tr>";
            }
            $(".device_property tbody").append(tbodyString);

            $("#addDeviceBtn").removeAttr("disabled");     
            $("#confirmDeviceType").attr("disabled","disabled");      
        },
        error: function () {
            messageToast('error', '发生异常！',3000);
        }
    });
}

// 给页面中所有表单赋值
function assignmentForm(datas) {
    var elements = getElements();
    var tempInput;
    for (var i = 0; i < elements.length; i++) {
        tempInput = elements[i];
        $("input[name='" + tempInput + "']").val(datas[tempInput]);
    }
}

//获取form中的所有的<input>对象
function getElements() {
    var tagElements = $("#energyisland_addDeviceForm input");
    var elements = new Array();
    for (var j = 0; j < tagElements.length; j++) {
        elements.push(tagElements[j].name);
    }
    return elements;
}
