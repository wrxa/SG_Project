var oldFormData;
var imgmesg;
$(document).ready(function () {
    init();
    // 定义面包屑个数
    var breakCount = 14;
    // 定义面包屑上id的模块类型
    var moduleName = "ccpp";
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
    window.location.href="/ccpp/packagdownload"
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
    imgmesg = messageToast('info', '加载图像中......',3000000);
    setTimeout(addimgobj,3000);
});
//追加照片
function addimgobj(){
    $.ajax({
        cache: true,
        type: "POST",
        url: './getSurplusImg',
        data: {
        },
        async: false,
        error: function (request) {
            document.body.removeChild(imgmesg)
            messageToast('error', '检索发生异常！', 3000);
        },
        success: function (data) {
            document.body.removeChild(imgmesg)
            var trString = "";
            if(data.imgnamelist.length == 0){
                trString += '<p><font size="4">无图像生成，不满足生成图像条件</font></p>'
                $(".imglist center").append(trString);
                return;
            }else{
                for(var k = 0; k < data.imglist.length; k++){
                    index = k+data.imgnameprelist.length
                    trString += '<img src="' + data.imglist[k].netPath + '" title="'+data.imglist[k].chineseName+index+'" style="width:70%;">'
                    trString += '<p><font size="4">'+data.imglist[k].chineseName+index+'</font></p>'
                    trString += '<br><br>'
                    $(".imglist center").append(trString);
                }
            }
        }
    });
}