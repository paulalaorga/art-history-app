<template>
    <div>
     <SmallHomeComponent />
    </div>
  </template>
  
  <script>
  import SmallHomeComponent from "./views/SmallHomeComponent.vue";
  
  export default {
    name: "HomeComponent",
    components: {
      SmallHomeComponent,
    },
    data() {
      return {
        isMobile: false,
      };
    },
    computed: {
      currentComponent() {
        return this.isMobile ? "SmallHomeComponent" : "DesktopHomeComponent";
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