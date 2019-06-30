<template>
    <v-layout justify-center align-center wrap>
        <v-flex xs10>
            <v-layout my-4 justify-center align-center>
                <h1 class="display-2">Contact</h1>
            </v-layout>
            <feedback />
			<team />
        </v-flex>
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

