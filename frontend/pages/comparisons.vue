<template>
    <v-layout id="wrap-container3" justify-center align-center wrap>
        <v-flex xs10>
            <v-layout my-4 justify-center align-center>
                <h1 class="display-2">Comparisons</h1>
            </v-layout>
            <v-flex my-4 pa-3>
                <p class="main-text">While terawatt-hours (TWh) are a standard unit used to measure electricity consumption, it can be difficult for some to put these figures into perspective without additional context.</p>
                <p class="main-text">TThis section attempts to provide an unbiased and objective ground for helping visitors to independently assess the magnitude of Bitcoin’s electricity consumption and compare it to other uses of electricity.</p>
                <p class="main-text"><em><strong>Note:</strong> All comparisons are based on our <a href="https://cbeci.org/" target="_blank">best-guess estimate</a> of Bitcoin's total electricity consumption.</em></p>
            </v-flex>
            <comparisonsPC />
            <comparisonsRP />
            <comparisonsCards />
            <histogram />
            <comparisonsFF />
        </v-flex>
    </v-layout>
</template>

<script>
import countriesCards from '~/components/comparisons/Countries'
import PC from '~/components/comparisons/PC'
import RP from '~/components/comparisons/RP'
import FF from '~/components/comparisons/FF'
import Histogram from '~/components/comparisons/Histogram'

export default {
    name: 'comparisons',
    components: {
        comparisonsCards: countriesCards,
        comparisonsPC: PC,
        comparisonsRP: RP,
        comparisonsFF: FF,
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
