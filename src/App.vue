<template>
  <v-app>
    <SmallHomeComponent/>
  </v-app>
</template>

<script>
import SmallHomeComponent from "./components/views/SmallHomeComponent.vue";

export default {
  name: "App",
  components: {
    SmallHomeComponent,
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