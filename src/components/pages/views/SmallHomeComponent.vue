<template>
  <div class="sm-light">
    <div class="sm-header-frame">
      <div class="sm-header-frame2">
        <div class="sm-header-frame3">
          <div class="sm-art-history">ART HISTORY</div>
        </div>
      </div>
    </div>
    <div class="sm-timeline-frame">
      <div class="sm-timeline-frame1">
        <div class="sm-timeline-frame2">
          <div class="sm-timeline-frame3">
            <v-list class="sm-timeline-content-list">
              <v-list-item
                v-for="era in data"
                :key="era.era"
                :picture="era.picture"
              >
              <router-link  :to="{ name: 'EraPage', params: { id: era.era }}">
                <div class="sm-timeline-era">{{ era.era }}</div>
                <img  class="sm-era-image" :src="era.picture" alt="Picture Frame"/></router-link>
              </v-list-item>
            </v-list>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "SmallHomeComponent",
  data() {
    return {
      data: [],
      loading: false,
      error: null, // To store error messages for display or debugging
    };
  },
  mounted() {
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
        this.data = Object.keys(data.TimeLine).map((key) => {
          const era = data.TimeLine[key];
          return {
            era: era.Era,
            years: era.Years,
            picture: era.Picture,
          };
        });
      }
    },
    selectedEra(eraId) {
      this.$router.push({ name: "EraPage", params: { id: eraId } });
      console.log("Selected Era:", era);
    },
  },
};
</script>

<style>

.sm-light {
  background-color: #fff;
  display: flex;
  max-width: 480px;
  min-width: 375px;
  width: 100%;
  flex-direction: column;
  margin: 0 auto;
  font-family: 'Times New Roman', Times, serif;
}
.sm-header-frame {
  background-color: #322c2c;
  display: flex;
  width: 100%;
  flex-direction: column;
  font-size: 58px;
  color: #322c2c;
  font-weight: 700;
  letter-spacing: -5.8px;
  line-height: 118%;
  justify-content: center;
  padding: 7px 12px;
}
.sm-header-frame2 {
  background-color: #fffafa;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 4px 7px;
}
.sm-header-frame3 {
  background-color: #322c2c;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 6px 13px;
}
.sm-art-history {
  font-family: 'Times New Roman', Times, serif;
  background-color: #fffafa;
  text-align: justify;
  font-size: 1.2em;
}
.sm-timeline-frame2 {
  background-color: #322c2c;
  display: flex;
  width: 100%;
  flex-direction: column;
  justify-content: center;
  padding: 0 12px;
}
.sm-timeline-frame3 {
  background-color: #fffafa;
  display: flex;
  flex-direction: column;
  padding: 7px 6px 0;
}
.sm-timeline-content-list {
  background-color: #322c2c;
  display: flex;
  flex-direction: column;
}
.sm-timeline-era {
  margin-top: 8px;
  margin-bottom: 8px;
  border-style: solid;
  background-color: #fffafa;
  color: #322c2c;
  padding: 8px;
  text-transform: uppercase;
  text-align: center;
  font-size: 35px;
  font-family: 'Times New Roman', Times, serif;
  font-weight: 700;
  font-size: calc(2vw + 2vh + 2vmin);
  overflow-y: hidden;
}
.sm-era-image {
  margin-top: 8px;
  display: flex;
  flex-direction: column;
  max-width: 412px;
  height: 500px;
  filter: grayscale(50%) brightness(90%) contrast(110%) saturate(10%);
  overflow: hidden;
}
img {
  width: auto;
  height: 100%;
  object-fit: cover;
  object-position: top;
  position: relative;
  aspect-ratio: 2;
 
}
a {
    text-decoration: none;
}
</style>
