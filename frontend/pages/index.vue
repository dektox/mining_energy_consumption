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
    <chart />
    <span style="line-height: 45px">You can adjust the variables that influence CBECI:</span>
    <controllers />
  </v-layout>
</template>

<script>
import axios from 'axios'
import Controllers from '~/components/Controllers'
import Cards from '~/components/Cards'
import ChartLoading from '~/components/ChartLoading'

export default {
  name: 'index',
  components: {
    controllers: Controllers,
    cards: Cards,
    chart: () => ({ component: import('~/components/Chart'), loading: ChartLoading, delay: 400 })
  },
  data() {
    return {
    }
  },
  fetch ({ $axios, store }) {
      store.dispatch('INITIALIZATION')
  },
  methods: {
  }
}
</script>
