<template>
  <v-app>
    <component :is="currentComponent" />
  </v-app>
</template>

<script>
import SmallHomeComponent from "./components/SmallHomeComponent.vue";
import DesktopHomeComponent from "./components/DesktopHomeComponent.vue";

export default {
  name: "App",
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
