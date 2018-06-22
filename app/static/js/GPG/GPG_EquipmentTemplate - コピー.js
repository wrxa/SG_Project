var oldFormData;

$(document).ready(function () {
    /*
    init();
    // 定义面包屑个数
    var breakCount = 12;
    // 定义面包屑上id的模块类型
    var moduleName = "gpg";
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
    */

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


    $("#saveEquipmentTemplate").bind('click', saveEquipmentTemplate);

    getGPGEquipmentTemplate();

    var dataformInit = $("#GPG_EquipmentTemplateForm").serializeArray();  
    oldFormData = JSON.stringify({ dataform: dataformInit });
    createLabelBind("GPG_EquipmentTemplateForm", oldFormData);

    //jQuery实现textarea高度根据内容自适应
    $.fn.extend({
        txtaAutoHeight: function () {
            return this.each(function () {
                var $this = $(this);
                if (!$this.attr('_initAdjustHeight')) {
                    $this.attr('_initAdjustHeight', $this.outerHeight());
                }
                setAutoHeight(this).on('input', function () {
                    setAutoHeight(this);
                });
            });
            function setAutoHeight(elem) {
                var $obj = $(elem);
                return $obj.css({ height: $obj.attr('_initAdjustHeight'), 'overflow-y': 'hidden' }).height(elem.scrollHeight);
            }
        }
    });
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

function getGPGEquipmentTemplate(){
    $.ajax({
        url: '/getGPGEquipmentTemplate',
        data: {},
        type: 'post',
        cache: false,
        dataType: 'json',
        success: function (data) {          
            drawEquipmentList(data);
            //textarea高度自适应，暂时不做
            // $(function () {
            //     $('textarea').txtaAutoHeight();
            // });
            var dataformInit = $("#GPG_EquipmentTemplateForm").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
            createLabelBind("GPG_EquipmentTemplateForm", oldFormData);
        },
        error: function () {
            messageToast('error', '发生异常！',3000);
        }
    });
}

function isReadonly(uid){
    var flag = false;
    if(uid == null){
        return false;
    }       
    var dbUidArray = ['uid1','uid2','uid3','uid4','uid11','uid12','uid13','uid14','uid16',
            'uid17','uid18','uid20','uid21','uid22','uid28','uid29','uid30',
            'uid31','uid35','uid36','uid98','uid100','uid101','uid102','uid107',
            'uid108','uid109','uid110','uid111','uid112','uid113','uid114',
            'uid115','uid116'];
    for(var i = 0; i < dbUidArray.length; i++){
        if(dbUidArray[i] == uid){
            flag = true;
            break;
        }
    }
    return flag;
}

function analyzeEquipmentType(data, type){
    var equipmentCount = data.equipment_name.length;
    var title="";
    var tbodyString ="";
    switch(type){
        case "1heat":
            title = "一、热机部分";
            break;
        case "2elec":
            title = "二、电气部分";
            break;
        case "3control":
            title = "三、热控部分";
            break;
        case "4control-fire":
            title = "点火控制系统";
            break;
        case "5monitor-fire":
            title = "炉膛火焰监视部分";
            break;
        case "6monitor-water":
            title = "汽包水位监视部分";
            break;
        case "7water":
            title = "四、水工部分";
            break;
        case "8chemistry-water":
            title = "五、化学水系统";
            break;
    }

    if(type == "5monitor-fire"){
        tbodyString += "<tr class='alert alert-success alert-dismissible' role='alert'>"
        + "<td align='center'></td>"
        + "<td align='left' id='title_cctv'><b>●工业电视监控系统</b></td>"
        + "<td align='center'></td>"
        + "<td align='center'></td>"
        + "<td align='center'></td>"
        + "<td align='center'></td>"
        + "<td align='center'></td></tr>";
    }
    if(type == "4control-fire" || type == "5monitor-fire" || type == "6monitor-water"){
        tbodyString += "<tr class='alert alert-success alert-dismissible' role='alert'>"
        + "<td align='center'></td>"
        + "<td align='left'><b>●" + title + "</b></td>"
        + "<td align='center'></td>"
        + "<td align='center'></td>"
        + "<td align='center'></td>"
        + "<td align='center'></td>"
        + "<td align='center'></td></tr>";
    }else{
        tbodyString += "<tr class='alert alert-success alert-dismissible' role='alert' attr_type='" + type + "'>"
        + "<td align='center'></td>"
        + "<td align='center'></td>"
        + "<td align='center' id='title_" + type + "'><b>" + title + "</b></td>"
        + "<td align='center'></td>"
        + "<td align='center'></td>"
        + "<td align='center'></td>"
        + "<td align='center'>"

        //删除该组全部设备, 暂时不做
        //+ "<button type='button' class='glyphicon glyphicon-trash' attr_del_id='" + j + "' onClick='deleteEquipmentByType(this)'></button>"
        + "</td></tr>";
    }   

    var index = 1;
    for(var j = 0; j < equipmentCount; j++){
        if(data.equipment_type[j] == type){

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
            // + "' value='" + data.equipment_content[j] + "'>";
            // +"</td>";

            if(isReadonly(data.equipment_uid[j])){
                tbodyString += "<td align='center'>"
                + "<textarea readonly='readonly' class='form-control content' wrap='soft' style='width:100%;height:40px;resize:none;' type='text' name='equipmentContent_" + j + "' id='equipmentContent_" + j + "'>"
                + "该部分内容和数据库计算绑定,不可编辑该模板</textarea>"
                + "</td>";
            }else{
                tbodyString += "<td align='center'>"
                + "<textarea onkeydown='checkEnter(event)' class='form-control content' wrap='soft' style='width:100%;height:40px;resize:none;' type='text' name='equipmentContent_" + j + "' id='equipmentContent_" + j + "'>"
                + data.equipment_content[j] + "</textarea>"
                + "</td>";
            }

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
    $(".equipment_list tbody").empty();
    var tbodyString = "";
    tbodyString += analyzeEquipmentType(data, "1heat");
    tbodyString += analyzeEquipmentType(data, "2elec");
    tbodyString += analyzeEquipmentType(data, "3control");
    tbodyString += analyzeEquipmentType(data, "4control-fire");
    tbodyString += analyzeEquipmentType(data, "5monitor-fire");
    tbodyString += analyzeEquipmentType(data, "6monitor-water");
    tbodyString += analyzeEquipmentType(data, "7water");
    tbodyString += analyzeEquipmentType(data, "8chemistry-water");

    $(".equipment_list tbody").append(tbodyString);
}

function insertRow(index, type){
    var rowObj = "<tr>"
    + "<td><input class='form-control uid' type='hidden' name='newUid' value='' /></td>"
    + "<td><textarea onkeydown='checkEnter(event)' wrap='soft' style='width:100%;height:40px;resize:none;' name='newName' class='form-control name' type='text'></textarea>"
    + "<input name='newType' class='form-control type' type='hidden' value='" + type + "' /></td>"
    + "<td><textarea onkeydown='checkEnter(event)' wrap='soft' style='width:100%;height:40px;resize:none;' name='newContent' class='form-control content' type='text'></textarea></td>"
    + "<td><textarea onkeydown='checkEnter(event)' wrap='soft' style='width:100%;height:40px;resize:none;' name='newUnit' class='form-control unit' type='text'></textarea></td>"
    + "<td><textarea onkeydown='checkEnter(event)' wrap='soft' style='width:100%;height:40px;resize:none;' name='newCount' class='form-control count' type='text'></textarea></td>"
    + "<td><textarea onkeydown='checkEnter(event)' wrap='soft' style='width:100%;height:40px;resize:none;' name='newRemark' class='form-control remark' type='text'></textarea></td>"
    + "<td align='center' style='vertical-align: middle;'>"
    + "<button type='button' class='glyphicon glyphicon-trash' onClick='deleteEquipment(this,false)'></button>"
    +"</td>"
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
    $(obj).parent().parent().remove();
    if(flag == true){
        saveEquipmentTemplate(0);
    }   
}

//删除该组全部设备, 暂时不做
function deleteEquipmentByType(obj) {
    var attr_type = $(obj).parent().parent().attr("attr_type");
    $("input.type").each(function(){
        if($(this).val() == attr_type){
            $(this).parent().parent().remove();
        }
      });
    //$(obj).parent().parent().remove();
    saveEquipmentTemplate(0);
}

function saveEquipmentTemplate(flag){
    var nameData = $("textarea.name").serialize().replace(/\+/g," ");

    $("textarea.content").each(function(){
        if($(this)[0].readOnly == true){
            $(this)[0].value = '';
            $(this)[0].textContent = '';
        }
    });

    var contentData = $("textarea.content").serialize().replace(/\+/g," ");
    var remarkData = $("textarea.remark").serialize().replace(/\+/g," ");
    var unitData = $("textarea.unit").serialize().replace(/\+/g," ");
    var countData = $("textarea.count").serialize().replace(/\+/g," ");

    $.ajax({
        url: '/saveGPGEquipmentTemplate',
        data: {
                "uidData": $("input.uid").serialize(),
                "nameData": nameData,
                "typeData": $("input.type").serialize(),
                "contentData": contentData,
                "unitData": unitData,
                "countData": countData,
                "remarkData": remarkData
            },
        type: 'post',
        cache: false,
        dataType: 'json',
        success: function (data) {
            if(data.state == 'success'){
                getGPGEquipmentTemplate();
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

            var dataformInit = $("#GPG_EquipmentTemplateForm").serializeArray();  
            oldFormData = JSON.stringify({ dataform: dataformInit });
            createLabelBind("GPG_EquipmentTemplateForm", oldFormData);
        },
        error: function () {
            messageToast('error', '发生异常！',2000);
        }
    });
}
