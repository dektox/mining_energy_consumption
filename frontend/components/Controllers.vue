<template>
    <v-flex my-3>
        <v-card elevation="5">
            <v-toolbar
                    card
                    dense
            >
                <v-toolbar-title>
                    <span class="subheading">PUE - Power Usage Effectiveness</span>
                    <v-tooltip bottom>
                        <template v-slot:activator="{ on }">
                            <v-icon v-on="on">help</v-icon>
                        </template>
                        <span><p style="text-align: center;"><strong>PUE</strong> is the ratio of the total amount of energy used by a computer&nbsp;data <br />centre&nbsp;facility&nbsp;to the&nbsp;energy&nbsp;delivered to computing equipment; <br />it shows how much energy is used by the computing equipment in contrast&nbsp;to cooling and other overhead. <br />An ideal PUE is 1.0; Google&rsquo;s PUE is reportedly 1.11 as of 2019.</p></span>
                    </v-tooltip>
                </v-toolbar-title>
            </v-toolbar>
            <v-flex pa-3>
                <v-slider
                        v-model="pue"
                        min="1"
                        step="0.01"
                        max="2"
                        thumb-label="always"
                        color="#ffb81c"
                >
                    <template v-slot:prepend>
                        1
                    </template>
                    <template v-slot:append>
                        2
                    </template>
                </v-slider>
            </v-flex>
            <v-toolbar
                    card
                    dense
            >
                <v-toolbar-title>
                    <span class="subheading">Electricity Cost</span>
                    <v-tooltip bottom>
                        <template v-slot:activator="{ on }">
                            <v-icon v-on="on">help</v-icon>
                        </template>
                        <span>The average price miners pay for electricity, USD cents per kWh</span>
                    </v-tooltip>
                </v-toolbar-title>
            </v-toolbar>
            <v-flex pa-3>
                <v-slider
                        v-model="price"
                        min="1"
                        step="0.1"
                        max="20"
                        color="#ffb81c"
                        thumb-label="always"
                >
                    <template v-slot:prepend>
                        1 ¢
                    </template>
                    <template v-slot:append>
                        20 ¢
                    </template>
                </v-slider>
            </v-flex>
        </v-card>
    </v-flex>
</template>

<script>
import _ from 'lodash'
import axios from 'axios'

export default {
    name: 'Controllers',
    data() {
        return {
        }
    },
    computed: {
        pue: {
            get() {
                return this.$store.getters.GET_PUE
            },
            set(newVal) {
                this.changePUE(newVal)
            }
        },
        price: {
            get() {
                return (this.$store.getters.GET_PRICE * 100).toFixed(1)
            },
            set(newVal) {
                this.changePrice(newVal/100)
            }
        }
    },
    methods: {
        changePrice: _.debounce(async function(newVal) {
            try{
                const res = await axios.get(`https://ccaf.tech/api/data/${newVal}`)
                await this.$store.commit('SET_DATA', res.data)
                const estimated = await axios.get(`https://www.ccaf.tech/api/guess/${newVal}`)
                const min = await axios.get(`https://www.ccaf.tech/api/min/${newVal}`)
                const max = await axios.get(`https://www.ccaf.tech/api/max/${newVal}`)
                await this.$store.commit('SET_NUMBERS', [estimated.data, min.data, max.data])
                await this.$store.commit('SET_PRICE', newVal)
            } catch (e) {
                console.log(e)
            }
        }, 100, {leading:false, trailing:true}),
        changePUE: _.debounce(async function(newVal) {
            this.$store.commit('SET_PUE', newVal)
        }, 100, {leading:false, trailing:true})
    }
}
</script>
