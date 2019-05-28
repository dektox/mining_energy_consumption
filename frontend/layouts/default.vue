<template>
  <v-app>
    <v-toolbar fixed app color="#ffb81c" height="120">
      <v-layout align-center row>
        <v-flex class="pointer" @click="gotoMain()">
          <img src="~static/logo.png" height="60">
        </v-flex>
        <v-divider vertical/>
        <v-flex mx-4>
          <img src="~static/logo2.png" height="80">
        </v-flex>
        <v-spacer />
        <v-btn-toggle v-model="links" mandatory class="transparent">
          <v-btn flat>
            <v-flex pr-5>
              <nuxt-link to="/">
                main
              </nuxt-link>
            </v-flex>
          </v-btn>
          <v-btn flat>
            <v-flex pr-5>
              <nuxt-link to="/methodology">
                methodology
              </nuxt-link>
            </v-flex>
          </v-btn>
          <v-btn flat>
            <v-flex pr-5>
              <nuxt-link to="/comparisons">
                comparisons
              </nuxt-link>
            </v-flex>
          </v-btn>
        </v-btn-toggle>
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
  },
  computed: {
      links: {
          get: function () {
              let link = 0
              switch (this.$route.path) {
                  case '/': link = 0
                      break
                  case '/methodology': link = 1
                      break
                  case '/comparisons': link = 2
                      break
                  default: link = 1
                      break
              }
              return link
          },
          set: function (newVal) {
              return newVal
          }
      }
  },
  methods: {
      gotoMain() {
          this.$router.push('/')
      }
  }
}
</script>
