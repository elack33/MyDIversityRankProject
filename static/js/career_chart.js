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
            data: [
                {
                    name: "Accounting",
                    y: accounting
                },
                {
                    name: "general_business",
                    y: general_business
                },

                {
                    name: "Software Development",
                    y: software_development,
                    sliced: true,
                    selected: true
                },
                {
                    name: "admin_clerical",
                    y: admin_clerical
                },
                {
                    name: "general_labor",
                    y: general_labor
                },
                {
                    name: "pharmaceutical",
                    y: pharmaceutical
                },
                {
                    name: "automotive",
                    y: automotive
                },
                {
                    name: "government",
                    y: government
                },
                {
                    name: "professional_services",
                    y: professional_services
                },
                {
                    name: "banking",
                    y: banking
                },
                {
                    name: "grocery",
                    y: grocery
                },
                {
                    name: "purchasing_procurement",
                    y: purchasing_procurement
                },
                {
                    name: "biotech",
                    y: biotech
                },
                {
                    name: "health_care",
                    y: health_care
                },
                {
                    name: "qa_quality_control",
                    y: qa_quality_control
                },
                {
                    name: "journalism",
                    y: journalism
                },
                {
                    name: "hotel_hospitality",
                    y: hotel_hospitality
                },
                {
                    name: "Real_Estate",
                    y: Real_Estate
                },
                {
                    name: "business_development",
                    y: business_development
                },
                {
                    name: "human_resources",
                    y: human_resources
                },
                {
                    name: "research",
                    y: research
                },
                {
                    name: "construction",
                    y: construction
                },
                {
                    name: "information_technology",
                    y: information_technology
                },
                {
                    name: "restaurant_food_service",
                    y: restaurant_food_service
                },
                {
                    name: "consultant",
                    y: consultant
                },
                {
                    name: "installation_repair",
                    y: installation_repair
                },
                {
                    name: "retail",
                    y: retail
                },
                {
                    name: "customer_service",
                    y: customer_service
                },
                {
                    name: "insurance",
                    y: insurance
                },
                {
                    name: "sales",
                    y: sales
                },
                {
                    name: "design",
                    y: design
                },
                {
                    name: "inventory",
                    y: inventory
                },
                {
                    name: "science",
                    y: science
                },
                {
                    name: "distribution_shipping",
                    y: distribution_shipping
                },
                {
                    name: "legal",
                    y: legal
                },
                {
                    name: "skilled_labor_trades",
                    y: skilled_labor_trades
                },
                {
                    name: "education_teaching",
                    y: education_teaching
                },
                {
                    name: "legal_admin",
                    y: legal_admin
                },
                {
                    name: "strategy_planning",
                    y: strategy_planning
                },
                {
                    name: "engineering",
                    y: engineering
                },
                {
                    name: "management",
                    y: management
                },
                {
                    name: "supply_chain",
                    y: supply_chain
                },
                {
                    name: "entry_level",
                    y: entry_level
                },
                {
                    name: "manufacturing",
                    y: manufacturing
                },
                {
                    name: "telecommunications",
                    y: telecommunications
                },
                {
                    name: "executive",
                    y: executive
                },
                {
                    name: "marketing",
                    y: marketing
                },
                {
                    name: "training",
                    y: training
                },
                {
                    name: "facilities",
                    y: facilities
                },
                {
                    name: "media",
                    y: media
                },
                {
                    name: "newspaper",
                    y: newspaper
                },
                {
                    name: "transportation",
                    y: transportation
                },
                {
                    name: "finance",
                    y: finance
                },
                {
                    name: "nonprofit",
                    y: nonprofit
                },
                {
                    name: "social_services",
                    y: social_services
                },
                {
                    name: "warehouse",
                    y: warehouse
                },
                {
                    name: "other",
                    y: other
                }
            ]
        }]
    });
});