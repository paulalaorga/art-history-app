<template>
  <div class="sm-light">
    <div class="header-frame">
      <div class="header-frame2">
        <div class="header-frame3">
          <div class="art-history">ART HISTORY</div>
        </div>
      </div>
    </div>
    <div class="timeline-frame">
      <div class="timeline-frame1">
        <div class="timeline-frame2">
          <div class="timeline-frame3">
            <v-list class="timeline-content-list">
              <v-list-item
                v-for="era in data"
                :key="era.era"
                :picture="era.picture"
              >
                <div class="timeline-period">
                  {{ era.era }}
                </div>
                <div class="period-image">
                  <img :src="era.picture" alt="Picture Frame" />
                </div>
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
  },
};
</script>

<style scoped>
.sm-light {
  background-color: #fff;
  display: flex;
  max-width: 480px;
  width: 100%;
  flex-direction: column;
  margin: 0 auto;
  font-family: 'Times New Roman', Times, serif;
}
.header-frame {
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
.header-frame2 {
  background-color: #fffafa;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 4px 7px;
}
.header-frame3 {
  background-color: #322c2c;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 6px 13px;
}
.art-history {
  font-family: 'Times New Roman', Times, serif;
  background-color: #fffafa;
  text-align: justify;
  font-size: 1.2em;
}
.timeline-frame2 {
  background-color: #322c2c;
  display: flex;
  width: 100%;
  flex-direction: column;
  justify-content: center;
  padding: 0 12px;
}
.timeline-frame3 {
  background-color: #fffafa;
  display: flex;
  flex-direction: column;
  padding: 7px 6px 0;
}
.timeline-content-list {
  background-color: #322c2c;
  display: flex;
  flex-direction: column;
}
.timeline-period {
  border-style: solid;
  border-width: 8px;
  background-color: #fffafa;
  color: #322c2c;
  padding: 8px 16px 8px 16px;
  text-transform: uppercase;
  text-align: center;
  font-size: 35px;
  font-family: 'Times New Roman', Times, serif;
  font-weight: 700;
  font-size: calc(2vw + 2vh + 2vmin);
}
.period-image {
  padding-top: 8px;
  display: flex;
  flex-direction: column;
  align-items: top;
  justify-content: top;
  width: 412px;
  height: 300px;
  filter: grayscale(50%) brightness(90%) contrast(110%) saturate(10%);
  overflow: hidden;
  aspect-ratio: 1;
}
.img {
  width: 100%;
  height: 100%;
  object-fit: auto;
  object-position: top;
  position: relative;
  aspect-ratio: 2;
}
</style>
