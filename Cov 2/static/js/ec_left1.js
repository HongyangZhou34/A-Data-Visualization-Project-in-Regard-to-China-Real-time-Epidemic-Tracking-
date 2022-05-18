var ec_left1 = echarts.init(document.getElementById('l1'), "dark");

var ec_left1_Option = {
	//heading style
	title: {
		text: "The National cumulative trend of Covid-19",
		textStyle: {
			// color: 'white',
		},
		left: 'left',
	},
	tooltip: {
		trigger: 'axis',
		transitionDuration: 0,

		//Pointer
		axisPointer: {
			type: 'line',
			lineStyle: {
				color: '#7171C6'
			}
		},
	},
	legend: {
		data: ['cumulative diagnosis', 'existing suspects', "cumulative cure", "cumulative death"],
		left: "right",
		top: '8%',
	},

	//the location of graph
	grid: {
		left: '4%',
		right: '6%',
		bottom: '4%',
		top: 50,
		containLabel: true
	},
	xAxis: [{
		type: 'category',
		//the start location and end location of x axis are not at the edge
		// boundaryGap : true,
		data: []//['01.20', '01.21', '01.22']
	}],
	yAxis: [{
		type: 'value',
		//the setting of font of y axis
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
		//the setting of y axisline
		axisLine: {
			show: true
		},
		//the setting of line which parallels with x aixs
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
		name: "cumulative diagnosis",
		type: 'line',
		smooth: true,
		data: []//[260, 406, 529]
	}, {
		name: "existing suspects",
		type: 'line',
		smooth: true,
		data: []//[54, 37, 3935]
	},
		{
		name: "cumulative cure",
		type: 'line',
		smooth: true,
		data: []//[25, 25, 25]
	}, {
		name: "cumulative death",
		type: 'line',
		smooth: true,
		data: []//[6, 9, 17]
	}]
};

ec_left1.setOption(ec_left1_Option)
