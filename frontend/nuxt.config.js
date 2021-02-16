require('dotenv').config()
import VuetifyLoaderPlugin from 'vuetify-loader/lib/plugin'
import pkg from './package'
import shrinkRay from 'shrink-ray-current'

export default {
  mode: 'universal',

  /*
  ** Headers of the page
  */
  head: {
    title: 'Cambridge Bitcoin Electricity Consumption Index (CBECI)',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: pkg.description },
      { hid: 'keywords', name: 'keywords', content: 'Bitcoin, Cryptocurrency, Electricity, Energy, Mining, Efficiency, PoW, ASIC, Proof-of-work, Environmental, Blockchain, Index' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      {
        rel: 'stylesheet',
        href:
          'https://fonts.googleapis.com/css?family=Exo+2:300,400,500,700|Material+Icons'
      },
      {
          rel: 'stylesheet',
          href:
              'https://fonts.googleapis.com/css?family=Open+Sans:300,400,500,700|Material+Icons'
      },
      {
          rel: 'stylesheet',
          href:
              'https://fonts.googleapis.com/css?family=Sorts+Mill+Goudy&display=swap'
      }
    ]
  },

  /*
  ** Customize the progress-bar color
  */
  // loading: '~/components/loading.vue',

  /*
  ** Global CSS
  */
  css: [
    '~/assets/style/app.styl',
    '~/assets/style/base.scss',
    'katex/dist/katex.min.css'
],

  /*
  ** Plugins to load before mounting the App
  */
  plugins: [
    '@/plugins/vuetify',
    { src: '~plugins/ga.js', ssr: false },
    { src: '~plugins/katex2js.js', ssr: false },
  ],

  server: {
      port: process.env.PORT || 7776, // default: 3000
  },
  /*
  ** Nuxt.js dev-modules
  */
  buildModules: [
    // Doc: https://github.com/nuxt-community/eslint-module
    '@nuxtjs/dotenv'
  ],
  /*
  ** Nuxt.js modules
  */
  modules: [
    '@nuxtjs/axios',
    '@nuxtjs/robots',
    'cookie-universal-nuxt',
    '@nuxtjs/dotenv'
  ],
  robots: {
      UserAgent: '*',
      Allow: '/'
  },
  render: {
      compressor: shrinkRay()
  },
  axios: {
    proxyHeaders: false,
    credentials: false,
    baseURL: 'https://cbeci.org/api'
  },
  /*
  ** Build configuration
  */
  build: {
    transpile: ['vuetify/lib'],
    plugins: [new VuetifyLoaderPlugin()],
    loaders: {
      stylus: {
        import: ['~assets/style/variables.styl']
      }
    },
    /*
    ** You can extend webpack config here
    */
    extend(config, ctx) {
    }
  }
}
