import { createApp } from 'vue'
import { createPinia } from 'pinia'

import './index.css'
import axios from './plugins/axios'

import App from './App.vue'
import router from './router'
import { useGenericStore } from './stores/genericStore'

const app = createApp(App)

app.use(createPinia())

// Register the store globally
const genericStore = useGenericStore()
app.config.globalProperties.$genericStore = genericStore

app.use(router)
app.use(axios)

app.mount('#app')

