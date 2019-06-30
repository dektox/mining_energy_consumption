<template>
    <v-flex my-4 pa-3>
        <v-layout align-center justify-center>
          <h2 class="display-1">
            Feedback
          </h2>
        </v-layout>
        <v-layout align-center justify-center my-3>
            <v-flex xs10 ma-3 class="text-xs-center">
                <v-form
                        ref="form"
                        v-model="valid"
                        lazy-validation
                >
                    <v-flex>
                        <p class="text-sm-left">We look forward to receiving feedback, comments, suggestions, and constructive criticism that will help us refine the methodology, add more content, and improve the overall index. Please use the form below to share your thoughts.</p>
                    </v-flex>
                    <v-text-field
                            v-model="name"
                            :rules="nameRules"
                            label="Name"
                            solo
                            required
                    />
                    <v-text-field
                            v-model="organization"
                            label="Organisation"
                            solo
                    />
                    <v-text-field
                            v-model="email"
                            :rules="emailRules"
                            label="E-mail"
                            required
                            solo
                    />

                    <v-textarea
                            v-model="message"
                            label="Your message ..."
                            required
                            solo
                    />

                    <v-flex>
                        <p class="text-sm-left"><strong>How we use your personal information:</strong></p>
                        <p class="text-sm-left">Cambridge Judge Business School will use your personal information to reply to your enquiry only. Read more about how we handle your personal information and your rights under the data protection legislation <a href="https://www.information-compliance.admin.cam.ac.uk/data-protection/general-data" target="_blank">here</a>.</p>
                    </v-flex>
                    <v-checkbox
                            v-model="checkbox"
                            :rules="[v => !!v || 'Your consent is required to continue']"
                            label="I have read and understood the above statement and consent to my personal information being used as described."
                            required
                    />

                    <v-flex v-if="status">
                        success
                    </v-flex>
                    <v-btn
                            v-else
                            :disabled="!valid"
                            :loading="loading"
                            color="#FFB81C"
                            @click="validate"
                    >
                        Send
                    </v-btn>

                </v-form>
            </v-flex>

        </v-layout>
    </v-flex>
</template>

<script>
    export default {
        name: 'feedback',
        data() {
            return {
                valid: true,
                loading: false,
                name: '',
                nameRules: [
                    v => !!v || 'Name is required',
                    v => (v && v.length <= 10) || 'Name must be less than 10 characters'
                ],
                email: '',
                emailRules: [
                    v => !!v || 'E-mail is required',
                    v => /.+@.+/.test(v) || 'E-mail must be valid'
                ],
                organization: '',
                message: '',
                checkbox: false,
                status: false
            }
        },
        computed: {
        },
        methods: {
            validate () {
                if (this.$refs.form.validate()) {
                    const self = this
                    self.loading = true
                    this.$axios.post('/user', {
                        email: self.email,
                        message: self.message,
                        name: self.name,
                        organisation: self.organisation
                    })
                        .then(function (response) {
                            self.loading = false
                            self.status = true
                        })
                        .catch(function (error) {
                            self.loading = false
                        });
                }
            },
            reset () {
                this.$refs.form.reset()
            },
            resetValidation () {
                this.$refs.form.resetValidation()
            }
        }
    }
</script>
