export default function ({ isHMR, app, store, route, params, req, error, redirect }) {
    if (isHMR) { // ignore if called from hot module replacement
        return;
    }

    const Cookie = process.client ? require('js-cookie') : undefined
    let cookieControl = Cookie.get('CookieControl')
    if (cookieControl &&  JSON.parse(cookieControl).analytics === 'true') {
        store.commit('SET_COOK', true)
    }
}
