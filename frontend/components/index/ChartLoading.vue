<template>
    <v-flex style="position: relative">
        <v-layout class="loading" justify-center align-center><v-flex>Loading data ...</v-flex></v-layout>
        <highcharts :constructor-type="'stockChart'" :options="{
        chart: {
          marginBottom: (containerWidth > 1000) ? 100 : 20,
          reflow: false,
          marginLeft: (containerWidth > 1000) ? 100 : 20,
          marginRight: (containerWidth > 1000) ? 100 : 20,
          height: (containerWidth > 1000) ? '56%' : 400,
          width: (containerWidth > 1000) ? containerWidth * 0.9 : containerWidth
        },
        credits: {
            enabled: false
        },
        title: {
            text: 'Bitcoin electricity consumption, TWh (annualised)',
            align: 'left'
        },
        subtitle: {
            text: (containerWidth > 400) ? 'Select an area by dragging across the lower chart' : '',
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
            maxZoom: 0.1,
            opposite: false
        },
        tooltip: {
            formatter: function () {
              const point = this.points[0]
              return Highcharts.dateFormat('%A %B %e %Y', this.x) + '<br/>' +
              '<b>' + this.points[1].series.name + '</b>' + ': ' + Highcharts.numberFormat(this.points[1].y, 2) + '<br/>' +
              '<b>' + this.points[2].series.name + '</b>' + ': ' + Highcharts.numberFormat(this.points[2].y, 2) + '<br/>' +
              '<b>' + this.points[0].series.name + '</b>' + ': ' + Highcharts.numberFormat(this.points[0].y, 2);
            },
            shared: true
        },
        legend: {
            enabled: false
        },
        plotOptions: {
            series: {
                showInNavigator: (containerWidth > 400),
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
            },
            enabled: (containerWidth > 400)
        },
        scrollbar: {
            enabled: (containerWidth > 400)
        },
        rangeSelector: {
            enabled: (containerWidth > 400),
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
            inputBoxWidth: 90,
            inputBoxHeight: 18,
            inputPosition: {
                x: -90
            },
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
    import Highcharts from 'highcharts'
    import exportingInit from 'highcharts/modules/exporting'
    if (typeof Highcharts === 'object') {
        exportingInit(Highcharts)
    }

    export default {
        name: 'Loading',
        components: {
            highcharts: Chart,
        },
        data() {
            return {
                containerWidth: 1000
            }
        },
        mounted() {
            this.containerWidth = document.getElementById("wrap-container").getBoundingClientRect().width
        },
        computed: {
            dataSerieaMIN() {
                const data  = this.$store.getters.GET_DATA || []
                const res = []
                data.forEach((el) => {
                    res.push([el.timestamp * 1000, el.min_consumption])
                })
                return res
            },
            dataSerieaMAX() {
                const data  = this.$store.getters.GET_DATA || []
                const res = []
                data.forEach((el) => {
                    res.push([el.timestamp * 1000, el.max_consumption])
                })
                return res
            },
            dataSerieaESTIMATED() {
                const data  = this.$store.getters.GET_DATA || []
                const res = []
                data.forEach((el) => {
                    res.push([el.timestamp * 1000, el.guess_consumption])
                })
                return res
            },
            Highcharts() {
                return Highcharts
            }
        }
    }
</script>
