<template>
    <v-flex>
        <v-switch
                v-model="log"
                label="Logarithmic scale"
                color="#ffb81c"
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
            text: 'Country ranking, annual electricity consumption',
            align: 'left'
        },
        tooltip: {
            formatter: function () {
              const point = this.points[0]
              return '<b>' + point.point.country + '</b><br/>' +
              'Total consumption: ' + point.y + ' TWh<br/>' +
              'Country rank: ' + point.x + '<br/>' +
              'Bitcoin percentage: ' + point.point.bitcoin_percentage + '%';
            },
            shared: true
        },
        xAxis: {
            type: 'linear',
            tickAmount: 60,
            labels: {
                formatter: function () {
                    return (isBitcoin(this.value) ? '<b>Bitcoin</b>' : '');
                },
                rotation: -45,
                y: 40,
                style: {
                    fontSize: '14px',
                    fontFamily: 'Verdana, sans-serif',
                    color: '#ffb81c'
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
            data: data
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
    name: 'Histogram',
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
        console.log(this.containerWidth)
    },
    computed: {
        charts() {
            return charts
        },
        data() {
            return this.$store.getters.GET_COUNTRIES.slice(0,60) || []
        }
    },
    methods: {
        isBitcoin(n) {
            const country = this.data.find(el => el.x === n)
            console.log(country)
            return country.country === 'Bitcoin'
        }
    }
}
</script>
