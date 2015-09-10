 var chart1 = $(function () {
    $('#chart_panel').highcharts({
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            type: 'pie'
        },
        title: {
            text: 'Browser market shares January, 2015 to May, 2015'
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                    style: {
                        color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                    }
                }
            }
        },
        series: [{
            name: "Stuff",
            colorByPoint: true,
            data: [{
                name: "Things!",
                y: 56.33
            }, {
                name: "Nopes!",
                y: 24.03,
                sliced: true,
                selected: true
            }, {
                name: "Laser kittens",
                y: 10.38
            }, {
                name: "Goats",
                y: 4.77
            }, {
                name: "Weaponized Back hair",
                y: 0.91
            }, {
                name: "Yups",
                y: 0.2
            }]
        }]
    });
});