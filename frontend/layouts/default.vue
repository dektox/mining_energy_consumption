<template>
  <v-app>
    <v-toolbar fixed app color="#ffb81c" class="header">
      <v-layout align-center row justify-start>
        <v-flex mr-4 shrink class="pointer logo1">
          <a href="https://www.jbs.cam.ac.uk/faculty-research/centres/alternative-finance/" target="_blank">
            <img src="~static/logo.png" class="logo">
          </a>
        </v-flex>
        <v-divider vertical/>
        <v-flex mx-3 shrink>
          <img src="~static/logo2.png" class="logo2">
        </v-flex>
        <v-spacer />
        <span class="hidden-sm-and-down" style="font-size: 26px">
          Cambridge Bitcoin Electricity Consumption Index
        </span>
        <v-menu class="hidden-md-and-up">
          <v-toolbar-side-icon slot="activator"></v-toolbar-side-icon>
          <v-list>
            <v-list-group value="true">
              <template v-slot:activator>
                <v-list-tile-title>CBECI</v-list-tile-title>
              </template>
              <v-list-tile>
                <v-list-tile-content>
                  <v-list-tile-title>
                    <nuxt-link :class="{'active': $route.path === '/'}" to="/">
                      INDEX
                    </nuxt-link>
                  </v-list-tile-title>
                </v-list-tile-content>
              </v-list-tile>
              <v-list-tile>
                <v-list-tile-content>
                  <v-list-tile-title>
                    <nuxt-link :class="{'active': $route.path === '/cbeci/methodology'}" to="/cbeci/methodology">
                      Methodology
                    </nuxt-link>
                  </v-list-tile-title>
                </v-list-tile-content>
              </v-list-tile>
              <v-list-tile>
                <v-list-tile-content>
                  <v-list-tile-title>
                    <nuxt-link :class="{'active': $route.path === '/cbeci/comparisons'}" to="/cbeci/comparisons">
                      Comparisons
                    </nuxt-link>
                  </v-list-tile-title>
                </v-list-tile-content>
              </v-list-tile>
            </v-list-group>
<!--            <v-list-group value="true">-->
<!--              <template v-slot:activator>-->
<!--                <v-list-tile-title>Mining Map</v-list-tile-title>-->
<!--              </template>-->
<!--              <v-list-tile>-->
<!--                <v-list-tile-content>-->
<!--                  <v-list-tile-title>-->
<!--                    <nuxt-link :class="{'active': $route.path === '/mining_map'}" to="/mining_map">-->
<!--                      Visualisation-->
<!--                    </nuxt-link>-->
<!--                  </v-list-tile-title>-->
<!--                </v-list-tile-content>-->
<!--              </v-list-tile>-->
<!--              <v-list-tile>-->
<!--                <v-list-tile-content>-->
<!--                  <v-list-tile-title>-->
<!--                    <nuxt-link :class="{'active': $route.path === '/mining_map/methodology'}" to="/mining_map/methodology">-->
<!--                      Methodology-->
<!--                    </nuxt-link>-->
<!--                  </v-list-tile-title>-->
<!--                </v-list-tile-content>-->
<!--              </v-list-tile>-->
<!--            </v-list-group>-->
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
        <v-flex px-3 class="text-xs-left">
          <nuxt-link :class="{'active': $route.path === '/'}" to="/">
            Index
          </nuxt-link>
        </v-flex>
        <v-flex px-3 class="text-xs-left">
          <nuxt-link :class="{'active': $route.path === '/cbeci/methodology'}" to="/cbeci/methodology">
            Methodology
          </nuxt-link>
        </v-flex>
        <v-flex px-3 class="text-xs-left">
          <nuxt-link :class="{'active': $route.path === '/cbeci/comparisons'}" to="/cbeci/comparisons">
            Comparisons
          </nuxt-link>
        </v-flex>
      </v-flex>
<!--      <v-flex pr-5 class="text-xs-left">-->
<!--        <nuxt-link :class="{'active': $route.path === '/mining_map'}" to="/mining_map">-->
<!--          MINING MAP-->
<!--        </nuxt-link>-->
<!--        <v-flex px-3 class="text-xs-left">-->
<!--          <nuxt-link :class="{'active': $route.path === '/mining_map'}" to="/mining_map">-->
<!--            Visualisation-->
<!--          </nuxt-link>-->
<!--        </v-flex>-->
<!--        <v-flex px-3 class="text-xs-left">-->
<!--          <nuxt-link :class="{'active': $route.path === '/mining_map/methodology'}" to="/mining_map/methodology">-->
<!--            Methodology-->
<!--          </nuxt-link>-->
<!--        </v-flex>-->
<!--      </v-flex>-->
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
        <v-card-actions class="footer justify-center">
          Cambridge Centre for Alternative Finance © {{ new Date().getFullYear() }}
        </v-card-actions>
      </v-card>
    </v-footer>
    <div class="cookies" :class="{active: cookies}">
      <div class="cookies__cover"></div>
      <div class="cookies__panel">
        <v-layout column pa-4>
          <v-flex class="hidden-md-and-up" my-4>
            <h3 class="display-2">
              This site uses cookies
            </h3>
          </v-flex>
          <v-layout :v-bind="binding" fill-height wrap align-center row justify-start>
            <v-flex xs6>
              <div>
                We use Google Analytics to see how people use our website. This helps us improve the website. The data we have is anonymised.
              </div>
            </v-flex>
            <v-flex class="hidden-md-and-up" xs12 my-4>
            </v-flex>
            <v-spacer />
            <v-flex>
              <v-btn dark @click.stop="setCookies">
                Accept Cookies and Close
              </v-btn>
            </v-flex>
            <v-flex>
              <v-btn dark href="https://www.jbs.cam.ac.uk/about-this-site/cookies/" target="_blank">
                Learn more
              </v-btn>
            </v-flex>
          </v-layout>
        </v-layout>
      </div>
    </div>
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
      cookies() {
          if (!process.server) {
              if (this.$cookies.get('CookieControl')) {
                  if (this.$cookies.get('CookieControl').analytics !== 'true')
                      this.$store.commit('SET_COOK', false)
              } else {
                  this.$store.commit('SET_COOK', false)
              }
          }
          return !this.$store.state.cooks
      }
  },
  methods: {
      gotoMain() {
          this.$router.push('/')
      },
      setCookies() {
          this.$store.commit('SET_COOK', true)
      },
      binding() {
          const binding = {}
          if (!process.server) {
              if (this.$vuetify.breakpoint.xsOnly) binding.column = true
          }
          return binding
      }
  }
}
</script>
