<template>
    <v-flex>
        <highcharts :constructor-type="'stockChart'" :options="{
        chart: {
          marginBottom: (containerWidth > 400) ? 120 : 0,
          marginLeft: (containerWidth > 400) ? 100 : 0,
          marginRight: (containerWidth > 400) ? 100 : 0,
          height: (containerWidth > 400) ? '56%' : 300,
          width: (containerWidth > 400) ? containerWidth * 0.9 : containerWidth,
          type: 'scatter',
          zoomType: 'xy'
        },
        title: {
            text: 'Mining equipment efficiency over time, J/Gh',
            align: 'left'
        },
        xAxis: {
            type: 'datetime',
            plotLines: [{
                color: 'rgb(170,170,170)',
                dashStyle: 'solid',
                value: (new Date()).getTime(), // Value of where the line will appear
                width: 1,
                label: {
                    text: 'Today',
                    verticalAlign: 'middle'
                }
             }]
        },
        yAxis: {
            title: {
                text: null
            },
            max: 0.6,
            opposite: false,
            type: 'logarithmic'
        },
        legend: {
            enabled: false
        },
        plotOptions: {
            scatter: {
                marker: {
                    radius: 5,
                    states: {
                        hover: {
                            enabled: true,
                            lineColor: 'rgb(100,100,100)'
                        }
                    }
                },
                states: {
                    hover: {
                        marker: {
                            enabled: false
                        }
                    }
                },
                // tooltip: {
                //     pointFormat:  '{point.x} {point.y}',
                //     headerFormat: ''
                // }
            }
        },
        tooltip: {
            formatter: function () {
              const point = this.point
              return '<b>' + 'Miner name' + '</b>' + ': ' + point.pointName + '<br/>' +
              '<b>' + 'Date of release' + '</b>' + ': ' + charts.dateFormat('%B %Y', this.x) + '<br/>' +
              '<b>' + point.series.name + '</b>' + ': ' + charts.numberFormat(point.y, 2) + ' J/Gh';
            },
            shared: true
        },
        navigator: {
            enabled: false
        },
        scrollbar: {
            enabled: false
        },
        rangeSelector: {
            enabled: false,
        },
        series: [
          {
            name: 'Efficiency',
            color: '#ffb81c',
            data: data,
          },
        ],
        exporting: {
            enabled: false
        }
      }" />
    </v-flex>
</template>

<script>
import {Chart} from 'highcharts-vue'
import charts from 'highcharts'
import stockInit from 'highcharts/modules/stock'

stockInit(charts)

export default {
    name: 'Chart2',
    components: {
        highcharts: Chart,
    },
    data() {
        return {
            containerWidth: 1000,
            data: this.parseDate([
                ["Bitmain Antminer S3",1404172800,0.77  ],
                ["Bitmain Antminer S5",1417392000,0.51  ],
                ["Bitmain Antminer S7",1441065600,0.27  ],
                ["Bitmain Antminer S9 (11.5Th)",1464739200,0.1  ],
                ["Bitmain Antminer S7-LN",1464739200,0.26  ],
                ["Bitmain Antminer R4",1485907200,0.1  ],
                ["Bitmain Antminer S9 (12.5Th)",1485907200,0.1  ],
                ["Bitmain Antminer T9 (11.5Th)",1491004800,0.13  ],
                ["Canaan AvalonMiner 741",1491004800,0.16  ],
                ["Bitmain Antminer S9 (13Th)",1498867200,0.1  ],
                ["Bitmain Antminer T9 (12.5Th)",1501545600,0.13  ],
                ["Bitmain Antminer S9 (13.5Th)",1504224000,0.1  ],
                ["Pantech SX6",1504224000,0.12  ],
                ["Bitmain Antminer S9 (14Th)",1509494400,0.1  ],
                ["Bitfury B8",1512086400,0.13  ],
                ["Ebang Ebit E9+",1514764800,0.14  ],
                ["Bitmain Antminer T9+ (10.5Th)",1514764800,0.14  ],
                ["MicroBT Whatsminer M3",1514764800,0.17  ],
                ["Bitfily Snow Panther A1",1514764800,0.11  ],
                ["Pantech WX6",1514764800,0.15  ],
                ["Ebang Ebit E10",1517443200,0.09  ],
                ["Canaan AvalonMiner 821",1517443200,0.1  ],
                ["Bitmain Antminer V9 (4Th)",1519862400,0.26  ],
                ["MicroBT Whatsminer M3X",1519862400,0.16  ],
                ["Halong Mining DragonMint T1",1522540800,0.09  ],
                ["Canaan AvalonMiner 841",1522540800,0.09  ],
                ["ASICminer 8 Nano Pro",1525132800,0.05  ],
                ["Innosilicon T2 Terminator",1525132800,0.09  ],
                ["Bitmain Antminer S9i (14Th)",1525132800,0.09  ],
                ["Bitmain Antminer S9i (13.5Th)",1525132800,0.1  ],
                ["Bitmain Antminer S9i (13Th)",1525132800,0.1  ],
                ["Ebang Ebit E9.2",1525132800,0.11  ],
                ["Ebang Ebit E9.3",1525132800,0.11  ],
                ["Bitfily Snow Panther B1",1530403200,0.09  ],
                ["Aladdin Miner 16Th/s Bitcoin",1530403200,0.09  ],
                ["Ebang Ebit E9i",1530403200,0.11  ],
                ["Innosilicon T2 Turbo",1533081600,0.08  ],
                ["Bitfily Snow Panther B1+",1533081600,0.09  ],
                ["Bitmain Antminer S9j (14.5Th)",1533081600,0.09  ],
                ["Bitmain Antminer S9 Hydro (18Th)",1533081600,0.1  ],
                ["MicroBT Whatsminer M10S",1535760000,0.06  ],
                ["MicroBT Whatsminer M10",1535760000,0.07  ],
                ["Innosilicon T2 Turbo+ 32T",1535760000,0.07  ],
                ["Canaan AvalonMiner 921",1535760000,0.09  ],
                ["Ebang Ebit E11++",1538352000,0.05  ],
                ["ASICminer 8 Nano 44Th",1538352000,0.05  ],
                ["Ebang Ebit E11+",1538352000,0.06  ],
                ["Ebang Ebit E11",1538352000,0.07  ],
                ["GMO miner B2",1538352000,0.08  ],
                ["Bitfury Tardis",1541030400,0.08  ],
                ["Bitmain Antminer S11 (20.5Th)",1541030400,0.07  ],
                ["GMO miner B3",1541030400,0.1  ],
                ["Holic H22",1543622400,0.08  ],
                ["Holic H28",1543622400,0.08  ],
                ["Innosilicon T3 43T",1546300800,0.05  ],
                ["Innosilicon T3 39T",1551398400,0.06  ],
                ["Bitmain Antminer S17 Pro (53Th)",1554076800,0.04  ],
                ["Bitmain Antminer S17 Pro (50Th)",1554076800,0.04  ],
                ["Bitmain Antminer S17 (56Th)",1554076800,0.05  ],
                ["Bitmain Antminer S17 (53Th)",1554076800,0.05  ],
                ["Innosilicon T3+ 52T",1556668800,0.04  ],
                ["Bitmain Antminer T17 (40Th)",1556668800,0.06  ],
                ["StrongU STU-U8",1561939200,0.05  ],
                ["MicroBT Whatsminer M20S",1564617600,0.05  ],
                ["MicroBT Whatsminer M21",1564617600,0.06  ]
            ])
        }
    },
    async mounted() {
        this.containerWidth = document.getElementById("wrap-container2").getBoundingClientRect().width
    },
    computed: {
        charts() {
            return charts
        },
    },
    methods: {
        parseDate(date) {
            return date.map((el)=> {
                return {
                    x: el[1] * 1000,
                    y: el[2],
                    pointName: el[0]
                }
            })
        },
    }
}
</script>

