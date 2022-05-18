var ec_right1 = echarts.init(document.getElementById('r1'),"dark");
var ec_right1_option = {
	//heading style
	title : {
	    text : "TOP5 of the most diagnosed in China",
	    textStyle : {
	        color : 'white',
	    },
	    left : 'left'
	},
	  color: ['#3398DB'],
	    tooltip: {
	        trigger: 'axis',
			transitionDuration: 0,
	        axisPointer: {            // axispointer，axis trigger is valid
	            type: 'shadow'        // default: straightline，choose：'line' | 'shadow'
	        }
	    },
    xAxis: {
        type: 'category',
		axisLabel: {interval: 0},
        data: []
    },
    yAxis: {
        type: 'value'
    },
    series: [{
        data: [],
        type: 'bar',
		barMaxWidth:"50%"
    }]
};
ec_right1.setOption(ec_right1_option)