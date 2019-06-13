import Vue from 'vue'
import axios from 'axios'
import _ from 'lodash'

export const state = () => ({
  data: [],
  numbers: [],
  pue: 1.2,
  price: 0.066,
  countries: [],
  progress: true,
  progress2: true
})

export const getters = {
  GET_DATA: state => state.data,
  GET_NUMBERS: (state) => {
      return state.numbers.map(el => el * state.pue)
  },
  GET_PUE: state => state.pue,
  GET_PRICE: state => state.price,
  GET_COUNTRIES: state => state.countries
}

export const mutations = {
  SET_DATA(state, payload) { state.data = payload.data },
  SET_NUMBERS(state, [estimated, min, max]) { state.numbers = [estimated, min, max]},
  SET_PUE(state, payload) { state.pue = payload },
  SET_PRICE(state, payload) { state.price = payload },
  SET_COUNTRIES(state, payload) { state.countries = payload},
  SET_PROGRESS(state, payload) { state.progress = payload},
  SET_PROGRESS2(state, payload) { state.progress2 = payload},
}

export const actions = {

    LOAD_COUNTRIES: async ({ commit }) => {
        try {
            const res = await axios.get(`https://cbeci.org/api/countries`)
            await commit('SET_COUNTRIES', res.data.data)
        } catch (e) { alert(e) }
    },

    LOAD_DATA: async ({ commit }, price) => {
        try {
            await commit('SET_PROGRESS2', true)
            const res = await axios.get(`https://cbeci.org/api/data/${price}`)
            await commit('SET_DATA', res.data)
            await commit('SET_PROGRESS2', false)
        } catch (e) { alert(e) }
    },

    LOAD_NUMBERS: async ({ commit, state }, price) => {
        try {
            if (!price) price = state.price
            await commit('SET_PROGRESS', true)
            const [estimated, min, max] = await Promise.all([
                axios.get(`https://www.cbeci.org/api/guess/${price}`),
                axios.get(`https://www.cbeci.org/api/min/${price}`),
                axios.get(`https://www.cbeci.org/api/max/${price}`)
            ])
            await commit('SET_NUMBERS', [estimated.data, min.data, max.data])
            await commit('SET_PROGRESS', false)
        } catch (e) { alert(e) }
    },

    INITIALIZATION: ({ commit, dispatch, state }) => {
        if (!_.isEmpty(state.numbers)) return
        try {
            dispatch('LOAD_DATA', state.price)
            dispatch('LOAD_NUMBERS', state.price)
        } catch (e) { alert(e) }
    },

    UPDATE_DATA_AFTER_PRICE_CHANGE: ({ commit, dispatch }, price) => {
        try {
            commit('SET_PRICE', price)
            dispatch('LOAD_DATA', price)
            dispatch('LOAD_NUMBERS', price)
        } catch (e) {
            alert(e)
        }
    }
}
