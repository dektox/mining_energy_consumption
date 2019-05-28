<template>
    <v-flex mb-3>
        <v-layout row align-center>
            <v-flex ma-3>
                <v-card elevation="5">
                    <v-flex pa-4 class="text-xs-center">
                        <span><b>MAX</b></span>
                        <br/><br/>
                        <v-progress-circular v-if="progress" indeterminate :size="50" :width="5"/>
                        <span v-else style="font-size: 32px">
                <b>{{(numbers[2] * pue).toFixed(2) }}</b>
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
                <b>{{(numbers[0] * pue).toFixed(2) }}</b>
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
                <b>{{(numbers[1] * pue).toFixed(2) }}</b>
              </span>
                        <br/>
                        <span>TWh yearly</span>
                    </v-flex>
                </v-card>
            </v-flex>
        </v-layout>
    </v-flex>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Cards',
    data() {
        return {
            progress: false,
        }
    },
    created () {
        const self = this
        setInterval(function(){ self.getNewData() }, 30000)
    },
    computed: {
        numbers() {
            return this.$store.getters.GET_NUMBERS || [0,0,0]
        },
        pue() {
            return this.$store.getters.GET_PUE
        },
        price() {
            return this.$store.getters.GET_PRICE
        }
    },
    methods: {
        async getNewData() {
            this.progress = true
            const estimated = await axios.get(`https://www.ccaf.tech/api/guess/${this.price}`)
            const min = await axios.get(`https://www.ccaf.tech/api/min/${this.price}`)
            const max = await axios.get(`https://www.ccaf.tech/api/max/${this.price}`)
            await this.$store.commit('SET_NUMBERS', [estimated.data, min.data, max.data])
            this.progress = false
        }
    }
}
</script>
