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
                                    <v-icon v-on="on">help</v-icon>
                                </template>
                                <span>
                            <p style="text-align: center;">
                                <strong>PUE</strong> is the ratio of the total amount of energy used by a computer&nbsp;data <br />centre&nbsp;facility&nbsp;to the&nbsp;energy&nbsp;delivered to computing equipment; <br />it shows how much energy is used by the computing equipment <br />in contrast&nbsp;to cooling and other overhead. <br />An ideal PUE is 1.0; Google&rsquo;s PUE is reportedly 1.11 as of 2019.
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
                            <template v-slot:prepend>
                                1
                            </template>
                            <template v-slot:append>
                                2
                            </template>
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
                                @end="changePrice"
                        >
                            <template v-slot:prepend>
                                1 ¢
                            </template>
                            <template v-slot:append>
                                20 ¢
                            </template>
                        </v-slider>
                    </v-flex>
                </v-flex>
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
    }
}
</script>
