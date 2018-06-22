$(document).ready(function () {

    // 给检索按钮绑定事件
    $('#queryPlans').bind('click', queryPlans);
    // 给删除按钮绑定事件
    // $('table tbody tr td a .deletePlan').on('click', deletePlan);
    $(".plan-list").on("click", "tbody tr td a:nth-child(2)", function() {
        var planId = $(this).parent().parent().children("td:first-child").text();
        deletePlan(planId);
    });

});

// 根据查询条件显示查询结果
function queryPlans() {
    var company_id = $("#findByCompany").val();
    var user_id = $("#findByUser").val();
    var moduleName = $("#menuSelect").val();
    $.ajax({
        url: '/queryPlans',
        data: { "company_id": company_id, 'user_id': user_id, 'moduleName': moduleName},
        type: 'post',
        cache: false,
        dataType: 'json',
        success: function (data) {
            $(".plan-list tbody").empty();
            var trString = "";
            for (var i = 0; i < data.newPlans.length; i++) {
                trString += "<tr><td>" + data.newPlans[i].id + "</td><td>";
                for (var j = 0; j < data.users.length; j++) {
                    if (data.newPlans[i].user_id == data.users[j].id) {
                        trString += data.users[j].user_name;
                    }
                }
                trString += "</td><td>";
                for (var k = 0; k < data.companys.length; k++) {
                    if (data.newPlans[i].company_id == data.companys[k].id) {
                        trString += data.companys[k].company_name;
                    }
                }
                trString += "</td><td>" + data.newPlans[i].company_location 
                    + "</td><td>" + data.newPlans[i].plan_create_date 
                    + "</td><td>" + data.newPlans[i].plan_update_date 
                    + "</td><td><a type='button' class='btn btn-success' href='/gasPowerGeneration/" 
                    + data.newPlans[i].id + "'><i class='fa fa-pencil-square-o'></i> 编辑方案</a>&nbsp;<a type='button' class='btn btn-danger deletePlan'><i class='fa fa-trash-o'></i> 删除方案</a></td></tr>";
            }
            $(".plan-list tbody").append(trString);
        },
        error: function () {
            messageToast('error', '检索发生异常！', 3000);
        }
    });
}



// 根据查询条件显示查询结果
function deletePlan(planId) {
    // var planId = $(this).text();
    // console.log($(this));
    // alert(planId);
    // var planId = $(this).parent().parent().children("td:first-child").text();
    var moduleName = $("#menuSelect").val();
    var company_id = $("#findByCompany").val();
    var user_id = $("#findByUser").val();
    $.ajax({
        url: '/deletePlan',
        data: { "planId": planId, "company_id": company_id, 'user_id': user_id, 'moduleName': moduleName},
        type: 'post',
        cache: false,
        dataType: 'json',
        success: function (data) {
            $(".plan-list tbody").empty();
            var trString = "";
            for (var i = 0; i < data.newPlans.length; i++) {
                trString += "<tr><td>" + data.newPlans[i].id + "</td><td>";
                for (var j = 0; j < data.users.length; j++) {
                    if (data.newPlans[i].user_id == data.users[j].id) {
                        trString += data.users[j].user_name;
                    }
                }
                trString += "</td><td>";
                for (var k = 0; k < data.companys.length; k++) {
                    if (data.newPlans[i].company_id == data.companys[k].id) {
                        trString += data.companys[k].company_name;
                    }
                }
                trString += "</td><td>" 
                + data.newPlans[i].company_location 
                + "</td><td>" + data.newPlans[i].plan_create_date 
                + "</td><td>" + data.newPlans[i].plan_update_date 
                + "</td><td><a type='button' class='btn btn-success' href='/gasPowerGeneration/" 
                + data.newPlans[i].id + "'><i class='fa fa-pencil-square-o'></i> 编辑方案</a>&nbsp;<a type='button' class='btn btn-danger deletePlan'><i class='fa fa-trash-o'></i> 删除方案</a></td></tr>";
            }
            $(".plan-list tbody").append(trString);
            messageToast('success', '删除方案成功！', 3000);
        },
        error: function () {
            messageToast('error', '删除方案发生异常！', 3000);
        }
    });
}
