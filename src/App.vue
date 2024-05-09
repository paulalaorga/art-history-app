<template>
  <v-app>
    <v-card :dark="isDarkTheme">
      <v-card-title>
        <HeaderComponent />
      </v-card-title>
      <v-card-text>
       
        <h1>Welcome to Your Art History App</h1>
        <PeriodList />
      </v-card-text>
      <v-card-actions>
        <FooterComponent />
      </v-card-actions>
    </v-card>
  </v-app>
</template>

<script>
import HeaderComponent from '@/components/HeaderComponent.vue'
import FooterComponent from '@/components/FooterComponent.vue'
import PeriodList from './components/PeriodList.vue';


export default {
  name: 'App',
  components: {
    HeaderComponent,
    PeriodList,
    FooterComponent
  },
  data() {
    return {
      isDarkTheme: false
    };
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
