<template>
  <div>
    <!-- Pass the id prop to EraPageSmall component -->
    <EraPageSmall v-if="isMobile" :id="selectedEraId" />
    <!-- Or pass the id prop to EraPageDesktop component -->
    <EraPageDesktop v-else :id="selectedEraId" />
  </div>
</template>

<script>
import EraPageSmall from "./views/EraPageSmall.vue";
import EraPageDesktop from "./views/EraPageDesktop.vue";

export default {
  name: "EraPage",
  components: {
    EraPageSmall,
    EraPageDesktop,
  },
  computed: {
    selectedEraId() {
      return this.$route.params.id;
    },
    isMobile() {
      return window.innerWidth <= 768; // You can adjust the breakpoint as needed
    },
  },
  mounted() {
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
/* Add your styles here if needed */
</style>
