<template>
  <v-app>
    <v-navigation-drawer
            :value="drawer"
            :permanent="drawer"
            temporary
            absolute
            right
            style="background-color: #FEE9BA"
    >
      <v-layout column pa-4 mr-4>
        <h2 class="display-1">
          This site uses cookies
        </h2>
        <v-flex my-4>
          We use Google Analytics to see how people use our website. This helps us improve the website. The data we have is anonymised.
        </v-flex>
        <v-flex>
          <v-btn dark @click.stop="setCookies">
            Accept Cookies and Close
          </v-btn>
          <v-btn dark href="https://www.jbs.cam.ac.uk/about-this-site/cookies/" target="_blank">
            Learn more
          </v-btn>
        </v-flex>
      </v-layout>
    </v-navigation-drawer>
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
    <v-footer height="auto">
      <v-card
              class="flex"
              flat
              tile
      >
        <v-card-actions class="grey lighten-3 justify-center">
          Cambridge Centre for Alternative Finance © 2019
        </v-card-actions>
      </v-card>
    </v-footer>
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
      drawer() {
          return !this.$store.state.cooks
      }
  },
  methods: {
      gotoMain() {
          this.$router.push('/')
      },
      setCookies() {
          this.$store.commit('SET_COOK', true)
      }
  }
}
</script>
