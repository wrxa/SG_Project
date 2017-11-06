$(document).ready(function() {
    
    // 左侧菜单切换的样式
    var leftMeun = ['collapsed index', 'elements', 'charts', 'tables', 'typography', 'icons',
                    'coalQuestionnaire', 'coalFurnace', 'coalSteamTurbine', 'coalHandingSystem', 'coalDesulfurization' ,
                    'coalBoilerAuxiliaries', 'coalRemovalAshSlag', 'coalCirculatingWater', 'coalSmokeAirSystem',
                    'biomassQuestionnaire', 'biomassFurnace', 'biomassSteamTurbine','biomassFuelStorTran',
                    'biomassDesulDenit', 'biomassDASRemove', 'biomassBoilerAuxiliaries', 'biomassOfficialProcess',
                    'ccppQuestionnaire', 'ccppFurnace', 'ccppSteamTurbine',
		    'GPG_Questionnaire', 'GPG_BoilerOfPTS', 'GPG_GasAirSystem', 'GPG_SmokeResistance', 'GPG_WindResistance'
                    ];
    var menuSelect = $("#menuSelect").val();

    for (var i = 0; i < leftMeun.length; i++) {
        if (menuSelect == leftMeun[i]) {
            if(menuSelect == 'coalQuestionnaire' || menuSelect == 'coalFurnace' || menuSelect == 'coalSteamTurbine' || menuSelect == 'coalHandingSystem' || menuSelect == 'coalDesulfurization' || menuSelect == 'coalBoilerAuxiliaries' || menuSelect == 'coalRemovalAshSlag' || menuSelect == 'coalCirculatingWater' || menuSelect == 'coalSmokeAirSystem') {
                // alert()
                if($('.sidebar a[data-toggle="collapse"]').hasClass('collapsed')) {
                    $('#coalMean').attr('class', 'index active');
                    $('#coal').attr('class', 'collapse in');
                } else {
                    $('#coalMean').attr('class', 'collapsed index');
                }
            }
            if(menuSelect == 'biomassQuestionnaire' || menuSelect == 'biomassFurnace' || menuSelect == 'biomassSteamTurbine' || menuSelect == 'biomassFuelStorTran' || menuSelect == 'biomassDesulDenit' || menuSelect == 'biomassDASRemove' || menuSelect == 'biomassBoilerAuxiliaries' || menuSelect == 'biomassOfficialProcess') {
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
            if(menuSelect == 'GPG_Questionnaire'|| menuSelect == 'GPG_BoilerOfPTS' || menuSelect == 'GPG_GasAirSystem'
                || menuSelect == 'GPG_SmokeResistance' || menuSelect == 'GPG_WindResistance') {
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

// 给页面中所有表单赋值
function assignmentForm(datas, formName) {
    var elements = getElements(formName);
    var tempInput;
    for (var i = 0; i < elements.length; i++) {
        tempInput = elements[i];
        $("input[name='" + tempInput + "']").val(datas[tempInput]);
    }
}


//获取form中的所有的<input>对象
function getElements(formName) {
    var tagElements = $("#" + formName + " input");
    var elements = new Array();
    for (var j = 0; j < tagElements.length; j++) {
        elements.push(tagElements[j].name);
    }
    return elements;
}


// 解锁子菜单
function unlockMeunCoalCHP() {
    // $('.coalFurnace, .coalHandingSystem, .coalDesulfurization, .coalSteamTurbine, .coalBoilerAuxiliaries, .coalRemovalAshSlag, .coalCirculatingWater, .coalSmokeAirSystem').removeClass('unselect');
    // $('.coalFurnace, .coalHandingSystem, .coalDesulfurization, .coalSteamTurbine, .coalBoilerAuxiliaries, .coalRemovalAshSlag, .coalCirculatingWater, .coalSmokeAirSystem').removeAttr('onclick');

    $('.coalFurnace, .coalHandingSystem').removeClass('unselect');
    $('.coalFurnace, .coalHandingSystem').removeAttr('onclick');
}

// 解锁子菜单
function unlockMeunBiomassCHP() {
    $('.biomassFurnace, .biomassFuelStorTran, .biomassDesulDenit, .biomassDASRemove, .biomassBoilerAuxiliaries, .biomassOfficialProcess').removeClass('unselect');
    $('.biomassFurnace, .biomassFuelStorTran, .biomassDesulDenit, .biomassDASRemove, .biomassBoilerAuxiliaries, .biomassOfficialProcess').removeAttr('onclick');
}

// 解锁子菜单
function unlockMeunGPG() {
    $('.GPG_BoilerOfPTS, .GPG_GasAirSystem, .GPG_SmokeResistance, .GPG_WindResistance').removeClass('unselect');
    $('.GPG_BoilerOfPTS, .GPG_GasAirSystem, .GPG_SmokeResistance, .GPG_WindResistance').removeAttr('onclick');
}

//锁定子菜单
function lockMeunGPG() {
    $('.GPG_BoilerOfPTS, .GPG_GasAirSystem, .GPG_SmokeResistance, .GPG_WindResistance').addClass('unselect');
    $('.GPG_BoilerOfPTS, .GPG_GasAirSystem, .GPG_SmokeResistance, .GPG_WindResistance').attr("onclick", "return false;");
}