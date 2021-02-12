<template>
    <v-layout id="wrap-container2" justify-center align-center wrap>
        <v-flex xs12 md10 my-4>
            <h1 class="display-4 text-xs-center">Methodology</h1>
        </v-flex>
        <overview />
        <model />
        <discussion />
        <change-log />
    </v-layout>
</template>

<script>
import Overview from '~/components/methodology/Overview'
import Model from '~/components/methodology/Model'
import Discussion from '~/components/methodology/Discussion'
import ChangeLog from '~/components/methodology/ChangeLog'

export default {
    name: 'methodology',
    components: {
        overview: Overview,
        model: Model,
        discussion: Discussion,
        changeLog: ChangeLog
    },
    data() {
        return {
        }
    }
}
</script>
