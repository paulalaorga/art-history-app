import { createApp } from 'vue';
import App from './App.vue';
import router from './router/index.js';  // Ensure you have an index.js in your router directory

// Vuetify
import 'vuetify/styles';  // Ensure you have installed Vuetify properly
import { createVuetify } from 'vuetify';
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';


// Create Vuetify instance
const vuetify = createVuetify({ components, directives });


// Create and mount the Vue application
const app = createApp(App);
app.use(vuetify);
app.use(router);
app.mount('#app');
