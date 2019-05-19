<template>
  <v-layout
    column
    justify-center
    align-center
    ref="container"
  >
    <v-flex mt-3>
      <v-layout row align-center>
        <v-flex mr-3>
          <img src="~static/live.png" height="40">
        </v-flex>
        <v-flex>
          <span style="line-height: 45px">Yearly energy consumption rate</span>
        </v-flex>
      </v-layout>
    </v-flex>
    <v-flex mb-3>
      <v-layout row align-center>
        <v-flex ma-3>
          <v-card elevation="5">
            <v-flex pa-4 class="text-xs-center">
              <span><b>MAX</b></span>
              <br/><br/>
              <v-progress-circular v-if="progress" indeterminate :size="50" :width="5"/>
              <span v-else style="font-size: 32px">
                <b>{{ numbers[2].toFixed(2) }}</b>
              </span>
              <br/>
              <span>TWh yearly</span>
            </v-flex>
          </v-card>
        </v-flex>
        <v-flex ma-3>
          <v-card elevation="5">
            <v-flex class="text-xs-center" pa-4>
              <span><b>{{ 'Estimated'.toUpperCase() }}</b></span>
              <br/><br/>
              <v-progress-circular v-if="progress" indeterminate :size="70" :width="7"/>
              <span v-else style="font-size: 54px">
                <b>{{ numbers[0].toFixed(2) }}</b>
              </span>
              <br/>
              <span>TWh yearly</span>
            </v-flex>
          </v-card>
        </v-flex>
        <v-flex ma-3>
          <v-card elevation="5">
            <v-flex pa-4 class="text-xs-center">
              <span><b>MIN</b></span>
              <br/><br/>
              <v-progress-circular v-if="progress" indeterminate :size="50" :width="5"/>
              <span v-else style="font-size: 32px">
                <b>{{ numbers[1].toFixed(2) }}</b>
              </span>
              <br/>
              <span>TWh yearly</span>
            </v-flex>
          </v-card>
        </v-flex>
      </v-layout>
    </v-flex>
    <v-flex>
      <highcharts :options="{
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
              '<b>' + this.points[0].series.name + '</b>' + ': ' + charts.numberFormat(this.points[0].y, 2) + '<br/>' +
              '<b>' + this.points[1].series.name + '</b>' + ': ' + charts.numberFormat(this.points[1].y, 2) + '<br/>' +
              '<b>' + this.points[2].series.name + '</b>' + ': ' + charts.numberFormat(this.points[2].y, 2);
            },
            shared: true
        },
        legend: {
            enabled: false
        },
        plotOptions: {
            series: {
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
    <v-layout row v-if="false">
      <v-flex shrink style="width: 60px">
        <v-text-field
          v-model="slider[0]"
          class="mt-0"
          hide-details
          single-line
          type="number"
        />
      </v-flex>
      <v-flex>
        <v-range-slider
          v-model="slider"
          :max="600"
          :min="20"
          :step="10"
        />
      </v-flex>
      <v-flex shrink style="width: 60px">
        <v-text-field
          v-model="slider[1]"
          class="mt-0"
          hide-details
          single-line
          type="number"
        />
      </v-flex>
    </v-layout>
  </v-layout>
</template>

<script>
import {Chart} from 'highcharts-vue'
import charts from 'highcharts'
import axios from 'axios'

export default {
  name: 'index',
  components: {
    highcharts: Chart
  },
  data() {
    return {
      slider: [30, 120],
      progress: false,
      containerWidth: 1000
    }
  },
  created () {
    self = this
    setInterval(async function() {
      self.progress = true
      const estimated = await axios.get('https://www.ccaf.tech/api/guess')
      const min = await axios.get('https://www.ccaf.tech/api/min')
      const max = await axios.get('https://www.ccaf.tech/api/max')
      await self.$store.commit('SET_NUMBERS', [estimated.data, min.data, max.data])
      self.progress = false
    }, 30000)
  },
  async mounted() {
    this.containerWidth = this.$refs.container.clientWidth
  },
  async fetch ({ $axios, store }) {
    try {
      const res = await $axios.get('https://ccaf.tech/api/data')
      await store.commit('SET_DATA', res.data)
      const estimated = await $axios.get('https://www.ccaf.tech/api/guess')
      const min = await $axios.get('https://www.ccaf.tech/api/min')
      const max = await $axios.get('https://www.ccaf.tech/api/max')
      await store.commit('SET_NUMBERS', [estimated.data, min.data, max.data])
    } catch (e) {
      alert(e)
    }
  },
  computed: {
    numbers() {
      return this.$store.getters.GET_NUMBERS || [0,0,0]
    },
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
    charts() {
      return charts
    }
  },
  methods: {
  }
}
</script>
