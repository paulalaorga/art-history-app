<template>
  <div class="era-page-desktop">
    <div v-if="foundEra" class="era-content">
      <div class="era-title">
        {{ foundEra.era }}
      </div>
      <v-list class="era-content-list">
        <v-list-item 
        v-for="period in foundEra.periods" :key="period.period">
          <div class="era-period">
            {{ period.period }}
          </div>
          <div class="era-period-image">
            <img :src="period.picture" alt="Picture Frame" />
          </div>
        </v-list-item>
      </v-list>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "EraPage",
  components: {
  },
  props: ["id"],
  data() {
    return {
      foundEra: null,
      loading: false,
      error: null, // To store error messages for display or debugging
    };
  },
  mounted() {
    console.log("Era ID:", this.id);
    this.fetchData();
  },
  methods: {
    async fetchData() {
      this.loading = true;
      const url = "https://art-database.onrender.com/data.json"; // Endpoint URL
      try {
        const response = await axios.get(url);
        console.log("Data received:", response.data); // Log the raw data from the server
        this.processData(response.data);
      } catch (error) {
        console.error("Error fetching data:", error);
        this.error = "Failed to fetch data. See console for details."; // Update the error message for the UI
      } finally {
        this.loading = false; // Ensure loading is always turned off after the fetch operation
      }
    },
    processData(data) {
      if (data && data.TimeLine) {
        const foundEra = Object.values(data.TimeLine).find(era => era.Era === this.id);
        console.log("Found Era:", foundEra); // Log the found era
        if (foundEra) {
          if (typeof foundEra.Periods === "object") {
            this.foundEra = {
            era: foundEra.Era,
            periods: Object.values(foundEra.Periods).map(period => ({
              period: period.Period,
              years: period.Years,
              picture: period.Picture,
              works: period.Works
              })),
            };
          };
          console.log("Processed Era Data:", foundEra); // Log the processed data
    } else {
      console.log("Era not found");
    }
  } else {
    console.log("Invalid data format");
}
}
}
};


</script>

<style scoped>
.era-page-desktop {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.era-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
}

.era-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
}

.era-content-list {
  width: 100%;
}

.era-period {
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 10px;
}

.era-period-image {
  margin-bottom: 20px;
}

.era-period-image img {
  width: 100%;
  max-width: 600px;
  height: auto;
}


</style>