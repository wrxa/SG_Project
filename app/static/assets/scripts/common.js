$(document).ready(function() {
    
    // 左侧菜单切换的样式
    var leftMeun = ['collapsed index', 'elements', 'charts', 'tables', 'typography', 'icons',
                    'coalQuestionnaire', 'coalFurnace', 'coalSteamTurbine', 'coalHandingSystem',
                    'biomassQuestionnaire', 'biomassFurnace', 'biomassSteamTurbine',
                    'ccppQuestionnaire', 'ccppFurnace', 'ccppSteamTurbine',
                    'GPG_Questionnaire'
                    ];
    var menuSelect = $("#menuSelect").val();

    for (var i = 0; i < leftMeun.length; i++) {
        if (menuSelect == leftMeun[i]) {
            if(menuSelect == 'coalQuestionnaire' || menuSelect == 'coalFurnace' || menuSelect == 'coalSteamTurbine' || menuSelect == 'coalHandingSystem') {
                // alert()
                if($('.sidebar a[data-toggle="collapse"]').hasClass('collapsed')) {
                    $('#coalMean').attr('class', 'index active');
                    $('#coal').attr('class', 'collapse in');
                } else {
                    $('#coalMean').attr('class', 'collapsed index');
                }
            }
            if(menuSelect == 'biomassQuestionnaire' || menuSelect == 'biomassFurnace' || menuSelect == 'biomassSteamTurbine') {
                // alert()
                if($('.sidebar a[data-toggle="collapse"]').hasClass('collapsed')) {
                    $('#biomassMean').attr('class', 'index active');
                    $('#biomass').attr('class', 'collapse in');
                } else {
                    $('#biomassMean').attr('class', 'collapsed index');
                }
            }
            if(menuSelect == 'ccppQuestionnaire' || menuSelect == 'ccppFurnace' || menuSelect == 'ccppSteamTurbine') {
                // alert()
                if($('.sidebar a[data-toggle="collapse"]').hasClass('collapsed')) {
                    $('#ccppMean').attr('class', 'index active');
                    $('#ccpp').attr('class', 'collapse in');
                } else {
                    $('#ccppMean').attr('class', 'collapsed index');
                }
            }
            if(menuSelect == 'GPG_Questionnaire') {
                // alert()
                if($('.sidebar a[data-toggle="collapse"]').hasClass('collapsed')) {
                    $('#gaspowerMean').attr('class', 'index active');
                    $('#gaspower').attr('class', 'collapse in');
                } else {
                    $('#gaspowerMean').attr('class', 'collapsed index');
                }
            }
            $("." + menuSelect).addClass('active');
        }
    }

    // 表格数据添加绑定事件
    // $('#listUser').bind('click', list_user);

});

$(function () { 
	$("[data-toggle='popover']").popover();
});

$(window).on('click', function(event) {
    var target = $(event.target);
    if (!target.hasClass('popover')
            && target.parent('.popover-content').length === 0
            && target.parent('.popover-title').length === 0
            && target.parent('.popover').length === 0
            && target.data("toggle") !== "popover") {
        $("[data-toggle='popover']").popover('hide');
    }else{
        target.popover('toggle');
    }
});



/**
 * 查询所有用户权限信息
 */
// function list_user() {
//     $.getJSON("./list_user", function (result) {
//         datas = result.datas;
//         alert(datas);
//     });
// }