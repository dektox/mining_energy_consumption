import Vue from 'vue'
import axios from 'axios'
import _ from 'lodash'
import Cookies from 'js-cookie'
const api = 'https://cbeci.org/api'

export const state = () => ({
  data: [],
  numbers: [0,0,0],
  price: 0.05,
  countries: [],
  progress: true,
  progress2: true,
  cooks: false
})

export const getters = {
  GET_DATA: state => state.data,
  GET_COUNTRIES: state => state.countries
}

export const mutations = {
  SET_DATA(state, payload) { state.data = payload.data },
  SET_NUMBERS(state, [estimated, min, max]) { state.numbers = [estimated, min, max]},
  SET_PRICE(state, payload) { state.price = payload },
  SET_COUNTRIES(state, payload) { state.countries = payload},
  SET_PROGRESS(state, payload) { state.progress = payload},
  SET_PROGRESS2(state, payload) { state.progress2 = payload},
  SET_COOK(state, payload) {
      state.cooks = payload
      if(payload) {
          Cookies.set('CookieControl', {analytics: 'true' }, {
              expires: 365
          });
      }
  },
}

export const actions = {

    LOAD_COUNTRIES: async ({ commit }) => {
        try {
            const res = await axios.get(`${api}/countries`)
            await commit('SET_COUNTRIES', res.data)
        } catch (e) { console.log(e) }
    },

    LOAD_DATA: async ({ commit }, price) => {
        try {
            const res = await axios.get(`${api}/data/${price}`)
            await commit('SET_DATA', res.data)
        } catch (e) { console.log(e) }
    },

    LOAD_NUMBERS: async ({ commit, state }, price) => {
        try {
            if (!price) price = state.price
            await commit('SET_PROGRESS', true)
            const [estimated, min, max] = await Promise.all([
                axios.get(`${api}/guess/${price}`),
                axios.get(`${api}/min/${price}`),
                axios.get(`${api}/max/${price}`)
            ])
            await commit('SET_NUMBERS', [estimated.data, min.data, max.data])
            await commit('SET_PROGRESS', false)
        } catch (e) { console.log(e) }
    },

    INITIALIZATION: async ({ commit, dispatch, state }) => {
        if (state.numbers[0] !== 0) return
        try {
            await commit('SET_PROGRESS2', true)
            await Promise.all([
                dispatch('LOAD_DATA', state.price),
                dispatch('LOAD_NUMBERS', state.price)
            ])
            await commit('SET_PROGRESS2', false)
        } catch (e) { console.log(e) }
    },

    UPDATE_DATA_AFTER_PRICE_CHANGE: ({ commit, dispatch }, price) => {
        try {
            commit('SET_PRICE', price)
            dispatch('LOAD_DATA', price)
            dispatch('LOAD_NUMBERS', price)
        } catch (e) {
            console.log(e)
        }
    }
}
