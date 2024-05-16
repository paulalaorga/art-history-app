<template>
    <div>
      <component :is="currentComponent" />
    </div>
  </template>
  
  <script>
  import SmallHomeComponent from "./views/SmallHomeComponent.vue";
  import DesktopHomeComponent from "./views/DesktopHomeComponent.vue";
  
  export default {
    name: "HomeComponent",
    components: {
      SmallHomeComponent,
      DesktopHomeComponent,
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