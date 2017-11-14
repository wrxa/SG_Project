$(document).ready(function () {
    unlockMeunBiomassCHP();
    var sorts = ['width', 'coefficient'];

    $("#beltWidth").change(function () {

        var id = $(this).val();
            $.ajax({
                url: './beltSort',
                data: { "id": id },
                type: 'post',
                cache: false,
                dataType: 'json',
                success: function (data) {
                    $("#belt_coefficient").val(data.beltSort.coefficient);
                },
                error: function () {
                    alert("异常！");
                }
            });

    });

});