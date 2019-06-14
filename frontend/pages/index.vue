<template>
  <v-layout column justify-center align-center id="wrap-container">
    <v-flex mb-3>
      <v-layout row align-center>
        <v-flex mr-3>
          <img src="~static/live.png" height="40">
        </v-flex>
        <v-flex>
          <span style="line-height: 45px">Yearly electricity consumption rate</span>
        </v-flex>
      </v-layout>
    </v-flex>
    <cards />
    <chartLoading v-if="progress"/>
    <chart v-else/>
    <span style="line-height: 45px">You can adjust the variables that influence CBECI:</span>
    <controllers />
  </v-layout>
</template>

<script>
import axios from 'axios'
import Controllers from '~/components/Controllers'
import Cards from '~/components/Cards'
import ChartLoading from '~/components/ChartLoading'
import Chart from '~/components/Chart'

export default {
  name: 'index',
  components: {
    controllers: Controllers,
    cards: Cards,
    chartLoading: ChartLoading,
    chart: Chart
  },
  data() {
    return {
    }
  },
    computed: {
        progress() {
            return this.$store.state.progress2
        },
    },
  fetch ({ $axios, store }) {
      store.dispatch('INITIALIZATION')
  },
  methods: {
  }
}
</script>
