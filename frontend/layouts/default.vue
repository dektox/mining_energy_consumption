<template>
  <v-app>
    <v-toolbar fixed app color="#ffb81c" class="header">
      <v-layout align-center row justify-start>
        <v-flex class="pointer logo" @click="gotoMain()">
          <img src="~static/logo.png" class="logo">
        </v-flex>
        <v-divider vertical/>
        <v-flex mx-4>
          <img src="~static/logo2.png" class="logo2">
        </v-flex>
        <v-spacer />
        <span class="hidden-sm-and-down" style="font-size: 26px">
          Cambridge Bitcoin Electricity Consumption Index
        </span>
        <v-menu class="hidden-md-and-up">
          <v-toolbar-side-icon slot="activator"></v-toolbar-side-icon>
          <v-list>
            <v-list-tile>
              <v-list-tile-content>
                <v-list-tile-title>
                  <nuxt-link :class="{'active': $route.path === '/'}" to="/">
                    CBECI
                  </nuxt-link>
                </v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
            <v-list-tile>
              <v-list-tile-content>
                <v-list-tile-title>
                  <nuxt-link :class="{'active': $route.path === '/comparisons'}" to="/comparisons/">
                    Comparisons
                  </nuxt-link>
                </v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
            <v-list-tile>
              <v-list-tile-content>
                <v-list-tile-title>
                  <nuxt-link :class="{'active': $route.path === '/methodology'}" to="/methodology/">
                    Methodology
                  </nuxt-link>
                </v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
            <v-list-tile>
              <v-list-tile-content>
                <v-list-tile-title>
                  <nuxt-link :class="{'active': $route.path === '/faq'}" to="/faq/">
                    FAQ
                  </nuxt-link>
                </v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
            <v-list-tile>
              <v-list-tile-content>
                <v-list-tile-title>
                  <nuxt-link :class="{'active': $route.path === '/contact'}" to="/contact/">
                    Contact
                  </nuxt-link>
                </v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
          </v-list>
        </v-menu>
      </v-layout>
    </v-toolbar>
    <v-layout column class="menu hidden-sm-and-down">
      <v-flex pr-5 class="text-xs-left">
        <nuxt-link :class="{'active': $route.path === '/'}" to="/">
          CBECI
        </nuxt-link>
      </v-flex>
      <v-flex pr-5 class="text-xs-left">
        <nuxt-link :class="{'active': $route.path === '/comparisons/'}" to="/comparisons/">
          Comparisons
        </nuxt-link>
      </v-flex>
      <v-flex pr-5 class="text-xs-left">
        <nuxt-link :class="{'active': $route.path === '/methodology/'}" to="/methodology/">
          Methodology
        </nuxt-link>
      </v-flex>
      <v-flex class="text-xs-left" pr-5>
        <nuxt-link :class="{'active': $route.path === '/faq/'}" to="/faq/">
          FAQ
        </nuxt-link>
      </v-flex>
      <v-flex class="text-xs-left" pr-5>
        <nuxt-link :class="{'active': $route.path === '/contact/'}" to="/contact/">
          Contact
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
        methodologyAnchors: [
            {text: '1', link: ''},
            {text: '2', link: '/#1'},
            {text: '3', link: '/#2'},
            {text: '4', link: '/#3'},
        ]
    }
  },
  computed: {
  },
  methods: {
      gotoMain() {
          this.$router.push('/')
      }
  }
}
</script>
