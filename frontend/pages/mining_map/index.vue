<template>
  <v-layout column justify-center align-center id="wrap-container">
    <v-flex xs12 md10 my-4>
      <h1 class="display-4 text-xs-center">Bitcoin Mining Map</h1>
    </v-flex>
    <v-layout row align-center justify-center>
      <v-flex xs12 md10 my-4>
        <div style="width: 100%">
          The Bitcoin Mining Map developed by the Cambridge Centre for Alternative Finance (CCAF) presents the geographic distribution of Bitcoin hashrate for the period ending April 2019 - April 2020. This geographic map displays the share of Bitcoin’s average monthly hashrate per country and per Chinese provinces.
        </div>
      </v-flex>
    </v-layout>
    <v-layout row align-center>
      <v-flex>
        <iframe :width="containerWidth / 12 * 10" :height="containerWidth / 32 * 15" src="https://app.powerbi.com/view?r=eyJrIjoiNDMyY2FlOTgtYTU3Mi00Y2RmLWI5MGItZGE1YjliMWJmOGQyIiwidCI6IjAwYzliM2IxLTAzMTItNGMzMy1hZTdmLTgwZjNhNzU5ZGVjMSIsImMiOjh9" frameborder="0" allowFullScreen="true" />
      </v-flex>
    </v-layout>
    <v-layout row align-center justify-center>
      <v-flex xs12 md10 my-4>
        <div style="width: 100%">
          The underlying data was kindly provided by the following Bitcoin mining pools: BTC.com, Poolin, and ViaBTC, who agreed to share country-level and province-level information based on the geo-location of hashers connecting to their pool. All figures are presented at the aggregate level to prevent from singling out a mining pool’s information.
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
  components: {
    Swiper,
    SwiperSlide
  },
  async fetch ({ store }) {
  },
  data() {
    return {
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
    this.containerWidth = document.getElementById("wrap-container").getBoundingClientRect().width
  },
  watch() {

  }
}
</script>
