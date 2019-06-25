<template>
    <v-layout id="wrap-container3" justify-center align-center wrap my-4>
        <v-flex xs10>
            <v-layout mb-4 justify-center align-center>
                <h1 class="display-2">Comparisons</h1>
            </v-layout>
            <p class="main-text">While Terawatt-hours (TWh) are a standard unit of energy used to measure energy production and consumption, it can be difficult for laymen to assess without additional context.
We provide a set of comparisons below to help readers put numbers into perspective.</p>
            <p class="main-text"></p>
            <p class="main-text">This section attempts to provide an unbiased and objective ground for helping visitors to independently assess the magnitude of Bitcoin’s electricity consumption and compare it to other uses of electricity.</p>
            <p class="main-text"></p>
            <p class="main-text"><em><strong>Note:<strong/> All comparisons are based on our best-guess estimate of Bitcoin's total electricity consumption.</em></p>
            <comparisonsPC />
            <comparisonsRP />
            <comparisonsCards />
            <histogram />
        </v-flex>
    </v-layout>
</template>

<script>
import countriesCards from '~/components/ComparisonsCards'
import PC from '~/components/ComparisonsPC'
import RP from '~/components/ComparisonsRP'
import Histogram from '~/components/Histogram'

export default {
    name: 'comparisons',
    components: {
        comparisonsCards: countriesCards,
        comparisonsPC: PC,
        comparisonsRP: RP,
        histogram: Histogram
    },
    data() {
        return {}
    },
    async fetch ({ store }) {
        try {
            await store.dispatch('UPDATE_DATA_AFTER_PRICE_CHANGE', 0.05)
            await store.dispatch('INITIALIZATION')
            store.dispatch('LOAD_COUNTRIES')
        } catch (e) {
            alert(e)
        }
    }
}
</script>
