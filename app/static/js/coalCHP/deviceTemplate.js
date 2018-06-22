var oldFormData;

$(document).ready(function () {
      init();
      // 定义面包屑个数
      var breakCount = 17;
      // 定义面包屑上id的模块类型
      var moduleName = "coalchp";
      initPreNext(moduleName, breakCount);
      // 上一页
      $('.pre').bind('click', function(){
          clickPre(breakCount, moduleName);
      });
      // 下一页
      $('.next').bind('click', function(){
          clickNext(breakCount, moduleName);
      });
   
      $("#saveEquipmentList").bind('click', saveEquipmentList);
      
          $("#getEquipmentList").bind('click', getEquipmentList);
      
          getEquipmentList();
      
          var dataformInit = $("#coalequipmentListForm").serializeArray();  
          oldFormData = JSON.stringify({ dataform: dataformInit });
          createLabelBind("coalequipmentListForm", oldFormData);
});

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

function getEquipmentList(){
    $.ajax({
        url: '/getEquipmentTemplate',
        data: {},
        type: 'post',
        cache: false,
        dataType: 'json',
        success: function (data) {
            drawEquipmentList(data);
        },
        error: function () {
            messageToast('error', '发生异常！',3000);
        }
    });
}

function analyzeEquipmentType(data, type){
    var equipmentCount = data.equipment_name.length;
    var title="";

    titleLists = [{ "title":"一、锅炉专业主要设备清册", "type":"a"},
    { "title":"二、汽轮机专业主要设备清册", "type":"b"},
    { "title":"三、输煤专业主要设备清册", "type":"c"},
    { "title":"四、除灰专业主要设备清册", "type":"d"},
    { "title":"五、除渣专业主要设备清册", "type":"e"},
    { "title":"六、供排水系统主要设备清册 ", "type":"f"},
    // { "title":"6.1、循环水系统", "type":"f11"},
    { "title":"6.1、循环水系统", "type":"f12"},
    { "title":"6.2、补给水系统", "type":"f2"},
    { "title":"6.3、排水系统", "type":"f3"},
    { "title":"6.4、消防系统", "type":"f4"},
    { "title":"6.5、其它设备", "type":"f5"},
    { "title":"七、化水专业主要设备清册", "type":"g"},
    { "title":"7.1、原水预处理系统", "type":"g1"},
    { "title":"7.2、除盐水系统", "type":"g2"},
    { "title":"7.3、化学加药系统", "type":"g3"},
    { "title":"7.4、水汽取样系统", "type":"g4"},
    { "title":"7.5、循环水加药系统", "type":"g5"},
    { "title":"7.6、循环水补水软化装置", "type":"g6"},
    { "title":"7.7、实验室仪器仪表", "type":"g7"},
    { "title":"八、电气专业主要设备清册", "type":"h"},
    { "title":"8.1、电气一次部分", "type":"h1"},
    { "title":"8.2、电气110kV户内GIS装备", "type":"h2"},
    { "title":"8.3、电气二次部分", "type":"h3"},
    { "title":"九、热工控制主要设备及清册", "type":"i"},
    { "title":"9.1、机炉控制系统", "type":"i1"},
    { "title":"9.2、辅助车间控制系统及仪表", "type":"i2"}]
    titleId = ["a","b","c","d","e","f","g","h","i"]
    id = 0;
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
    prohibitionlist = ['3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '17', '18', '19', '20', '22', '23', '33', '34', '35', '36', '38', '42', '47', '48', '49', '50', '53', '54', '55', '56', '73', '74', '91', '101', '103', '104', '105', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151'];
    countlist = ['3', '4', '5', '6', '7', '8', '11', '12']
    var tbodyString = "<tr attrid='" + type + "' class='alert alert-success alert-dismissible' role='alert'>"
        + "<td align='center'></td>"
        + "<td align='center'></td>"
        + "<td align='center' id=title" + id + ">●<b>" + title + "<b></td>"
        + "<td align='center'></td>"
        + "<td align='center'></td>"
        + "<td align='center'></td>"
        + "<td align='center'></td></tr>";
  
        var index = 1;
        for(var j = 0; j < equipmentCount; j++){
            if(data.equipment_type[j] == type){
    
                tbodyString += "<tr  attrid='" + type + "' class='alert alert-success alert-dismissible' role='alert' id='tr_" + j + "'>";
                tbodyString += "<td align='center' style='vertical-align: middle'>"
                + index
                + "<input class='form-control uid' type='hidden' name='equipmentUid_" + j + "' id='equipmentUid_" + j 
                + "' value='" + data.equipment_uid[j] + "'>"
                + "</td>";
    
    
                tbodyString += "<td align='center'>"
                // + equipment_json.equipment_name[j]
                // + "<input class='form-control name' type='text' name='equipmentName_" + j + "' id='equipmentName_" + j 
                // + "' value='" + equipment_json.equipment_name[j] + "'/>"
                + "<textarea style='resize:none;height: 40px;' onkeydown='checkEnter(event)' wrap='soft' class='form-control name' name='equipmentContent_" + j + "' id='equipmentContent_" + j + "'>" + data.equipment_name[j] + "</textarea>"
                + "<input class='form-control type' type='hidden' name='equipmentType_" + j + "' id='equipmentType_" + j 
                + "' value='" + data.equipment_type[j] + "'/>"
                + "</td>";
                
                tbodyString += "<td align='center'> <textarea style='resize:none;height: 40px;'";
                for(var n = 0; n<prohibitionlist.length; n++){
                    if(data.equipment_uid[j] == prohibitionlist[n]){
                        tbodyString +=  " readonly='readonly'";
                        break;
                    }
                }
                tbodyString += " onkeydown='checkEnter(event)' wrap='soft' class='form-control content' name='equipmentContent_" + j + "' id='equipmentContent_" + j + "'>" + data.equipment_content[j] + "</textarea>"
                + "</td>";
                
                tbodyString += "<td align='center'><textarea style='resize:none;height: 40px;'";
                for(var n = 0; n<countlist.length; n++){
                    if(data.equipment_uid[j] == countlist[n]){
                        tbodyString +=  " readonly='readonly'";
                        break;
                    }
                }
                tbodyString += "onkeydown='checkEnter(event)' wrap='soft' class='form-control count' name='equipmentCount_" + j + "' id='equipmentCount_" + j + "'>" + data.equipment_count[j] + "</textarea>"
                +"</td>";

                tbodyString += "<td align='center'>"
                // + equipment_json.equipment_unit[j]
                + "<textarea style='resize:none;height: 40px;' onkeydown='checkEnter(event)' wrap='soft' class='form-control unit' name='equipmentUnit_" + j + "' id='equipmentUnit_" + j + "'>" + data.equipment_unit[j] + "</textarea>"
                // + "<input class='form-control unit' type='text' name='equipmentUnit_" + j + "' id='equipmentUnit_" + j
                // + "' value='" + equipment_json.equipment_unit[j] + "'/>";
                +"</td>";

                tbodyString += "<td align='center'>"
                // + equipment_json.equipment_remark[j]
                // + "<input class='form-control remark' type='hidden' name='equipmentRemark_" + j + "' id='equipmentRemark_" + j
                // + "' value='" + equipment_json.equipment_remark[j] + "'/>";
                + "<textarea style='resize:none;height: 40px;' onkeydown='checkEnter(event)' wrap='soft' class='form-control remark' name='equipmentContent_" + j + "' id='equipmentContent_" + j + "'>" + data.equipment_remark[j] + "</textarea>"
                +"</td>";
    
                tbodyString += "<td align='center' style='vertical-align: middle'>"
                + "<button type='button' class='glyphicon glyphicon-trash' attr_del_id='" + j + "' onClick='deleteEquipment(this, true)'></button>"
                + "&nbsp;&nbsp;<button type='button' class='glyphicon glyphicon-plus' attr_add_id='" + j 
                + "' attr_add_type='" + data.equipment_type[j] + "' onClick='addEquipment(this)'></button>"
                // + "&nbsp;&nbsp;<button type='button' class='glyphicon glyphicon-pencil' attr_edit_id='" + j 
                // + "' attr_edit_type='" + equipment_json.equipment_type[j] + "' onClick='editEquipment(this)'></button>"
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
    bs = ['a', 'b', 'c', 'd', 'e', 'f', 'f12', 'f2', 'f3', 'f4', 'f5', 'g', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'h', 'h1', 'h2', 'h3', 'i', 'i1', 'i2']
    for (var index = 0; index < bs.length; index++) {
        tbodyString += analyzeEquipmentType(data, bs[index])
        
    }

    $(".equipment_list tbody").append(tbodyString);
}

function insertRow(index, type){  

    var rowObj = "<tr attrid='" + type + "'>"
    + "<td><input class='form-control uid' type='text'  value='' name='newUid' readonly='true'/></td>"
    + "<td><textarea onkeydown='checkEnter(event)' wrap='soft' style='width:100%;height:40px;resize:none;' name='newName' class='form-control name'/>"
    + "<input name='newType' class='form-control type' type='hidden' value='" + type + "' /></td>"
    + "<td><textarea onkeydown='checkEnter(event)' wrap='soft' style='width:100%;height:40px;resize:none;' name='newContent' class='form-control content'/></td>"
    + "<td><textarea onkeydown='checkEnter(event)' wrap='soft' style='width:100%;height:40px;resize:none;' name='newUnit' class='form-control unit'/></td>"
    + "<td><textarea onkeydown='checkEnter(event)' wrap='soft' style='width:100%;height:40px;resize:none;' name='newCount' class='form-control count'/></td>"
    + "<td><textarea onkeydown='checkEnter(event)' wrap='soft' style='width:100%;height:40px;resize:none;' name='newRemark' class='form-control remark'/></td>"
    + "<td align='center' style='vertical-align: middle;'>"
    + "<button type='button' class='glyphicon glyphicon-trash' onClick='deleteEquipment(this,false)'></button>"
    + "</td>"
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
function deleteEquipment(obj, flag) {
    thisattrid = $(obj).parent().parent().attr("attrid");
    objlist = $(obj).parent().parent().parent().children();
    
    numflag = 0;
    for(var i=0; i<objlist.length; i++){
        // alert(objlist[i])
        attrid = objlist[i].attributes.attrid.value;
        if(attrid == thisattrid){
            numflag++;
        }
    }
    if(numflag == 2){
        messageToast('info', '每个模块至少预留一条记录！',2000);
        return;
    }
    $(obj).parent().parent().remove();
    if(flag == true){
        saveEquipmentList(0);
    } 
}

function saveEquipmentList(flag){
    var nameData = $("input.name").serialize().replace(/\+/g," ");
    var contentData = $("input.content").serialize().replace(/\+/g," ");
    $.ajax({
        url: '/saveEquipmentTemplate',
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
                getEquipmentList();
                if(flag == 0){
                    messageToast('success', '燃煤热电联产-设备清单删除成功',2000);
                }else{
                    messageToast('success', '燃煤热电联产-设备清单保存成功',2000);
                }             
            }else{
                if(flag == 0){
                    messageToast('error', '燃煤热电联产-设备清单删除失败',2000);
                }else{
                    messageToast('success', '燃煤热电联产-设备清单保存失败',2000);
                }
            }

            var dataformInit = $("#coalequipmentListForm").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
            createLabelBind("coalequipmentListForm", oldFormData);
        },
        error: function () {
            messageToast('error', '发生异常！',2000);
        }
    });
}