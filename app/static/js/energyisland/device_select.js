var needDataJson;
var runningDataJson;

$(document).ready(function () {
    // init();
    $('#boilerdata').hide();
    $('#boilercheckbox').bind('click', function(){
        if($("#boilerdata").is(':visible')){
            $('#boilerdata').hide();
        }else{
            $('#boilerdata').show();
        }
    });

    $('#submitData').bind('click', submitQuestionnaire);
    initCheckBox()
    // 调整图表大小
    // $(window).resize(resize);
})

// 深拷贝对象
var cloneObj = function(obj){
    var str, newobj = obj.constructor === Array ? [] : {};
    if(typeof obj !== 'object'){
        return;
    } else if(window.JSON){
        str = JSON.stringify(obj), //系列化对象
        newobj = JSON.parse(str); //还原
    } else {
        for(var i in obj){
            newobj[i] = typeof obj[i] === 'object' ? cloneObj(obj[i]) : obj[i]; 
        }
    }
    return newobj;
}

// 提交保存页面所有表单数据
function submitQuestionnaire() {
    var result = '';
    var result1 = '';
    var result2 = '';
    $.each($('input[name="checkboxname"]:checked'),function(){
        result += "#" + $(this).val()
    });

    $.each($('input[name="checkboxname2"]:checked'),function(){
        result1 += "#" + $(this).val()
    });

    $.each($('input[name="checkboxname3"]:checked'),function(){
        result2 += "#" + $(this).val()
    });

    

    $.ajax({
            url: '/energyIsland/get_device_select',
            data: { 
                'result': result, 
                'result1': result1, 
                'result2': result2,
                "rsglrqForm": $('#rsglrqForm').serialize(),
                "rqglzqForm": $('#rqglzqForm').serialize(),
                "yrglrsglForm": $('#yrglrsglForm').serialize(),
                "yrgldyzqglForm": $('#yrgldyzqglForm').serialize()},
            type: 'post',
            cache: false,
            dataType: 'json',
            success: function (data_json) {
                messageToast('success', '能源互联岛-设备选择成功',2000);
            },
            error: function () {
                messageToast('error', '能源互联岛-设备选择失败',2000);
               
            }
    });
}

function initCheckBox(){
    $.ajax({
        url: '/energyIsland/get_checked_box',
        data: {},
        type: 'post',
        cache: false,
        dataType: 'json',
        success: function (data_json) {
            // messageToast('success', '能源互联岛-设备选择成功',2000);
            setCheckBox(data_json)
        },
        error: function () {
            messageToast('error', '能源互联岛-设备选择失败',2000);
        }
    });
}

function setCheckBox(data_json){
    $.each($('input[name="checkboxname"]'), function(){
        if(data_json.out_resource[$(this).attr('value')].used == 1){
            // $(this).prop('checked', true)
            $(this).click()
        }
    });
    $.each($('input[name="checkboxname2"]'), function(){
        if($.inArray($(this).attr('value'), data_json.device) != -1){
            // $(this).prop('checked', true)
            $(this).click()
        }
    });
    $.each(data_json.boiler, function(index, boiler){
        var val = boiler.modelnum
        $('input[name="checkboxname3"][value="' + val +  '"]').click()
        $.each(boiler.modelnumvalue, function(index, row){
            $('input[name=' + row.name + ']').val(row.value)
        });
    });
}
