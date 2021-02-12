<template>
    <v-layout id="wrap-container2" justify-center align-center wrap>
        <v-flex xs12 md10 my-4>
            <h1 class="display-4 text-xs-center">Change Log</h1>
        </v-flex>
        <change-log />
    </v-layout>
</template>

<script>
import ChangeLog from '~/components/methodology/ChangeLog'

export default {
    name: 'changes',
    components: {
        changeLog: ChangeLog
    },
    data() {
        return {
        }
    }
}
</script>
