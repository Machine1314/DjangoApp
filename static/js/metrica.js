var data = {
    timestamp : {{ dates }},
    temps : [
        22.88,
        22.88,
        22.88,
        22.88,
        22.88,
        22.88,
        22.88,
        22.88,
        22.94,
        22.94,
        23.00,
        23.00,
        23.00,
        23.00
    ],
    temps2 : [
        40,
        100,
        90,
        67
    ]
}

 Highcharts.chart('container', {
        chart : {
            type : 'line',
            zoomType : 'x'
        },
        title : {
            text : 'Tendecia Actual vs Ideal',
            x : -20
        },
        xAxis : {
            categories : data.timestamp,
            labels : {
                rotation : -90,
                // the step config is how you control how many x-axis labes are shown
                // this will help when there are lots of labels
                step : 3
            }
        },
        yAxis : {
            title : {
                text : 'Horas'
            }
        },
        tooltip : {
            valueSuffix : 'h'
        },
        series : [
            {
                name : 'Ideal',
                data : data.temps
            },
            {
                name : 'Actual',
                data : data.temps2
            }
        ]
    });