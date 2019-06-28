<template>
  <v-layout column justify-center align-center id="wrap-container">
    <v-layout row align-center my-4>
      <v-flex pa-3>
        <img src="~static/live.png" height="40">
      </v-flex>
      <v-flex pa-3>
        <v-layout column>
          <span class="index-text">Bitcoin network power</span>
          <v-layout row>
            <v-icon class="icon-custom">
              updated
            </v-icon>
            <span class="index-subtext">updated every 30 seconds</span>
          </v-layout>
        </v-layout>
      </v-flex>
    </v-layout>
    <cards />
    <chartLoading v-if="progress"/>
    <chart v-else/>
    <v-layout row align-center my-4>
      <span>You can adjust the electricity cost parameter below to explore how the model reacts.</span>
    </v-layout>
    <controllers />
  </v-layout>
</template>

<script>
import Controllers from '~/components/index/Controllers'
import Cards from '~/components/index/Cards'
import ChartLoading from '~/components/index/ChartLoading'
import Chart from '~/components/index/Chart'

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
  fetch ({ store }) {
      store.dispatch('INITIALIZATION')
  },
  methods: {
  }
}
</script>
