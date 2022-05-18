var ec_center = echarts.init(document.getElementById('c2'), "dark");

var mydata = [{'name': 'Shanghai', 'value': 318}, {'name': 'Yunnan', 'value': 162}]

var ec_center_option = {
    title: {
        text: '',
        subtext: '',
        x: 'left'
    },
    tooltip: {
        trigger: 'item',
        transitionDuration: 0,
    },
    //the navigator logo on the left side
    visualMap: {
        show: true,
        x: 'left',
        y: 'bottom',
        textStyle: {
            fontSize: 8,
        },
        splitList: [{ start: 1,end: 9 },
            {start: 10, end: 99 }, 
			{ start: 100, end: 999 },
            {  start: 1000, end: 9999 },
            { start: 10000 }],
        color: ['#8A3310', '#C64918', '#E55B25', '#F2AD92', '#F9DCD1']
    },
    //assign attribute
    series: [{
        name: 'cumulative diagnosis',
        type: 'map',
        mapType: 'china',
        roam: false, //drag and zoom
        itemStyle: {
            normal: {
                borderWidth: .5, //the width of framework
                borderColor: '#009fe8', //the color of framework
                areaColor: "#ffefd5", //the color of area
            },
            emphasis: { //Mouse over the related settings of the map highlight
                borderWidth: .5,
                borderColor: '#4b0082',
                areaColor: "#fff",
            }
        },
        label: {
            normal: {
                show: true, //name of province
                fontSize: 8,
            },
            emphasis: {
                show: true,
                fontSize: 8,
            }
        },
        data:[] //mydata //data
    }]
};
ec_center.setOption(ec_center_option)