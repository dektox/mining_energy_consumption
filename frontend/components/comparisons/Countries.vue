<template>
    <v-flex my-4 pa-3>
        <v-layout align-center justify-center>
            <h2 class="display-1">
                Country Ranking
            </h2>
        </v-layout>
        <v-layout v-bind="binding" align-center justify-center my-3>
            <v-flex v-for="(country, i) in countries" :key="i" ma-3>
                <v-card v-if="i === 2" elevation="5">
                    <v-flex pa-4 class="text-xs-center">
                        <img :src="country.logo" class="country-img-large">
                        <br/>
                        <span class="title">
                            {{ country.country }}
                        </span>
                        <br/>
                        <span style="font-size: 54px">
                            <b>{{ country.y | decimals }}</b>
                        </span>
                        <br>
                        <span>TWh per year</span>
                    </v-flex>
                </v-card>
                <v-card v-else elevation="5">
                    <v-flex pa-4 class="text-xs-center">
                        <img :src="country.logo" class="country-img">
                        <br/>
                        <span class="title">
                            {{ country.country }}
                        </span>
                        <br/>
                        <span style="font-size: 32px">
                            <b>{{ country.y | decimals }}</b>
                        </span>
                        <br>
                        <span>TWh per year</span>
                    </v-flex>
                </v-card>
            </v-flex>
        </v-layout>
        <v-layout my-3>
          <span>
              <b>Source:</b><br/>
              Countries data - <a target="_blank" href="https://www.cia.gov/library/publications/resources/the-world-factbook/fields/253rank.html">CIA Factbook</a>, 2016 est.
          </span>
        </v-layout>
    </v-flex>
</template>

<script>
    import {percentage, decimals} from '~/assets/js/filters.js'

    export default {
        name: 'Countries',
        filters: {
            percentage,
            decimals
        },
        data() {
            return {
            }
        },
        computed: {
            progress() {
                return this.$store.state.progress
            },
            countries() {
                const arr = this.$store.getters.GET_COUNTRIES
                const i = arr.findIndex(el => el.country === 'Bitcoin')
                return [arr[i+2] || {}, arr[i+1] || {}, arr[i] || {}, arr[i-1] || {}, arr[i-2] || {}]
            },
            binding() {
                const binding = {}
                if (this.$vuetify.breakpoint.xsOnly) binding.column = true
                return binding
            }
        }
    }
</script>
