
import {createApp} from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import '../jsmpeg.min'

// 适配flex

import axios from 'axios'
//让请求携带上浏览器的cookie
axios.defaults.withCredentials=false
Vue.prototype.$axios = axios
import installElementPlus from './plugins/element'
import './assets/css/icon.css'


const app = createApp(App)
installElementPlus(app)
app
    .use(store)
    .use(router)
    .mount('#app')