<template>
    <v-flex mb-4>
        <v-layout align-center justify-center my-4>
            <h3 class="display-2 text-xs-center">
                To Mars on Tesla Model 3
            </h3>
        </v-layout>
        <v-layout align-center justify-center my-4>
            <v-flex xs12 md8 class="text-xs-center">
                <v-card elevation="5">
                    <v-flex pa-4>
                        <v-flex>
                            <span>Given current Bitcoin electricity estimate
                                <v-progress-circular v-if="progress" indeterminate :size="50" :width="5"/>
                                <b v-else>{{numbers2[0]}} TWh</b>
                            and Tesla Model 3 consumption standing at 11.9 kWh per 100 km. <br><br>
                                Model 3 could've made (121.88*10^12 / 11.9*10^3) * 100 km =<br> 1024*10^9 km using this energy. <br><br>
                                This is enough to travel to Mars ...
                            </span>
                        </v-flex>
                        <v-layout align-center justify-center mt-4>
                            <v-flex xs6 pa-3>
                                <v-flex>
                                    <img src="~static/images/funFacts/roadster.jpg" object-fit="contain" width="100%">
                                </v-flex>
                            </v-flex>
                            <v-flex xs6 pa-3>
                                <v-progress-circular v-if="progress" indeterminate :size="50" :width="5"/>
                                <span v-else style="font-size: 32px"><b>{{numbers2[0] * 100000 / 11.9 / 225 | round}} times</b></span>
                            </v-flex>
                        </v-layout>
                    </v-flex>
                </v-card>
            </v-flex>
        </v-layout>
        <v-layout my-4 align-center justify-center wrap>
            <v-flex xs12 md10>
                <span>
              <b>Source:</b><br/>
              <a href="https://thedriven.io/2020/10/20/model-3-achieves-record-low-energy-consumption-in-driving-efficiency-test/" target="_blank">Model 3 achieves record low energy consumption in driving efficiency test</a>; own calculations
          </span>
            </v-flex>
        </v-layout>
    </v-flex>
</template>

<script>
  import {percentage, decimals, one_dec, round} from '~/assets/js/filters.js'
  export default {
    name: 'MaskMars',
    filters: {
      percentage,
      decimals,
      one_dec,
      round
    },
    data() {
      return {
      }
    },
    computed: {
      progress() {
        return this.$store.state.progress
      },
      numbers2() {
        const data  = [...this.$store.getters.GET_DATA].pop() || {}
        return [data.guess_consumption || 0, data.min_consumption || 0, data.max_consumption || 0]
      }
    }
  }
</script>
