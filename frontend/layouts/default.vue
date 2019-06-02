<template>
  <v-app>
    <v-toolbar fixed app color="#ffb81c" height="120">
      <v-layout align-center row justify-start>
        <v-flex class="pointer logo" @click="gotoMain()">
          <img src="~static/logo.png" height="60">
        </v-flex>
        <v-divider vertical/>
        <v-flex mx-4>
          <img src="~static/logo2.png" height="80">
        </v-flex>
        <v-spacer />
        <span style="font-size: 32px">
          Cambridge Bitcoin Energy Consumption Index
        </span>
      </v-layout>
    </v-toolbar>
    <v-layout column class="menu">
      <v-flex pr-5 class="text-xs-left">
        <nuxt-link :class="{'active': links === 0}" to="/">
          cbeci
        </nuxt-link>
      </v-flex>
      <v-flex pr-5 class="text-xs-left">
        <nuxt-link :class="{'active': links === 1}" to="/comparisons">
          comparisons
        </nuxt-link>
      </v-flex>
      <v-flex pr-5 class="text-xs-left">
        <nuxt-link :class="{'active': links === 2}" to="/methodology">
          methodology
        </nuxt-link>
      </v-flex>
      <v-flex class="text-xs-left" pr-5>
        <nuxt-link :class="{'active': links === 3}" to="/qanda">
          Q&A
        </nuxt-link>
      </v-flex>
    </v-layout>
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
                  case '/methodology': link = 2
                      break
                  case '/comparisons': link = 1
                      break
                  case '/qanda': link = 3
                      break
                  default: link = 0
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
