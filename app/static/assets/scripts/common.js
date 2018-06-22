var template_id;
var template_name;
var greenStyle = "RGB(192,230,219)|#CCFF99|#333|RGB(26,176,131)|#66CC99|RGB(192,230,219)|#66CC99";
// var greenStyle = "#99CC99|#CCFF99|#333|#dbe9d8|#66CC99|#99CC99|#66CC99";
// 1.主菜单一级菜单选中颜色
// 2.主菜单二级菜单选中左侧颜色
// 3。字体颜色
// 4.背景颜色
// 5.主菜单二级菜单选中颜色
// 6.一级菜单包括子菜单全部选中颜色
// 7.子菜单颜色
var blueStyle = "#252c35|#00AAFF|#AEB7C2|#2B333E|#337ab7|#252c35|#337ab7";

$(document).ready(function() {
        /************************************************ 以下代码处理用户编辑模板时，选择要插入MD中的数据库字段  ****************************************************************************/
        $('#selectTemplate').click(function(){
            $.ajax({
                cache: false,
                type: "POST",
                url: '/getTemplateByModule',
                data: {},
                async: false,
                error: function (request) {
                    messageToast('error', '发生异常！',3000);
                },
                success: function (data) {
                    createTableContent(data.reportTemplateJson);
                    addSelectTableClick(data.reportTemplateJson);
                    $('#selectTemplatemodal').modal({backdrop: 'static', keyboard: false});
                    $("#closeSelectTemplateBtn").on("click", function () {
                        $("#selectTemplatemodal").modal('hide');
                        $("#template_content tr:gt(0)").empty();
                        $("#template_content tr").not(':eq(0)').empty()
                    });
                }
            });
        });
    
        function getJsonLength(jsonData) {
            var jsonLength = 0;  
            for(var item in jsonData) {  
                jsonLength++;   
            } 
            return jsonLength;  
        }
        
        function createTableContent(reportTemplateJson) {
            var length = getJsonLength(reportTemplateJson)
            var table = $('#template_content');
            $("#selectTemplateInfo").html("请选择模板");
            $("#template_title").html("模板名称");
            for(var i = 0; i < length; i++){
                var tr = $("<tr></tr>");
                tr.appendTo(table)
                var td = $("<td> <a name=" + reportTemplateJson[i].template_id + ">" + reportTemplateJson[i].template_name + "</td>");
                td.appendTo(tr);
            }
        }
    
        function addSelectTableClick(reportTemplateJson){
            var length = getJsonLength(reportTemplateJson)
            for(var i = 0; i < length; i++){
                var template_id =  reportTemplateJson[i].template_id;
                var template_name =  reportTemplateJson[i].template_id;
                $("a[name='" + template_id  + "']").bind('click', {template_id: template_id, template_name: template_name }, getTemplateByName)
            }
        }
    
        function getTemplateByName(event){
            template_id = event.data.template_id;
            template_name = event.data.template_name;
            $("#alertInfoselecttemplate").modal({backdrop: 'static', keyboard: false});
            $("#alertContentselecttemplate").html("确定选取该模板吗？");
            $("#closeBtnselecttemplate").html("取消");       
        }
        $("#closeBtnselecttemplate").on("click", function (){
            $("#alertInfoselecttemplate").modal('hide');
        });

        $("#confirmBtnselecttemplate").on("click", function (){
            $("#alertInfoselecttemplate").modal('hide');
            $.ajax({
                cache: false,
                type: "POST",
                url: '/setPlanReportTemplate',
                data: { "template_id": template_id, "template_name": template_name },
                async: false,
                error: function (request) {
                    messageToast('error', '发生异常！',3000);
                },
                success: function (data) {
                    $("#selectTemplatemodal").modal('hide');
                    $("#template_content tr:gt(0)").empty();
                    $("#template_content tr").not(':eq(0)').empty()
                    messageToast('success', data.message, 3000);
                }
            });
        });   

        $('#selectTemplatemodal').on('hidden.bs.modal', function () {
            //$('#table_content tr').html("");
            $("#template_content tr:gt(0)").empty();
            $("#template_content tr").not(':eq(0)').empty()
        })
     /****************************************************************************************************************************************************************************/


    // 左侧菜单切换的样式
    var leftMeun = ['collapsed index', 'coalCHPplanList', 'coalCHPreport', 'coalCHPequipmentList',
                    'biomassplanList', 'biomassreport', 'biomassEquipmentTemplate',
                    'biomassreporttemplateList', 'biomassFuelMaintain', 'ccppreporttemplateList',
                    'gpgreporttemplateList', 'coalCHPreporttemplateList',
                    'ccppplanList', 'ccppreport', 'ccppequipmenttemplateList',
                    'gpgplanList', 'gpgreport', 'energyisland_questionnaire', 'energyisland_addDevice', 'energyisland_graph',
                    'energyIslandplanList', 'energyisland_specification'];
                    // 'energyIslandreport', 'energyIslandtemplateList'
    var menuSelect = $("#menuSelect").val();

    for (var i = 0; i < leftMeun.length; i++) {
        if (menuSelect == leftMeun[i]) {
            if(menuSelect == 'coalCHPplanList' || menuSelect == 'coalCHPreport' || menuSelect == 'coalCHPreporttemplateList' || menuSelect == 'coalCHPequipmentList') {
                if($('.sidebar a[data-toggle="collapse"]').hasClass('collapsed')) {
                    $('#coalMean').attr('class', 'index active');
                    $('#coal').attr('class', 'collapse in');
                } else {
                    $('#coalMean').attr('class', 'collapsed index');
                }
            }
            if(menuSelect == 'biomassplanList' || menuSelect == 'biomassreport' || menuSelect == 'biomassreporttemplateList' || menuSelect == 'biomassFuelMaintain' ||  menuSelect == 'biomassEquipmentTemplate') {
                if($('.sidebar a[data-toggle="collapse"]').hasClass('collapsed')) {
                    $('#biomassMean').attr('class', 'index active');
                    $('#biomass').attr('class', 'collapse in');
                } else {
                    $('#biomassMean').attr('class', 'collapsed index');
                }
            }
            if(menuSelect == 'ccppplanList' || menuSelect == 'ccppreport' || menuSelect == 'ccppreporttemplateList' || menuSelect == 'ccppequipmenttemplateList') {
                if($('.sidebar a[data-toggle="collapse"]').hasClass('collapsed')) {
                    $('#ccppMean').attr('class', 'index active');
                    $('#ccpp').attr('class', 'collapse in');
                } else {
                    $('#ccppMean').attr('class', 'collapsed index');
                }
            }
            if(menuSelect == 'gpgplanList'|| menuSelect == 'gpgreport' || menuSelect == 'gpgreporttemplateList') {
                if($('.sidebar a[data-toggle="collapse"]').hasClass('collapsed')) {
                    $('#gaspowerMean').attr('class', 'index active');
                    $('#gaspower').attr('class', 'collapse in');
                } else {
                    $('#gaspowerMean').attr('class', 'collapsed index');
                }
            }
            // 能源互联岛部分
            if(menuSelect == 'energyisland_questionnaire' ||menuSelect == 'energyisland_addDevice' || menuSelect == 'energyisland_graph' || menuSelect == 'energyIslandplanList' || menuSelect == 'energyisland_specification') {
                // || menuSelect == 'energyIslandreport' || menuSelect == 'energyIslandtemplateList'
                if($('.sidebar a[data-toggle="collapse"]').hasClass('collapsed')) {
                    $('#energyislandMean').attr('class', 'index active');
                    $('#energyisland').attr('class', 'collapse in');
                } else {
                    $('#energyislandMean').attr('class', 'collapsed index');
                }
            }
            $("." + menuSelect).addClass('active');
        }
    }

    $('#coalCHPplanList, #gpgplanList, #biomassplanList, #ccppplanList').on('click', function() {
        if(!$('#breadcrumbSwitch').hasClass('hide')) {
            // $('#breadcrumbSwitch').attr("data-flag", "0");
            $('#breadcrumbSwitch').addClass('hide');
         }

    });
//     $('#planAdd').on('click', function() {
//         alert("ss");
//         if($('#breadcrumbSwitch').hasClass('hide')) {
//             $('#breadcrumbSwitch').removeClass('hide');
//     }
// });
var classStlye = getCookies();
if(classStlye != "") {
    if (classStlye=="blue") {
        getCookieStyle(blueStyle);
    }else{
        getCookieStyle(greenStyle);
    }
}else{
    setCookie("skinStyle","blue",365);
    getCookieStyle(blueStyle);
}
 // 切换皮肤按钮点击
    $('#changeSkin').on('click', function() {
        var classStlye = getCookies();
        
        if (classStlye=="blue") {
            setCookie("skinStyle","green",365);
            getCookieStyle(greenStyle);
            
        }else{
            setCookie("skinStyle","blue",365);
            getCookieStyle(blueStyle);
        }
       
    });
});

function setCookie(cname,cvalue,exdays){
    var d = new Date();
    d.setTime(d.getTime()+(exdays*24*60*60*1000));
    var expires = "expires="+d.toGMTString();
    document.cookie = cname+"="+cvalue+"; "+expires+"; path=/";
}

function getCookies(){
    var cookieStyles = "";
    
    var strCookie = document.cookie;
    var arrCookie = strCookie.split("; ");
    for(var i = 0; i < arrCookie.length; i++){
        var arr = arrCookie[i].split("=");
        if("skinStyle" == arr[0]){
            cookieStyles = arr[1];
        }
    }
    return cookieStyles;
}
function getCookieStyle(cookieStyles){
    var cookieStyle = cookieStyles.split('|');

    $('.sidebar .nav > li > a').css("color", cookieStyle[2]);
    $('#wrapper .sidebar').css("background-color", cookieStyle[3]);
    $('.sidebar .nav > li > a:focus, .sidebar .nav > li > a.active').css('background-color', cookieStyle[0]);
    $('.sidebar .nav > li > a:focus, .sidebar .nav > li > a.active').css('border-left-color', cookieStyle[1]);
    // $('.sidebar .nav > li > a').css("background-color", cookieStyle[4]);
    $('#subPages ul li a.active').css("background-color", cookieStyle[4]);
    $('#coal ul li a.active').css("background-color", cookieStyle[4]);
    $('#biomass ul li a.active').css("background-color", cookieStyle[4]);
    $('#ccpp ul li a.active').css("background-color", cookieStyle[4]);
    $('#gaspower ul li a.active').css("background-color", cookieStyle[4]);
    $('#energyisland ul li a.active').css("background-color", cookieStyle[4]);
    $('.sidebar .nav .nav').css("background-color", cookieStyle[5]);
    $('.st-menu').css("background", cookieStyle[6]);
}


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
        if (datas[tempInput] != "" || datas[tempInput] == "0") {
            $("input[name='" + tempInput + "']").val(datas[tempInput]);
            $("input[name='" + tempInput + "']").removeClass("default-color");
        }
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
 * 解锁面包屑菜单
 */
function unlockBreadcrumb() {
    $(".newPlan").removeAttr("onclick");
    $(".newPlan").removeClass("forbid-click");
    $(".newPlan").parent("li").removeAttr("title");
}

/**
 * input焦点产生，失去焦点样式
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
    if (flag == 'info_long')
    {
        m.style.cssText="width: 50%;min-width: 150px;opacity: 0.7;height: 60px;color: rgb(255, 255, 255);line-height: 60px;text-align: center;border-radius: 5px;position: fixed;top: 40%;left: 25%;z-index: 999999;background: rgb(26, 178, 255);font-size: 16px;";
        
    }
    document.body.appendChild(m);
    setTimeout(function() {
        var d = 0.5;
        m.style.webkitTransition = '-webkit-transform ' + d + 's ease-in, opacity ' + d + 's ease-in';
        m.style.opacity = '0';
        setTimeout(function() { document.body.removeChild(m)}, d * 1000);
    }, duration);
    return m
}


/**
 * 当前页面表单数值修改后，在未保存的情况下跳转到其他页面时的提示
 * @param {要跳转的新页面标示} labelId 
 * @param {当前页面表单} formName 
 * @param {当前表单的原始数值} oldFormData 
 */
function createLabelBind(formName, oldFormData){
    $('#breadcrumbDiv a').each(function(){
        var id = $(this).attr('id');
        var href = $(this).attr('href');
        if(id != null){
            if(href !="#"){
                $(this).unbind();
                $(this).bind('click', {labelID: id, formName: formName, oldFormData: oldFormData}, isModified);
            }
        }      
    });

    $('#sidebar-nav a').each(function(){
        var id = $(this).attr('id');
        var href = $(this).attr('href');
        if(id !="coalMean" && id !="biomassMean" && id !="ccppMean" && id !="gaspowerMean" && id !="energyislandMean"){
            $('#' + id)[0].setAttribute("onclick",'return false;');
            $(this).unbind();
            $(this).bind('click', {labelID: id, formName: formName, oldFormData: oldFormData}, isModified);
        }
    });
}

function isModified(event){
    var labelId = event.data.labelID;
    var formName = event.data.formName;
    var oldFormData = event.data.oldFormData;
    var dataformNew = $("#" + formName).serializeArray();  
    newFormData = JSON.stringify({ dataform: dataformNew });

    if(newFormData != oldFormData){
        $("#alertInfo").modal('show');
        $("#alertContent").html("页面有数值修改未保存，确定离开本页面吗？");
        $("#confirmBtn").on("click", function () {
            $("#alertInfo").modal('hide');
            $('#' + labelId)[0].setAttribute("onclick",'true');
            $('#' + labelId)[0].click();
        });
    }else{
        $('#' + labelId)[0].setAttribute("onclick",'true');
        $('#' + labelId)[0].click();
    }
}


function hasParentClass( e, classname ) {
    if(e === document) return false;
    if( classie.has( e, classname ) ) {
        return true;
    }
    return e.parentNode && hasParentClass( e.parentNode, classname );
}


function mobilecheck() {
    var check = false;
    (function(a){if(/(android|ipad|playbook|silk|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows (ce|phone)|xda|xiino/i.test(a)||/1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(a.substr(0,4)))check = true})(navigator.userAgent||navigator.vendor||window.opera);
    return check;
}

function init() {

    if($('#breadcrumbSwitch').hasClass('hide')) {
        $('#breadcrumbSwitch').removeClass('hide');
    }
    // var container = document.getElementById( 'st-container' ),
    //     buttons = Array.prototype.slice.call( document.querySelectorAll( '#st-trigger-effects > a' ) ),
    //     // event type (if mobile use touch events)
    //     eventtype = mobilecheck() ? 'touchstart' : 'click',
    //     resetMenu = function() {
    //         classie.remove( container, 'st-menu-open' );
    //     },
    //     bodyClickFn = function(evt) {
    //         if( !hasParentClass( evt.target, 'st-menu' ) ) {
    //             resetMenu();
    //             document.removeEventListener( eventtype, bodyClickFn );
    //         }
    //     };

    // buttons.forEach( function( el, i ) {
    //     var effect = el.getAttribute( 'data-effect' );

    //     el.addEventListener( eventtype, function( ev ) {
    //         ev.stopPropagation();
    //         ev.preventDefault();
    //         container.className = 'st-container'; // clear
    //         classie.add( container, effect );
    //         setTimeout( function() {
    //             classie.add( container, 'st-menu-open' );
    //         }, 25 );
    //         document.addEventListener( eventtype, bodyClickFn );
    //     });
    // } );

}

/**
 * 删除list里当前参数剩下的list
 * @param {*当前的参数} cut 
 */
function cutCssName(list, cut) {
    var newCss = [];
    for (var i = 0; i < list.length; i++) {
        if (cut != list[i])
        newCss.push(list[i]);
    }
    return newCss;
}

/**
 * 
 */
function maxPage(count){
    var remainder = count % 5;
    var page = 0;
    if (remainder == 0) {
        page = count / 5;
    }
    else {
        page = parseInt(count / 5) + 1;
    }
    return page;
}

/**
 * 初始化显示上一页下一页按钮样式
 */
function initPreNext(module, count){
    currentPage = $(".pre").attr("data-page");
    page = maxPage(count);
    for (var i = 1; i < page+1; i++) {
        temp = i*5;
        // 第一页
        if(currentPage == 5){
        $('.next').parent().attr("class", "current");
        $('.pre').parent().attr("class", "");
        // 最后一页 
        }else if (currentPage<=i*5 && currentPage>(i-1)*5) {
            $('.pre').parent().attr("class", "current");
            $('.next').parent().attr("class", "");
        // 中间页
        }else if(currentPage>5 && currentPage<=(i-1)*5) {
            $('.pre').parent().attr("class", "current");
            $('.next').parent().attr("class", "current");
        }

    }
    // 隐藏除当前模块，显示当前五个模块
    movePage(module, count, currentPage);
}

/**
 * 面包屑显示当页5个所有模块，并隐藏其余面包模块
 * @param {*当前的参数} cut 
 */
function movePage(module, count, currentPage) {
    for (var i = 1; i < count+1; i++) {
        if (i > currentPage-5 && i<=currentPage){
            if (!$("#"+module+""+i).parent().hasClass("show")){
                $("#"+module+""+i).parent().addClass("show");
            }
            if ($("#"+module+""+i).parent().hasClass("hide")){
                $("#"+module+""+i).parent().removeClass("hide");
            }
        }else{
            if(!$("#"+module+""+i).parent().hasClass("hide")) {
                $("#"+module+""+i).parent().addClass("hide");
            }
            if($("#"+module+""+i).parent().hasClass("show")) {
            $("#"+module+""+i).parent().removeClass("show");
            }
        }
        
    }
}

// 上一页
function clickPre(breakCount, moduleName){
    currentPage = $(".pre").attr("data-page");
    maxCount = maxPage(breakCount);
    if (5<currentPage && currentPage<=maxCount*5){
        $(".pre").attr("data-page", parseInt(currentPage)-5);
        currentPage = $(".pre").attr("data-page");
        movePage(moduleName, breakCount, currentPage);
        if(currentPage>5 && currentPage <= breakCount){

            $('.pre').parent().attr("class", "current");
            $('.next').parent().attr("class", "current");
        }
        if(currentPage<=5) {
            $('.pre').parent().removeAttr("class");
        }
    }
}

// 下一页
function clickNext(breakCount, moduleName){
    currentPage = $(".pre").attr("data-page");
    maxCount = maxPage(breakCount);
    if (5<=currentPage && currentPage<maxCount*5){
        $(".pre").attr("data-page", parseInt(currentPage)+5);
        currentPage = $(".pre").attr("data-page");
        movePage(moduleName, breakCount, currentPage);
        if(currentPage>5 && currentPage <= breakCount){
            $('.pre').parent().attr("class", "current");
        }
        if(currentPage>=breakCount) {
            $('.next').parent().removeAttr("class");
        }
    }
}





/**
 * 
 * @param {*} listModule 当前页面所有模块list
 * @param {*} current 当前选中
 */
function changeModule(listModule, current) {

    // 右侧
    if($("." + current).hasClass('hide')) {
        $("." + current).removeClass('hide');
    }
    // 除了当前选中的其它模块list
    newList = cutCssName(listModule, current);
    for (var i = 0; i < newList.length; i++) {
        // 右侧
        if(!$("." + newList[i]).hasClass('hide')) {
            $("." + newList[i]).addClass('hide');
        }
        // 左侧
        if($("#" + newList[i]).hasClass('left-hover')) {
            $("#" + newList[i]).removeClass('left-hover');
        }
    }

    // 左侧
    if(!$("#" + current).hasClass('left-hover')) {
        $("#" + current).addClass('left-hover');
    }

    // 切换菜单时关闭打开的提示框
    $("[data-toggle='popover']").popover('hide');


}

function isNumber(val){
    if(val == ""){
        return true;
    }
    var regPos = /^\d+(\.\d+)?$/; //非负浮点数
    var regNeg = /^(-(([0-9]+\.[0-9]*[1-9][0-9]*)|([0-9]*[1-9][0-9]*\.[0-9]+)|([0-9]*[1-9][0-9]*)))$/; //负浮点数
    if(regPos.test(val) || regNeg.test(val)){
        return true;
    }else{
        return false;
    }
}

in_array = function(notvalidcolumname, element) {
    for (var i = 0; i < notvalidcolumname.length; i++) {
        if (notvalidcolumname[i] == element) {
            return true; 
        } 
    }
    return false; 
} 

function valid(tempInputName, notvalidcolumname){
    if(!(in_array(notvalidcolumname, tempInputName))){
        $("input[name='" + tempInputName + "']").blur(function () {
            numvar = $(this).val()
            if(!isNumber(numvar)){
                messageToast('error', "输入有误:\""+$(this).val()+"\"", 3000);
                //小提示框
                $(this).val("")
                $(this).focus();
                $(this).attr("style", "border-color:red");
            }
        });
    }
}