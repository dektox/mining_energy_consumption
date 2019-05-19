import Vue from 'vue'

export const state = () => ({
  data: [],
  numbers: []
})

export const getters = {
  GET_DATA: state => state.data,
  GET_NUMBERS: state => state.numbers
}

export const mutations = {
  SET_DATA(state, payload) { state.data = payload.data },
  SET_NUMBERS(state, [estimated, min, max]) { state.numbers = [estimated, min, max]}
}

export const actions = {
}
