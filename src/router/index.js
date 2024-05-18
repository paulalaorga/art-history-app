import { createRouter, createWebHistory } from 'vue-router';
import HomeComponent from '../components/pages/HomeComponent.vue';
import EraPage from '../components/pages/EraPage.vue';
import PeriodPage from '../components/pages/PeriodPage.vue';


const routes = [
  { path: '/', component: HomeComponent, name: 'Home'},
  { path: '/era/:id', component: EraPage, props: true, name: 'EraPage'},
  { path: '/period/:id', component: PeriodPage, props: true, name: 'PeriodPage'}

];

const router = createRouter({
  history: createWebHashHistory(),  // Use the HTML5 History API
  routes                        // Short for `routes: routes`
});

export default router;