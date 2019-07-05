<template>
    <v-layout id="wrap-container2" justify-center align-center wrap>
        <v-layout my-4 justify-center align-center>
            <h1 class="display-4">Methodology</h1>
        </v-layout>
        <overview />
        <keep-alive>
            <model />
        </keep-alive>
        <discussion />
    </v-layout>
</template>

<script>
import Overview from '~/components/methodology/Overview'
import Model from '~/components/methodology/Model'
import Discussion from '~/components/methodology/Discussion'

export default {
    name: 'methodology',
    components: {
        overview: Overview,
        model: Model,
        discussion: Discussion
    },
    data() {
        return {
        }
    }
}
</script>
