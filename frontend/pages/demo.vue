<template>
  <v-layout column justify-center align-center id="wrap-container">
    <v-layout row align-center>
      <v-flex>
        <img src="~static/live.png" height="40">
      </v-flex>
      <v-flex pa-3>
        <v-layout column>
          <span class="index-text">&nbsp;Bitcoin network power</span>
          <v-layout row>
            <v-icon class="icon-custom">
              updated
            </v-icon>
            <span style="margin-left: 4px" class="index-subtext">updated every 30 seconds</span>
          </v-layout>
        </v-layout>
      </v-flex>
    </v-layout>
    <client-only>
      <cards />
    </client-only>
    <!--<chartLoading v-if="progress"/>-->
    <chart />
    <v-layout row align-center my-4>
      <a href="https://cbeci.org/api/csv" target="_blank">Download data in CSV format</a>
    </v-layout>
    <v-layout row align-center my-4>
      <span>You can adjust the electricity cost parameter below to explore how the model reacts.</span>
    </v-layout>
    <client-only>
      <controllers />
    </client-only>
  </v-layout>
</template>

<script>
import Controllers from '~/components/index/Controllers'
// import Cards from '~/components/index/Cards'
import ChartLoading from '~/components/index/ChartLoading'
import Chart from '~/components/index/Chart'

export default {
  name: 'index',
  layout: 'demo',
  mounted() {
    if (!this.$store.getters.authenticated) {
      return this.$router.push('/login')
    }
  },
  components: {
    controllers: Controllers,
    cards: () => import('~/components/index/Cards'),
    chartLoading: ChartLoading,
    chart: Chart
  },
  async fetch ({ store }) {
      await store.dispatch('INITIALIZATION')
  },
  data() {
    return {
      containerWidth: 0
    }
  },
  computed: {
      progress() {
          return this.$store.state.progress2
      }
  }
}
</script>
