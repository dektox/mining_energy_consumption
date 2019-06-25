<template>
    <v-flex>
        <v-switch
                v-model="log"
                :label="log ? 'log scale' : 'linear scale'"
        ></v-switch>
        <highcharts :constructor-type="'stockChart'" :options="{
        chart: {
          marginBottom: (containerWidth > 400) ? 120 : 0,
          marginLeft: (containerWidth > 400) ? 100 : 0,
          marginRight: (containerWidth > 400) ? 100 : 0,
          height: (containerWidth > 400) ? '56%' : 300,
          width: (containerWidth > 400) ? containerWidth * 0.9 : containerWidth,
          type: 'column'
        },
        title: {
            text: 'Country Ranking',
            align: 'left'
        },
        tooltip: {
            formatter: function () {
              return '<b>' + 'Country' + '</b>' + ': ' + this.points[0].key + '<br/>' +
              '<b>' + 'Consumption' + '</b>' + ': ' + this.y + ' TWh per year';
            },
            shared: true
        },
        xAxis: {
            type: 'category',
            labels: {
                rotation: -45,
                style: {
                    fontSize: '13px',
                    fontFamily: 'Verdana, sans-serif'
                }
            }
        },
        yAxis: {
            title: { text: 'TWh per year' },
            max: 6000,
            opposite: false,
            type: log ? 'logarithmic' : ''
        },
        legend: {
            enabled: false
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
            name: 'Country Ranking',
            color: '#a2bdff',
            data: data,
          },
          {
            name: 'Country Ranking',
            color: '#ffb81c',
            data: data2,
          }
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
    name: 'Chart3',
    components: {
        highcharts: Chart,
    },
    data() {
        return {
            containerWidth: 1000,
            log: false
        }
    },
    async mounted() {
        this.containerWidth = document.getElementById("wrap-container3").getBoundingClientRect().width
    },
    computed: {
        charts() {
            return charts
        },
        data() {
            const data  = this.$store.getters.GET_COUNTRIES || []
            const bitcoin = [...this.$store.getters.GET_DATA].pop() || {}
            const arr = data.slice(0, 60).map(el => [el[1], parseInt(el[3])] )
            const newarr = arr.concat([['Bitcoin', parseInt(bitcoin.guess_consumption.toFixed(2))]])
            return newarr.sort((a, b) => {
                return a[1] - b[1]
            })
        },
        data2() {
            const bitcoin = [...this.$store.getters.GET_DATA].pop() || {}
            return [['Bitcoin', parseInt(bitcoin.guess_consumption.toFixed(2))]]
        }
    },
}
</script>
