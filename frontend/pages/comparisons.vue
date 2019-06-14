<template>
    <v-layout column justify-center align-center>
        <v-layout column align-center justify-center my-3>
            <v-flex>
                <span style="font-size: 32px">Comparisons</span>
            </v-flex>
            <v-flex>
                <v-layout align-center justify-center>
                    <v-flex xs10>
                        <span style="font-size: 16px"><br />While Terawatt-hours (TWh) are a standard unit of energy used to measure energy production and consumption, it can be difficult for laymen to assess without additional context.
We provide a set of comparisons below to help readers put numbers into perspective.
All comparisons are based on our best estimate of Bitcoin's total energy consumption
            </span>
                    </v-flex>
                </v-layout>
            </v-flex>
        </v-layout>
        <comparisonsPC />
        <comparisonsRP />
        <comparisonsCards />
    </v-layout>
</template>

<script>
import axios from 'axios'

export default {
    name: 'comparisons',
    components: {
        comparisonsCards: () => import('~/components/ComparisonsCards'),
        comparisonsPC: () => import('~/components/ComparisonsPC'),
        comparisonsRP: () => import('~/components/ComparisonsRP'),
    },
    data() {
        return {}
    },
    async fetch ({ store }) {
        try {
            await store.dispatch('UPDATE_DATA_AFTER_PRICE_CHANGE', 0.05)
            await store.commit('SET_PUE', 1.1)
            await store.dispatch('INITIALIZATION')
            store.dispatch('LOAD_COUNTRIES')
        } catch (e) {
            alert(e)
        }
    }
}
</script>
