var ec_left2 = echarts.init(document.getElementById('l2'), "dark");
var ec_left2_Option = {
	tooltip: {
		trigger: 'axis',
		transitionDuration: 0,
		//pointer
		axisPointer: {
			type: 'line',
			lineStyle: {
				color: '#7171C6'
			}
		},
	},
	legend: {
		data: ['cumulative diagnosis', 'cumulative suspects'],
		left: "right"
	},
	//heading style
	title: {
		text: "The National cumulative trend of Covid-19",
		textStyle: {
			color: 'white',
		},
		left: 'left'
	},
	//location of graph
	grid: {
		left: '4%',
		right: '6%',
		bottom: '4%',
		top: 50,
		containLabel: true
	},
	xAxis: [{
		type: 'category',
		//x轴坐标点开始与结束点位置都不在最边缘
		// boundaryGap : true,

		data: []
	}],
	yAxis: [{
		type: 'value',
		//the setting of y axis font

		//the setting of y axis line
		axisLine: {
			show: true
		},
		axisLabel: {
			show: true,
			color: 'white',
			fontSize: 12,
			formatter: function(value) {
				if (value >= 1000) {
					value = value / 1000 + 'k';
				}
				return value;
			}
		},
		//the setting of line which parallels with x axis
		splitLine: {
			show: true,
			lineStyle: {
				color: '#17273B',
				width: 1,
				type: 'solid',
			}
		}
	}],
	series: [{
		name: "newly diagnosis",
		type: 'line',
		smooth: true,
		data: []
	}, {
		name: "newly suspects",
		type: 'line',
		smooth: true,
		data: []
	}]
};

ec_left2.setOption(ec_left2_Option)
