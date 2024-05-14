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
            v-for="(year, i) in years"
            :key="i"
            dot-color="white"
          >
            <template v-slot:opposite>
              <div
                :class="`pt-1 font-weight-bold text-white`"
                v-text="year.year"
              ></div>
            </template>
            <div class="timeline-content">
              <h2 :class="`mt-n1 font-weight-bold mb-4 text-inherit`">
                Loremipsum
              </h2>
            </div>
          </v-timeline-item>
        </v-timeline>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HeaderComponent",
  data: () => ({
    years: [
      {
        color: "cyan",
        year: "1960",
      },
      {
        color: "green",
        year: "1970",
      },
      {
        color: "pink",
        year: "1980",
      },
      {
        color: "amber",
        year: "1990",
      },
      {
        color: "orange",
        year: "2000",
      },
    ],
  }),
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
  font-size: 8.2vw;
}

@media (max-width: 480px) {
  .header,
  .h-frame1,
  .h-frame2,
  .h-frame3,
  .h-frame4 {
    width: auto; /* Full width of the parent */
    height: auto; /* Adjust height based on content */
    padding-top: 10%; /* Maintain aspect ratio with padding-top */
  }
  .art-history {
    font-size: 8vw;
  }
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
.bc {
  position: absolute;
  top: 4px;
  left: 82px;
  letter-spacing: -0.1em;
  line-height: 117.77%;
  display: inline-block;
  width: 179px;
  height: 40px;
}
.year {
  position: absolute;
  top: 89px;
  left: 1009px;
  width: 261px;
  height: 44px;
  font-size: 32px;
  color: #fffafa;
}
.timeline-item {
  position: relative;
  padding: 16px;
  background-color: #fff;
  border-radius: 8px;
  margin-bottom: 16px;
}
.timeline-content h2 {
  font-size: 30px; /* Adjust the font size as needed */
  color: inherit; /* Inherit the color from the parent */
  padding: 10px;
  background-color: #fff;
  display: inline;
  text-align: center;
}
</style>
