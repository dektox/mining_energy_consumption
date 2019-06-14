<template>
    <v-flex my-3>
        <v-card elevation="5">
            <v-layout v-bind="binding" align-center justify-center wrap>
                <v-flex>
                    <v-toolbar card dense>
                        <v-toolbar-title>
                            <span class="subheading">PUE - Power Usage Effectiveness</span>
                            <v-tooltip bottom>
                                <template v-slot:activator="{ on }">
                                    <v-icon style="cursor: pointer" v-on="on">help</v-icon>
                                </template>
                                <span>
                            <p style="text-align: center;">
                                PUE is a measure of data centre energy efficiency: data centres generally consume more energy than is required to simply run equipment like servers because of cooling and other overhead. The higher the ratio, the less efficiently energy is used.</span></p>
<p><br /><span style="font-weight: 400;">Data centres with PUE ratios below 1.2 are generally considered efficient. For reference, </span><a href="https://www.google.com/about/datacenters/efficiency/internal/"><span style="font-weight: 400;">Google&rsquo;s average PUE</span></a><span style="font-weight: 400;"> is 1.11, whereas the average PUE of most data centres </span><a href="https://www.datacenterknowledge.com/archives/2011/05/10/uptime-institute-the-average-pue-is-1-8/"><span style="font-weight: 400;">corresponds to 1.8</span></a><span style="font-weight: 400;"> or more.
                            </p>
                        </span>
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
                                @end="changePUE"
                        >
                            <template v-slot:prepend>1</template>
                            <template v-slot:append>2</template>
                        </v-slider>
                    </v-flex>
                </v-flex>
                <v-flex>
                    <v-toolbar
                            card
                            dense
                    >
                        <v-toolbar-title>
                            <span class="subheading">Electricity Cost</span>
                            <v-tooltip bottom>
                                <template v-slot:activator="{ on }">
                                    <v-icon style="cursor: pointer" v-on="on">help</v-icon>
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
                                @end="changePrice"
                        >
                            <template v-slot:prepend>1 ¢</template>
                            <template v-slot:append>20 ¢</template>
                        </v-slider>
                    </v-flex>
                </v-flex>
            </v-layout>
            <v-layout align-center justify-center wrap pa-3>
                <span><a @click="updateValues">Click here</a> to restore default assumptions </span>
                <v-tooltip bottom>
                    <template v-slot:activator="{ on }">
                        <v-icon style="cursor: pointer" v-on="on">help</v-icon>
                    </template>
                    <span>Sometext</span>
                </v-tooltip>
            </v-layout>
        </v-card>
    </v-flex>
</template>

<script>
export default {
    name: 'Controllers',
    data() {
        return {
            pue: this.$store.state.pue,
            price: (this.$store.state.price * 100).toFixed(1)
        }
    },
    computed: {
        binding() {
            const binding = {}
            if (this.$vuetify.breakpoint.smAndDown) binding.column = true
            return binding
        }
    },
    methods: {
        changePrice() {
            this.$store.dispatch('UPDATE_DATA_AFTER_PRICE_CHANGE', this.price / 100)
        },
        changePUE() {
            this.$store.commit('SET_PUE', this.pue)
        },
        updateValues() {
            this.price = 5
            this.pue = 1.1
            this.$store.dispatch('UPDATE_DATA_AFTER_PRICE_CHANGE', this.price / 100)
            this.$store.commit('SET_PUE', this.pue)
        }
    }
}
</script>
