var oldFormData;

$(document).ready(function () {
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

    $("#packagdownload").on("click", function () {       
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

    // var dataformInit = $("#GPG_ImageForm").serializeArray();  
    // oldFormData = JSON.stringify({ dataform: dataformInit });
    // createLabelBind("GPG_ImageForm", oldFormData);
});