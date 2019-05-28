<template>
    <v-flex mb-3>
        <v-card elevation="5">
            <v-toolbar
                    card
                    dense
            >
                <v-toolbar-title>
                    <span class="subheading">PUE</span>
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
                    <span class="subheading">Electricity cost</span>
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
