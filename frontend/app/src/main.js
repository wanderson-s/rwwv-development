import Vue from 'vue'
import App from './App.vue'
import router from './router'
// Bootstrap
import BootstrapVue from 'bootstrap-vue'
import BootstrapVueIcons from 'bootstrap-vue'
import IconsPlugin from 'bootstrap-vue'
import BIcon from 'bootstrap-vue'
import BIconArrowUp from 'bootstrap-vue'
import BIconArrowDown from 'bootstrap-vue'
import FormCheckboxPlugin from 'bootstrap-vue'
import BFormCheckboxGroup from 'bootstrap-vue'

// Import Bootstrap an BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'bootstrap-vue/dist/bootstrap-vue-icons.min.css'
// Request HTTP
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.config.productionTip = false
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(BootstrapVueIcons)
Vue.use(FormCheckboxPlugin)
Vue.use(VueAxios, axios)

Vue.component('BIcon', BIcon)
Vue.component('BIconArrowUp', BIconArrowUp)
Vue.component('BIconArrowDown', BIconArrowDown)
Vue.component('b-form-checkbox-group', BFormCheckboxGroup)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
