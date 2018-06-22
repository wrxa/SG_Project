var g_tableName = "";
var contents = [{"id": "1", "content": "用法简介：\n1. 鼠标选中“文档目录”，点击“添加子标题”按钮，添加一级子目录。\n2. 鼠标选中生成的子级目录，点击“添加子标题”按钮，添加该目录的子级目录。\n3. 鼠标选中目录，点击“删除”按钮，删除该目录结构。\n4. 鼠标选中目录，点击“重命名”按钮或者点击键盘“F2”按钮，重命名目录。\n5. 鼠标选中目录拖拽可交换目录结构位置。\n6. 插入表格或图片后，点击“切换预览方式”按钮，可预览表格和图片，再次点击此按钮回到结构预览。\n7. 插入图表后需要在图表前后各留一行空行。\n8. 编辑模板时，请不要忘记点击“保存”按钮，将数据保存到数据库方便下次使用。\n"}];
var menu = [{"id":"1","text":"文档目录", "children":[]}];
$(function() {
    initdata();
 //  创建实例
 $('#left-menu').jstree({
    'core' : {
        "animation" : 0,
        "check_callback" : true,
        "themes" : { "stripes" : true },
        'data' : menu
    },
    "types" : {
      "#" : {
        "max_children" : 50,
        "max_depth" : 5,
        "icon" : "glyphicon glyphicon-file",
        "valid_children" : ["file"]
      },
      "file" : {
        "icon" : "glyphicon glyphicon-file",
        "valid_children" : ["file"]
      }
    },
    "plugins" : [
      "dnd", "search",
      "state", "types", "wholerow"
    ]
});


// 搜索事件
var to = false;
$('#search-menu').keyup(function () {
  if(to) { clearTimeout(to); }
  to = setTimeout(function () {
    var v = $('#search-menu').val();
    $('#left-menu').jstree(true).search(v);
  }, 250);
});

$('#left-menu').on('changed.jstree', function (e, data) {
    // 初始化清空textArea框
    $('#right-content').val("");
    if(data.selected.length) {
        $('#right-menu').html(data.instance.get_node(data.selected[0]).text);
        for (var j = 0; j < contents.length; j++) {
            contentId = data.instance.get_node(data.selected[0]).id;
            // alert("contents[j].id=="+contents[j].id+ "   contentId=="+ contentId);
           if (contents[j].id == contentId) {
                $('#right-content').val(contents[j].content);
           }
        }
        // content.id = data.instance.get_node(data.selected[0]).id;
        // content.text = data.instance.get_node(data.selected[0]).text;
        
    }

}).jstree();

/**
 * 对应右侧文本发生变化自动保存到页面中，并高亮提示用户需要保存
 */
$("#right-content").on("change", function(){
    saveContent();
});

/**
 * 添加新段落按钮绑定事件
 */
$("#newLine").bind('click', newLine);

   /**
     * 右侧保存按钮事件
     * 1.保存textarea中的内容到contents对象中
     * 2.获得所有菜单结构的json信息
     * 3.解析json获得每个id的目录级别加入contents中
     * 4.发送菜单结构json和contents json到后台
     */
    $('#saveMD').click(function() {
        if ($("[name='template_name']").val() == ""){
            messageToast('info', '请输入模板名！',1000);
        }else{
            // 步骤二
            data = $('#left-menu').jstree("get_json");
            // 步骤三
            simpleJson = parseJstreeJson(data);
            for (var i = 0; i < simpleJson.length; i++) {
    
                for (var k = 0; k < contents.length; k++) {
                    if(simpleJson[i].id == contents[k].id) {
                        // var classLen =  eval("("+simpleJson[i].parentNode+")"); 
                        contents[k]["class"] = simpleJson[i].parentNode;
                    }
                }
            }
        // 步骤四
            templateId = $("#templateId").val();
            template_name = $("[name='template_name']").val();
            $.ajax({
                cache: false,
                type: "POST",
                url: '/savetemplate',
                data: { 
                    // 'flask-pagedown-body':$('#flask-pagedown-body').val(),
                    'templateId': templateId,
                    'template_name': template_name,
                    'content': JSON.stringify(contents),
                    'menu': JSON.stringify(data)
                },
                async: false,
                error: function (request) {
                    messageToast('error', '消息提示：保存失败！',2000);

                },
                success: function (data) {
                    if (data.state == "1")
                    {
                        messageToast('success', '保存成功！',2000);
                        $("#saveMD").css("color", "#676a6d");
                        $("#templateId").val(data.templateId)
                        // 保存过后解除绑定的beforeunload事件
                        $(window).unbind('beforeunload');
                    }else if(data.state == "3"){
                        messageToast('info', '消息提示：该模板名称已经被使用！',2000);
                    }
                    else{
                        messageToast('error', '消息提示：保存失败！',2000);
                    }
                }
            });
        }     
    });

    /************************************************ 以下代码处理用户编辑模板时，选择要插入MD中的数据库字段  ****************************************************************************/
    $('#test_SelectDB').click(function(){
        var moduleName = $("#moduleName").val();
        $.ajax({
            cache: false,
            type: "POST",
            url: '/getTableNameByModule',
            data: { "moduleName": moduleName },
            async: false,
            error: function (request) {
                messageToast('error', '发生异常！',3000);
            },
            success: function (data) {
                createTableContent(data.tableNameJson);
                addSelectTableClick(data.tableNameJson);
                $('#selectData').modal({backdrop: 'static', keyboard: false});
                $("#closeSelectDataBtn").on("click", function () {
                    $("#selectData").modal('hide');
                    //$('#table_content tr').empty();
                    //$('#table_content tr').html("");
                    $("#table_content tr:gt(0)").empty();
                    $("#table_content tr").not(':eq(0)').empty()
                });
            }
        });
    });

    $('#ptable_title').click(function(){
        var moduleName = $("#moduleName").val();
        $.ajax({
            cache: false,
            type: "POST",
            url: '/getTableNameByModule',
            data: { "moduleName": moduleName },
            async: false,
            error: function (request) {
                messageToast('error', '发生异常！',3000);
            },
            success: function (data) {
                $("#table_content tr:gt(0)").empty();
                $("#table_content tr").not(':eq(0)').empty()
                createTableContent(data.tableNameJson);
                addSelectTableClick(data.tableNameJson);
                $('#selectData').modal({backdrop: 'static', keyboard: false});
                $("#closeSelectDataBtn").on("click", function () {
                    $("#selectData").modal('hide');
                    $("#table_content tr:gt(0)").empty();
                    $("#table_content tr").not(':eq(0)').empty()
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
    
    function createTableContent(tableNameJson) {
        var length = getJsonLength(tableNameJson)
        var table = $('#table_content');
        $("#selectDataInfo").html("方案数据");
        $("#table_title").html("模块列表");
        for(var i = 0; i < length; i++){
            if(tableNameJson[i].table_description != "null" &&
                tableNameJson[i].table_description != null && tableNameJson[i].table_description != ""){
                var tr = $("<tr></tr>");
                tr.appendTo(table)
                var td = $("<td> <a name=" + tableNameJson[i].table_name + ">" + tableNameJson[i].table_description + "</td>");
                td.appendTo(tr);
            }
        }
    }

    function addSelectTableClick(tableNameJson){
        var length = getJsonLength(tableNameJson)
        for(var i = 0; i < length; i++){
            var tableName =  tableNameJson[i].table_name;
            $("a[name='" + tableName  + "']").bind('click', {tableName: tableName}, getColumnNameByTable)
        }
    }

    function getColumnNameByTable(event){
        g_tableName = event.data.tableName;
        $.ajax({
            cache: false,
            type: "POST",
            url: '/getColumnNameByTable',
            data: { "tableName": g_tableName },
            async: false,
            error: function (request) {
                messageToast('error', '发生异常！',3000);
                g_tableName = "";
            },
            success: function (data) {
                var myobj = eval(data.columnNameJson)
                createColumnContent(myobj);
                addSelectColumnClick(myobj);
            }
        });
    }

    function createColumnContent(columnNameJson){
        var length = getJsonLength(columnNameJson);
        var table = $('#table_content');
        $("#selectDataInfo").html("请选择内容");
        $("#table_title").html("内容");
        $("#table_content tr:gt(0)").empty();
        $("#table_content tr").not(':eq(0)').empty()
        for(var i = 0; i < length; i++){
            if(columnNameJson[i].column_name !="id" && columnNameJson[i].column_name !="plan_id"){
                if(columnNameJson[i].column_description != "null" &&
                    columnNameJson[i].column_description != null && columnNameJson[i].column_description != ""){
                    var tr = $("<tr></tr>");
                    tr.appendTo(table)
                    var td = $("<td> <a name=" + columnNameJson[i].column_name + ">" + columnNameJson[i].column_description + "</td>");
                    td.appendTo(tr);
                }
            }
        }
    }

    function addSelectColumnClick(columnNameJson){
        var length = getJsonLength(columnNameJson)
        for(var i = 0; i < length; i++){
            var columnName =  columnNameJson[i].column_name;
            var columnDescription =  columnNameJson[i].column_description;
            if(columnDescription != null && columnDescription != "" && columnDescription != "null"){
                $("a[name='" + columnName  + "']").bind('click', {columnName: columnName}, writeColunmToMD);
            }
        }
    }

    //将选择的字段写入MD中
    function writeColunmToMD(event){
        var columnName = event.data.columnName;
        $("#alertInfo").modal({backdrop: 'static', keyboard: false});
        $("#alertContent").html("确定选取该内容吗？");
        $("#closeBtn").html("取消");
        $("#confirmBtn").on("click", function () {
            $("#alertInfo").modal('hide');
            if(columnName != null && columnName !="" && columnName !="null"){
                var newd = "@@" + g_tableName + "." + columnName + "@@";
                var textarea = document.getElementById("right-content");
                cursurPosition = getTxt1CursorPosition()
                var startStr = textarea.value.substr(0,cursurPosition);  
                var endStr = textarea.value.substr(cursurPosition, textarea.value.length); 
                textarea.value = startStr + newd + endStr;
            }  
            columnName = "";
            $("#selectData").modal('hide');
            $("#table_content tr:gt(0)").empty();
            $("#table_content tr").not(':eq(0)').empty()
	    // 添加数据库字段自动保存
        saveContent();
        new Editor(document.getElementById("right-content"), document.getElementById("flask-pagedown-body-preview"));
        }); 

        $("#closeBtn").on("click", function (){
            columnName ="";
            $("#alertInfo").modal('hide');
        });  
    }
    $('#selectData').on('hidden.bs.modal', function () {
        $("#table_content tr:gt(0)").empty();
        $("#table_content tr").not(':eq(0)').empty()
    })
/*************************************************************************************************************************************/


/************************************************ 以下代码处理用户编辑模板时，选择要插入MD中的文本逻辑  ****************************************************************************/
$('#addlogic').click(function(){
    var moduleName = $("#moduleName").val();
    $.ajax({
        cache: false,
        type: "POST",
        url: '/getLogicByModule',
        data: { "moduleName": moduleName },
        async: false,
        error: function (request) {
            messageToast('error', '发生异常！',3000);
        },
        success: function (data) {
            createTableContentlogic(data.logicJson);
            addSelectTableClicklogic(data.logicJson);
            $('#selectDatalogic').modal({backdrop: 'static', keyboard: false});
            $("#closeSelectDataBtnlogic").on("click", function () {
                $("#selectDatalogic").modal('hide');
                $("#table_contentlogic tr:gt(0)").empty();
                $("#table_contentlogic tr").not(':eq(0)').empty()
            });
        }
    });
});

function createTableContentlogic(logicJson) {
    var length = getJsonLength(logicJson)
    var table = $('#table_contentlogic');
    //$("#selectDataInfologic").html("请选择数据表");
    //$("#table_titlelogic").html("数据表名");
    if(length <= 0){
        var tr = $("<tr></tr>");
            tr.appendTo(table)
            var td = $("<td> <a name=#> 该模板不存在特殊逻辑 </td>");
            td.appendTo(tr);
    }else{
        for(var i = 0; i < length; i++){
            if(logicJson[i].textlogicremarks != "null" &&
            logicJson[i].textlogicremarks != null && logicJson[i].textlogicremarks != ""){
                var tr = $("<tr></tr>");
                tr.appendTo(table)
                var td = $("<td> <a name=" + logicJson[i].textlogickey + ">" + logicJson[i].textlogicremarks + "</td>");
                td.appendTo(tr);
            }
        }
    }   
}

function addSelectTableClicklogic(logicJson){
    var length = getJsonLength(logicJson)
    for(var i = 0; i < length; i++){
        var textlogickey =  logicJson[i].textlogickey;
        $("a[name='" + textlogickey  + "']").bind('click', {textlogickey: textlogickey}, writeColunmToMDlogic)
    }
}

//将选择的字段写入MD中
function writeColunmToMDlogic(event){
    textlogickey = event.data.textlogickey;
    $("#alertInfologic").modal({backdrop: 'static', keyboard: false});
    $("#alertContentlogic").html("确定选取该内容吗？");
    $("#closeBtnlogic").html("取消");
    $("#confirmBtnlogic").on("click", function () {
        $("#alertInfologic").modal('hide');
        if(textlogickey != null && textlogickey !="" && textlogickey !="null"){
            var newd = textlogickey;
            var textarea = document.getElementById("right-content");
            cursurPosition = getTxt1CursorPosition()
            var startStr = textarea.value.substr(0,cursurPosition);  
            var endStr = textarea.value.substr(cursurPosition, textarea.value.length); 
            textarea.value = startStr + newd + endStr;
        }  
        columnName = "";
        $("#selectDatalogic").modal('hide');
        $("#table_contentlogic tr:gt(0)").empty();
        $("#table_contentlogic tr").not(':eq(0)').empty()
    // 添加数据库字段自动保存
    saveContent();
    new Editor(document.getElementById("right-content"), document.getElementById("flask-pagedown-body-preview"));
    }); 

    $("#closeBtnlogic").on("click", function (){
        columnName ="";
        $("#alertInfologic").modal('hide');
    });  
}
$('#selectDatalogic').on('hidden.bs.modal', function () {
    $("#table_contentlogic tr:gt(0)").empty();
    $("#table_contentlogic tr").not(':eq(0)').empty()
})
/*************************************************************************************************************************************/



    $('#save').click(function() {
        templateId = $("#templateId").val();
        $.ajax({
            cache: false,
            type: "POST",
            url: '/saveMd',
            data: { 
                'flask-pagedown-body':$('#flask-pagedown-body').val(),
                'htmldata':document.getElementById("flask-pagedown-body-preview").innerHTML,
                'templateId': templateId
            },
            async: false,
            error: function (request) {
                messageToast('error', '消息提示：保存失败！',2000);

            },
            success: function (data) {
                if (data.state == "1")
                {
                    window.open("/converMD/" + templateId);
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
                    var newd = "\n!["+result.message+"]("+result.data+")\n";
                    var textarea = document.getElementById("right-content");
                    cursurPosition = getTxt1CursorPosition()
                    var startStr = textarea.value.substr(0,cursurPosition);  
                    var endStr = textarea.value.substr(cursurPosition, textarea.value.length); 
                    textarea.value = startStr + newd + endStr;
                    saveContent();
                    $("#file").val("");
                }
                messageToast('success', '图片上传成功!',3000);
                new Editor(document.getElementById("right-content"), document.getElementById("flask-pagedown-body-preview"));
            },    
            error : function() {
                messageToast('error', '消息提示：上传失败，请检查网络后重试!',3000);
            }
        });
    });

    new Editor(document.getElementById("right-content"), document.getElementById("flask-pagedown-body-preview"));
});


function Editor(input, preview) {
    this.update = function () {  
      var contant = input.value;
      var htmlStr = markdown.toHTML(contant, "Maruku");
      preview.innerHTML = htmlStr;  
    };  
    input.editor = this;  
    this.update();  
}

/**
 * 创建目录
 */
function menu_create() {
    var ref = $('#left-menu').jstree(true),
        sel = ref.get_selected();
    if(!sel.length) { return false; }
    sel = sel[0];
    sel = ref.create_node(sel, {"type":"file"});
    if(sel) {
        ref.edit(sel);
        content = {"id": sel, "content": ""};
        contents.push(content);
    }
}

/**
 * 重命名当前目录
 */
function menu_rename() {
    var ref = $('#left-menu').jstree(true),
        sel = ref.get_selected();
    if(!sel.length) { return false; }
    sel = sel[0];
    ref.edit(sel);
}

/**
 * 删除当前目录
 */
function menu_delete() {
    var ref = $('#left-menu').jstree(true),
        sel = ref.get_selected();
    if(!sel.length) { return false; }

    ref.delete_node(sel);
    for (var i = 0; i < contents.length; i++) {
        if(ref == contents[i].id) {
            contents.splice(i, 1);
        }
        
    }
}

/**
 * 解析嵌套json成简单格式json
 * @param {*从jstree中获取到的嵌套型json} json 
 */
function parseJstreeJson(json) {
    var newJson = json.concat([]);
    var len = newJson.length;   //长度
    var parentNode = [];
    // console.log('newJson', newJson);
    for (var i = 0; i < len; i++) {
        var item = newJson[i];
        if (item.children && item.children.length != 0) {
            var child = item.children;
            for (var j = 0; j < child.length; j++) {
                if (item.parentNode) {
                    child[j].parentNode = item.parentNode.concat([item.id]);
                }
                else {
                    child[j].parentNode = [item.id]
                }
                // console.log(item.parentNode, item.id);
                newJson[len + j] = child[j];
            }
            len = newJson.length;
        }
    }
    return newJson;

}

/**
 * 实时将textArea中内容暂时保存到页面中
 */
function saveContent(){
    $("#saveMD").css("color", "dodgerblue");
    // 离开页面绑定事件beforeunload
    $(window).bind('beforeunload',function(){return '您输入的内容尚未保存，确定离开此页面吗？';});
    var ref = $('#left-menu').jstree(true),
    sel = ref.get_selected();
    if(!sel.length) { return false; }
    for (var j = 0; j < contents.length; j++) {
        if (contents[j].id == sel) {
            contents[j].content = $('#right-content').val();
        }
    }
}


/**
 * 进入编辑模板页面后加载数据
 */
function initdata() {
    $.ajax({
        cache: true,
        type: "POST",
        url: '/initTemplate',
        data: {"templateId": $("#templateId").val()},
        async: false,
        error: function (request) {
            messageToast('error', '发生异常！',3000);
        },
        success: function (data) {
            if (data.state == "1") {
                menu = data.menu;
                contents = data.contents;
                $('[name=template_name]').val(data.template_name);
            }
           
        }
    });
}

/**
 * 动态生成表格
 */
function createTable(column, rows) {
    table = "";
    head = "";
    body = "";
    for (var i = 0; i < parseInt(column); i++){
        head += "| ";
    }
    headL = "";
    for (var i = 0; i < column; i++){
        headL += "|:------";
    }
    head = head + "|\n" + headL;

    for (var j = 0; j <  parseInt(rows) - 1; j++){
        line = "";
        for (var i = 0; i <  parseInt(column); i++){
            line += "| ";
        }
        body += "\n" + line + "|";
    }
    table = "表[手动输入]" + "\n" + "\n" + head + body + "\n";
    return table;
}

/**
 * 点击选择几行几列
 */
function selectTable(){
    var column = $("#table-cols").val();
    var rows = $("#table-rows").val();

    if (!isNaN(column) && !isNaN(rows) && parseInt(column) > 1 && parseInt(rows) > 1) {
        var newd = createTable(column, rows);
        $('#popoverTable').popover('hide');
        var textarea = document.getElementById("right-content");
        cursurPosition = getTxt1CursorPosition();
        var startStr = textarea.value.substr(0,cursurPosition);  
        var endStr = textarea.value.substr(cursurPosition, textarea.value.length); 
        textarea.value = startStr + newd + endStr;
        new Editor(document.getElementById("right-content"), document.getElementById("flask-pagedown-body-preview"));
        saveContent();
    }
    
}

/**
 * 换新段落
 */
function newLine(){
    var newd = "\n" + "##### ";
    var textarea = document.getElementById("right-content");
    cursurPosition = getTxt1CursorPosition();
    var startStr = textarea.value.substr(0,cursurPosition);  
    var endStr = textarea.value.substr(cursurPosition, textarea.value.length); 
    textarea.value = startStr + newd + endStr;
    new Editor(document.getElementById("right-content"), document.getElementById("flask-pagedown-body-preview"));
    saveContent();
}

    //获得鼠标焦点离文本域开始的距离，若没有焦点则返回0
    function getTxt1CursorPosition(){  
        var oTxt1 = document.getElementById("right-content");
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

    /**
     * 预览和目录相互切换
     */
    function exchange_preview(){
        // 当前结构模式-->预览模式
        if($('.preview').hasClass('hide')) {
            $('.preview').removeClass("hide");
            $('.construct').addClass("hide");
            new Editor(document.getElementById("right-content"), document.getElementById("flask-pagedown-body-preview"));
        }else{
        // 当前预览模式-->结构模式
        $('.construct').removeClass("hide");
        $('.preview').addClass("hide");
        }
    }