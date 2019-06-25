<template>
    <v-layout my-4>
        <v-card elevation="5">
            <v-layout v-bind="binding" align-center justify-center wrap>
                <v-flex>
                    <v-toolbar
                            card
                            dense
                    >
                        <v-toolbar-title>
                            <span class="subheading">Electricity Cost</span>
                            <v-tooltip max-width="400" bottom>
                                <template v-slot:activator="{ on }">
                                    <v-icon style="cursor: pointer" v-on="on">help</v-icon>
                                </template>
                                <span>This variable corresponds to the average price per kWh paid by miners globally (in USD cents). The CBECI uses this parameter to model the economic lifetime of mining hardware in terms of mining revenues and electricity costs.</span>
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
                <span><a @click="updateValues">Click here</a> to restore default assumption </span>
                <v-tooltip max-width="400" bottom>
                    <template v-slot:activator="{ on }">
                        <v-icon style="cursor: pointer" v-on="on">help</v-icon>
                    </template>
                    <span>The CBECI assumes a constant average electricity price of 0.05 USD per kilowatt-hour (kWh) by default. The rationale for this assumption is explained in the Methodology section.</span>
                </v-tooltip>
            </v-layout>
        </v-card>
    </v-layout>
</template>

<script>
    export default {
        name: 'Controllers',
        data() {
            return {
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
            updateValues() {
                this.price = 5
                this.$store.dispatch('UPDATE_DATA_AFTER_PRICE_CHANGE', this.price / 100)
            }
        }
    }
</script>
