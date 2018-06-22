var oldFormData;
var notDisplay;
var pSelect, pointFlow;

$(document).ready(function () {
    init();
    // 定义面包屑个数
    var breakCount = 16;
    // 定义面包屑上id的模块类型
    var moduleName = "biomass";
    initPreNext(moduleName, breakCount);
    // 上一页
    $('.pre').bind('click', function(){
        clickPre(breakCount, moduleName);
    });
    // 下一页
    $('.next').bind('click', function(){
        clickNext(breakCount, moduleName);
    });

    // 点击选择模块
    $('.left-select').bind('click', function(){
        // 当前页面所有模块list
        listModule = ["q-1", "q-2", "q-3", "q-4", "q-5", "q-6", "q-7", "q-8", "q-9", "q-10", "q-11", "q-12"];
        var moduleName = $(this).attr("id");
        // 切换页面右侧内容
        changeModule(listModule, moduleName);
    })

    $("#saveEquipmentList").bind('click', saveEquipmentList);

    getBiomassEquipmentList();

    $('#biomass15').attr('onclick', "messageToast('info', '正在进行出图处理，请稍候！',16000);")
    
    var dataformInit = $("#biomassEquipmentListForm").serializeArray();  
    oldFormData = JSON.stringify({ dataform: dataformInit });
    createLabelBind("biomassEquipmentListForm", oldFormData);
});

function getBiomassEquipmentList(){
    $.ajax({
        url: '/getBiomassEquipmentList',
        data: {},
        type: 'post',
        cache: false,
        dataType: 'json',
        success: function (data) {          
            drawEquipmentList(data);
            // messageToast('success', 'success',3000);
            var dataformInit = $("#biomassEquipmentListForm").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
            createLabelBind("biomassEquipmentListForm", oldFormData);
        },
        error: function () {
            messageToast('error', '发生异常！',3000);
        }
    });
}

function analyzeEquipmentType(data, type){
    var equipmentCount = data.equipment_name.length;
    var title="";

    titleLists = [{ "title":"一、锅炉及其辅助设备", "type":"a"},
    { "title":"二、汽轮机及其辅助设备", "type":"b"},
    { "title":"三、点火油系统", "type":"c"},
    { "title":"四、燃料供应系统", "type":"d"},
    { "title":"五、除渣系统", "type":"e"},
    { "title":"方案（一）：机械干法除渣", "type":"e1"},
    { "title":"方案（二）：机械湿法捞渣", "type":"e2"},
    { "title":"六、除灰系统 ", "type":"f"},
    { "title":"七、压缩空气系统", "type":"g"},
    { "title":"八、供排水系统", "type":"h"},
    { "title":"（一）循环水系统 ：自然通风", "type":"h11"},
    { "title":"（一）循环水系统 ：强制通风", "type":"h12"},
    { "title":"（二）补给水系统", "type":"h2"},
    { "title":"（三）排水系统", "type":"h3"},
    { "title":"（四）消防系统", "type":"h4"},
    { "title":"（五）其它设备", "type":"h5"},
    { "title":"九、化学水处理系统", "type":"i"},
    { "title":"（一）原水预处理部分", "type":"i1"},
    { "title":"（二）锅炉补给水处理系统", "type":"i2"},
    { "title":"（三）化学加药处理系统", "type":"i3"},
    { "title":"（四）水汽取样系统", "type":"i4"},
    { "title":"（五）循环水加药系统", "type":"i5"},
    { "title":"（六）循环水补水软化装置", "type":"i6"},
    { "title":"（七）实验室仪器仪表", "type":"i7"},
    { "title":"十、电气系统", "type":"j"},
    { "title":"（一）电气一次部分", "type":"j1"},
    { "title":"（二）电气110kV户内GIS装备", "type":"j2"},
    { "title":"（三）电气二次部分", "type":"j3"},
    { "title":"十一、热工控制系统", "type":"k"},
    { "title":"（一）DCS部分", "type":"k1"},
    { "title":"（二）锅炉部分", "type":"k2"},
    { "title":"（三）汽机部分", "type":"k3"},
    { "title":"（四）公用部分", "type":"k4"},    
    ]

    titleLists2 = [{ "title":"一、锅炉及其辅助设备", "type":"a"},
    { "title":"二、汽轮机及其辅助设备", "type":"b"},
    { "title":"三、燃料供应系统", "type":"d"},
    { "title":"四、除渣系统", "type":"e"},
    { "title":"方案（一）：机械干法除渣", "type":"e1"},
    { "title":"方案（二）：机械湿法捞渣", "type":"e2"},
    { "title":"五、除灰系统 ", "type":"f"},
    { "title":"六、压缩空气系统", "type":"g"},
    { "title":"七、供排水系统", "type":"h"},
    { "title":"（一）循环水系统 ：自然通风", "type":"h11"},
    { "title":"（一）循环水系统 ：强制通风", "type":"h12"},
    { "title":"（二）补给水系统", "type":"h2"},
    { "title":"（三）排水系统", "type":"h3"},
    { "title":"（四）消防系统", "type":"h4"},
    { "title":"（五）其它设备", "type":"h5"},
    { "title":"八、化学水处理系统", "type":"i"},
    { "title":"（一）原水预处理部分", "type":"i1"},
    { "title":"（二）锅炉补给水处理系统", "type":"i2"},
    { "title":"（三）化学加药处理系统", "type":"i3"},
    { "title":"（四）水汽取样系统", "type":"i4"},
    { "title":"（五）循环水加药系统", "type":"i5"},
    { "title":"（六）循环水补水软化装置", "type":"i6"},
    { "title":"（七）实验室仪器仪表", "type":"i7"},
    { "title":"九、电气系统", "type":"j"},
    { "title":"（一）电气一次部分", "type":"j1"},
    { "title":"（二）电气110kV户内GIS装备", "type":"j2"},
    { "title":"（三）电气二次部分", "type":"j3"},
    { "title":"十、热工控制系统", "type":"k"},
    { "title":"（一）DCS部分", "type":"k1"},
    { "title":"（二）锅炉部分", "type":"k2"},
    { "title":"（三）汽机部分", "type":"k3"},
    { "title":"（四）公用部分", "type":"k4"},    
    ]
    

    id = 0;
    titleId = ["a","b","c","d","e","f","g","h","i","j","k"]

    if (notDisplay == false) {
        for (var index = 0; index < titleLists.length; index++) {
        // var title = titleLists[index];
        if (type == titleLists[index]["type"]){
            title = titleLists[index]["title"]
            for (var i = 0; i < titleId.length; i++) {
                if (type == titleId[i])
                id = i+1;
            }
        }
        }
    } else {
        for (var index = 0; index < titleLists2.length; index++) {
        // var title = titleLists[index];
        if (type == titleLists2[index]["type"]){
            title = titleLists2[index]["title"]
            for (var i = 0; i < titleId.length; i++) {
                if (type == titleId[i])
                id = i+1;
            }
        }
        }
    } 

    var tbodyString = "<tr class='alert alert-success alert-dismissible' role='alert'>"
        + "<td align='center'></td>"
        + "<td align='center'></td>"
        + "<td align='center' id=title" + id + ">" + title + "</td>"
        + "<td align='center'></td>"
        + "<td align='center'></td>"
        + "<td align='center'></td>"
        + "<td align='center'></td></tr>";

        var index = 1;
        var noStart = false;
        var noWater = false;
        for(var j = 0; j < equipmentCount; j++){
            // 若方案书中无启动锅炉系统，则无此项。
            if(data['equipment_uid'][j] == '29' && data['equipment_content'][j] == ''){
                noStart = true;
            } else {
                noStart = false;
            }

            // 生物质发电项目无此项
            if(data['equipment_uid'][j] == '196' && pointFlow == 0){
                noWater = true;
            } else {
                noWater = false;
            }

            if(data.equipment_type[j] == type && noStart == false && noWater == false){
                // var index = parseInt(j)+ parseInt(1);
    
                // tbodyString += "<tr class='alert alert-success alert-dismissible' role='alert' id='tr_" + j + "'>";
                // tbodyString += "<td align='center'>"
                // + index 
                // + "<input class='form-control uid' type='hidden' name='equipmentUid_" + j + "' id='equipmentUid_" + j 
                // + "' value=" + data.equipment_uid[j] + ">"
                // + "</td>";
    
                // tbodyString += "<td align='center'>"
                // + "<input class='form-control name' type='text' name='equipmentName_" + j + "' id='equipmentName_" + j 
                // + "' value=" + data.equipment_name[j] + ">"
                // + "<input class='form-control type' type='hidden' name='equipmentType_" + j + "' id='equipmentType_" + j 
                // + "' value=" + data.equipment_type[j] + ">"
                // +"</td>";
                
                // tbodyString += "<td align='center'>"
                // + "<input class='form-control content' type='text' name='equipmentContent_" + j + "' id='equipmentContent_" + j
                // + "' value=" + data.equipment_content[j] + ">";
                // +"</td>";
    
                // tbodyString += "<td align='center'>"
                // + "<input class='form-control unit' type='text' name='equipmentUnit_" + j + "' id='equipmentUnit_" + j
                // + "' value=" + data.equipment_unit[j] + ">";
                // +"</td>";
    
                // tbodyString += "<td align='center'>"
                // + "<input class='form-control count' type='text' name='equipmentCount_" + j + "' id='equipmentCount_" + j
                // + "' value=" + data.equipment_count[j] + ">";
                // +"</td>";
    
                // tbodyString += "<td align='center'>"
                // + "<input class='remark' type='text' style='display:inline' name='equipmentRemark_" + j + "' id='equipmentRemark_" + j
                // + "' value=" + data.equipment_remark[j] + ">&nbsp;&nbsp;"
                // + "<button type='button' class='btn-danger' style='display:inline' attr_del_id='" + j + "' onClick='deleteEquipment(this)'>删除</button>"
                // + "&nbsp;&nbsp;<button type='button' class='btn-primary' style='display:inline' attr_add_id='" + j 
                // + "' attr_add_type='" + data.equipment_type[j] + "' onClick='addEquipment(this)'>增加</button>"
                // +"</td>";

            tbodyString += "<tr class='alert alert-success alert-dismissible' role='alert' id='tr_" + j + "'>";
            tbodyString += "<td align='center' style='vertical-align: middle;'>"
            + index 
            + "<input class='form-control uid' type='hidden' name='equipmentUid_" + j + "' id='equipmentUid_" + j 
            + "' value='" + data.equipment_uid[j] + "' />"
            + "</td>";

            tbodyString += "<td align='center'>"
            + "<textarea onkeydown='checkEnter(event)' class='form-control name' wrap='soft' style='width:100%;height:40px;resize:none;' type='text' name='equipmentName_" + j + "' id='equipmentName_" + j + "'>"
            + data.equipment_name[j] + "</textarea>"
            + "<input class='form-control type' type='hidden' name='equipmentType_" + j + "' id='equipmentType_" + j 
            + "' value='" + data.equipment_type[j] + "' />"
            +"</td>";
            
            // tbodyString += "<td align='center'>"
            // + "<input class='form-control content' type='text' name='equipmentContent_" + j + "' id='equipmentContent_" + j
            // + "' value='" + data.equipment_content[j] + "' />";
            // +"</td>";

            tbodyString += "<td align='center'>"
            + "<textarea onkeydown='checkEnter(event)' class='form-control content' wrap='soft' style='width:100%;height:40px;resize:none;' type='text' name='equipmentContent_" + j + "' id='equipmentContent_" + j + "'>"
            + data.equipment_content[j] + "</textarea>"
            +"</td>";

            tbodyString += "<td align='center'>"
            + "<textarea onkeydown='checkEnter(event)' class='form-control unit' wrap='soft' style='width:100%;height:40px;resize:none;' type='text' name='equipmentUnit_" + j + "' id='equipmentUnit_" + j + "'>"
            + data.equipment_unit[j] + "</textarea>"
            +"</td>";

            tbodyString += "<td align='center'>"
            + "<textarea onkeydown='checkEnter(event)' class='form-control count' wrap='soft' style='width:100%;height:40px;resize:none;' type='text' name='equipmentCount_" + j + "' id='equipmentCount_" + j + "'>"
            + data.equipment_count[j] + "</textarea>"
            +"</td>";

            tbodyString += "<td align='center'>"
            + "<textarea onkeydown='checkEnter(event)' class='form-control remark' wrap='soft' style='width:100%;height:40px;resize:none;' type='text' name='equipmentRemark_" + j + "' id='equipmentRemark_" + j + "'>"
            + data.equipment_remark[j] + "</textarea>"  //&nbsp;&nbsp;"
            // + "<button type='button' class='glyphicon glyphicon-trash' style='display:inline' attr_del_id='" + j + "' onClick='deleteEquipment(this)'></button>"
            // + "&nbsp;&nbsp;<button type='button' class='glyphicon glyphicon-plus' style='display:inline' attr_add_id='" + j 
            // + "' attr_add_type='" + data.equipment_type[j] + "' onClick='addEquipment(this)'></button>"
            +"</td>";

            tbodyString += "<td align='center' style='vertical-align: middle;'>"
            + "<button type='button' class='glyphicon glyphicon-trash' attr_del_id='" + j + "' onClick='deleteEquipment(this, true)'></button>"
            + "&nbsp;<button type='button' class='glyphicon glyphicon-plus' attr_add_id='" + j 
            + "' attr_add_type='" + data.equipment_type[j] + "' onClick='addEquipment(this)'></button>"
            +"</td>";
                
                tbodyString +="</tr>";  
                index++;
            }
            
        }
        return tbodyString;
}

//动态画页面
function drawEquipmentList(data){
    //var equipmentCount = data.equipment_name.length;
    $(".equipment_list tbody").empty();
    var tbodyString = "";

    getType();

    if ((data["equipment_content"][0].indexOf('循环流化床锅炉') != -1 || data["equipment_content"][0].indexOf('高低差速循环流化床锅炉') != -1) && (data["equipment_content"][0].indexOf('锅炉计算') == -1))  {
        notDisplay = true;
    } else {
        notDisplay = false;
    }
    
    bs = ['a', 'b', 'c', 'd', 'e', 'e1', 'e2', 'f', 'g', 'h', 'h11', 'h12', 'h13', 'h2', 'h3', 'h4', 'h5', 'i', 'i1', 'i2', 'i3', 'i4', 'i5', 'i6', 'i7', 'j', 'j1', 'j2', 'j3', 'k', 'k1', 'k2', 'k3', 'k4']
    for (var index = 0; index < bs.length; index++) {

        if(bs[index] == 'c') {
            if ((data["equipment_content"][0].indexOf('循环流化床锅炉') == -1 && data["equipment_content"][0].indexOf('高低差速循环流化床锅炉') == -1) || (data["equipment_content"][0].indexOf('锅炉计算') != -1)) {
                tbodyString += analyzeEquipmentType(data, bs[index])
            } 
        } else if(bs[index] == 'e1') {
            if ((data["equipment_content"][0].indexOf('循环流化床锅炉') != -1 || data["equipment_content"][0].indexOf('高低差速循环流化床锅炉') != -1) || (data["equipment_content"][0].indexOf('锅炉计算') != -1)){
                tbodyString += analyzeEquipmentType(data, bs[index])  
            }

        } else if(bs[index] == 'e2') {
            if ((data["equipment_content"][0].indexOf('循环流化床锅炉') == -1 && data["equipment_content"][0].indexOf('高低差速循环流化床锅炉') == -1) || (data["equipment_content"][0].indexOf('锅炉计算') != -1)) {
                tbodyString += analyzeEquipmentType(data, bs[index])  
            }
        } else if(bs[index] == 'h11') {
            if(pSelect == "1" || pSelect == null) {
                tbodyString += analyzeEquipmentType(data, bs[index])  
            }
        } else if(bs[index] == 'h12') {
            if(pSelect == '2' || pSelect == null) {
                tbodyString += analyzeEquipmentType(data, bs[index])  
            }
        } else if(bs[index] == 'h5') {
            if(pointFlow > 0 || pointFlow == null) {
                tbodyString += analyzeEquipmentType(data, bs[index])  
            }

        } else {
            tbodyString += analyzeEquipmentType(data, bs[index])  
        }
        // tbodyString += analyzeEquipmentType(data, bs[index])
  
    }

    $(".equipment_list tbody").append(tbodyString);
}

function insertRow(index, type){

    var rowObj = "<tr>"
    + "<td><input class='form-control uid' type='text' readonly='true' name='equipmentUid_new'/></td>"
    + "<td><textarea name='newName' class='form-control name' type='text'/>"
    + "<input name='newType' class='form-control type' type='hidden' value='" + type + "' /></td>"
    + "<td><textarea name='newContent' class='form-control content' type='text'/></td>"
    + "<td><textarea name='newUnit' class='form-control unit' type='text'/></td>"
    + "<td><textarea name='newCount' class='form-control count' type='text'/></td>"
    + "<td><textarea name='newRemark' class='form-control remark' type='text'/></td>"
    + "</tr>";

    var trId = "#tr_" + index;
    $(trId).after(rowObj);
}

function addEquipment(obj){
    var currentId = $(obj).attr("attr_add_id");
    var currentType = $(obj).attr("attr_add_type");
    insertRow(currentId, currentType);
}

//删除该条设备
function deleteEquipment(obj) {
    $(obj).parent().parent().remove();
    saveEquipmentList(0);
}

function saveEquipmentList(flag){
    $.ajax({
        url: '/saveBiomassEquipmentList',
        data: {
                "uidData": $("input.uid").serialize().replace(/\+/g," "),
                "nameData": $("textarea.name").serialize().replace(/\+/g," "),
                "typeData": $("input.type").serialize().replace(/\+/g," "),
                "contentData": $("textarea.content").serialize().replace(/\+/g," "),
                "unitData": $("textarea.unit").serialize().replace(/\+/g," "),
                "countData": $("textarea.count").serialize().replace(/\+/g," "),
                "remarkData": $("textarea.remark").serialize().replace(/\+/g," ")
            },
        type: 'post',
        cache: false,
        dataType: 'json',
        success: function (data) {
            if(data.state == 'success'){
                getBiomassEquipmentList();
                if(flag == 0){
                    messageToast('success', '删除成功',2000);
                }else{
                    messageToast('success', '保存成功',2000);
                }             
            }else{
                if(flag == 0){
                    messageToast('error', '删除失败',2000);
                }else{
                    messageToast('error', '保存失败',2000);
                }
            }

            var dataformInit = $("#biomassEquipmentListForm").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
            createLabelBind("biomassEquipmentListForm", oldFormData);
        },
        error: function () {
            messageToast('error', '发生异常！',2000);
        }
    });
}

//获得冷却塔类型
function getType() {
    planId = $('#planId').val();
    $.ajax({
        cache: true,
        type: "POST",
        url: './getType',
        data: { "planId": planId },
        async: false,
        error: function (request) {
            // alert("Connection error1");
        },
        success: function (data) {
            pSelect = data.getDatas.p_select;
            pointFlow = data.getDatas.e_exhaust_point_flow   
        }
    });
}

function checkEnter(e){
    var et=e||window.event;
    var keycode=et.charCode||et.keyCode;   
    if(keycode==13){
        if(window.event)
           window.event.returnValue = false;
         else
           e.preventDefault();//for firefox
    }
}


