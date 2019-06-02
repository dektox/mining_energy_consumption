<template>
    <v-layout
            column
            justify-center
            align-center
            ref="container"
    >
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
    async fetch ({ $axios, store }) {
        try {
            const res = await $axios.get(`https://ccaf.tech/api/countries`)
            await store.commit('SET_COUNTRIES', res.data.data)
        } catch (e) {
            alert(e)
        }
    }
}
</script>
