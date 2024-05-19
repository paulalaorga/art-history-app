import { createRouter, createWebHashHistory } from 'vue-router';
import HomePage from '../components/pages/HomePage.vue';
import EraPage from '../components/pages/EraPage.vue';
import PeriodPage from '../components/pages/PeriodPage.vue';


const routes = [
  { path: '/', component: HomePage, name: 'Home'},
  { path: '/era/:id', component: EraPage, props: true, name: 'EraPage'},
  { path: '/period/:id', component: PeriodPage, props: true, name: 'PeriodPage'}

];

const router = createRouter({
  history: createWebHashHistory(),  // Use the HTML5 History API
  routes                        // Short for `routes: routes`
});

export default router;