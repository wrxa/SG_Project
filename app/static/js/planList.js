var planId;
var m;

$(document).ready(function () {
    // 给检索按钮绑定事件
    $('#queryPlans').bind('click', queryPlans);
    // 给删除按钮绑定事件
    $(".plan-list").on("click", "tbody tr td a:nth-child(2)", function () {
        planId = $(this).parent().parent().children("td:first-child").attr("data-id");
        // 删除确认
        $("#alertInfo").modal('show');
        $("#alertContent").html("请确认是否删除该方案？");
    });
    
    
    $(".plan-list").on("click", "tbody tr td:nth-child(4)", function () {
        planId = $(this).parent().children("td:first-child").attr("data-id");
        $.ajax({
            cache: false,
            type: "POST",
            url: '/getmainequipemntpara',
            data: {'planId': planId},
            async: false,
            error: function (request) {
               
            },
            success: function (data) {
                $("#alertparaContent").val(data.main_equipment_para)
            }
        });
        $("#alterparaInfo").modal('show');
    });

    $("#paraconfirmBtn").on("click", function () {
        $.ajax({
            cache: false,
            type: "POST",
            url: '/updatamainequipemntpara',
            data: {'planId': planId, 'main_equipment_para': $("#alertparaContent").val()},
            async: false,
            error: function (request) {
               
            },
            success: function (data) {
                $("#alterparaInfo").modal('hide');
                queryPlans()
            }
        });
    });

    $("#confirmBtn").on("click", function () {
        deletePlan(planId);
        $("#alertInfo").modal('hide');
    });


    // 给预览按钮绑定事件
    $(".yulan").on("click", function () {
        //启动进度条:线程
        m = messageToast('info', '正在生成图像中......',30000000);
        planId = $(this).parent().parent().children("td:first-child").attr("data-id");
        // setTimeout(prepreviewdealwith,100);
        new Worker("/static/js/progressbar.js").onmessage = function(){
            prepreviewdealwith()
        };
    });

    $.getJSON("/getAutoComplete", function (result) {
        $( "#findByCompany" ).autocomplete({
        source: result.companysComplete
      });
        $( "#findByUser" ).autocomplete({
        source: result.usersComplete
      });
    });
});

function test(){
    $(".progress").css("display", "block");
    var blower = null;
    blower = new LoadingBlower("#loadingContainer");
    blower.addProgress(100);
}

function prepreviewdealwith(){
    $.ajax({
        cache: false,
        type: "POST",
        url: '/prepreviewdealwith',
        data: {'planId': planId},
        async: false,
        error: function (request) {
           
        },
        success: function (data) { 
            if(data.exceptionInfo != null){
                document.body.removeChild(m)
                messageToast('info', data.exceptionInfo,3000);
                return;
            }
            mdcontent = data.mdcontent
            htmlcontent = markdown.toHTML(data.mdcontent, "Maruku");
            $.ajax({
                cache: false,
                type: "POST",
                url: '/gethtmlandmd',
                data: {'planId': planId, 'htmlcontent': htmlcontent, 'mdcontent': mdcontent},
                async: false,
                error: function (request) {
                   
                },
                success: function (data) {
                    if(data.state == 1){
                        document.body.removeChild(m)
                        // 关闭进度条
                        messageToast('info', '解析模板文件中......',2000);
                        // worker.terminate();
                        setTimeout(tz,2000);
                        // window.open("/converMD/" + planId);
                    }
                }
            });
        }
    });
}

function tz(){
    window.open("/converMD/" + planId);
}

// 根据查询条件显示查询结果
function queryPlans() {
    var company_id = $("#findByCompany").val();
    var user_id = $("#findByUser").val();
    var moduleName = $("#moduleName").val();
    $.ajax({
        url: '/queryPlans',
        data: { "company_id": company_id, 'user_id': user_id, 'moduleName': moduleName },
        type: 'post',
        cache: false,
        dataType: 'json',
        success: function (data) {
            if ($("#pageFlag").val() == "report") {
                $(".report-list tbody").empty();
            }
            if ($("#pageFlag").val() == "planList") {
                $(".plan-list tbody").empty();
            }
            var trString = "";
            for (var i = 0; i < data.newPlans.length; i++) {

                trString += "<tr><td data-id='"+data.newPlans[i].id+"' id='tempId'>" + data.newPlans[i].plan_name +"</td><td>";
                for (var k = 0; k < data.companys.length; k++) {
                    if (data.newPlans[i].company_id == data.companys[k].id) {
                        trString += data.companys[k].company_name;
                    }
                }
                if(data.newPlans[i].main_equipment_para != null){
                    // trString += "</td><td>" + data.newPlans[i].company_location + "</td><td style='cursor: pointer;' title='"+data.newPlans[i].main_equipment_para+"'>" + data.newPlans[i].main_equipment_para.substring(0,13) + "...</td><td>";
                    trString += "</td><td>" + data.newPlans[i].company_location + "</td><td style='cursor: pointer;'>"
                    for(var m = 0; m < data.newPlans[i].main_equipment_para_list.length; m++){
                        trString += "<div>● " + data.newPlans[i].main_equipment_para_list[m] + "</div>"
                    }
                    trString += "</td><td>";
                }else{
                    trString += "</td><td>" + data.newPlans[i].company_location + "</td><td style='cursor: pointer;'>...</td><td>";
                }                

                for (var j = 0; j < data.users.length; j++) {
                    if (data.newPlans[i].user_id == data.users[j].id) {
                        trString += data.users[j].user_name;
                    }
                }
                trString += "</td><td>" + data.newPlans[i].plan_create_date.substring(0,10) + "</td><td>";
                if(data.newPlans[i].approver_id == null){
                    trString += "<span class='label label-info'>未审核</span></td><td><span class='label label-info'>未审核</span>";
                }else{
                    for (var j = 0; j < data.users.length; j++) {
                        if (data.newPlans[i].approver_id == data.users[j].id) {
                            trString += data.users[j].user_name;
                        }
                    }
                    trString += "</td><td>" + data.newPlans[i].approve_time.substring(0,10);
                }
                
                if ($("#pageFlag").val() == "report") {
                    if(data.newPlans[i].plan_state == -1){
                        trString += "</td><td><div class='progress'> <div class='progress-bar progress-bar-danger' role='progressbar' aria-valuenow='100' aria-valuemin='0' aria-valuemax='100' style='width: 25%;'> <span>未绑定</span> </div> </div></td>";
                    }
                    if(data.newPlans[i].plan_state == 0){
                        trString += "</td><td><div class='progress'> <div class='progress-bar progress-bar-warning' role='progressbar' aria-valuenow='100' aria-valuemin='0' aria-valuemax='100' style='width: 50%;'> <span>未审核</span> </div> </div></td>";
                    }
                    if(data.newPlans[i].plan_state == 1){
                        trString += "</td><td><div class='progress'> <div class='progress-bar progress-bar-info' role='progressbar' aria-valuenow='100' aria-valuemin='0' aria-valuemax='100' style='width: 75%;'> <span>审核中</span> </div> </div></td>";
                    }
                    if(data.newPlans[i].plan_state == 2){
                        trString += "</td><td><div class='progress'> <div class='progress-bar progress-bar-success' role='progressbar' aria-valuenow='100' aria-valuemin='0' aria-valuemax='100' style='width: 100%;'> <span>已审核</span> </div> </div></td>";
                    }
                    // trString += "<td><a type='button' title='编辑报告' href='/editPlanReport/" + data.newPlans[i].id + "'><i class='fa fa-pencil-square-o'></i></a>&nbsp;";
                    if (data.newPlans[i].template_id != null) {
                        trString += "<td><a type='button' href='/converMD/" + data.newPlans[i].id + "' target='_blank' title='预览报告' style='margin-left: 10px;'><i class='fa fa-file-text-o'></i></a></td></tr>";
                    }else{
                        if (data.newPlans[i].moduleName == "coalCHP"){
                            trString += "<td><a href='/coalChooseTemplate/"+data.newPlans[i].id+"'>选择模板</a></td></tr>";
                        }else if(data.newPlans[i].moduleName == "gasPowerGeneration") {
                            trString += "<td><a href='/GPG_ChooseTemplate/"+data.newPlans[i].id+"'>选择模板</a></td></tr>";
                        }else if(data.newPlans[i].moduleName == "biomassCHP") {
                            trString += "<td><a href='/biomassChooseTemplate/"+data.newPlans[i].id+"'>选择模板</a></td></tr>";
                        }else if(data.newPlans[i].moduleName == "CCPP") {
                            trString += "<td><a href='/ccpp/toChooseTemplate/"+data.newPlans[i].id+"'>选择模板</a></td></tr>";
                        }
                        
                    }
                }
                if ($("#pageFlag").val() == "planList") {
                    trString += "</td><td><a type='button' title='编辑方案' class='btn-margin' href='/editPlan/" + data.newPlans[i].id + data.newPlans[i].moduleName+ "'><i class='fa fa-pencil-square-o'></i></a>&nbsp;<a type='button' class='btn-margin' style='margin-left: 20px;' title='删除方案'><i class='fa fa-trash-o'></i></a></td></tr>";
                }
            }
            if ($("#pageFlag").val() == "report") {
                $(".report-list tbody").append(trString);
            }
            if ($("#pageFlag").val() == "planList") {
                $(".plan-list tbody").append(trString);
            }

        },
        error: function () {
            messageToast('error', '检索发生异常！', 3000);
        }
    });
}

// 根据查询条件显示查询结果
function deletePlan(planId) {
    var moduleName = $("#moduleName").val();
    var company_id = $("#findByCompany").val();
    var user_id = $("#findByUser").val();
    $.ajax({
        url: '/deletePlan',
        data: { "planId": planId, "company_id": company_id, 'user_id': user_id, 'moduleName': moduleName },
        type: 'post',
        cache: false,
        dataType: 'json',
        success: function (data) {
            $("#findByCompany").val("");
            $("#findByUser").val("");
            $(".plan-list tbody").empty();
            var trString = "";
            for (var i = 0; i < data.newPlans.length; i++) {
                trString += "<tr><td data-id='"+data.newPlans[i].id+"' id='tempId'> " + data.newPlans[i].plan_name +"</td><td>";
                for (var k = 0; k < data.companys.length; k++) {
                    if (data.newPlans[i].company_id == data.companys[k].id) {
                        trString += data.companys[k].company_name;
                    }
                }//data.newPlans[i].plan_update_date.substring(0,10)
                if(data.newPlans[i].main_equipment_para != null){
                    //trString += "</td><td>" + data.newPlans[i].company_location + "</td><td style='cursor: pointer;' title='"+data.newPlans[i].main_equipment_para+"'>" + data.newPlans[i].main_equipment_para.substring(0,13) + "...</td><td>";
                    trString += "</td><td>" + data.newPlans[i].company_location + "</td><td style='cursor: pointer;'>"
                    for(var m = 0; m < data.newPlans[i].main_equipment_para_list.length; m++){
                        trString += "<div>● " + data.newPlans[i].main_equipment_para_list[m] + "</div>"
                    }
                    trString += "</td><td>";
                }else{
                    trString += "</td><td>" + data.newPlans[i].company_location + "</td><td style='cursor: pointer;'>...</td><td>";
                }

                for (var j = 0; j < data.users.length; j++) {
                    if (data.newPlans[i].user_id == data.users[j].id) {
                        trString += data.users[j].user_name;
                    }
                }

                trString += "</td><td>" + data.newPlans[i].plan_create_date.substring(0,10) + "</td><td>";
                if(data.newPlans[i].approver_id == null){
                    trString += "<span class='label label-info'>未审核</span></td><td><span class='label label-info'>未审核</span>";
                }else{
                    for (var j = 0; j < data.users.length; j++) {
                        if (data.newPlans[i].approver_id == data.users[j].id) {
                            trString += data.users[j].user_name;
                        }
                    }
                    trString += "</td><td>" + data.newPlans[i].approve_time.substring(0,10);
                }

                trString += "</td><td><a type='button' title='编辑方案' class='btn-margin' href='/editPlan/" + data.newPlans[i].id +　data.newPlans[i].moduleName+  "'><i class='fa fa-pencil-square-o'></i></a>&nbsp;<a type='button' class='btn-margin' style='margin-left: 20px;' title='删除方案'><i class='fa fa-trash-o'></i></a></td></tr>";
            }
            $(".plan-list tbody").append(trString);
            messageToast('success', '删除方案成功！', 3000);
        },
        error: function () {
            messageToast('error', '删除方案发生异常！', 3000);
        }
    });
}