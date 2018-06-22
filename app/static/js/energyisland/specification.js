$(document).ready(function () {

    $('#1_calculate_button').bind('click', calculateAnnualUtilizationRate);
    $('#2_calculate_button').bind('click', calculateSaveEfficiency2);
    $('#3_calculate_button').bind('click', calculateSaveEfficiency3);
    $('#4_calculate_button').bind('click', calculateSaveEfficiency4);
    $('#5_calculate_button').bind('click', calculateUseEfficiency);
    $('#6_calculate_button').bind('click', calculateHeatPowerRate);
    $('#co2_calculate_button').bind('click', calculateCO2UseEfficiency);
    $('#so2_calculate_button').bind('click', calculateSO2UseEfficiency);
    $('#nox_calculate_button').bind('click', calculateNOxUseEfficiency);

    // 点击选择模块
    $('.left-select').bind('click', function(){
        // 当前页面所有模块list
        listModule = ["q-1", "q-2", "q-3", "q-4", "q-5", "q-6", "q-7", "q-8", "q-9"];
        var moduleName = $(this).attr("id");
        // 切换页面右侧内容
        changeModule(listModule, moduleName);
    });
});

function isNull(array){
    var flag = false;
    for(var i = 0; i < array.length; i++){
        if(array[i] == null || $.trim(array[i]) == ''){
            flag = true;
            break;
        }
    }
    return flag;
}

function calculateAnnualUtilizationRate(){
    var output_power = $('#1_output_power').val();
    var q1 = $('#1_q1').val();
    var q2 = $('#1_q2').val();
    var gas_amount = $('#1_gas_amount').val();
    var gas_ql = $('#1_gas_ql').val();

    var arr = new Array();
    arr.push(output_power);
    arr.push(q1);
    arr.push(q2);
    arr.push(gas_amount);
    arr.push(gas_ql);

    // if(output_power == null || heat_amount == null || cold_amount == null || gas_amount == null 
    //     || gas_ql == null || $.trim(output_power) == '' || $.trim(heat_amount) == '' || $.trim(cold_amount) == '' 
    //     || $.trim(gas_amount) == '' || $.trim(gas_ql) == '' ) {
    //     messageToast('info', '请输入全部数据',2000);
    // }else{
    //     var result = (3.6*Number(output_power)+Number(heat_amount)+Number(cold_amount))/(Number(gas_amount)*Number(gas_ql));
    //     $('#1_annual_utilization_rate').val(result);
    // }

    if(isNull(arr)) {
        messageToast('info', '请输入全部数据',2000);
    }else{
        var result = (3.6*Number(output_power)+Number(q1)+Number(q2))/(Number(gas_amount)*Number(gas_ql));
        $('#1_annual_utilization_rate').val(result);
    }
}

function calculateSaveEfficiency2(){
    var use_power = $('#2_use_power').val();
    var power_efficiency = $('#2_power_efficiency').val();
    var qh = $('#2_qh').val();
    var net_trans_efficiency = $('#2_net_trans_efficiency').val();
    var net_gen_efficiency = $('#2_net_gen_efficiency').val();
    var boiler_efficiency = $('#2_boiler_efficiency').val();

    var arr = new Array();
    arr.push(use_power);
    arr.push(power_efficiency);
    arr.push(qh);
    arr.push(net_trans_efficiency);
    arr.push(net_gen_efficiency);
    arr.push(boiler_efficiency);

    if(isNull(arr)){
        messageToast('info', '请输入全部数据',2000);  
    }else{
        var result = 1-(Number(use_power)/Number(power_efficiency))/
            (Number(use_power)/(Number(net_trans_efficiency)*Number(net_gen_efficiency))+(Number(qh)/Number(boiler_efficiency)));
        $('#2_save_efficiency').val(result);
    }
}

function calculateSaveEfficiency3(){
    var use_power = $('#3_use_power').val();
    var gen_efficiency = $('#3_gen_efficiency').val();
    var qc = $('#3_qc').val();
    var net_trans_efficiency = $('#3_net_trans_efficiency').val();
    var net_gen_efficiency = $('#3_net_gen_efficiency').val();
    var cope = $('#3_cope').val();

    var arr = new Array();
    arr.push(use_power);
    arr.push(gen_efficiency);
    arr.push(qc);
    arr.push(net_trans_efficiency);
    arr.push(net_gen_efficiency);
    arr.push(cope);

    if(isNull(arr)){
        messageToast('info', '请输入全部数据',2000);  
    }else{
        var result = 1-(Number(use_power)/Number(gen_efficiency))/
            (Number(use_power)/(Number(net_trans_efficiency)*Number(net_gen_efficiency))+(Number(qc)/(Number(cope)*Number(net_trans_efficiency)*Number(net_gen_efficiency))));
        $('#3_save_efficiency').val(result);
    }
}

function calculateSaveEfficiency4(){
    var use_power = $('#4_use_power').val();
    var gen_efficiency = $('#4_gen_efficiency').val();
    var qc = $('#4_qc').val();
    var net_trans_efficiency = $('#4_net_trans_efficiency').val();
    var net_gen_efficiency = $('#4_net_gen_efficiency').val();
    var cope = $('#4_cope').val();
    var nh = $('#4_nh').val();
    var copa = $('#4_copa').val();

    var arr = new Array();
    arr.push(use_power);
    arr.push(gen_efficiency);
    arr.push(qc);
    arr.push(net_trans_efficiency);
    arr.push(net_gen_efficiency);
    arr.push(cope);
    arr.push(nh);
    arr.push(copa);

    if(isNull(arr)){
        messageToast('info', '请输入全部数据',2000);  
    }else{
        var result = 1-
            (Number(use_power)/Number(gen_efficiency)+(Number(qc)-Number(use_power)*Number(nh)*Number(copa)/Number(gen_efficiency))/(Number(cope)*(Number(net_trans_efficiency)*Number(net_gen_efficiency))))/
            (Number(use_power)/(Number(net_trans_efficiency)*Number(net_gen_efficiency))+Number(qc)/(Number(cope)*Number(net_trans_efficiency)*Number(net_gen_efficiency)))
        $('#4_save_efficiency').val(result);
    }
}

function calculateUseEfficiency(){
    var heat = $('#5_heat').val();
    var cold = $('#5_cold').val();
    var power = $('#5_power').val();
    var consume = $('#5_consume').val();
    var ql = $('#5_ql').val();
    var power_purchase = $('#5_power_purchase').val();
    var net_supply_efficiency = $('#5_net_supply_efficiency').val();

    var arr = new Array();
    arr.push(heat);
    arr.push(cold);
    arr.push(power);
    arr.push(consume);
    arr.push(ql);
    arr.push(power_purchase);
    arr.push(net_supply_efficiency);

    if(isNull(arr)){
        messageToast('info', '请输入全部数据',2000);  
    }else{
        var result = (Number(heat)+Number(cold)+Number(power)*3600)/(Number(consume)*Number(ql)+(Number(power_purchase)*3600)/Number(net_supply_efficiency));
        $('#5_use_efficiency').val(result);
    }
}

function calculateHeatPowerRate(){
    var heat = $('#6_heat').val();
    var power_amount = $('#6_power_amount').val();

    var arr = new Array();
    arr.push(heat);
    arr.push(power_amount);

    if(isNull(arr)){
        messageToast('info', '请输入全部数据',2000);  
    }else{
        var result = Number(heat)/(Number(power_amount)*3600);
        $('#6_heat_power_rate').val(result);
    }
}

function calculateCO2UseEfficiency(){
    var co2_b_use_power = $('#co2_b_use_power').val();
    var co2_b_use_gas = $('#co2_b_use_gas').val();
    var co2_b_use_coal = $('#co2_b_use_coal').val();
    var co2_d_use_power = $('#co2_d_use_power').val();
    var co2_d_use_gas = $('#co2_d_use_gas').val();
    var co2_d_use_coal = $('#co2_d_use_coal').val();
    var co2_power_coefficient = $('#co2_power_coefficient').val();
    var co2_gas_coefficient = $('#co2_gas_coefficient').val();
    var co2_coal_coefficient = $('#co2_coal_coefficient').val();

    var arr = new Array();
    arr.push(co2_b_use_power);
    arr.push(co2_b_use_gas);
    arr.push(co2_b_use_coal);
    arr.push(co2_d_use_power);
    arr.push(co2_d_use_gas);
    arr.push(co2_d_use_coal);
    arr.push(co2_power_coefficient);
    arr.push(co2_gas_coefficient);
    arr.push(co2_coal_coefficient);

    if(isNull(arr)){
        messageToast('info', '请输入全部数据',2000);  
    }else{
        var result = ((Number(co2_b_use_power)-Number(co2_d_use_power))*Number(co2_power_coefficient)+(Number(co2_b_use_gas)-Number(co2_d_use_gas))*Number(co2_gas_coefficient)+(Number(co2_b_use_coal)-Number(co2_d_use_coal))*Number(co2_coal_coefficient))*2.46*10;
        $('#co2_use_efficiency').val(result);
    }
}

function calculateSO2UseEfficiency(){
    var so2_b_use_power = $('#so2_b_use_power').val();
    var so2_b_use_gas = $('#so2_b_use_gas').val();
    var so2_b_use_coal = $('#so2_b_use_coal').val();
    var so2_d_use_power = $('#so2_d_use_power').val();
    var so2_d_use_gas = $('#so2_d_use_gas').val();
    var so2_d_use_coal = $('#so2_d_use_coal').val();
    var so2_power_coefficient = $('#so2_power_coefficient').val();
    var so2_gas_coefficient = $('#so2_gas_coefficient').val();
    var so2_coal_coefficient = $('#so2_coal_coefficient').val();

    var arr = new Array();
    arr.push(so2_b_use_power);
    arr.push(so2_b_use_gas);
    arr.push(so2_b_use_coal);
    arr.push(so2_d_use_power);
    arr.push(so2_d_use_gas);
    arr.push(so2_d_use_coal);
    arr.push(so2_power_coefficient);
    arr.push(so2_gas_coefficient);
    arr.push(so2_coal_coefficient);

    if(isNull(arr)){
        messageToast('info', '请输入全部数据',2000);  
    }else{
        var result = ((Number(so2_b_use_power)-Number(so2_d_use_power))*Number(so2_power_coefficient)+(Number(so2_b_use_gas)-Number(so2_d_use_gas))*Number(so2_gas_coefficient)+(Number(so2_b_use_coal)-Number(so2_d_use_coal))*Number(so2_coal_coefficient))*0.075*10;
        $('#so2_use_efficiency').val(result);
    }
}

function calculateNOxUseEfficiency(){
    var nox_b_use_power = $('#nox_b_use_power').val();
    var nox_b_use_gas = $('#nox_b_use_gas').val();
    var nox_b_use_coal = $('#nox_b_use_coal').val();
    var nox_d_use_power = $('#nox_d_use_power').val();
    var nox_d_use_gas = $('#nox_d_use_gas').val();
    var nox_d_use_coal = $('#nox_d_use_coal').val();
    var nox_power_coefficient = $('#nox_power_coefficient').val();
    var nox_gas_coefficient = $('#nox_gas_coefficient').val();
    var nox_coal_coefficient = $('#nox_coal_coefficient').val();

    var arr = new Array();
    arr.push(nox_b_use_power);
    arr.push(nox_b_use_gas);
    arr.push(nox_b_use_coal);
    arr.push(nox_d_use_power);
    arr.push(nox_d_use_gas);
    arr.push(nox_d_use_coal);
    arr.push(nox_power_coefficient);
    arr.push(nox_gas_coefficient);
    arr.push(nox_coal_coefficient);

    if(isNull(arr)){
        messageToast('info', '请输入全部数据',2000);  
    }else{
        var result = ((Number(nox_b_use_power)-Number(nox_d_use_power))*Number(nox_power_coefficient)+(Number(nox_b_use_gas)-Number(nox_d_use_gas))*Number(nox_gas_coefficient)+(Number(nox_b_use_coal)-Number(nox_d_use_coal))*Number(nox_coal_coefficient))*0.0375*10;
        $('#nox_use_efficiency').val(result);
    }
}
