<template>
  <v-app>
    <v-card>
      <v-card-text>
        <h1>Art History App</h1>
        <PeriodList />
      </v-card-text>
      <v-card-actions>
        <FooterComponent />
      </v-card-actions>
    </v-card>
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
/*   color: #8B2727; */
  background-color: #ECEBDF;
  margin-top: 60px;
} 
</style>
