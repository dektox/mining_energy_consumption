<template>
  <v-container>
    <v-flex align="center" justify="center" style="height: 100vh;">
      <v-flex>
        <v-layout row align-center justify-center>
          <v-flex xs6>
            <v-form
              ref="form"
              v-model="valid"
              lazy-validation
            >
              <v-text-field
                v-model="password"
                :append-icon="show ? 'visibility_off' : 'visibility'"
                :rules="[rules.requiredPassword, rules.min]"
                :type="show ? 'text' : 'password'"
                label="Password"
                autocomplete="new-password"
                hint="At least 8 characters"
                class="input-group--focused"
                @click:append="show = !show"
                @keyup.enter="login"
              />
              <v-btn
                :disabled="!valid || password === ''"
                text
                tile
                class="green"
                @click="login"
              >
                Login
              </v-btn>
            </v-form>
          </v-flex>
        </v-layout>
      </v-flex>
    </v-flex>
  </v-container>
</template>

<script>

import Cookies from "js-cookie";

export default {
  name: 'Login',
  components: {},
  data() {
    return {
      valid: false,
      show: false,
      error: undefined,
      password: '',
      email: '',
      rules: {
        requiredPassword: v => !!v || '',
        min: v => (v && v.length >= 8) || ''
      }
    }
  },
  methods: {
    async login() {
      try {
        await this.$store.dispatch('signInWithEmail', this.password)
        this.$router.push('/demo')
      } catch (e) {
        this.error = e
      }
    }
  }
}
</script>
