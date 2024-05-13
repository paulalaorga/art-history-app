<template>
  <v-app>
     <HomeViewComponent />
  </v-app>
</template>

<script>
import HomeViewComponent from './components/HeaderComponent.vue';

export default {
  name: 'App',
  components: {
    HomeViewComponent
  },
}
</script>

<style>
/* #app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  background-color: #ECEBDF;
  margin-top: 60px;
}  */
</style>
