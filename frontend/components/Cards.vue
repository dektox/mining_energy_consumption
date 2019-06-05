<template>
    <v-flex mb-3>
        <v-layout v-bind="binding" align-center justify-space-around wrap>
            <v-flex ma-3>
                <v-card elevation="5">
                    <v-flex pa-4 class="text-xs-center">
                        <span class="card-text"><b>MIN</b></span>
                        <br/><br/>
                        <v-progress-circular v-if="progress" indeterminate :size="50" :width="5"/>
                        <span v-else class="card-sm">
                            <b>{{ numbers[1] | decimals }}</b>
                        </span>
                        <br/>
                        <span class="card-text">TWh per year</span>
                    </v-flex>
                </v-card>
            </v-flex>
            <v-flex ma-3>
                <v-card elevation="5">
                    <v-flex class="text-xs-center" pa-4>
                        <span class="card-text"><b>{{ 'Estimated'.toUpperCase() }}</b></span>
                        <br/><br/>
                        <v-progress-circular v-if="progress" indeterminate :size="70" :width="7"/>
                        <span v-else class="card-lg">
                            <b>{{ numbers[0] | decimals }}</b>
                        </span>
                        <br/>
                        <span class="card-text">TWh per year</span>
                    </v-flex>
                </v-card>
            </v-flex>
            <v-flex ma-3>
                <v-card elevation="5">
                    <v-flex pa-4 class="text-xs-center">
                        <span class="card-text"><b>MAX</b></span>
                        <br/><br/>
                        <v-progress-circular v-if="progress" indeterminate :size="50" :width="5"/>
                        <span v-else class="card-sm">
                            <b>{{ numbers[2] | decimals }}</b>
                        </span>
                        <br/>
                        <span class="card-text">TWh per year</span>
                    </v-flex>
                </v-card>
            </v-flex>
        </v-layout>
    </v-flex>
</template>

<script>
    import axios from 'axios'
    import {percentage, decimals} from '~/assets/js/filters.js'

    export default {
        name: 'Cards',
        filters: {
            percentage,
            decimals
        },
        data() {
            return {
            }
        },
        created() {
            const self = this
            setInterval(function () {
                self.getNewData()
            }, 30000)
        },
        computed: {
            numbers() {
                return this.$store.getters.GET_NUMBERS || [0, 0, 0]
            },
            progress() {
                return this.$store.state.progress
            },
            binding() {
                const binding = {}
                if (this.$vuetify.breakpoint.xsOnly) binding.column = true
                return binding
            }
        },
        methods: {
            async getNewData() {
                await this.$store.dispatch('LOAD_NUMBERS')
            }
        }
    }
</script>
