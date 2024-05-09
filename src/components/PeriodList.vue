<template>
  <div>
    <v-timeline v-if="!isSmallScreen" align="start">
      <v-timeline-item
          v-for="item in items"
          :key="item.id"
          :dot-color="'#8B2727'"
      >
        <template v-slot:opposite>
        <div class="timeline-content">
          <span class="timeline-years">{{ item.years }}</span>
          <span class="text-h6 timeline-period">{{ item.period }}</span>
        </div>
        </template>
      </v-timeline-item>
    </v-timeline>

    <v-list v-else>
      <v-list-item
          v-for="item in items"
          :key="item.id"
      >
        <v-list-item class="timeline-content">
          <span class="timeline-years">{{ item.years }}</span>
          <span class="text-h6 timeline-period">{{ item.period }}</span>
        </v-list-item>
      </v-list-item>
    </v-list>
  </div>
</template>
  
  <script>
  export default {
    data: () => ({
      isSmallScreen: false,
      items: [
        {
          id: 1,
          years: "625 BC - AD 476",
          period: "Ancient Rome"
        },
        {
          id: 2,
          years: "476 - 1400 AD",
          period: "Medieval Art"
        },
        {
          id: 3,
          years: "1400 - 1600 AD",
          period: "Renaissance Art"
        },
        {
          id: 4,
          years: "1600 - 1800 AD",
          period: "Baroque Art"
        },
        {
          id: 5,
          years: "1800 - 1900 AD",
          period: "Romanticism"
        },
        {
          id: 6,
          years: "1900 - 1945 AD",
          period: "Modern Art"
        },
        {
          id: 7,
          years: "1945 - Present",
          period: "Contemporary Art"
        },
      ],
    }),
    created() {
    this.handleResize();
    window.addEventListener('resize', this.handleResize);
  },
  destroyed() {
    window.removeEventListener('resize', this.handleResize);
  },
  methods: {
    handleResize() {
      this.isSmallScreen = window.innerWidth < 600;
    }
  }
}
  </script>
  
  <style>
.timeline-content {
  width: 500px; /* Adjust this value based on your layout needs */
  max-width: 100%;
  border: 1px solid #333;
  padding: 10px;
  box-sizing: border-box;
  align-items: center;
  display: flex;
  flex-direction: column;
}

.timeline-years {
  font-weight: bold; /* Make the years bold to stand out */
  color: #555; /* Dark grey for better readability */
  margin-bottom: 4px; /* Add some space between the years and the period name */
  display: flex;

}

.timeline-period {
  color: #333; /* Slightly darker text for contrast */
}
</style>