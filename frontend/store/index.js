import Vue from 'vue'

export const state = () => ({
  data: [],
  numbers: [],
  pue: 1.2,
  price: 0.066,
})

export const getters = {
  GET_DATA: state => state.data,
  GET_NUMBERS: state => state.numbers,
  GET_PUE: state => state.pue,
  GET_PRICE: state => state.price

}

export const mutations = {
  SET_DATA(state, payload) { state.data = payload.data },
  SET_NUMBERS(state, [estimated, min, max]) { state.numbers = [estimated, min, max]},
  SET_PUE(state, payload) { state.pue = payload },
  SET_PRICE(state, payload) { state.price = payload },
}

export const actions = {
}
