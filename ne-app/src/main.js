import Vue from 'vue'
import App from './App.vue'
import router from './router'
<<<<<<< HEAD
import axios from './plugins/axios'
import vuetify from './plugins/vuetify'
import VueAxios from './plugins/axios'
Vue.use(VueAxios, axios)
Vue.config.productionTip = false

=======
import vuetify from './plugins/vuetify';

Vue.config.productionTip = false
>>>>>>> a96517be5f9a608192f6efc6fc960457dc596edd

new Vue({
  router,
  vuetify,
  render: h => h(App)
<<<<<<< HEAD
}).$mount('#app')
=======
}).$mount('#app')
>>>>>>> a96517be5f9a608192f6efc6fc960457dc596edd
