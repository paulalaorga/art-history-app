<template>
  <body :class="{ 'dark-theme': darkMode }">
    <v-timeline v-if="!isSmallScreen" align="start">
      <v-timeline-item
        v-for="item in items"
        :key="item.id"
        :dot-color="'#333'"
      >
        <template v-slot:opposite>
          <div class="timeline-content">
            <span class="timeline-years">{{ item.years }}</span>
            <span :class="getFontClass(item.period)" class="timeline-period">{{
              item.period
            }}</span>
          </div>
        </template>
      </v-timeline-item>
    </v-timeline>

    <v-list v-else>
      <v-list-item
        v-for="item in items"
        :key="item.id"
        class="timeline-content-list"
        @mouseover="showPeriod(item.id)"
        @mouseleave="hidePeriod"
      >
        <span class="timeline-years">{{ item.years }}</span>
        <span
          :class="getFontClass(item.period)"
          v-if="visiblePeriod === item.id"
          class="timeline-period"
          >{{ item.period }}</span
        >
      </v-list-item>
    </v-list>
  </body>
</template>

<script>
export default {
  data: () => ({
    isSmallScreen: false,
    visiblePeriod: null,
    darkMode: window.matchMedia("(prefers-color-scheme: dark)").matches, // Initial dark mode state
    items: [
      {
        id: 1,
        years: "625 BC - AD 476",
        period: "Ancient Rome",
      },
      {
        id: 2,
        years: "476 - 1400 AD",
        period: "Medieval Art",
      },
      {
        id: 3,
        years: "1400 - 1600 AD",
        period: "Renaissance Art",
      },
      {
        id: 4,
        years: "1600 - 1800 AD",
        period: "Baroque Art",
      },
      {
        id: 5,
        years: "1800 - 1900 AD",
        period: "Romanticism",
      },
      {
        id: 6,
        years: "1900 - 1945 AD",
        period: "Modern Art",
      },
      {
        id: 7,
        years: "1945 - Present",
        period: "Contemporary Art",
      },
    ],
  }),
  created() {
    this.handleResize();
    window.addEventListener("resize", this.handleResize);
  },
  destroyed() {
    window.removeEventListener("resize", this.handleResize);
  },
  methods: {
    handleResize() {
      this.isSmallScreen = window.innerWidth < 600;
    },
    showPeriod(id) {
      this.visiblePeriod = id;
    },
    hidePeriod() {
      this.visiblePeriod = null;
    },
    getFontClass(period) {
      if (period.includes("Ancient Rome")) return "ancient-rome-font";
      if (period.includes("Medieval Art")) return "medieval-art-font";
      if (period.includes("Renaissance Art")) return "renaissance-art-font";
      if (period.includes("Baroque Art")) return "baroque-art-font";
      if (period.includes("Romanticism")) return "romanticism-font";
      if (period.includes("Modern Art")) return "modern-art-font";
      if (period.includes("Contemporary Art")) return "contemporary-art-font";
      return ""; // default font class
    },
    toggleDarkMode() {
      this.darkMode = !this.darkMode;
    },
    handleSystemThemeChange() {
      const themeMatcher = window.matchMedia('(prefers-color-scheme: dark)');
      themeMatcher.addEventListener('change', (e) => {
        this.darkMode = e.matches;
      });
  },
},
};
</script>

<style>
.ancient-rome-font {
  font-family: "Cinzel", serif;
}
.medieval-art-font {
  font-family: "Macondo Swash Caps", cursive;
}
.renaissance-art-font {
  font-family: "Monsieur La Doulaise";
  font-weight: 400;
  font-style: normal;
}
.baroque-art-font {
  font-family: "UnifrakturMaguntia", cursive;
}
.romanticism-font {
  font-family: "Snell Roundhand", cursive;
}
.modern-art-font {
  font-family: "Monoton";
}
.contemporary-art-font {
  font-family: "Silkscreen";
  font-size: x-large;
}

  .dark-theme {
    background-color: #515151;
  }
  .dark-theme .timeline-content,
  .dark-theme .timeline-content-list {
    border: 1px solid #fcfbfb;
    background-color: #333;
    color: #fdfcfc;
  }
  .dark-theme .timeline-years, 
  .dark-theme .timeline-period {
    color: #fdfcfc;
  }


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

.timeline-content:hover
.timeline-years {
  display: none;
}

.timeline-content:hover 
.timeline-period {
  font-size: xxx-large;
}

.timeline-years {
  font-weight: bold; /* Make the years bold to stand out */
  color: #555; /* Dark grey for better readability */
  margin-bottom: 4px; /* Add some space between the years and the period name */
  display: flex;
}

.timeline-period {
  color: #333; /* Slightly darker text for contrast */
  font-size: x-large;
}

.timeline-content-list:hover .timeline-period {
  display: block; /* Show on hover */
}
.timeline-content-list:hover .timeline-years {
  display: none; /* Show on hover */
}

.timeline-content-list {
  border: 1px solid #333;
  padding: 10px;
  margin-bottom: 10px;
  background-color: #8b2727;
  align-items: center;
  display: flex;
  flex-direction: column;
}

.timeline-content-list .timeline-years {
  color: #fff; /* White text for better visibility */
  font-size: large;
}

.timeline-content-list .timeline-period {
  display: none; /* Hide by default */
  color: #fff; /* White text for better visibility */
  font-size: xxx-large;
}
</style>
