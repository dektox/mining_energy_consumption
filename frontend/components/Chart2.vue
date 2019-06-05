<template>
    <v-flex>
        <!--<v-progress-circular v-if="progress" indeterminate :size="50" :width="5"/>-->
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
                tooltip: {
                    pointFormat: '{point.x}, {point.y}',
                    headerFormat: ''
                }
            }
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
            name: 'ESTIMATED consumption',
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
                ["12/1/14",0.51  ],
                ["09/1/15",0.27  ],
                ["06/1/16",0.1  ],
                ["06/1/16",0.26  ],
                ["02/1/17",0.1  ],
                ["02/1/17",0.1  ],
                ["04/1/17",0.13  ],
                ["04/1/17",0.16  ],
                ["07/1/17",0.1  ],
                ["08/1/17",0.13  ],
                ["09/1/17",0.1  ],
                ["09/1/17",0.12  ],
                ["11/1/17",0.1  ],
                ["12/1/17",0.13  ],
                ["01/1/18",0.14  ],
                ["01/1/18",0.14  ],
                ["01/1/18",0.17  ],
                ["01/1/18",0.11  ],
                ["01/1/18",0.15  ],
                ["02/1/18",0.09  ],
                ["02/1/18",0.1  ],
                ["03/1/18",0.26  ],
                ["03/1/18",0.16  ],
                ["04/1/18",0.09  ],
                ["04/1/18",0.09  ],
                ["05/1/18",0.05  ],
                ["05/1/18",0.09  ],
                ["05/1/18",0.09  ],
                ["05/1/18",0.1  ],
                ["05/1/18",0.1  ],
                ["05/1/18",0.11  ],
                ["05/1/18",0.11  ],
                ["07/1/18",0.09  ],
                ["07/1/18",0.09  ],
                ["07/1/18",0.11  ],
                ["08/1/18",0.08  ],
                ["08/1/18",0.09  ],
                ["08/1/18",0.09  ],
                ["08/1/18",0.1  ],
                ["09/1/18",0.06  ],
                ["09/1/18",0.07  ],
                ["09/1/18",0.07  ],
                ["09/1/18",0.09  ],
                ["10/1/18",0.05  ],
                ["10/1/18",0.05  ],
                ["10/1/18",0.06  ],
                ["10/1/18",0.07  ],
                ["10/1/18",0.08  ],
                ["11/1/18",0.08  ],
                ["11/1/18",0.07  ],
                ["11/1/18",0.1  ],
                ["12/1/18",0.08  ],
                ["12/1/18",0.08  ],
                ["01/1/19",0.05  ],
                ["03/1/19",0.06  ],
                ["04/1/19",0.04  ],
                ["04/1/19",0.04  ],
                ["04/1/19",0.05  ],
                ["04/1/19",0.05  ],
                ["05/1/19",0.04  ],
                ["05/1/19",0.06  ],
                ["07/1/19",0.05  ],
                ["08/1/19",0.05  ],
                ["08/1/19",0.06  ]
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
        progress() {
            return this.$store.state.progress2
        }
    },
    methods: {
        parseDate(date) {
            return date.map((el)=> {
                return [new Date(el[0]).getTime(), el[1]]
            })
        },
    }
}
</script>
