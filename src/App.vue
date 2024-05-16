<template>
  <v-app>
    <SmallHomeComponent />
  </v-app>
</template>

<script>
import SmallHomeComponent from "./components/SmallHomeComponent.vue";

export default {
  name: "App",
  components: {
    SmallHomeComponent,
  },
};
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
