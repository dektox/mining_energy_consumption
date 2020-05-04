<template>
  <v-layout column justify-center align-center id="wrap-container">
    <v-flex xs12 md10 my-4>
      <h1 class="display-4 text-xs-center">Bitcoin Mining Map</h1>
    </v-flex>
    <v-layout row align-center justify-center>
      <v-flex xs12 md10 my-4>
        <div style="width: 100%">
          The Bitcoin Mining Map visualises the approximate geographic distribution of global Bitcoin hashrate. The average hashrate share by country is available for display in monthly intervals starting from April 2019. A second map with an exclusive focus on China’s hashrate distribution by province is available.
        </div>
      </v-flex>
    </v-layout>
    <v-layout row align-center>
      <v-flex>
        <iframe :width="containerWidth / 12 * 10" :height="containerWidth / 32 * 15" src="https://app.powerbi.com/view?r=eyJrIjoiY2M3Mzg4NDYtNTQwNi00MzIxLWJhNzQtMDQ1MmFlZjhmZTM5IiwidCI6IjAwYzliM2IxLTAzMTItNGMzMy1hZTdmLTgwZjNhNzU5ZGVjMSIsImMiOjh9" frameborder="0" allowFullScreen="true" />
      </v-flex>
    </v-layout>
    <v-layout row align-center justify-center>
      <v-flex xs12 md10 my-4>
        <div style="width: 100%">
          The chart below shows the average monthly hashrate breakdown by country in descending order. Please note that the diagramme uses a logarithmic scale.
        </div>
      </v-flex>
    </v-layout>
    <v-layout row align-center>
      <v-flex>
        <iframe :width="containerWidth / 12 * 10" :height="containerWidth / 32 * 15" src="https://app.powerbi.com/view?r=eyJrIjoiZTEwYjU0YmYtMmEzOS00ZjhhLTk5YWQtMjk0NWFlYWJhOWMwIiwidCI6IjAwYzliM2IxLTAzMTItNGMzMy1hZTdmLTgwZjNhNzU5ZGVjMSIsImMiOjh9" frameborder="0" allowFullScreen="true" />
      </v-flex>
    </v-layout>
    <v-layout row align-center justify-center>
      <v-flex xs12 md10 my-4>
        <div style="width: 100%">
          The map is based on geo-location data (i.e. IP addresses) of hashers connecting to the Bitcoin mining pools BTC.com, Poolin, and ViaBTC, who have kindly agreed to share aggregate-level data for research purposes. These pools collectively represent approximately 37% of Bitcoin total hashrate over the examined period.
          <sup @click="menu = true" style="text-decoration: underline; cursor: pointer">1</sup>
          <v-dialog v-model="menu" :max-width="600" offset-x>
            <v-card>
              <v-flex pa-4>
                BTC.com, Pool Stats, available at:
                <a target="_blank" href="https://btc.com/stats/pool?pool_mode=year">https://btc.com/stats/pool?pool_mode=year</a>
              </v-flex>
            </v-card>
          </v-dialog>
          Figures are presented in aggregate to obfuscate pool-specific information. Please visit the
          <nuxt-link to="/mining_map/methodology">
            Methodology
          </nuxt-link>
            tab for further information.
        </div>
      </v-flex>
    </v-layout>
    <v-layout row align-center justify-center>
      <v-flex>
        <div>
          Underlying data provided by:
        </div>
      </v-flex>
    </v-layout>
    <v-layout  row align-center justify-center>
      <v-flex ma-4>
        <swiper class="swiper" :options="swiperOption">
          <swiper-slide class="slide-1" :style="{width: containerWidth/5 + 'px'}">
            <a href="https://pool.btc.com" target="_blank" style="display: inline-block; width: 100%; height: 100%" />
          </swiper-slide>
          <swiper-slide class="slide-2" :style="{width: containerWidth/5 + 'px'}">
            <a href="https://www.poolin.com" target="_blank" style="display: inline-block; width: 100%; height: 100%" />
          </swiper-slide>
          <swiper-slide class="slide-3" :style="{width: containerWidth/5 + 'px'}">
            <a href="https://www.viabtc.com" target="_blank" style="display: inline-block; width: 100%; height: 100%" />
          </swiper-slide>
<!--          <div class="swiper-button-prev" slot="button-prev"></div>-->
<!--          <div class="swiper-button-next" slot="button-next"></div>-->
        </swiper>
      </v-flex>
    </v-layout>
<!--    <v-layout row align-center justify-center>-->
<!--      <v-flex mx-3>-->
<!--        <img src="~static/images/logo/photo_2020-04-20 17.37.34.jpeg" height="40">-->
<!--      </v-flex>-->
<!--      <v-flex mx-3>-->
<!--        <img src="~static/images/logo/photo_2020-04-20 17.37.40.jpeg" height="40">-->
<!--      </v-flex>-->
<!--      <v-flex mx-3>-->
<!--        <img src="~static/images/logo/photo_2020-04-20 17.37.43.jpeg" height="40">-->
<!--      </v-flex>-->
<!--    </v-layout>-->
  </v-layout>
</template>

<script>
import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
import 'swiper/css/swiper.css'

export default {
  name: 'index',
  layout: 'demo',
  components: {
    Swiper,
    SwiperSlide
  },
  async fetch ({ store }) {
  },
  data() {
    return {
      menu: false,
      swiperOption: {
        slidesPerView: 3,
        spaceBetween: 30,
        slidesPerGroup: 3,
        loop: false,
        loopFillGroupWithBlank: false,
        pagination: {
          el: '.swiper-pagination',
          clickable: true
        },
        navigation: {
          nextEl: '.swiper-button-next',
          prevEl: '.swiper-button-prev'
        }
      },
      containerWidth: null
    }
  },
  mounted() {
    if (!this.$store.getters.authenticated) {
      return this.$router.push('/login')
    }
    this.containerWidth = document.getElementById("wrap-container").getBoundingClientRect().width
  },
  watch() {

  }
}
</script>
