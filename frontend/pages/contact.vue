<template>
    <v-layout justify-center align-center wrap>
        <v-flex xs10>
            <v-layout my-4 justify-center align-center>
                <h1 class="display-2">Contacts</h1>
            </v-layout>
            <feedback />
        </v-flex>
    </v-layout>
</template>

<script>
import feedback from '~/components/contact/Feedback'

export default {
    name: 'contact',
    components: {
        feedback: feedback,
    },
    data() {
        return {

        }
    }
}
</script>
