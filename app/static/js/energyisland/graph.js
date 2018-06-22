var needDataJson;
var runningDataJson;

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

var getDevicePrefix = function(device_class, device_type) {
    var prefix = ''
    var prefix2 = ''
    if (device_class == '1') {
        switch(device_type) {
            case '1':
                prefix = "蒸汽型溴化锂机组-型号:"
                break;
            case '2':
                prefix = "高温水大温差型-型号:HDC-"
                break;
            case '3':
                prefix = "低温水大温差型-型号:LCC-"
                prefix2 = "DH"
                break;
            case '4':
                prefix = "低温水型-型号:LCC-"
                break;
            case '5':
                prefix = "高温水型-型号:HCC-"
                break;
            case '6':
                prefix = "烟气热水补燃型溴化锂吸收式冷温水机-型号:YP-"
                prefix2 = "LHE"
                break;
            case '7':
                prefix = "烟气热水型溴化锂吸收式冷温水机-型号:YP-"
                prefix2 = "LHD"
                break;
            case '8':
                prefix = "烟气双效型溴化锂吸收式冷温水机-型号:YP-"
                prefix2 = "LHB"
                break;
            case '9':
                prefix = "烟气补燃型溴化锂吸收式冷温水机-型号:YP-"
                prefix2 = "LHC"
                break;
            default:
                prefix = "溴化锂吸收式直燃三用机-型号:DG-"
                prefix2 = "G(K)HDC"
                break;
        }
    }else if (device_class == '4'){

    }else if (device_class == '5'){
        
    }else if (device_class == '8'){
        if(device_type == '4'){
            prefix = "余热热水锅炉"
        }else if(device_type == '5'){
            prefix = "余热蒸汽锅炉"
        }
    }
    return {'prefix': prefix, 'prefix2': prefix2}
}

var addDeviceList = function(data_json_dict, typical_day=1, running_plan=0) {
    $('#device_list').children().remove()
    switch(typical_day){
        case 1:
            deviceList = data_json_dict.front_data_day_1
            break;
        case 2:
            deviceList = data_json_dict.front_data_day_2
            break;
        case 3:
            deviceList = data_json_dict.front_data_day_3
            break;
        case 4:
            deviceList = data_json_dict.front_data_day_4
            break;
        default:
            deviceList = []
            break;
    }
    var tr = $("<tr></tr>")
    tr.append($("<td></td>").text("发电设备"))
    tr.append($("<td></td>").text("参数"))
    tr.append($("<td></td>").text("蒸汽设备"))
    tr.append($("<td></td>").text("参数"))
    tr.append($("<td></td>").text("制冷设备"))
    tr.append($("<td></td>").text("参数"))
    tr.append($("<td></td>").text("供暖设备"))
    tr.append($("<td></td>").text("参数"))
    tr.append($("<td></td>").text("热水设备"))
    tr.append($("<td></td>").text("参数"))
    tr.append($("<td></td>").text("供气设备"))
    tr.append($("<td></td>").text("参数"))
    $('#device_list').append(tr)
    var plan_data = deviceList[running_plan]
    if(plan_data){
        var device_name_dict = {}
        var device_name_index = plan_data.electric.props.prop_name[0]
        var electric_device_name = plan_data.electric.props.prop_value[0]
        tr = $("<tr></tr>")
        tr.append($("<td></td>").text(electric_device_name))
        tr.append($("<td></td>").text(plan_data.electric.load.toFixed(1) + " kW × " + plan_data.electric.number))
        device_name_dict.electric = electric_device_name
        var waste = plan_data.waste
        if (waste.steam != null){
            var prefix = getDevicePrefix(waste.steam.device_class, waste.steam.device_type)
            tr.append($("<td></td>").text(prefix.prefix + prefix.prefix2))
            tr.append($("<td></td>").text(waste.steam.load.toFixed(3) + " t/h × " + waste.steam.number))
            device_name_dict.steam = prefix.prefix + prefix.prefix2
        }else{
            tr.append($("<td></td>").text("无"))
            tr.append($("<td></td>").text("无"))
        }
        if (waste.cool != null){
            var prefix = getDevicePrefix(waste.cool.device_class, waste.cool.device_type)
            var num = waste.cool.props.prop_value[0]
            tr.append($("<td></td>").text(prefix.prefix + num + prefix.prefix2))
            tr.append($("<td></td>").text(waste.cool.load.toFixed(1) + " kW × " + waste.cool.number))
            device_name_dict.cool = prefix.prefix + num + prefix.prefix2
        }else{
            tr.append($("<td></td>").text("无"))
            tr.append($("<td></td>").text("无"))
        }
        if (waste.heat != null || waste.heat_plate != null){
            var prefix
            var txt = ""
            var load_txt=""
            if (waste.heat_plate != null){
                var prefix = getDevicePrefix(waste.heat_plate.device_class, waste.heat_plate.device_type)
                txt = txt + prefix.prefix + prefix.prefix2 + " + 板换"
                load_txt = load_txt +waste.heat_plate.load.toFixed(1) + " kW × " + waste.heat_plate.number
                device_name_dict.heat = txt
            }else{
                if (waste.heat != null){
                    var prefix = getDevicePrefix(waste.heat.device_class, waste.heat.device_type)
                    txt = txt + prefix.prefix + prefix.prefix2
                    load_txt = load_txt +waste.heat.load.toFixed(1) + " kW × " + waste.heat.number
                    device_name_dict.heat = txt
                }
            }
            tr.append($("<td></td>").text(txt))
            tr.append($("<td></td>").text(load_txt))
        }else{
            tr.append($("<td></td>").text("无"))
            tr.append($("<td></td>").text("无"))
        }
        if (waste.hot_water != null){
            var prefix = getDevicePrefix(waste.heat_plate.device_class, waste.heat_plate.device_type)
            var txt = ""
            txt = txt + prefix.prefix + prefix.prefix2 + " + 板换"
            tr.append($("<td></td>").text(txt))
            tr.append($("<td></td>").text(waste.hot_water.load.toFixed(3) + " t/h × " + waste.hot_water.number))
            device_name_dict.hot_water = txt
        }else{
            tr.append($("<td></td>").text("无"))
            tr.append($("<td></td>").text("无"))
        }
        if (waste.air != null){
            var air_device_name = waste.air.props.prop_value[1]
            tr.append($("<td></td>").text( air_device_name))
            tr.append($("<td></td>").text(waste.air.load.toFixed(2) + " t/h × " + waste.air.number))
            device_name_dict.air = air_device_name
        }else{
            tr.append($("<td></td>").text("无"))
            tr.append($("<td></td>").text("无"))
        }
        $('#device_list').append(tr)
        return device_name_dict
    }
}

// 格式化显示图标悬浮框
var axisPoint = function(params, unit){
    var result = params[0].name + '<br>'
    params.forEach(function(item) {
          result += '<span style="display:inline-block;margin-right:5px;border-radius:10px;width:9px;height:9px;background-color:' + item.color + '"></span>'
        if(parseFloat(item.data)>=0){
            result += item.seriesName + ": " + '<span style="color:#FFFFFF">' + item.data + " " + unit + "</span><br>"
        }else if(parseFloat(item.data)<0){
            result += item.seriesName + ": " + '<span style="color:#049500">' + item.data + " " + unit + "</span><br>"
        }
    })
    return result
}

// 调整图大小
var resize = function() {
    parent = $("#electric_graph").parent();
    newWidth = parent.width() - 30;
    newHeight = newWidth / 2.5
    $("#electric_graph").css( 'width', newWidth);
    $("#steam_graph").css( 'width', newWidth);
    $("#cool_graph").css( 'width', newWidth);
    $("#heat_graph").css( 'width', newWidth);
    $("#hot_water_graph").css( 'width', newWidth);
    $("#air_graph").css( 'width', newWidth);
    // $('#cost_income_graph').css( 'width', newWidth);
    $("#electric_graph").css( 'height', newHeight);
    $("#steam_graph").css( 'height', newHeight);
    $("#cool_graph").css( 'height', newHeight);
    $("#heat_graph").css( 'height', newHeight);
    $("#hot_water_graph").css( 'height', newHeight);
    $("#air_graph").css( 'height', newHeight);
    // $('#cost_income_graph').css( 'height', newHeight);
    electricGraph.resize();
    steamGraph.resize();
    coolGraph.resize();
    heatGraph.resize();
    hotWaterGraph.resize();
    airGraph.resize();
    // costIncomeGraph.resize();
}

var create_out_resource_data = function(waste){
    var steam_out_resource_data = []
    var steam_out_resource_data_2 = []
    var cool_out_resource_data = []
    var cool_out_resource_data_2 = []
    var heat_out_resource_data = []
    var heat_out_resource_data_2 = []
    var heat_out_resource_data_3 = []
    var hot_water_out_resource_data = []
    var hot_water_out_resource_data_2 = []
    var air_out_resource_data = []
    var steam_out_resource_data_running = []
    var cool_out_resource_data_running = []
    var heat_out_resource_data_running = []
    var hot_water_out_resource_data_running = []
    var air_out_resource_data_running = []
    for (running_hour in waste['operating_state']) {
        // 电，蒸汽，冷，热，热水，空气
        if (waste['operating_state'][running_hour]['output_x'].length  == 7) {
            steam_out_resource_data_running.push(waste.operating_state[running_hour].out_resource_running[1])
            cool_out_resource_data_running.push(waste.operating_state[running_hour].out_resource_running[2])
            heat_out_resource_data_running.push(waste.operating_state[running_hour].out_resource_running[3] + waste.operating_state[running_hour].out_resource_running[4])
            hot_water_out_resource_data_running.push(waste.operating_state[running_hour].out_resource_running[5])
            air_out_resource_data_running.push(waste.operating_state[running_hour].out_resource_running[6])
        }
    }
    for(i=0;i<24;i++){
        if(waste.out_resource.air['空压站'] && waste.out_resource.air['空压站'].used != 0){
            if(air_out_resource_data_running[i] < waste.out_resource.air['空压站'].load){
                air_out_resource_data.push(air_out_resource_data_running[i].toFixed(1))
            }else{
                air_out_resource_data.push(waste.out_resource.air['空压站'].load.toFixed(1))
            }
        }
        if(waste.out_resource.cool['热泵'] && waste.out_resource.cool['热泵'].used != 0){
            if(cool_out_resource_data_running[i] < waste.out_resource.cool['热泵'].load){
                cool_out_resource_data.push("0")
                cool_out_resource_data_2.push(cool_out_resource_data_running[i].toFixed(0))
            }else{
                cool_out_resource_data_2.push(waste.out_resource.cool['热泵'].load.toFixed(0))
                var left_heat = cool_out_resource_data_running[i] - waste.out_resource.cool['热泵'].load
                if(waste.out_resource.cool['现有制冷设备'] && waste.out_resource.cool['现有制冷设备'].used != 0){
                    if(left_heat < waste.out_resource.cool['现有制冷设备'].load){
                        cool_out_resource_data.push(left_heat.toFixed(0))
                    }else{
                        cool_out_resource_data.push(waste.out_resource.cool['现有制冷设备'].load.toFixed(0))
                    }
                }else{
                    cool_out_resource_data.push("0")
                }
            }
        }else{
            var left_heat = cool_out_resource_data_running[i]
            if(waste.out_resource.cool['现有制冷设备'] && waste.out_resource.cool['现有制冷设备'].used != 0){
                if(left_heat < waste.out_resource.cool['现有制冷设备'].load){
                    cool_out_resource_data.push(left_heat.toFixed(0))
                }else{
                    cool_out_resource_data.push(waste.out_resource.cool['现有制冷设备'].load.toFixed(0))
                }
            }else{
                cool_out_resource_data.push("0")
            }
        }
        if(waste.out_resource.heat['热泵'] && waste.out_resource.heat['热泵'].used != 0){
            if(heat_out_resource_data_running[i] < waste.out_resource.heat['热泵'].load){
                heat_out_resource_data.push("0")
                heat_out_resource_data_2.push("0")
                heat_out_resource_data_3.push(heat_out_resource_data_running[i].toFixed(0))
            }else{
                heat_out_resource_data_3.push(waste.out_resource.heat['热泵'].load.toFixed(0))
                var left_heat = heat_out_resource_data_running[i] - waste.out_resource.heat['热泵'].load
                if(waste.out_resource.heat['外部供热设备'] && waste.out_resource.heat['现有制冷设备'] && waste.out_resource.heat['外部供热设备'].used != 0 && waste.out_resource.heat['现有制冷设备'].used != 0 && (waste.out_resource.heat['外部供热设备'].load + waste.out_resource.heat['现有制冷设备'].load > left_heat)){
                    var ratio = waste.out_resource.heat['外部供热设备'].load / (waste.out_resource.heat['现有制冷设备'].load + waste.out_resource.heat['外部供热设备'].load)
                    heat_out_resource_data.push((ratio * left_heat).toFixed(0))
                    heat_out_resource_data_2.push(((1 - ratio) * left_heat).toFixed(0))
                }else{
                    if(waste.out_resource.heat['外部供热设备'] && waste.out_resource.heat['外部供热设备'].used != 0){
                        if(left_heat < waste.out_resource.heat['外部供热设备'].load){
                            heat_out_resource_data.push(left_heat.toFixed(0))
                        }else{
                            heat_out_resource_data.push(waste.out_resource.heat['外部供热设备'].load.toFixed(0))
                        }
                    }else{
                        heat_out_resource_data.push("0")
                    }
                    if(waste.out_resource.heat['现有制冷设备'] && waste.out_resource.heat['现有制冷设备'].used != 0){
                        if(left_heat < waste.out_resource.heat['现有制冷设备'].load){
                            heat_out_resource_data_2.push(left_heat.toFixed(0))
                        }else{
                            heat_out_resource_data_2.push(waste.out_resource.heat['现有制冷设备'].load.toFixed(0))
                        }
                    }else{
                        heat_out_resource_data_2.push("0")
                    }
                }
            }
        }else{
            var left_heat = heat_out_resource_data_running[i]
            if(waste.out_resource.heat['外部供热设备'] && waste.out_resource.heat['现有制冷设备'] && waste.out_resource.heat['外部供热设备'].used != 0 && waste.out_resource.heat['现有制冷设备'].used != 0 && (waste.out_resource.heat['外部供热设备'].load + waste.out_resource.heat['现有制冷设备'].load > left_heat)){
                var ratio = waste.out_resource.heat['外部供热设备'].load / (waste.out_resource.heat['现有制冷设备'].load + waste.out_resource.heat['外部供热设备'].load)
                heat_out_resource_data.push((ratio * left_heat).toFixed(0))
                heat_out_resource_data_2.push(((1 - ratio) * left_heat).toFixed(0))
            }else{
                if(waste.out_resource.heat['外部供热设备'] && waste.out_resource.heat['外部供热设备'].used != 0){
                    if(left_heat < waste.out_resource.heat['外部供热设备'].load){
                        heat_out_resource_data.push(left_heat.toFixed(0))
                    }else{
                        heat_out_resource_data.push(waste.out_resource.heat['外部供热设备'].load.toFixed(0))
                    }
                }else{
                    heat_out_resource_data.push("0")
                }
                if(waste.out_resource.heat['现有制冷设备'] && waste.out_resource.heat['现有制冷设备'].used != 0){
                    if(left_heat < waste.out_resource.heat['现有制冷设备'].load){
                        heat_out_resource_data_2.push(left_heat.toFixed(0))
                    }else{
                        heat_out_resource_data_2.push(waste.out_resource.heat['现有制冷设备'].load.toFixed(0))
                    }
                }else{
                    heat_out_resource_data_2.push("0")
                }
            }

        }
        if(waste.out_resource.hot_water['自有热水锅炉'] && waste.out_resource.hot_water['空压站余热利用'] && waste.out_resource.hot_water['自有热水锅炉'].used != 0 && waste.out_resource.hot_water['空压站余热利用'].used != 0 && (waste.out_resource.hot_water['自有热水锅炉'].load + waste.out_resource.hot_water['空压站余热利用'].load > hot_water_out_resource_data_running[i])){
            var ratio = waste.out_resource.hot_water['自有热水锅炉'].load / (waste.out_resource.hot_water['自有热水锅炉'].load + waste.out_resource.hot_water['空压站余热利用'].load)
            hot_water_out_resource_data.push((ratio * hot_water_out_resource_data_running[i]).toFixed(3))
            hot_water_out_resource_data_2.push(((1 - ratio) * hot_water_out_resource_data_running[i]).toFixed(3))
        }else{
            if(waste.out_resource.hot_water['自有热水锅炉'] && waste.out_resource.hot_water['自有热水锅炉'].used != 0){
                if(hot_water_out_resource_data_running[i] < waste.out_resource.hot_water['自有热水锅炉'].load){
                    hot_water_out_resource_data.push(hot_water_out_resource_data_running[i].toFixed(3))
                }else{
                    hot_water_out_resource_data.push(waste.out_resource.hot_water['自有热水锅炉'].load.toFixed(3))
                }
            }else{
                hot_water_out_resource_data.push("0")
            }
            if(waste.out_resource.hot_water['空压站余热利用'] && waste.out_resource.hot_water['空压站余热利用'].used != 0){
                if(hot_water_out_resource_data_running[i] < waste.out_resource.hot_water['空压站余热利用'].load){
                    hot_water_out_resource_data_2.push(hot_water_out_resource_data_running[i].toFixed(3))
                }else{
                    hot_water_out_resource_data_2.push(waste.out_resource.hot_water['空压站余热利用'].load.toFixed(3))
                }
            }else{
                hot_water_out_resource_data_2.push("0")
            }
        }
        if(waste.out_resource.steam['外部汽源'] && waste.out_resource.steam['自有蒸汽锅炉'] && waste.out_resource.steam['外部汽源'].used != 0 && waste.out_resource.steam['自有蒸汽锅炉'].used != 0 && (waste.out_resource.steam['外部汽源'].load + waste.out_resource.steam['自有蒸汽锅炉'].load > steam_out_resource_data_running[i])){
            var ratio = waste.out_resource.steam['外部汽源'].load / (waste.out_resource.steam['外部汽源'].load + waste.out_resource.steam['自有蒸汽锅炉'].load)
            steam_out_resource_data.push((ratio * steam_out_resource_data_running[i]).toFixed(3))
            steam_out_resource_data_2.push(((1 - ratio) * steam_out_resource_data_running[i]).toFixed(3))
        }else{
            if(waste.out_resource.steam['外部汽源'] && waste.out_resource.steam['外部汽源'].used != 0){
                if(steam_out_resource_data_running[i] < waste.out_resource.steam['外部汽源'].load){
                    steam_out_resource_data.push(steam_out_resource_data_running[i].toFixed(3))
                }else{
                    steam_out_resource_data.push(waste.out_resource.steam['外部汽源'].load.toFixed(3))
                }
            }else{
                steam_out_resource_data.push("0")
            }
            if(waste.out_resource.steam['自有蒸汽锅炉'] && waste.out_resource.steam['自有蒸汽锅炉'].used != 0){
                if(steam_out_resource_data_running[i] < waste.out_resource.steam['自有蒸汽锅炉'].load){
                    steam_out_resource_data_2.push(steam_out_resource_data_running[i].toFixed(3))
                }else{
                    steam_out_resource_data_2.push(waste.out_resource.steam['自有蒸汽锅炉'].load.toFixed(3))
                }
            }else{
                steam_out_resource_data_2.push("0")
            }
        }
    }
    if(steam_out_resource_data.length == 0){steam_out_resource_data = null}
    if(steam_out_resource_data_2.length == 0){steam_out_resource_data_2 = null}
    if(cool_out_resource_data.length == 0){cool_out_resource_data = null}
    if(cool_out_resource_data_2.length == 0){cool_out_resource_data_2 = null}
    if(heat_out_resource_data.length == 0){heat_out_resource_data = null}
    if(heat_out_resource_data_2.length == 0){heat_out_resource_data_2 = null}
    if(heat_out_resource_data_3.length == 0){heat_out_resource_data_3 = null}
    if(hot_water_out_resource_data.length == 0){hot_water_out_resource_data = null}
    if(hot_water_out_resource_data_2.length == 0){hot_water_out_resource_data_2 = null}
    if(air_out_resource_data.length == 0){air_out_resource_data = null}
    return {
        "外部蒸汽": steam_out_resource_data, "蒸汽锅炉": steam_out_resource_data_2,
        "热水": hot_water_out_resource_data, "空压站余热利用": hot_water_out_resource_data_2,
        "供热": heat_out_resource_data, "外部制冷设备供热": heat_out_resource_data_2,
        "外部制冷设备供冷": cool_out_resource_data, "外部空压站": air_out_resource_data,
        "热泵制冷": cool_out_resource_data_2, "热泵供热": heat_out_resource_data_3
    }
}
var setGraphDataNeed = function(data_json_dict, first_time=false, typical_day=1){
    // 使用刚指定的配置项和数据显示图表的需求数据。
    if (first_time){data_json = data_json_dict.front_data_day_1}
    else{
        switch(typical_day){
            case 1:
                data_json = data_json_dict.front_data_day_1
                break;
            case 2:
                data_json = data_json_dict.front_data_day_2
                break;
            case 3:
                data_json = data_json_dict.front_data_day_3
                break;
            case 4:
                data_json = data_json_dict.front_data_day_4
                break;
            default:
                data_json = []
                break;
        }
    }
    if (data_json['electric_curve'] != null) {
        $('#electric_graph').show()
        electricOption['series'][0]['data'] = data_json['electric_curve']
        electricGraph.setOption(electricOption);
    }else {
        $('#electric_graph').hide()
    }
    if (data_json['steam_curve'] != null) {
        $('#steam_graph').show()
        steamOption['series'][0]['data'] = data_json['steam_curve']
        steamOption['title']['text'] = '蒸汽曲线'
        steamGraph.setOption(steamOption);
    }else {
        $('#steam_graph').hide()
    }
    if (data_json['cool_curve'] != null) {
        $('#cool_graph').show()
        coolOption['series'][0]['data'] = data_json['cool_curve']
        coolOption['title']['text'] = '冷曲线'
        coolGraph.setOption(coolOption);
    }else {
        $('#cool_graph').hide()
    }
    if (data_json['heat_curve'] != null) {
        $('#heat_graph').show()
        heatOption['series'][0]['data'] = data_json['heat_curve']
        heatOption['title']['text'] = '热曲线'
        heatGraph.setOption(heatOption);
    }else {
        $('#heat_graph').hide()
    }
    if (data_json['hot_water_curve'] != null) {
        $('#hot_water_graph').show()
        hotWaterOption['series'][0]['data'] = data_json['hot_water_curve']
        hotWaterOption['title']['text'] = '热水曲线'
        hotWaterGraph.setOption(hotWaterOption);
    }else {
        $('#hot_water_graph').hide()
    }
    if (data_json['air_curve'] != null) {
        $('#air_graph').show()
        airOption['series'][0]['data'] = data_json['air_curve']
        airOption['title']['text'] = '空气曲线'
        airGraph.setOption(airOption);
    }else {
        $('#air_graph').hide()
    }
}

// 整理返回的数据，做成曲线
var getGraphCurveData = function(data_json_dict, typical_day=1, plan=0){
    var electric_running_data = []
    var steam_running_data = []
    var cool_running_data = []
    var heat_running_data = []
    var heat_running_data_2 = []
    var hot_water_running_data = []
    var electric_peak_data = []
    var steam_peak_data = []
    var cool_peak_data = []
    var heat_peak_data = []
    var heat_peak_data_2 = []
    var hot_water_peak_data = []
    var air_running_data = []
    var cost_running_data = []
    var income_running_data = []
    var photovoltaic_data = []
    var wind_data = []
    var out_resource_data_dict
    switch(typical_day)
    {
        case 1:
            data_json = data_json_dict.front_data_day_1
            break;
        case 2:
            data_json = data_json_dict.front_data_day_2
            break;
        case 3:
            data_json = data_json_dict.front_data_day_3
            break;
        case 4:
            data_json = data_json_dict.front_data_day_4
            break;
        default:
            data_json = []
            break;
    }
    if(data_json.length != 0){
        out_resource_data_dict = create_out_resource_data(data_json[plan]['waste'])
        for (running_hour in data_json[plan]['waste']['operating_state']) {
            // 电，蒸汽，冷，热，热水，空气
            if (data_json[plan]['waste']['operating_state'][running_hour]['output_x'].length  == 7) {
                electric_running_data.push(data_json[plan]['waste']['operating_state'][running_hour]['output_x'][0].toFixed(0))
                electric_peak_data.push(data_json[plan]['waste']['operating_state'][running_hour]['peak_x'][0].toFixed(0))
                steam_running_data.push(data_json[plan]['waste']['operating_state'][running_hour]['output_x'][1].toFixed(3))
                steam_peak_data.push(data_json[plan]['waste']['operating_state'][running_hour]['peak_x'][1].toFixed(3))
                cool_running_data.push(data_json[plan]['waste']['operating_state'][running_hour]['output_x'][2].toFixed(0))
                cool_peak_data.push(data_json[plan]['waste']['operating_state'][running_hour]['peak_x'][2].toFixed(0))
                heat_running_data.push((data_json[plan]['waste']['operating_state'][running_hour]['output_x'][3] + data_json[plan]['waste']['operating_state'][running_hour]['output_x'][4]).toFixed(0))
                heat_peak_data.push((data_json[plan]['waste']['operating_state'][running_hour]['peak_x'][3] + data_json[plan]['waste']['operating_state'][running_hour]['peak_x'][4]).toFixed(0))
                heat_running_data_2.push(data_json[plan]['waste']['operating_state'][running_hour]['output_x'][4].toFixed(0))
                heat_peak_data_2.push(data_json[plan]['waste']['operating_state'][running_hour]['peak_x'][4].toFixed(0))
                hot_water_running_data.push(data_json[plan]['waste']['operating_state'][running_hour]['output_x'][5].toFixed(3))
                hot_water_peak_data.push(data_json[plan]['waste']['operating_state'][running_hour]['peak_x'][5].toFixed(3))
                air_running_data.push(data_json[plan]['waste']['operating_state'][running_hour]['output_x'][6].toFixed(1))
                income_running_data.push(data_json[plan]['waste']['operating_state'][running_hour]['income'].toFixed(2))
                cost_running_data.push((data_json[plan]['waste']['operating_state'][running_hour]['cost'] + data_json[plan]['waste']['operating_state'][running_hour]['income']).toFixed(2))
            }else {
                electric_running_data.push(data_json[plan]['waste']['operating_state'][running_hour]['output_x'][0].toFixed(0))
                steam_running_data.push(data_json[plan]['waste']['operating_state'][running_hour]['output_x'][1].toFixed(3))
                cool_running_data.push(data_json[plan]['waste']['operating_state'][running_hour]['output_x'][2].toFixed(0))
                heat_running_data.push(data_json[plan]['waste']['operating_state'][running_hour]['output_x'][3].toFixed(0))
                hot_water_running_data.push(data_json[plan]['waste']['operating_state'][running_hour]['output_x'][4].toFixed(3))
                air_running_data.push(data_json[plan]['waste']['operating_state'][running_hour]['output_x'][5].toFixed(1))
            }
        }
        photovoltaic_data = data_json[plan]['waste']['photovoltaic']
        wind_data = data_json[plan]['waste']['wind']
    }
    return { 
        electric_running_data: electric_running_data,
        steam_running_data: steam_running_data,
        cool_running_data: cool_running_data,
        heat_running_data: heat_running_data,
        heat_running_data_2:heat_running_data_2,
        hot_water_running_data: hot_water_running_data,
        electric_peak_data: electric_peak_data,
        steam_peak_data: steam_peak_data,
        cool_peak_data: cool_peak_data,
        heat_peak_data: heat_peak_data,
        heat_peak_data_2: heat_peak_data_2,
        hot_water_peak_data: hot_water_peak_data,
        air_running_data: air_running_data,
        cost_running_data: cost_running_data,
        income_running_data: income_running_data,
        photovoltaic_data: photovoltaic_data,
        wind_data: wind_data,
        out_resource_data: out_resource_data_dict
    }
}

// 使用刚指定的配置项和数据显示图表的运行数据。
var setGraphDataRun = function(data_json, typical_day=1, running_plan=0, device_name_dict={}){
    curveData = getGraphCurveData(data_json, typical_day, running_plan)
    if(curveData.out_resource_data){
        costIncomeOption['series'][0]['data'] = curveData.income_running_data
        costIncomeOption['series'][1]['data'] = curveData.cost_running_data
        // costIncomeGraph.setOption(costIncomeOption)
        var label = {
                name:'',
                type:'bar',
                stack: '总量',
                barWidth: 15,
                data: null
            }
        if (electricOption['series'][0]['data'] != null) {
            var newElectricOption = cloneObj(electricOption)
            newElectricOption.series.push({name:'光伏', type:'bar', stack: '总量', barWidth: 15, data: null})
            newElectricOption.series[1].data = curveData.photovoltaic_data
            newElectricOption.series.push({name:'风电', type:'bar', stack: '总量', barWidth: 15, data: null})
            newElectricOption.series[2].data = curveData.wind_data
            var electric_device_name = device_name_dict.electric
            newElectricOption.series.push({name: electric_device_name, type:'bar', stack: '总量', barWidth: 15, data: null})
            newElectricOption.series[3]['data'] = curveData.electric_running_data
            newElectricOption.series.push({name:'市电', type:'bar', stack: '总量', barWidth: 15, data: null})
            newElectricOption.series[4]['data'] = curveData.electric_peak_data
            newElectricOption.legend.data = newElectricOption.legend.data.concat(['光伏', '风电', electric_device_name, '市电'])
            electricGraph.setOption(newElectricOption);
        }
        // return {
        //     "外部蒸汽": steam_out_resource_data, "蒸汽锅炉": steam_out_resource_data_2,
        //     "热水": hot_water_out_resource_data, "空压站余热利用": hot_water_out_resource_data_2,
        //     "供热": heat_out_resource_data, "外部制冷": heat_out_resource_data_2,
        //     "外部制冷": cool_out_resource_data, "外部空压站": air_out_resource_data,
        // }
        if (steamOption['series'][0]['data'] != null) {
            var newSteamOption = cloneObj(steamOption)
            var idx = 1
            if(curveData.out_resource_data['外部蒸汽'] != null){
                newSteamOption.series.push({name:'外部汽源', type:'bar', stack: '总量', barWidth: 15, data: null})
                newSteamOption.series[idx].data = curveData.out_resource_data['外部蒸汽']
                newSteamOption.legend.data = newSteamOption.legend.data.concat(['外部汽源'])
                idx++
            }
            if(curveData.out_resource_data['蒸汽锅炉'] != null){
                newSteamOption.series.push({name:'自有蒸汽锅炉', type:'bar', stack: '总量', barWidth: 15, data: null})
                newSteamOption.series[idx].data = curveData.out_resource_data['蒸汽锅炉']
                newSteamOption.legend.data = newSteamOption.legend.data.concat(['自有蒸汽锅炉'])
                idx++
            }
            newSteamOption.series.push({name:'余热蒸汽锅炉', type:'bar', stack: '总量', barWidth: 15, data: null})
            newSteamOption.series[idx]['data'] = curveData.steam_running_data
            newSteamOption.legend.data = newSteamOption.legend.data.concat(['余热蒸汽锅炉'])
            idx++
            newSteamOption.series.push({name:'燃气蒸汽锅炉', type:'bar', stack: '总量', barWidth: 15, data: null})
            newSteamOption.series[idx]['data'] = curveData.steam_peak_data
            newSteamOption.legend.data = newSteamOption.legend.data.concat(['燃气蒸汽锅炉'])
            steamGraph.setOption(newSteamOption);
        }
        if (coolOption['series'][0]['data'] != null) {
            var newCoolOption = cloneObj(coolOption)
            var idx = 1
            if(curveData.out_resource_data['热泵制冷'] != null){
                newCoolOption.series.push({name:'热泵制冷', type:'bar', stack: '总量', barWidth: 15, data: null})
                newCoolOption.series[idx].data = curveData.out_resource_data['热泵制冷']
                newCoolOption.legend.data = newCoolOption.legend.data.concat(['热泵制冷'])
                idx++
            }
            if(curveData.out_resource_data['外部制冷设备供冷'] != null){
                newCoolOption.series.push({name:'外部制冷设备供冷', type:'bar', stack: '总量', barWidth: 15, data: null})
                newCoolOption.series[idx].data = curveData.out_resource_data['外部制冷设备供冷']
                newCoolOption.legend.data = newCoolOption.legend.data.concat(['外部制冷设备供冷'])
                idx++
            }
            if(device_name_dict.cool){
                var cool_device_name = device_name_dict.cool
                newCoolOption.series.push({name: cool_device_name, type:'bar', stack: '总量', barWidth: 15, data: null})
                newCoolOption.series[idx]['data'] = curveData.cool_running_data
                newCoolOption.legend.data = newCoolOption.legend.data.concat([cool_device_name])
                idx++
                newCoolOption.series.push({name:'电制冷', type:'bar', stack: '总量', barWidth: 15, data: null})
                newCoolOption.series[idx]['data'] = curveData.cool_peak_data
                newCoolOption.legend.data = newCoolOption.legend.data.concat(['电制冷'])
                coolGraph.setOption(newCoolOption);
            }
        }
        if (heatOption['series'][0]['data'] != null) {
            var newHeatOption = cloneObj(heatOption)
            var idx = 1
            if(curveData.out_resource_data['热泵供热'] != null){
                newHeatOption.series.push({name:'热泵供热', type:'bar', stack: '总量', barWidth: 15, data: null})
                newHeatOption.series[idx].data = curveData.out_resource_data['热泵供热']
                newHeatOption.legend.data = newHeatOption.legend.data.concat(['热泵供热'])
                idx++
            }
            if(curveData.out_resource_data['供热'] != null){
                newHeatOption.series.push({name:'外部供热设备', type:'bar', stack: '总量', barWidth: 15, data: null})
                newHeatOption.series[idx].data = curveData.out_resource_data['供热']
                newHeatOption.legend.data = newHeatOption.legend.data.concat(['外部供热设备'])
                idx++
            }
            if(curveData.out_resource_data['外部制冷设备供热'] != null){
                newHeatOption.series.push({name:'外部制冷设备供热', type:'bar', stack: '总量', barWidth: 15, data: null})
                newHeatOption.series[idx].data = curveData.out_resource_data['外部制冷设备供热']
                newHeatOption.legend.data = newHeatOption.legend.data.concat(['外部制冷设备供热'])
                idx++
            }
            if(device_name_dict.heat){
                var heat_device_name = device_name_dict.heat
                newHeatOption.series.push({name: heat_device_name, type:'bar', stack: '总量', barWidth: 15, data: null})
                newHeatOption.series[idx]['data'] = curveData.heat_running_data
                newHeatOption.legend.data = newHeatOption.legend.data.concat([heat_device_name])
                idx++
                newHeatOption.series.push({name:'燃气热水锅炉', type:'bar', stack: '总量', barWidth: 15, data: null})
                newHeatOption.series[idx]['data'] = curveData.heat_peak_data
                newHeatOption.legend.data = newHeatOption.legend.data.concat(['燃气热水锅炉'])
                heatGraph.setOption(newHeatOption);
            }
        }
        if (hotWaterOption['series'][0]['data'] != null) {
            var newHotWaterOption = cloneObj(hotWaterOption)
            var idx = 1
            if(curveData.out_resource_data['自有热水锅炉'] != null){
                newHotWaterOption.series.push({name:'热水', type:'bar', stack: '总量', barWidth: 15, data: null})
                newHotWaterOption.series[idx].data = curveData.out_resource_data['热水']
                newHotWaterOption.legend.data = newHotWaterOption.legend.data.concat(['自有热水锅炉'])
                idx++
            }
            if(curveData.out_resource_data['空压站余热利用'] != null){
                newHotWaterOption.series.push({name:'空压站余热利用', type:'bar', stack: '总量', barWidth: 15, data: null})
                newHotWaterOption.series[idx].data = curveData.out_resource_data['空压站余热利用']
                newHotWaterOption.legend.data = newHotWaterOption.legend.data.concat(['空压站余热利用'])
                idx++
            }
            if(device_name_dict.hot_water){
                var hot_water_device_name = device_name_dict.hot_water
                newHotWaterOption.series.push({name: hot_water_device_name, type:'bar', stack: '总量', barWidth: 15, data: null})
                newHotWaterOption.series[idx]['data'] = curveData.hot_water_running_data
                newHotWaterOption.legend.data = newHotWaterOption.legend.data.concat([hot_water_device_name])
                idx++
                newHotWaterOption.series.push({name:'燃气热水锅炉', type:'bar', stack: '总量', barWidth: 15, data: null})
                newHotWaterOption.series[idx]['data'] = curveData.hot_water_peak_data
                newHotWaterOption.legend.data = newHotWaterOption.legend.data.concat(['燃气热水锅炉'])
                hotWaterGraph.setOption(newHotWaterOption);
            }
        }
        if (airOption['series'][0]['data'] != null) {
            var newAirOption = cloneObj(airOption)
            var idx = 1
            if(curveData.out_resource_data['外部空压站'] != null){
                newAirOption.series.push({name:'外部空压站', type:'bar', stack: '总量', barWidth: 15, data: null})
                newAirOption.series[idx].data = curveData.out_resource_data['外部空压站']
                newAirOption.legend.data = newAirOption.legend.data.concat(['外部空压站'])
                idx++
            }
            if(device_name_dict.air){
                var air_device_name = device_name_dict.air
                newAirOption.series.push({name: air_device_name, type:'bar', stack: '总量', barWidth: 15, data: null})
                newAirOption.series[idx]['data'] = curveData.air_running_data
                newAirOption.legend.data = newAirOption.legend.data.concat([air_device_name])
                idx++
                airGraph.setOption(newAirOption);
            }
        }
    }
    enable_select_typical_day()
}

var change_typical_day = function(){
    var data_val = $(this).val();
    var device_name_dict = addDeviceList(runningDataJson, typical_day=parseInt(data_val))
    setGraphDataNeed(needDataJson, first_time=false, typical_day=parseInt(data_val), device_name_dict=device_name_dict)
    setGraphDataRun(runningDataJson, typical_day=parseInt(data_val), 0, device_name_dict=device_name_dict)
    cost_calculate(runningDataJson, typical_day=parseInt(data_val), 0)
    add_running_plan(runningDataJson, typical_day=parseInt(data_val))
}

var enable_select_typical_day = function(){
    var select_options = $("#typical_day").find('option')
    select_options.each(function(){
        var name = $(this).attr('id')
        name = "front_data_" + name
        if (runningDataJson[name]){
            $(this).removeAttr("disabled")
        }
        else{
            $(this).attr("disabled", "")
        }
    })
}

var add_running_plan = function(data_json_dict, typical_day=1){
    switch(typical_day)
    {
        case 1:
            data_json = data_json_dict.front_data_day_1
            break;
        case 2:
            data_json = data_json_dict.front_data_day_2
            break;
        case 3:
            data_json = data_json_dict.front_data_day_3
            break;
        case 4:
            data_json = data_json_dict.front_data_day_4
            break;
        default:
            data_json = []
            break;
    }
    $("#running_plan").find('option').remove()
    for (i = 0;i < data_json.length;i++){
        $("#running_plan").append("<option value='" + (i + 1) + "'>设备方案"+ (i + 1) +"</option>");
    }
}

var change_running_plan = function(){
    var running_plan_val = $(this).val();
    var typical_day_val = $("#typical_day").val();
    var running_plan = parseInt(running_plan_val) - 1
    var device_name_dict = addDeviceList(runningDataJson, typical_day=parseInt(typical_day_val), running_plan=running_plan)
    setGraphDataRun(runningDataJson, typical_day=parseInt(typical_day_val), running_plan=running_plan, device_name_dict=device_name_dict)
    cost_calculate(runningDataJson, typical_day=parseInt(typical_day_val), running_plan=running_plan)
}

var cost_calculate = function(data_json_dict, typical_day=1, running_plan=0){
    var data_json = []
    switch(typical_day)
    {
        case 1:
            data_json = data_json_dict.front_data_day_1
            break;
        case 2:
            data_json = data_json_dict.front_data_day_2
            break;
        case 3:
            data_json = data_json_dict.front_data_day_3
            break;
        case 4:
            data_json = data_json_dict.front_data_day_4
            break;
        default:
            data_json = []
            break;
    }
    if(data_json.length != 0){
        var day_electric_supply = 0
        var day_electric_consumption = 0
        var day_water_consumption = 0
        var day_gas_consumption = 0
        var day_heat_supply = 0
        var day_cool_supply = 0
        var day_hot_water_supply = 0
        var electric_cost = 0
        var water_cost = 0
        var gas_cost = 0
        var electric_income = 0
        var heat_income = 0
        var hot_water_income = 0
        var cool_income = 0
        $.each(data_json[running_plan].waste.consumption_running.electric_consumption, function(index, value){
            day_electric_consumption = day_electric_consumption + this
        })
        $.each(data_json[running_plan].waste.consumption_running.water_consumption, function(index, value){
            day_water_consumption = day_water_consumption + this
            water_cost = water_cost + day_water_consumption * data_json[running_plan].price[index].water
        })
        $.each(data_json[running_plan].waste.consumption_running.gas_consumption, function(index, value){
            day_gas_consumption = day_gas_consumption + this
            gas_cost = gas_cost + day_gas_consumption * data_json[running_plan].price[index].gas
        })
        $.each(data_json[running_plan].waste.operating_state, function(index, value){
            day_electric_supply = day_electric_supply + this.output_x[0] + this.peak_x[0] + this.out_resource_running[0]
            electric_income = electric_income + (this.output_x[0] + this.peak_x[0] + this.out_resource_running[0] - data_json[running_plan].waste.consumption_running.electric_consumption[index]) * data_json[running_plan].price[index].electric
            electric_cost = electric_cost + (data_json[running_plan].need.electric_curve[index] - (this.output_x[0] + this.peak_x[0] + this.out_resource_running[0]) + data_json[running_plan].waste.consumption_running.electric_consumption[index]) * data_json[running_plan].price[index].electric
            day_cool_supply = day_cool_supply + this.output_x[2] + this.peak_x[2] + this.out_resource_running[2]
            cool_income = cool_income + day_cool_supply * data_json[running_plan].price[index].cool
            day_heat_supply = day_heat_supply + this.output_x[3] + this.peak_x[3] + this.out_resource_running[3] + this.output_x[4] + this.peak_x[4] + this.out_resource_running[4]
            heat_income = heat_income + day_heat_supply * data_json[running_plan].price[index].heat
            day_hot_water_supply = day_hot_water_supply + this.output_x[5] + this.peak_x[5] + this.out_resource_running[5]
            hot_water_income = hot_water_income + day_hot_water_supply * data_json[running_plan].price[index].hot_water
        })
        // 收入
        $("#running_income").find("#供电量").val((day_electric_supply - day_electric_consumption).toFixed(2))
        $("#running_income").find("#供热量").val(day_heat_supply.toFixed(2))
        $("#running_income").find("#供冷量").val(day_cool_supply.toFixed(2))
        $("#running_income").find("#供热水量").val(day_hot_water_supply.toFixed(4))
        $("#running_income").find("#供电收入").val(electric_income.toFixed(1))
        $("#running_income").find("#供热收入").val(heat_income.toFixed(1))
        $("#running_income").find("#供热水收入").val(hot_water_income.toFixed(1))
        $("#running_income").find("#供冷收入").val(cool_income.toFixed(1))
        var zcpt = $("#running_param").find("#政策补贴").val()
        $("#running_income").find("#政策补贴收入").val()
        var total_income = electric_income + heat_income + hot_water_income + cool_income + parseFloat(zcpt)
        $("#running_income").find("#总计").val(total_income.toFixed(1))
        // 成本
        $("#running_cost").find("#耗气量").val(day_gas_consumption.toFixed(4))
        $("#running_cost").find("#耗水量").val(day_water_consumption.toFixed(4))
        $("#running_cost").find("#耗电量").val(day_electric_consumption.toFixed(2))
        $("#running_cost").find("#耗气成本").val(gas_cost.toFixed(1))
        $("#running_cost").find("#耗水成本").val(water_cost.toFixed(1))
        $("#running_cost").find("#耗电成本").val(electric_cost.toFixed(1))
        $("#running_cost").find("#人工成本").val(parseFloat($("#劳动定员").val()) * parseFloat($("#年人均工资").val()))
        $("#running_cost").find("#维修成本").val(gas_cost.toFixed(1))
        $("#running_cost").find("#电力容量备用费").val(0)
        $("#running_cost").find("#总计").val(0)
        $("#running_cost").find("#绝对收益").val(0)
        $("#running_cost").find("#原有系统成本").val()
        $("#running_cost").find("#相对收益").val(0)
    }
}

$(document).ready(function () {
    // init();
    $('#submitData').bind('click', saveMarkData);
    // 绑定下拉框事件
    $("#typical_day").bind("change", change_typical_day);
    $("#running_plan").bind("change", change_running_plan);
    // echart画图代码
    // 基于准备好的dom，初始化echarts实例
    electricGraph = echarts.init(document.getElementById('electric_graph'));
    steamGraph = echarts.init(document.getElementById('steam_graph'));
    coolGraph = echarts.init(document.getElementById('cool_graph'));
    heatGraph = echarts.init(document.getElementById('heat_graph'));
    hotWaterGraph = echarts.init(document.getElementById('hot_water_graph'));
    airGraph = echarts.init(document.getElementById('air_graph'));
    // costIncomeGraph = echarts.init(document.getElementById('cost_income_graph'));
    $('#electric_graph').hide();
    $('#steam_graph').hide();
    $('#cool_graph').hide();
    $('#heat_graph').hide();
    $('#hot_water_graph').hide();
    $('#air_graph').hide();
    // $('#cost_income_graph').hide()
    $("#typical_day").hide();
    electricOption = cloneObj(option)
    electricOption['yAxis'][0]['axisLabel']['formatter'] = '{value} kW'
    electricOption['tooltip']['formatter'] = function(params, ticket, callback){
        var result = axisPoint(params, "kW")
        return result;             
    }
    steamOption = cloneObj(option)
    steamOption['yAxis'][0]['axisLabel']['formatter'] = '{value} t'
    steamOption['tooltip']['formatter'] = function(params, ticket, callback){
        var result = axisPoint(params, "t")
        return result;             
    }
    coolOption = cloneObj(option)
    coolOption['yAxis'][0]['axisLabel']['formatter'] = '{value} kW'
    coolOption['tooltip']['formatter'] = function(params, ticket, callback){
        var result = axisPoint(params, "kW")
        return result;             
    }
    heatOption = cloneObj(option)
    heatOption['yAxis'][0]['axisLabel']['formatter'] = '{value} kW'
    heatOption['tooltip']['formatter'] = function(params, ticket, callback){
        var result = axisPoint(params, "kW")
        return result;             
    }
    hotWaterOption = cloneObj(option)
    hotWaterOption['yAxis'][0]['axisLabel']['formatter'] = '{value} t'
    hotWaterOption['tooltip']['formatter'] = function(params, ticket, callback){
        var result = axisPoint(params, "t")
        return result;             
    }
    airOption = cloneObj(option)
    airOption['yAxis'][0]['axisLabel']['formatter'] = '{value} Nm³'
    airOption['tooltip']['formatter'] = function(params, ticket, callback){
        var result = axisPoint(params, "Nm³")
        return result;             
    }
    costIncomeOption = cloneObj(option)
    costIncomeOption['title']['text'] = '收入成本曲线'
    costIncomeOption['yAxis'][0]['axisLabel']['formatter'] = '{value} 元'
    costIncomeOption['xAxis'][0]['boundaryGap'] = true
    costIncomeOption['xAxis'][0]['axisPointer'] = {
        type: 'shadow'
    }
    costIncomeOption['tooltip']['formatter'] = function(params, ticket, callback){
        var result = axisPoint(params, "元")
        return result;             
    }
    costIncomeOption['legend']['data'] = ['收入','成本']
    costIncomeOption['series'] = [
        {
            name:'收入',
            type:'bar',
            areaStyle: { normal: {}},
            data: null
        },
        {
            name:'成本',
            type:'bar',
            areaStyle: {normal: {}},
            data: null
        }
    ]
    // 获取需求数据曲线，默认返回典型日1的数据
    $.ajax({
        url: '/energyIsland/get_graph_data_need',
        data: { "id": 'cvv' },
        type: 'post',
        cache: false,
        dataType: 'json',
        success: function (data_json) {
            $("#typical_day").show()
            // alert('success')
            needDataJson = data_json
            setGraphDataNeed(needDataJson)
            resize()
            // 获取运行数据默认返回典型日1的数据
            $.ajax({
                url: '/energyIsland/get_graph_data',
                data: { "id": 'cvv' },
                type: 'post',
                cache: false,
                dataType: 'json',
                success: function (data_json) {
                    // alert('success')
                    runningDataJson = data_json
                    var device_name_dict = addDeviceList(runningDataJson)
                    setGraphDataRun(runningDataJson, 1, 0, device_name_dict)
                    cost_calculate(runningDataJson, 1, 0)
                    add_running_plan(runningDataJson)
                    // $('#cost_income_graph').show()
                    $('#energyisland1').attr('onclick', "return true;")
                    $('#energyisland2').attr('onclick', "return true;")
                },
                error: function () {
                    alert("异常！");
                    $('#energyisland1').attr('onclick', "return true;")
                    $('#energyisland2').attr('onclick', "return true;")
                }
            });
        },
        error: function () {
            alert("异常！");
            $('#energyisland1').attr('onclick', "return true;")
            $('#energyisland2').attr('onclick', "return true;")
        }
    });
    // 调整图表大小
    $(window).resize(resize);
})

var saveMarkData = function(){
    $.ajax({
        url: '/energyIsland/save_mark_data',
        data: { 
            "running_param": $('#running_param_form').serialize(),
            "running_income": $('#running_income_form').serialize(),
            "running_cost": $('#running_cost_form').serialize()
        },
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
// 指定图表的配置项和数据
option = {
    title: {
        text: '电曲线'
    },
    // backgroundColor: '#5F5F5F',
    tooltip : {
        trigger: 'axis',
        axisPointer: {
            type: 'cross',
            label: {
                backgroundColor: '#6a7985'
            }
        }
        // ,
        // formatter: "a={a} <br/>b={b}: c={c}" // 这里是鼠标移上去的显示数据
    },
    legend: {
        data:['需求']
    },
    toolbox: {
        feature: {
            saveAsImage: {}
        }
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis : [
        {
            type : 'category',
            boundaryGap : true,
            data : function() {
                var list = [];
                for (var i = 0; i <= 23; i++) {
                    if (i <=8) {
                        list.push('0' + i + ':00~0' + (i + 1) + ':00');
                    }
                    else if (i ==9) {
                        list.push('09:00~10:00');
                    }
                    else{
                        list.push(i + ':00~' + (i + 1) + ':00');
                    }
                }
                return list;
            }()
        }
    ],
    yAxis : [
        {
            type : 'value',
            axisLabel: {
                show: true,
                interval: 0,
                formatter: '{value}'
                // formatter: function (value){return value + "单位";}
            }
        }
    ],
    series : [
        {
            name:'需求',
            type:'line',
            // stack: '总量',
            // areaStyle: { normal: {}},
            // itemStyle : {
            //     normal : {
            //         //圈圈的颜色
            //         color: '#4BAEC9',
            //         lineStyle:{
            //             //线的颜色
            //             color: '#4BAEC9'
            //         }
            //     }
            // },
            data: null
        }
        // ,
        // {
        //     name:'外部资源',
        //     type:'bar',
        //     stack: '总量',
        //     barWidth: 15,
        //     data: null
        // },
        // {
        //     name:'运行',
        //     type:'bar',
        //     stack: '总量',
        //     barWidth: 15,
        //     data: null
        // },
        // {
        //     name:'调峰',
        //     type:'bar',
        //     stack: '总量',
        //     barWidth: 15,
        //     data: null
        // }
    ]
};