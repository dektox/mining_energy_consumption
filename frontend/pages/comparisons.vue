<template>
    <v-layout column justify-center align-center>
        <v-flex my-3>
          <span style="font-size: 32px">
            Country Comparison
          </span>
        </v-flex>
        <comparisonsCards />
        <controllers />
    </v-layout>
</template>

<script>
import axios from 'axios'
import Controllers from '~/components/Controllers'
import ComparisonsCards from '~/components/ComparisonsCards'

export default {
    name: 'comparisons',
    components: {
        comparisonsCards: ComparisonsCards,
        controllers: Controllers,
    },
    data() {
        return {}
    },
    async fetch ({ store }) {
        try {
            await store.dispatch('INITIALIZATION')
            await store.dispatch('LOAD_COUNTRIES')
        } catch (e) {
            alert(e)
        }
    }
}
</script>
