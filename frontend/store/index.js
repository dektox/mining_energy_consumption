import Vue from 'vue'

export const state = () => ({
  data: [],
  numbers: [],
  pue: 1.2,
  price: 0.066,
  countries: [],
})

export const getters = {
  GET_DATA: state => state.data,
  GET_NUMBERS: state => state.numbers,
  GET_PUE: state => state.pue,
  GET_PRICE: state => state.price,
  GET_COUNTRIES: state => state.countries

}

export const mutations = {
  SET_DATA(state, payload) { state.data = payload.data },
  SET_NUMBERS(state, [estimated, min, max]) { state.numbers = [estimated, min, max]},
  SET_PUE(state, payload) { state.pue = payload },
  SET_PRICE(state, payload) { state.price = payload },
  SET_COUNTRIES(state, payload) { state.countries = payload}
}

export const actions = {
    nuxtServerInit ({ commit }, { req }) {
        commit('SET_NUMBERS', [2,3,4])
    }
}
