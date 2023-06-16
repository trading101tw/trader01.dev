import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import VueGtag from "vue-gtag";

//createApp(App).use(router).mount('#app')
createApp(App).use(router,VueGtag,{
  config: { id: 'G-7TGN654GDM' },
}
).mount('#app')
