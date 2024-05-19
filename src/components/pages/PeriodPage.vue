<template>
    <div>
    <PeriodPageSmall v-if="isMobile" :id="selectedPeriodId" />   
    <PeriodPageDesktop v-else :id="selectedPeriodId" />
    </div>
</template>

<script>
import PeriodPageDesktop from "./views/PeriodPageDesktop.vue";
import PeriodPageSmall from "./views/PeriodPageSmall.vue";

export default {
  name: "PeriodPage",
  components: {
    PeriodPageDesktop,
    PeriodPageSmall
  },
  computed: {
    selectedPeriodId() {
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
