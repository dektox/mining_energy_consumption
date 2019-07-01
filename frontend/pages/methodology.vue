<template>
    <v-layout id="wrap-container2" justify-center align-center wrap my-4>
        <v-flex xs10>
            <v-layout justify-center align-center>
                <h1 class="display-2">Methodology</h1>
            </v-layout>
            <overview />
            <keep-alive>
                <model />
            </keep-alive>
            <discussion />
        </v-flex>
    </v-layout>
</template>

<script>
import Overview from '~/components/methodology/Overview'
// import Model from '~/components/methodology/Model'
import Discussion from '~/components/methodology/Discussion'

export default {
    name: 'methodology',
    components: {
        overview: Overview,
        model: () => import('~/components/methodology/Model'),
        discussion: Discussion
    },
    data() {
        return {
        }
    }
}
</script>
