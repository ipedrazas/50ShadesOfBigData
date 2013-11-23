

$.ajax({
    url: 'http://localhost:5000/year',
    type: 'GET',
    success: function(result) {

	nv.addGraph(function() {
		var chart = nv.models.multiBarChart();

		chart.yAxis
		.tickFormat(d3.format(',.2f'));

		chart.showControls(false);

		d3.select('#chart_year svg')
		.datum(result)
		.transition().duration(500).call(chart);

		nv.utils.windowResize(chart.update);

		return chart;
	});
    }
});


$.ajax({
    url: 'http://localhost:5000/month',
    type: 'GET',
    success: function(result) {
	nv.addGraph(function() {
		var chart = nv.models.multiBarChart();

		chart.yAxis
		.tickFormat(d3.format(',.2f'));

		chart.showControls(false);

		d3.select('#chart_month svg')
		.datum(result)
		.transition().duration(500).call(chart);

		nv.utils.windowResize(chart.update);

		return chart;
	});
    }
});

