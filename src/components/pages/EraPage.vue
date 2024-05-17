<template>
  <div class="era-page-desktop">
    <div class="header">
      <div class="h-frame1"></div>
      <div class="h-frame2"></div>
      <div class="h-frame3"></div>
      <div class="h-frame4"></div>
      <b class="art-history">ART HISTORY</b>
    </div>
    <div class="timeline-frame">
      <div class="timeline-frame1"></div>
      <div class="timeline-frame2"></div>
      <div class="timeline-frame3">
        <div v-if="foundEra" class="era-title">
                {{ foundEra.era }}
        </div>
        <v-timeline v-if="foundEra" side="start" line-color="white" line-thickness="8px">
          <v-timeline-item
            v-for="period in foundEra.periods"
            :key="period.period"
            dot-color="white"
            :years="period.years"
            @mouseover="showPicture(period.picture)"
            @mouseleave="hidePicture"
          >
          <router-link  :to="{ name: 'PeriodPage', params: { id: period.period }}">
            <div class="timeline-content">
              <h2>
                {{ period.period }}
              </h2>
            </div>
            </router-link>
            <template v-slot:opposite>
<!--               <router-link  :to="{ name: 'PeriodPage', params: { id: period.period }}">
 -->              <div class="timeline-content">
              <h3>
                {{ period.years }}
              </h3>
            </div>
            </template>
          </v-timeline-item>
        </v-timeline>
    </div>
  </div>
  <div class="picture-frame" v-if="currentPicture">
      <img :src="currentPicture" alt="Picture Frame" />
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
      currentPicture: null,
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
},
showPicture(pictureUrl) {
      this.currentPicture = pictureUrl;
    },
    hidePicture() {
      this.currentPicture = null;
    },
}
};


</script>

<style>
.era-page-desktop {
  width: 100%;
  position: relative;
  background-color: #fff;
  height: 832px;
  overflow: hidden;
  text-align: left;
  font-size: 40px;
  color: #322c2c;
  margin: 0;
  font-family: 'Times New Roman', Times, serif;
}
.header {
  position: absolute;
  top: 13px;
  left: 7px;
  width: 621px;
  height: 329px;
  flex: 1;
}
.h-frame1 {
  position: absolute;
  top: 0px;
  left: 0px;
  background-color: #322c2c;
  width: 100%;
  height: 100%;
}
.h-frame2 {
  position: absolute;
  top: calc(50% - 152.2px);
  left: 11px;
  background-color: #fffafa;
  width: 596.8px;
  height: 305.7px;
}
.h-frame3 {
  position: absolute;
  top: 21.77px;
  left: 20.17px;
  background-color: #322c2c;
  width: 579.4px;
  height: 285.8px;
}
.h-frame4 {
  position: absolute;
  top: calc(50% - 132.5px);
  left: 31px;
  background-color: #fffafa;
  width: 557px;
  height: 263px;
}
.art-history {
  position: absolute;
  top: 23px;
  left: 31px;
  letter-spacing: 0.03em;
  line-height: 117.77%;
  display: inline-block;
  width: 70%;
  height: auto;
  font-size: 118px;
}

.timeline-frame {
  position: absolute;
  top: 0px;
  left: 638px;
  width: 100vw;
  height: 832px;
  justify-content: space-around;
  display: flex;
  flex-direction: column;
}
.timeline-frame1 {
  position: absolute;
  top: 0px;
  left: 0px;
  background-color: #322c2c;
  width: 100vw;
  height: 100vw;
  margin: 12px;
}
.timeline-frame2 {
  position: absolute;
  top: 24px;
  left: 24px;
  right: 24px;
  background-color: #fffafa;
  width: 100vw;
  height: 805px;
}
.timeline-frame3 {
  position: absolute;
  top: 34px;
  left: 34px;
  right: 34px;
  background-color: #322c2c;
  width: 52vw;
  height: 782px;
  font-size: 40px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: left;
}


a {
    text-decoration: none;
}

 .era-title {
  margin-top: 8px;
  display: flex;
  justify-content: center;
  padding: 31px 34px;
  text-align: center;
  padding: 8px 16px 8px 16px;
  text-transform: uppercase;
  font-family: 'Times New Roman', Times, serif;
  font-weight: 700;
  font-size: xxx-large;
  border-width: 8px;
  background-color: #fffafa;
  color: #322c2c;
  box-sizing: border-box;
  margin-bottom: 8px;
}

.timeline-content h2 {
  justify-content: start;
  text-align: center;
  padding: 8px 16px 8px 16px;
  text-transform: uppercase;
  font-family: 'Times New Roman', Times, serif;
  font-weight: 700;
  font-size: xx-large;
  border-width: 8px;
  background-color: #fffafa;
  color: #322c2c;
  padding: 8px 16px 8px 16px;
  width: 323px; 
  height: 70px; 
  justify-content: left;
} 
.timeline-content h3 {
  justify-content: flex-start;
  text-align: justify;
  padding: 8px 16px 8px 16px;
  text-transform: capitalize;
  font-family: 'Times New Roman', Times, serif;
  font-weight: 500;
  font-size: x-large;
  border-width: 8px;
  color: #fffafa;
  padding: 8px 16px 8px 16px;
}


.picture-frame {
  position: absolute;
  left: 115px;
  right: 0;
  bottom: 24px;
  height: 448px;
  width: 384px;
  display: flex;
  border: 8px solid #322c2c;
  align-items: center;
  filter: grayscale(50%) brightness(90%) contrast(110%) saturate(10%);
}
.picture-frame img {
  width: 100%;
  height: 100%;
  object-fit: cover; /* Ensures the image covers the frame */
  object-position: top;
  /* Adjust the values to achieve the desired effect */
}
</style>
