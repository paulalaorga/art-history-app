import { createApp } from "vue";
import App from "./App.vue";
import router from "./router/index.js"; // Asegúrate de que tienes un index.js en tu carpeta de router

// Importa los estilos globales
import "./global.css"; // Asegúrate de que la ruta es correcta

// Vuetify
import "vuetify/styles"; // Asegúrate de que has instalado Vuetify correctamente
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";

// Crea la instancia de Vuetify
const vuetify = createVuetify({ components, directives });

// Crea y monta la aplicación Vue
const app = createApp(App);
app.use(vuetify);
app.use(router);
app.mount("#app");
