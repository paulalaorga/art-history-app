import { createRouter, createWebHistory } from 'vue-router';
import HomeComponent from '../components/HomeComponent.vue';

const routes = [
  { path: '/', component: HomeComponent },
];

const router = createRouter({
  history: createWebHistory(),  // Use the HTML5 History API
  routes                        // Short for `routes: routes`
});
