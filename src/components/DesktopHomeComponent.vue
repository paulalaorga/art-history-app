<template>
  <div class="desktop-light">
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
        <v-timeline align="center" line-color="white" line-thickness="8px">
          <v-timeline-item
            v-for="era in data"
            :key="era.era"
            dot-color="white"
            :years="era.years"
          >
            <template v-slot:opposite>
              <div class="text-h4 font-small text-white"
              >{{ era.years }}</div>
            </template>
            <!-- @mouseover="showPicture(era.pictureUrl)" @mouseleave="hidePicture" -->
            <div class="timeline-content">
              <h2>
                {{ era.era }}
              </h2>
            </div>
          </v-timeline-item>
        </v-timeline>
      </div>
    </div>
    <div class="picture-frame">
      <img
        :src="currentPicture"
        alt="Picture Frame">
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "DesktopHomeComponent",
  data() {
    return {
      data: [],
      loading: false,
      error: null,  // To store error messages for display or debugging
      currentPicture: null
    };
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    async fetchData() {
      this.loading = true;
      const url = 'https://art-database.onrender.com/data.json';  // Endpoint URL
      try {
        const response = await axios.get(url);
        console.log("Data received:", response.data);  // Log the raw data from the server
        this.processData(response.data);

      } catch (error) {
        console.error('Error fetching data:', error);
        this.error = 'Failed to fetch data. See console for details.';  // Update the error message for the UI
      } finally {
        this.loading = false;  // Ensure loading is always turned off after the fetch operation
      }
    },
    processData(data) {
      if (data && data.TimeLine) {
        this.data = Object.keys(data.TimeLine).map(key => {
          const era = data.TimeLine[key];
          return {
            era: era.Era,
            years: era.Years,
            picture: era.Picture
          };
        });
        console.log("Processed Timeline Data:", this.data);
      }
    },
  }
};
</script>




<style scoped>

.desktop-light {
  width: 100%;
  position: relative;
  background-color: #fff;
  height: 832px;
  overflow: hidden;
  text-align: left;
  font-size: 40px;
  color: #322c2c;
  font-family: Roboto;
  margin: 0;
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
  font-family: initial;
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
  align-items: center;
  justify-content: center;
}
.timeline-frame1,
.timeline-frame2,
.timeline-frame3 {
  flex: 1;
}
.classicism-group {
  position: absolute;
  top: calc(50% - 46px);
  left: 0px;
  width: 272px;
  height: 92px;
}
.classicism {
  position: absolute;
  top: 22px;
  left: 18px;
  letter-spacing: -0.01em;
  line-height: 117.77%;
  display: inline-block;
  width: 240px;
  height: 49px;
}


.timeline-content h2 {
  font-size: 30px; /* Adjust the font size as needed */
  color: inherit; /* Inherit the color from the parent */
  padding: 10px;
  background-color: #fff;
  display: inline;
  justify-content: center;
  text-align: center;
  font-family: initial;
  background-origin: padding-box;
  text-transform:inherit;
}
.picture-frame {
    position: absolute;
    left: 70px;
    right: 0;
    bottom: 24px;
    height: 448px;
    display: none;
}
.timeline-content:hover + .picture-frame {
    display: block;
}

</style>
