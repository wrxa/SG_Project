$(document).ready(function () {
    var sorts = ['carbon', 'hydrogen', 'oxygen', 'nitrogen', 'sulfur', 'water',
        'grey', 'daf', 'grindability', 'low'];

    $("#coalDesign").change(function () {

        var id = $(this).val();
        if (id == "others") {
            for (var i = 0; i < sorts.length; i++) {
                $("#s_" + sorts[i] + "_design").val("");
            }
        } else {
            $.ajax({
                url: './coalSort',
                data: { "id": id },
                type: 'post',
                cache: false,
                dataType: 'json',
                success: function (data) {
                    $("#s_carbon_design").val(data.coalSort.carbon);
                    $("#s_hydrogen_design").val(data.coalSort.hydrogen);
                    $("#s_oxygen_design").val(data.coalSort.oxygen);
                    $("#s_nitrogen_design").val(data.coalSort.nitrogen);
                    $("#s_sulfur_design").val(data.coalSort.sulfur);
                    $("#s_water_design").val(data.coalSort.water);
                    $("#s_grey_design").val(data.coalSort.grey);
                    $("#s_daf_design").val(data.coalSort.daf);
                    $("#s_grindability_design").val(data.coalSort.grindability);
                    $("#s_low_design").val(data.coalSort.low);
                },
                error: function () {
                    alert("异常！");
                }
            });
        }
    });

    $("#coalCheck").change(function () {

        var id = $(this).val();
        if (id == "others") {
            for (var i = 0; i < sorts.length; i++) {
                $("#s_" + sorts[i] + "_check").val("");
            }
        } else {
            $.ajax({
                url: './coalSort',
                data: { "id": id },
                type: 'post',
                cache: false,
                dataType: 'json',
                success: function (data) {
                    $("#s_carbon_check").val(data.coalSort.carbon);
                    $("#s_hydrogen_check").val(data.coalSort.hydrogen);
                    $("#s_oxygen_check").val(data.coalSort.oxygen);
                    $("#s_nitrogen_check").val(data.coalSort.nitrogen);
                    $("#s_sulfur_check").val(data.coalSort.sulfur);
                    $("#s_water_check").val(data.coalSort.water);
                    $("#s_grey_check").val(data.coalSort.grey);
                    $("#s_daf_check").val(data.coalSort.daf);
                    $("#s_grindability_check").val(data.coalSort.grindability);
                    $("#s_low_check").val(data.coalSort.low);
                },
                error: function () {
                    alert("异常！");
                }
            });
        }
    });

});