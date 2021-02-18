<template>
    <div v-if="isOpen" class="cookies" :class="{active: isOpen}">
        <div class="cookies__cover" />
        <div class="cookies__panel">
            <v-layout align-center justify-center>
                <v-flex xs10>
                    <v-layout align-center justify-center>
                        <v-flex class="grow" md8 pa-4>
                            <slot name="message">
                                We use Google Analytics to see how people use our website. This helps us improve the
                                website. The data we have is anonymised.
                                <nuxt-link class="cookie__link" to="https://www.jbs.cam.ac.uk/about-this-site/cookies/"
                                           target="_blank">
                                    Learn More
                                </nuxt-link>
                            </slot>
                        </v-flex>
                        <v-flex class="shrink d-flex justify-end" cols="12" md="4">
                            <v-btn class="ma-2 main" dark @click="accept">
                                {{ buttonTextAccept }}
                            </v-btn>
                        </v-flex>
                    </v-layout>
                </v-flex>
            </v-layout>
        </div>
    </div>
</template>

<script>
  export default {
    name: 'CookieMessage',
    props: {
      buttonTextAccept: {
        type: String,
        default: 'Accept'
      },
      message: {
        type: String,
        default:
          'We use cookies to provide our services and for analytics and marketing. To find out more about our use of cookies, please see our Privacy Policy. By continuing to browse our website, you agree to our use of cookies.'
      },
      position: {
        type: String,
        default: 'top'
      }
    },
    data() {
      return {
        isOpen: false
      }
    },
    created() {
      if (!this.getGDPR() === true) {
        this.isOpen = true
      }
    },
    methods: {
      getGDPR() {
        if (this.$route.path.includes('privacy-policy')) {
          return true
        }
        if (process.browser) {
          return localStorage.getItem('GDPR:accepted', true)
        }
      },
      accept() {
        if (process.browser) {
          this.isOpen = false
          localStorage.setItem('GDPR:accepted', true)
          window[`ga-disable-${process.env.GA_ID}`] = false
          this.$store.commit('SHOW_HELP', true)
        }
      }
    }
  }
</script>

<style lang="scss" scoped>
    .cookie {
        z-index: 1000000;
        position: fixed;
        bottom: 0;

        &__overlay {
            .v-alert {
                width: 100vw;
                position: fixed;
                bottom: 0;
                left: 0;
                margin-bottom: 0 !important;
            }
        }

        &__link {
            color: black;
            text-decoration: underline;
            transition: all .25s;

            &:hover {
                text-decoration: none;
            }
        }
    }
</style>
