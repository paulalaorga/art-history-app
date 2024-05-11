<template>
  <v-app>
        <PeriodList />
        <FooterComponent />
  </v-app>
</template>

<script>
import FooterComponent from '@/components/FooterComponent.vue'
import PeriodList from './components/PeriodList.vue';


export default {
  name: 'App',
  components: {
    PeriodList,
    FooterComponent
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  background-color: #ECEBDF;
  margin-top: 60px;
} 
</style>
