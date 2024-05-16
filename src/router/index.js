import { createRouter, createWebHistory } from 'vue-router';
import HomeComponent from '../components/HomeComponent.vue';
import EraPage from '../components/pages/EraPage.vue';


const routes = [
  { path: '/', component: HomeComponent, name: 'Home'},
  { path: '/era/:id', component: EraPage, props: true, name: 'EraPage'}

];

const router = createRouter({
  history: createWebHistory(),  // Use the HTML5 History API
  routes                        // Short for `routes: routes`
});

export default router;