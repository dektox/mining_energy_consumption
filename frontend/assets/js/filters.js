
const percentage = num => num + ' %'

const decimals = num => num ? num.toFixed(2) : num

const one_dec = num => num ? num.toFixed(1) : num

const round = num => num ? Math.round(num) : num

export { percentage, decimals, one_dec, round }
