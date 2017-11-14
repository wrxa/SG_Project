$(document).ready(function () {
    unlockMeunBiomassCHP();
    //选择不同的锅炉，点火方式不同
    $("#fireType").change(function () {
        var id = $(this).val();
        switch (id)
        {
            //空白
            case "0":
                $("#fireWay").val("");
                break;
            //层燃炉
            case "1":
                $("#fireWay").val("人工点火（即床上火把点火）");
                break;
            //循环流化床锅炉
            case "2":
                $("#fireWay").val("0#轻柴油点火（一般为床下点火）");
                break;
        }
    });

});