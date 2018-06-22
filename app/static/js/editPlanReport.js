// {/* <script src="//oss.maxcdn.com/jquery.form/3.50/jquery.form.min.js"></script>
// <script src="http://malsup.github.io/min/jquery.form.min.js"></script> */}
$(function() {
    // 保存图标
    $('#saveMD').click(function() {
        planId = $("#editPlanId").val();
        $.ajax({
            cache: false,
            type: "POST",
            url: '/saveContent',
            data: { 
                'flask-pagedown-body':$('#flask-pagedown-body').val(),
                'planId': planId
            },
            async: false,
            error: function (request) {
                messageToast('error', '消息提示：保存失败！',2000);

            },
            success: function (data) {
                if (data.state == "1")
                {
                    messageToast('success', '保存成功！',2000);
                }
                else{
                    messageToast('error', '消息提示：保存失败！',2000);
                }

            }
        });
    });

    $('#save').click(function() {
        planId = $("#editPlanId").val();
        $.ajax({
            cache: false,
            type: "POST",
            url: '/saveMd',
            data: { 
                'flask-pagedown-body':$('#flask-pagedown-body').val(),
                'htmldata':document.getElementById("flask-pagedown-body-preview").innerHTML,
                'planId': planId
            },
            async: false,
            error: function (request) {
                messageToast('error', '消息提示：保存失败！',2000);

            },
            success: function (data) {
                if (data.state == "1")
                {
                    window.open("/converMD/" + planId);
                }
                else{
                    messageToast('error', '消息提示：保存失败！',2000);
                }

            }
        });
    });

    $(".uploadImage").on("change", function(){
        var imagePath = $("#file").val();    
        var strExtension = imagePath.substr(imagePath.lastIndexOf('.') + 1);    
        if (strExtension!='jpg') {   
            if (strExtension!='bmp') {   
                if (strExtension!='png') {   
                    messageToast('error', '消息提示：上传失败，请上传图片格式的文件！',3000);
                    return false;   
                }  
            }  
        } 
        //判断大小
        var maxSize = parseFloat($("#imgSizeLimt").val())*1024*1024; //Byte
        var fileSize = $("#file").prop('files')[0].size;
        if(fileSize >= maxSize){
            messageToast('error', '消息提示：上传失败，上传文件太大!',3000);
            return false;
        }
        $("#headimageform").ajaxSubmit({
            url : $("#headimageform").attr('action'),
            async : false, // 同步
            type : $("#headimageform").attr('method'),
            timeout : self.connect_timeout_ms,   
            success : function(result) {    
                if(result.state=='0'){  
                    var newd = "!["+result.message+"]("+result.data+")";
                    var textarea = document.getElementById("flask-pagedown-body");
                    cursurPosition = getTxt1CursorPosition()
                    var startStr = textarea.value.substr(0,cursurPosition);  
                    var endStr = textarea.value.substr(cursurPosition, textarea.value.length); 
                    textarea.value = startStr + newd + endStr;
                    $("#file").val("");
                }
                messageToast('success', '图片上传成功!',3000);
                new Editor(document.getElementById("flask-pagedown-body"), document.getElementById("flask-pagedown-body-preview"));
            },    
            error : function() {
                messageToast('error', '消息提示：上传失败，请检查网络后重试!',3000);
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
    //获得鼠标焦点离文本域开始的距离，若没有焦点则返回0
    function getTxt1CursorPosition(){  
        var oTxt1 = document.getElementById("flask-pagedown-body");
        var cursurPosition = -1;  
        // 查找你要判断的文本框  
        if(oTxt1.selectionStart == 0){  
            cursurPosition= 0;   
        }else if(oTxt1.selectionStart){//非IE浏览器  
            cursurPosition= oTxt1.selectionStart;   
        }else{//IE  
        var range = document.selection.createRange();  
        range.moveStart("character",-oTxt1.value.length);  
        cursurPosition=range.text.length;  
        }    
        return cursurPosition;  
    } 

    function Editor(input, preview) {  
        this.update = function () {  
          var contant = input.value;
          var htmlStr = markdown.toHTML(contant, "Maruku");
        //   alert(htmlStr)
          preview.innerHTML = htmlStr;  
        };  
        input.editor = this;  
        this.update();  
    }
    new Editor(document.getElementById("flask-pagedown-body"), document.getElementById("flask-pagedown-body-preview"));
    // var $ = function (id) { return document.getElementById(id); };  
})
