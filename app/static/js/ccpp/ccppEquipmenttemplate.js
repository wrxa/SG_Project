var oldFormData;
var imgmesg;
$(document).ready(function () {
    init();
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
    $("#saveEquipmentList").bind('click', saveEquipmentList);
    
    $("#getEquipmentList").bind('click', getEquipmentList);

    getEquipmentList();
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
        url: '/ccpp/getEquipmentTemplate',
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

function analyzeEquipmentType(equipment_json, prohibitionlist, type, title, id){
    var equipmentCount = equipment_json.equipment_name.length;
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
            if(equipment_json.equipment_type[j] == type){
                tbodyString += "<tr attrid='" + type + "' class='alert alert-success alert-dismissible' role='alert' id='tr_" + j + "'>";
                tbodyString += "<td align='center' style='vertical-align: middle'>"
                + index 
                + "<input class='form-control uid' type='hidden' name='equipmentUid_" + j + "' id='equipmentUid_" + j 
                + "' value='" + equipment_json.equipment_uid[j] + "'/>"
                + "</td>";
    
                tbodyString += "<td align='center'>"
                // + equipment_json.equipment_name[j]
                // + "<input class='form-control name' type='text' name='equipmentName_" + j + "' id='equipmentName_" + j 
                // + "' value='" + equipment_json.equipment_name[j] + "'/>"
                + "<textarea style='resize:none;height: 40px;' onkeydown='checkEnter(event)' wrap='soft' class='form-control name' name='equipmentContent_" + j + "' id='equipmentContent_" + j + "'>" + equipment_json.equipment_name[j] + "</textarea>"
                + "<input class='form-control type' type='hidden' name='equipmentType_" + j + "' id='equipmentType_" + j 
                + "' value='" + equipment_json.equipment_type[j] + "'/>"
                + "</td>";
                
                tbodyString += "<td align='center'> <textarea style='resize:none;height: 40px;'";
                for(var n = 0; n<prohibitionlist.length; n++){
                    if(equipment_json.equipment_uid[j] == prohibitionlist[n]){
                        tbodyString +=  " readonly='readonly'";
                        break;
                    }
                }
                tbodyString += " onkeydown='checkEnter(event)' wrap='soft' class='form-control content' name='equipmentContent_" + j + "' id='equipmentContent_" + j + "'>" + equipment_json.equipment_content[j] + "</textarea>"
                + "</td>";
                
                tbodyString += "<td align='center'>"
                // + equipment_json.equipment_count[j]
                + "<textarea style='resize:none;height: 40px;' onkeydown='checkEnter(event)' wrap='soft' class='form-control count' name='equipmentCount_" + j + "' id='equipmentCount_" + j + "'>" + equipment_json.equipment_count[j] + "</textarea>"
                // + "<input class='form-control count' type='text' name='equipmentCount_" + j + "' id='equipmentCount_" + j
                // + "' value='" + equipment_json.equipment_count[j] + "'/>";
                +"</td>";

                tbodyString += "<td align='center'>"
                // + equipment_json.equipment_unit[j]
                + "<textarea style='resize:none;height: 40px;' onkeydown='checkEnter(event)' wrap='soft' class='form-control unit' name='equipmentUnit_" + j + "' id='equipmentUnit_" + j + "'>" + equipment_json.equipment_unit[j] + "</textarea>"
                // + "<input class='form-control unit' type='text' name='equipmentUnit_" + j + "' id='equipmentUnit_" + j
                // + "' value='" + equipment_json.equipment_unit[j] + "'/>";
                +"</td>";

                tbodyString += "<td align='center'>"
                // + equipment_json.equipment_remark[j]
                // + "<input class='form-control remark' type='hidden' name='equipmentRemark_" + j + "' id='equipmentRemark_" + j
                // + "' value='" + equipment_json.equipment_remark[j] + "'/>";
                + "<textarea style='resize:none;height: 40px;' onkeydown='checkEnter(event)' wrap='soft' class='form-control remark' name='equipmentContent_" + j + "' id='equipmentContent_" + j + "'>" + equipment_json.equipment_remark[j] + "</textarea>"
                +"</td>";
    
                tbodyString += "<td align='center' style='vertical-align: middle'>"
                + "<button type='button' class='glyphicon glyphicon-trash' attr_del_id='" + j + "' onClick='deleteEquipment(this, true)'></button>"
                + "&nbsp;&nbsp;<button type='button' class='glyphicon glyphicon-plus' attr_add_id='" + j 
                + "' attr_add_type='" + equipment_json.equipment_type[j] + "' onClick='addEquipment(this)'></button>"
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
    $(".equipment_list tbody").empty();
    var tbodyString = "";
    var equipment_json = data.equipment_json
    var titlelist = data.titlelist
    var prohibitionlist = data.prohibitionlist
    var id = 1;
    for(var i=0; i<titlelist.length; i++){
        tbodyString += analyzeEquipmentType($.parseJSON(equipment_json), prohibitionlist, titlelist[i].key, titlelist[i].val, id);
        id += 1;
    }  
    $(".equipment_list tbody").append(tbodyString);
}

function insertRow(index, type){  
    var rowObj = "<tr attrid='" + type + "'>"
    + "<td><input name='newUid' class='form-control uid' type='text' value='' readonly='true'/></td>"
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
        messageToast('info', '燃气蒸汽联合循环-至少预留一空记录',2000);
        return;
    }
    $(obj).parent().parent().remove();
    if(flag == true){
        saveEquipmentTemplate(0);
    } 
}

function saveEquipmentList(flag){
    $.ajax({
        url: '/ccpp/saveEquipmentTemplate',
        data: {
                // "deleteId": deleteId, 
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
                    messageToast('success', '燃气蒸汽联合循环-设备清单模板删除成功',2000);
                }else{
                    messageToast('success', '燃气蒸汽联合循环-设备清单模板保存成功',2000);
                }             
            }else{
                if(flag == 0){
                    messageToast('error', '燃气蒸汽联合循环-设备清单模板删除失败',2000);
                }else{
                    messageToast('success', '燃气蒸汽联合循环-设备清单模板保存失败',2000);
                }
            }

            var dataformInit = $("#ccpp_equipmentListForm").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
            createLabelBind("ccpp_equipmentListForm", oldFormData);
        },
        error: function () {
            messageToast('error', '发生异常！',2000);
        }
    });
}