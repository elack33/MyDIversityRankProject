 var chart1 = $(function () {
    $('#chart_panel').highcharts({
        chart: {
            backgroundColor: '#e0e0f0',
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            type: 'pie'
        },
        title: {
            text: "My Friends' Careers"
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
            name: "My Friends' Careers",
            colorByPoint: true,
            data: [{
                name: "Software Development",
                y: 0
            }, {
                name: "Customer Service",
                y: 23.53,
                sliced: true,
                selected: true
            }, {
                name: "Web Services",
                y: 11.76
            }, {
                name: "Other",
                y: 5.8
            }, {
                name: "Engineer",
                y: 5.8
            }, {
                name: "Accounting/Bookkeeping",
                y: 5.8
            }, {
                name: "Healthcare",
                y: 5.8
            }, {
                name: "Retired",
                y: 11.6
            }, {
                name: "Teaching",
                y: 5.8
            }, {
                name: "Management",
                y: 5.8
            }, {
                name: "Graphic Design",
                y: 5.8
            }, {
                name: "Product Developer",
                y: 5.8
            }, {
                name: "Editor",
                y: 5.8
            }]
        }]
    });
});