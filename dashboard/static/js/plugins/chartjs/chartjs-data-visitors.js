
/*
* Chart JS 2.0 BETA ONLY!!!
*/
      var barChartData = {
            labels: ["January", "February", "March", "April", "May", "June", "July","August","September","October","November","December"],
            datasets: [{
                type: 'bar',
                  label: "Visitors",
                    data: [32, 25, 33, 88, 32, 92, 33, 45, 60, 70, 41, 29],
                    fill: false,
                    backgroundColor: '#46BFBD',
                    borderColor: '#4DBEA7',
                    hoverBackgroundColor: '#389897',
                    hoverBorderColor: '#46BFBD',
                    yAxisID: 'y-axis-1'
            }, {
                label: "Trend",
                    type:'line',
                    data: [65, 59, 34, 81, 56, 55, 40, 48, 60, 65, 70, 80],
                    fill: false,
                    bezierCurve : false,
                    pointDot : true,
                    borderColor: '#8DBCEF',
                    backgroundColor: '#8DBCEF',
                    pointBorderColor: '#FFFFFF',
                    pointBackgroundColor: '#3E5F90',
                    pointHoverBackgroundColor: '#3E5F90',
                    pointHoverBorderColor: '#3E5F90',
                    yAxisID: 'y-axis-2'
            } ]
        };
        
        window.onload = function() {
            var ctx = document.getElementById("chartjs-visitors").getContext("2d");
            window.myBar = new Chart(ctx, {
                type: 'bar',
                data: barChartData,
                options: {
                responsive: true,
                maintainAspectRatio: true,
                scaleShowGridLines : true,
                scaleGridLineColor : "rgba(0,0,0,.05)",
                barShowStroke : true,
                barStrokeWidth : 2,
                tooltips: {
                  mode: 'label'
              },
              elements: {
                line: {
                    fill: false
                }
            },
              scales: {
                xAxes: [{
                    display: true,
                    gridLines: {
                        display: false
                    },
                    labels: {
                        show: true,
                    }
                }],
                yAxes: [{
                    type: "linear",
                    display: true,
                    position: "left",
                    id: "y-axis-1",
                    gridLines:{
                        display: false
                    },
                    labels: {
                        show:true,
                        
                    }
                }, {
                    type: "linear",
                    display: true,
                    position: "right",
                    id: "y-axis-2",
                    gridLines:{
                        display: false
                    },
                    labels: {
                        show:true,
                        
                    }
                }]
            }
            }
            });
        };
/*
#8FDBC4
#4DBEA7

#8DBCEF
#3E5F90
*/