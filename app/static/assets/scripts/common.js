$(document).ready(function() {
    hiddenUnit();
    // 左侧菜单切换的样式
    var leftMeun = ['collapsed index', 'elements', 'charts', 'tables', 'typography', 'icons',
                    'coalPlanList', 'coalQuestionnaire', 'coalFurnace', 'coalSteamTurbine', 'coalHandingSystem', 'coalDesulfurization' ,
                    'coalBoilerAuxiliaries', 'coalRemovalAshSlag', 'coalCirculatingWater', 'coalSmokeAirSystem',
                    'biomassQuestionnaire', 'biomassFurnace', 'biomassSteamTurbine','biomassFuelStorTran',
                    'biomassDesulDenit', 'biomassDASRemove', 'biomassBoilerAuxiliaries', 'biomassOfficialProcess',
                    'ccppQuestionnaire', 'ccppFurnace', 'ccppSteamTurbine',
		    'GPG_Questionnaire', 'GPG_BoilerOfPTS', 'GPG_GasAirSystem', 'GPG_SmokeResistance', 'GPG_WindResistance'
                    ];
    var menuSelect = $("#menuSelect").val();

    for (var i = 0; i < leftMeun.length; i++) {
        if (menuSelect == leftMeun[i]) {
            if(menuSelect == 'coalPlanList' || menuSelect == 'coalQuestionnaire' || menuSelect == 'coalFurnace' || menuSelect == 'coalSteamTurbine' || menuSelect == 'coalHandingSystem' || menuSelect == 'coalDesulfurization' || menuSelect == 'coalBoilerAuxiliaries' || menuSelect == 'coalRemovalAshSlag' || menuSelect == 'coalCirculatingWater' || menuSelect == 'coalSmokeAirSystem') {
                if($('.sidebar a[data-toggle="collapse"]').hasClass('collapsed')) {
                    $('#coalMean').attr('class', 'index active');
                    $('#coal').attr('class', 'collapse in');
                } else {
                    $('#coalMean').attr('class', 'collapsed index');
                }
            }
            if(menuSelect == 'biomassQuestionnaire' || menuSelect == 'biomassFurnace' || menuSelect == 'biomassSteamTurbine' || menuSelect == 'biomassFuelStorTran' || menuSelect == 'biomassDesulDenit' || menuSelect == 'biomassDASRemove' || menuSelect == 'biomassBoilerAuxiliaries' || menuSelect == 'biomassOfficialProcess') {
                if($('.sidebar a[data-toggle="collapse"]').hasClass('collapsed')) {
                    $('#biomassMean').attr('class', 'index active');
                    $('#biomass').attr('class', 'collapse in');
                } else {
                    $('#biomassMean').attr('class', 'collapsed index');
                }
            }
            if(menuSelect == 'ccppQuestionnaire' || menuSelect == 'ccppFurnace' || menuSelect == 'ccppSteamTurbine') {
                if($('.sidebar a[data-toggle="collapse"]').hasClass('collapsed')) {
                    $('#ccppMean').attr('class', 'index active');
                    $('#ccpp').attr('class', 'collapse in');
                } else {
                    $('#ccppMean').attr('class', 'collapsed index');
                }
            }
            if(menuSelect == 'GPG_Questionnaire'|| menuSelect == 'GPG_BoilerOfPTS' || menuSelect == 'GPG_GasAirSystem'
                || menuSelect == 'GPG_SmokeResistance' || menuSelect == 'GPG_WindResistance') {
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

});

/**
 * 备注popover初始
 */
$(function () { 
	$("[data-toggle='popover']").popover();
});

// $(window).on('click', function(event) {
//     var target = $(event.target);
//     if (!target.hasClass('popover')
//             && target.parent('.popover-content').length === 0
//             && target.parent('.popover-title').length === 0
//             && target.parent('.popover').length === 0
//             && target.data("toggle") !== "popover") {
//         $("[data-toggle='popover']").popover('hide');
//     }else{
//         target.popover('toggle');
//     }
// });

/**
 * 给页面中所有表单赋值
 * @param {后台传来的数据} datas 
 * @param {form表单的formID} formName 
 */
function assignmentForm(datas, formName) {
    var elements = getElements(formName);
    var tempInput;
    for (var i = 0; i < elements.length; i++) {
        tempInput = elements[i];
        $("input[name='" + tempInput + "']").val(datas[tempInput]);
    }
}

/**
 * 获取form中的所有的<input>对象
 * @param {form表单的formID} formName 
 */
function getElements(formName) {
    var tagElements = $("#" + formName + " input");
    var elements = new Array();
    for (var j = 0; j < tagElements.length; j++) {
        elements.push(tagElements[j].name);
    }
    return elements;
}

/**
 * 解锁子菜单
 */
function unlockMeunCoalCHP() {
    $('.coalFurnace, .coalHandingSystem, .coalDesulfurization, .coalBoilerAuxiliaries, .coalRemovalAshSlag, .coalCirculatingWater, .coalSmokeAirSystem').removeClass('unselect');
    $('.coalFurnace, .coalHandingSystem, .coalDesulfurization, .coalBoilerAuxiliaries, .coalRemovalAshSlag, .coalCirculatingWater, .coalSmokeAirSystem').removeAttr('onclick');
}

// 解锁子菜单
function unlockMeunBiomassCHP() {
    $('.biomassFurnace, .biomassFuelStorTran, .biomassDesulDenit, .biomassDASRemove, .biomassBoilerAuxiliaries, .biomassOfficialProcess').removeClass('unselect');
    $('.biomassFurnace, .biomassFuelStorTran, .biomassDesulDenit, .biomassDASRemove, .biomassBoilerAuxiliaries, .biomassOfficialProcess').removeAttr('onclick');
}

/**
 * 解锁面包屑菜单
 */
function unlockBreadcrumb() {
    $(".newPlan").removeAttr("onclick");
    $(".newPlan").removeClass("forbid-click");
    $(".newPlan").parent("li").removeAttr("title");
}




/**
 * input框焦点时隐藏单位，失去焦点单位出现
 */
function hiddenUnit() {
    $("input").focus(function(){
        $(this).attr("style", "border-color:#00AAFF");
        // $(this).siblings(".show-unit").attr("style", "display:none");
    });

    $("input").focusout(function(){
        $(this).removeAttr("style");
        $(this).siblings(".show-unit").removeAttr("style");
    });
}


/**
 * 自动消失提示消息公共方法
 * @param {提示消息的类型（success/error/info）} flag 
 * @param {提示消息} msg 
 * @param {消息出现的毫秒数} duration 
 */
function messageToast(flag,msg,duration){
    duration=isNaN(duration)?3000:duration;
    var m = document.createElement('div');
    m.innerHTML = msg;
    m.style.cssText = '';
    if (flag == 'success')
    {
        m.style.cssText="width: 50%;min-width: 150px;opacity: 0.7;height: 60px;color: rgb(255, 255, 255);line-height: 60px;text-align: center;border-radius: 5px;position: fixed;top: 40%;left: 25%;z-index: 999999;background: rgb(84, 186, 43);font-size: 20px;";
        
    }
    if (flag == 'error')
    {
        m.style.cssText="width: 50%;min-width: 150px;opacity: 0.7;height: 60px;color: rgb(255, 255, 255);line-height: 60px;text-align: center;border-radius: 5px;position: fixed;top: 40%;left: 25%;z-index: 999999;background: rgb(195, 74, 68);font-size: 20px;";
        
    }
    if (flag == 'info')
    {
        m.style.cssText="width: 50%;min-width: 150px;opacity: 0.7;height: 60px;color: rgb(255, 255, 255);line-height: 60px;text-align: center;border-radius: 5px;position: fixed;top: 40%;left: 25%;z-index: 999999;background: rgb(26, 178, 255);font-size: 20px;";
        
    }
     document.body.appendChild(m);
    setTimeout(function() {
        var d = 0.5;
        m.style.webkitTransition = '-webkit-transform ' + d + 's ease-in, opacity ' + d + 's ease-in';
        m.style.opacity = '0';
        setTimeout(function() { document.body.removeChild(m)}, d * 1000);
    }, duration);
}