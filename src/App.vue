<template>
  <v-app>
     <DesktopHomeComponent />
  </v-app>
</template>

<script>
import DesktopHomeComponent from './components/DesktopHomeComponent.vue';

export default {
  name: 'App',
  components: {
    DesktopHomeComponent
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
