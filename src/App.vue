<template>
  <v-app>
    <HomeComponent />
  </v-app>
</template>

<script>
import HomeComponent from './components/HomeComponent.vue';

export default {
  name: "App",
  components: {
    HomeComponent,
  },
};
</script>

<style>
#app {
  font-family: 'Times New Roman', Times, serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>