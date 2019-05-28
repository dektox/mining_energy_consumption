<template>
    <v-flex>
        <highcharts :constructor-type="'stockChart'" :options="{
        chart: {
          marginBottom: 120,
          reflow: false,
          marginLeft: 100,
          marginRight: 100,
          height: containerWidth * 0.5,
          width: containerWidth * 0.9
        },
        credits: {
            enabled: false
        },
        title: {
            text: 'Energy consumption chart',
            align: 'left'
        },
        subtitle: {
            text: 'Select an area by dragging across the lower chart',
            align: 'left'
        },
        xAxis: {
            type: 'datetime'
        },
        yAxis: {
            title: {
                text: null
            },
            max: 100,
            maxZoom: 0.1
        },
        tooltip: {
            formatter: function () {
              const point = this.points[0]
              return charts.dateFormat('%A %B %e %Y', this.x) + '<br/>' +
              '<b>' + this.points[1].series.name + '</b>' + ': ' + charts.numberFormat(this.points[1].y, 2) + '<br/>' +
              '<b>' + this.points[2].series.name + '</b>' + ': ' + charts.numberFormat(this.points[2].y, 2) + '<br/>' +
              '<b>' + this.points[0].series.name + '</b>' + ': ' + charts.numberFormat(this.points[0].y, 2);
            },
            shared: true
        },
        legend: {
            enabled: false
        },
        plotOptions: {
            series: {
                showInNavigator: true,
                marker: {
                    enabled: false,
                    states: {
                        hover: {
                            enabled: true,
                            radius: 3
                        }
                    }
                }
            }
        },
        navigator: {
            series: {
                dataGrouping: {
                }
            }
        },
        rangeSelector: {
            buttonTheme: { // styles for the buttons
                fill: 'none',
                stroke: 'none',
                'stroke-width': 0,
                r: 8,
                style: {
                    color: '#ffb81c',
                    fontWeight: 'bold'
                },
                states: {
                    hover: {
                    },
                    select: {
                        fill: '#ffb81c',
                        style: {
                            color: 'white'
                        }
                    }
                }
            },
            inputBoxBorderColor: 'gray',
            inputBoxWidth: 120,
            inputBoxHeight: 18,
            inputStyle: {
                color: '#ffb81c',
                fontWeight: 'bold'
            },
            labelStyle: {
                color: 'silver',
                fontWeight: 'bold'
            },
            selected: 5
        },
        series: [
          {
            name: 'MIN consumption',
            color: '#f2d596',
            data: dataSerieaMIN,
            lineWidth: 1.5
          },
          {
            name: 'MAX consumption',
            color: 'grey',
            data: dataSerieaMAX,
            lineWidth: 1.5
          },
          {
            name: 'ESTIMATED consumption',
            color: '#ffb81c',
            data: dataSerieaESTIMATED,
            lineWidth: 2.5
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
    name: 'Chart',
    components: {
        highcharts: Chart,
    },
    data() {
        return {
            containerWidth: 1000
        }
    },
    async mounted() {
        this.containerWidth = document.getElementById("container").getBoundingClientRect().width
    },
    computed: {
        pue() {
            return this.$store.getters.GET_PUE
        },
        dataSerieaMIN() {
            const data  = this.$store.getters.GET_DATA || []
            const res = []
            data.forEach((el) => {
                res.push([el.timestamp * 1000, el.min_consumption * this.pue])
            })
            return res
        },
        dataSerieaMAX() {
            const data  = this.$store.getters.GET_DATA || []
            const res = []
            data.forEach((el) => {
                res.push([el.timestamp * 1000, el.max_consumption * this.pue])
            })
            return res
        },
        dataSerieaESTIMATED() {
            const data  = this.$store.getters.GET_DATA || []
            const res = []
            data.forEach((el) => {
                res.push([el.timestamp * 1000, el.guess_consumption * this.pue])
            })
            return res
        },
        charts() {
            return charts
        }
    }
}
</script>
