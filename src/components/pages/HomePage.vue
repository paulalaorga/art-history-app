<template>
    <div>
      <component :is="currentComponent" />
    </div>
  </template>
  
  <script>
  import HomePageSmall from "./views/HomePageSmall.vue";
  import HomePageDesktop from "./views/HomePageDesktop.vue";
  
  export default {
    name: "HomeComponent",
    components: {
      HomePageDesktop,
      HomePageSmall,
    },
    data() {
      return {
        isMobile: false,
      };
    },
    computed: {
      currentComponent() {
        return this.isMobile ? "HomePageSmall" : "HomePageDesktop";
      },
    },
    created() {
      this.checkWindowSize();
      window.addEventListener("resize", this.checkWindowSize);
    },
    beforeDestroy() {
      window.removeEventListener("resize", this.checkWindowSize);
    },
    methods: {
      checkWindowSize() {
        this.isMobile = window.innerWidth <= 768; // You can adjust the breakpoint as needed
      },
    },
  };
  </script>

  <style>

</style>