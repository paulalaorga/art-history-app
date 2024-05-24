<template>
  <div class="hp-desktop-light">
    <div class="hp-header">
      <div class="hp-h-frame1"></div>
      <div class="hp-h-frame2"></div>
      <div class="hp-h-frame3"></div>
      <div class="hp-h-frame4"></div>
      <b class="hp-art-history">ART HISTORY</b>
    </div>
    <div class="hp-timeline-frame">
      <div class="hp-timeline-frame1"></div>
      <div class="hp-timeline-frame2"></div>
      <div class="hp-timeline-frame3">
        <v-timeline side="start" line-color="white" line-thickness="8px">
          <v-timeline-item
            v-for="era in data"
            :key="era.era"
            dot-color="white"
            :years="era.years"
            @mouseover="showPicture(era.picture)"
            @mouseleave="hidePicture"
          >
          <router-link  :to="{ name: 'EraPage', params: { id: era.era }}">
            <div class="hp-timeline-content">
              <h2>
                {{ era.era }}
              </h2>
            </div>
            </router-link>
            <template v-slot:opposite>
              <router-link  :to="{ name: 'EraPage', params: { id: era.era }}">
              <div class="hp-timeline-content">
              <h3>
                {{ era.years }}
              </h3>
            </div>
            </router-link>
            </template>
          </v-timeline-item>
        </v-timeline>
      </div>
    </div>
    <div class="hp-picture-frame" v-if="currentPicture">
      <img :src="currentPicture" alt="Picture Frame" />
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "HomePageDesktop",
  data() {
    return {
      data: [],
      loading: false,
      error: null, // To store error messages for display or debugging
      currentPicture: null,
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
        this.processData(response.data);
      } catch (error) {
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
    showPicture(pictureUrl) {
      this.currentPicture = pictureUrl;
    },
    hidePicture() {
      this.currentPicture = null;
    },
  },
};
</script>

<style scoped>
.hp-desktop-light {
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
.hp-header {
  position: absolute;
  top: 13px;
  left: 7px;
  width: 621px;
  height: 329px;
  flex: 1;
}
.hp-h-frame1 {
  position: absolute;
  top: 0px;
  left: 0px;
  background-color: #322c2c;
  width: 100%;
  height: 100%;
}
.hp-h-frame2 {
  position: absolute;
  top: calc(50% - 152.2px);
  left: 11px;
  background-color: #fffafa;
  width: 596.8px;
  height: 305.7px;
}
.hp-h-frame3 {
  position: absolute;
  top: 21.77px;
  left: 20.17px;
  background-color: #322c2c;
  width: 579.4px;
  height: 285.8px;
}
.hp-h-frame4 {
  position: absolute;
  top: calc(50% - 132.5px);
  left: 31px;
  background-color: #fffafa;
  width: 557px;
  height: 263px;
}
.hp-art-history {
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

.hp-timeline-frame {
  position: absolute;
  top: 0px;
  left: 638px;
  width: 100vw;
  height: 832px;
  justify-content: space-around;
  display: flex;
  flex-direction: column;
}
.hp-timeline-frame1 {
  position: absolute;
  top: 0px;
  left: 0px;
  background-color: #322c2c;
  width: 100vw;
  height: 100vw;
  margin: 12px;
}
.hp-timeline-frame2 {
  position: absolute;
  top: 24px;
  left: 24px;
  right: 24px;
  background-color: #fffafa;
  width: 100vw;
  height: 805px;
}
.hp-timeline-frame3 {
  position: absolute;
  top: 34px;
  left: 34px;
  right: 34px;
  background-color: #322c2c;
  width: 52vw;
  height: 782px;
  font-size: 40px;
  display: flex;
  align-items: center;
}
.hp-timeline-frame1,
.hp-timeline-frame2,
.hp-timeline-frame3 {
  flex: 1;
}


.hp-timeline-content {
  display: flex;
  flex-direction: column;
  align-items: start;
  justify-content: space-between;
  padding: 8px 16px 8px 16px;
  right: 50px;
  text-decoration: none;
}

a {
    text-decoration: none;
}

.hp-timeline-content h2 {
  display: inline-block;
  justify-content: flex-start;
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
  box-sizing: border-box; /* Ensures padding and border are included in the width and height */
  width: 300px; /* Example fixed width */
  overflow: hidden;
}
.hp-timeline-content h3 {
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


.hp-picture-frame {
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
.hp-picture-frame img {
  width: 100%;
  height: 100%;
  object-fit: cover; /* Ensures the image covers the frame */
  object-position: top;
  /* Adjust the values to achieve the desired effect */
}
</style>
