<template>
    <v-layout justify-center align-center wrap>
        <v-flex xs12 md10 my-4>
            <h1 class="display-4 text-xs-center">Contact</h1>
        </v-flex>
        <feedback />
        <team />
    </v-layout>
</template>


<script>
import feedback from '~/components/contact/Feedback'
import team from '~/components/contact/Team_contributors'

export default {
    name: 'contact',
    components: {
        feedback: feedback,
		team: team,
    },
    data() {
        return {

        }
    }
}
</script>

