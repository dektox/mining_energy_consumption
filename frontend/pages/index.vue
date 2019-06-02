<template>
  <v-layout
    column
    justify-center
    align-center
    id="container"
  >
    <v-flex mb-3>
      <v-layout row align-center>
        <v-flex mr-3>
          <img src="~static/live.png" height="40">
        </v-flex>
        <v-flex>
          <span style="line-height: 45px">Yearly energy consumption rate</span>
        </v-flex>
      </v-layout>
    </v-flex>
    <cards />
    <span style="line-height: 45px">You can adjust the variables that influence CBECI:</span>
    <controllers />
    <chart />
  </v-layout>
</template>

<script>
import axios from 'axios'
import Controllers from '~/components/Controllers'
import Cards from '~/components/Cards'
import Chart from '~/components/Chart'

export default {
  name: 'index',
  components: {
    controllers: Controllers,
    cards: Cards,
    chart: Chart
  },
  data() {
    return {
    }
  },
  async fetch ({ $axios, store }) {
    try {
      const price = await store.getters.GET_PRICE
      const res = await $axios.get(`https://ccaf.tech/api/data/${price}`)
      await store.commit('SET_DATA', res.data)
      const estimated = await $axios.get(`https://www.ccaf.tech/api/guess/${price}`)
      const min = await $axios.get(`https://www.ccaf.tech/api/min/${price}`)
      const max = await $axios.get(`https://www.ccaf.tech/api/max/${price}`)
      await store.commit('SET_NUMBERS', [estimated.data, min.data, max.data])
    } catch (e) {
      alert(e)
    }
  },
  methods: {
  }
}
</script>
