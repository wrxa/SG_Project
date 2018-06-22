var templateId;
var template_id;
var template_name;
$(document).ready(function () {
    $(".template-list").on("click", "tbody tr td a:nth-child(2)", function () {
        templateId = $(this).parent().parent().children("td:first-child").attr("template-id");
        // 删除确认
        $("#alertInfo").modal('show');
        $("#alertContent").html("请确认是否删除该模板？");        
    });

    $("#confirmBtn").on("click", function () {
        deleteTemplate(templateId);
        $("#alertInfo").modal('hide');
    });

    $('#queryTemplate').bind('click', queryTemplate);
    $('#templateAdd').bind('click', getTemplateByModule);

    $.getJSON("/getAutoComplete", function (result) {
        $( "#findByTemplateName" ).autocomplete({
        source: result.templateComplete
      });
        $( "#findByUser" ).autocomplete({
        source: result.usersComplete
      });
    });

});
/************************************************ 以下代码处理用户编辑模板时，选择要插入MD中的数据库字段  ****************************************************************************/
function getTemplateByModule(){
    $.ajax({
        cache: false,
        type: "POST",
        url: '../getTemplateByModule',
        data: {},
        async: false,
        error: function (request) {
            messageToast('error', '发生异常！',3000);
        },
        success: function (data) {
            createTableContent(data.reportTemplateJson);
            addSelectTableClick(data.reportTemplateJson);
            $('#selectCopyTemplate').modal({backdrop: 'static', keyboard: false});
            $("#closeSelectCopyTemplateBtn").on("click", function () {
                $("#selectCopyTemplate").modal('hide');
                $("#copyTemplate_content tr:gt(0)").empty();
                $("#copyTemplate_content tr").not(':eq(0)').empty()
            });
        }
    });
}
function getJsonLength(jsonData) {
    var jsonLength = 0;  
    for(var item in jsonData) {  
        jsonLength++;   
    } 
    return jsonLength;  
}

function createTableContent(reportTemplateJson) {
    var length = getJsonLength(reportTemplateJson)
    var table = $('#copyTemplate_content');
    $("#selectCopyTemplateInfo").html("请选择模板");
    $("#copyTemplate_title").html("模板名称");
    for(var i = 0; i < length; i++){
        var tr = $("<tr></tr>");
        tr.appendTo(table)
        var td = $("<td> <a name=" + reportTemplateJson[i].template_id + ">拷贝" + reportTemplateJson[i].template_name + "</td>");
        td.appendTo(tr);
    }
    var tr = $("<tr></tr>");
    tr.appendTo(table)
    var td = $("<td> <a name='0'>新建模板</td>");
    td.appendTo(tr);
}

function addSelectTableClick(reportTemplateJson){
    var length = getJsonLength(reportTemplateJson)
    for(var i = 0; i < length; i++){
        var template_id =  reportTemplateJson[i].template_id;
        var template_name =  reportTemplateJson[i].template_id;
        $("a[name='" + template_id  + "']").bind('click', {template_id: template_id, template_name: template_name }, getTemplateByName)
    }
    $("a[name='0']").bind('click', {template_id: 0, template_name: '新建模板' }, getTemplateByName)
}

function getTemplateByName(event){
    template_id = event.data.template_id;
    template_name = event.data.template_name;
    $("#alertInfoCopyTemplate").modal({backdrop: 'static', keyboard: false});
    if(template_id == 0){
        $("#alertContentCopyTemplate").html("确定新建模板吗？");
    }else{
        $("#alertContentCopyTemplate").html("确定拷贝该模板吗？");
    }
    $("#closeBtnCopyTemplate").html("取消");
}
$("#closeBtnCopyTemplate").on("click", function (){
    $("#alertInfoCopyTemplate").modal('hide');
});

$("#confirmBtnCopyTemplate").on("click", function (){
    $("#alertInfoCopyTemplate").modal('hide');
    if(template_id == 0){
        // alert(template_id)
        window.location.href = "/creattemplate";
    }else{
        window.location.href = "/copytemplate/" + template_id;
    }
    
});           

$('#selectCopyTemplate').on('hidden.bs.modal', function () {
    //$('#table_content tr').html("");
    $("#copyTemplate_content tr:gt(0)").empty();
    $("#copyTemplate_content tr").not(':eq(0)').empty()
})
/****************************************************************************************************************************************************************************/
function queryTemplate(){
    var template_name = $("#findByTemplateName").val();
    var user_name = $("#findByUser").val();
    var moduleName = $("#moduleName").val();

    $.ajax({
        url: '/queryTemplate',
        data: { "template_name": template_name, 'user_name': user_name, 'moduleName': moduleName },
        type: 'post',
        cache: false,
        dataType: 'json',
        success: function (data) {
            $(".template-list tbody").empty();
            var trString = "";
            for (var i = 0; i < data.templateListJson.length; i++) {
                trString += "<tr><td template-id='" + data.templateListJson[i].id + "' id='tempId'>";
                trString += data.templateListJson[i].template_name;
                trString += "</td><td>";
                for (var j = 0; j < data.users.length; j++) {
                    if (data.templateListJson[i].user_id == data.users[j].id) {
                        trString += data.users[j].user_name;
                    }
                }

                trString += "</td><td>";
                trString += data.templateListJson[i].template_create_date.substring(0,10) + "</td><td>" 
                trString += data.templateListJson[i].template_update_date.substring(0,10);
                
                trString += "</td><td><a type='button' title='编辑模板' class='btn-margin' href='/edittemplate/" 
                    + data.templateListJson[i].id 
                    + "'><i class='fa fa-pencil-square-o'></i></a>&nbsp;<a type='button' class='btn-margin' style='margin-left: 20px;' title='删除方案'><i class='fa fa-trash-o'></i></a></td></tr>";
            }
            $(".template-list tbody").append(trString);
        },
        error: function () {
            messageToast('error', '检索发生异常！', 1000);
        }
    });
}

function deleteTemplate(templateId) {
    var moduleName = $("#moduleName").val();
    $.ajax({
        url: '/deleteTemplate',
        data: { 
                "templateId": templateId, 
                'moduleName': moduleName 
                /*, "company_id": company_id, 'user_id': user_id, 'moduleName': moduleName*/ 
            },
        type: 'post',
        cache: false,
        dataType: 'json',
        success: function (data) {
            if(data.state =="1"){
                messageToast('info', data.massage, 1000);
            }else if(data.state =="-1"){
                messageToast('error', data.massage, 1000);
            }else{
                $("#findByCompany").val("");
                $("#findByUser").val("");
                $(".template-list tbody").empty();
                var trString = "";
                for (var i = 0; i < data.templateListJson.length; i++) {
                    trString += "<tr><td template-id='" + data.templateListJson[i].id + "' id='tempId'>";
                    trString += data.templateListJson[i].template_name;
                    trString += "</td><td>";
                    for (var j = 0; j < data.users.length; j++) {
                        if (data.templateListJson[i].user_id == data.users[j].id) {
                            trString += data.users[j].user_name;
                        }
                    }

                    trString += "</td><td>";
                    trString += data.templateListJson[i].template_create_date.substring(0,10) + "</td><td>" 
                    trString += data.templateListJson[i].template_update_date.substring(0,10);
                    
                    trString += "</td><td><a type='button' title='编辑模板' class='btn-margin' href='/edittemplate/" 
                        + data.templateListJson[i].id 
                        + "'><i class='fa fa-pencil-square-o'></i></a>&nbsp;<a type='button' class='btn-margin' style='margin-left: 20px;' title='删除方案'><i class='fa fa-trash-o'></i></a></td></tr>";
                }
                $(".template-list tbody").append(trString);
                messageToast('success', data.massage, 1000);
            }         
        },
        error: function () {
            messageToast('error', '删除模板发生异常！', 1000);
        }
    });
}