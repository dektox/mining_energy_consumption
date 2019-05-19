<template>
  <v-app>
    <v-toolbar fixed app color="#ffb81c" height="120">
      <v-layout align-center row>
        <v-flex>
          <img src="~static/logo.png" height="60">
        </v-flex>
        <v-divider vertical/>
        <v-flex mx-4>
          <img src="~static/logo2.png" height="80">
        </v-flex>
        <v-spacer />
        <v-flex>
          <span style="font-size: 32px">
            Bitcoin mining energy consumption index
          </span>
        </v-flex>
      </v-layout>
    </v-toolbar>
    <v-content>
      <v-container>
        <nuxt />
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
    }
  }
}
</script>
