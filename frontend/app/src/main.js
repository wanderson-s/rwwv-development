import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import VCalendar from 'v-calendar'
import VueScrollTo  from 'vue-scrollto';

import '@fortawesome/fontawesome-free/js/all'

const app = createApp(App);
app.use(VCalendar, {
    locales: {
        'pt-BR': {
        firstDayOfWeek: 1,
        masks: {
          L: 'DD-MM-YYYY',
        }
      } 
    }
  });
app.use(VueScrollTo)
app.use(router).mount('#app')
