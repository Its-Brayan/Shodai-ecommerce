
 import '@mdi/font/css/materialdesignicons.css';
import { VDateInput } from 'vuetify/labs/VDateInput'
 import { VFileUpload } from 'vuetify/labs/VFileUpload'
import { createApp } from 'vue'

import { createPinia } from 'pinia'
import { createRulesPlugin } from 'vuetify/labs/rules'
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import router from './router'
import { AuthStore } from './stores/authstore'


import App from './App.vue'


const app = createApp(App)
const vuetify = createVuetify({
  components:{
    ...components,
    VFileUpload, // Registering the VFileUpload component
    VDateInput,
  },
 
  directives,
   plugins: {
    rules: createRulesPlugin(),
  },
})

app.use(createPinia())
// app.use(createRulesPlugin({ /* options */ }, vuetify.locale))
app.use(router)

app.use(vuetify)
const authStore = AuthStore()
authStore.initializeAuth()


app.mount('#app')
