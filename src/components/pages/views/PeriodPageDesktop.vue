<template>
  <div class="period-page-desktop">
    <div class="ppd-container-frame">
      <div class="ppd-container-frame2">
        <div class="ppd-container-flexbox">
          <div class="ppd-container-header">
            <div class="ppd-container-back" @click="goHome">Home</div>
            <div v-if="periodData" class="ppd-container-title" @click="goBack">
              {{ periodData.period }}
            </div>
          </div>
          <div class="ppd-container-content-flexbox">
            <div class="ppd-container-content-flexbox-container">
              <div class="ppd-container-content-flexbox-container-column">
                <div
                  class="ppd-container-content-flexbox-container-column-flexbox"
                >
                  <div
                    v-if="currentPicture"
                    class="ppd-container-content-flexbox-container-column-img"
                  >
                    <img
                      class="ppd-img"
                      :src="currentPicture.image"
                      alt="Picture Frame"
                    />
                    <div
                      v-if="
                        currentPicture.author &&
                        currentPicture.author.toLowerCase() !== 'unknown'"
                      class="ppd-work-list-author"
                    >
                      <h3>{{ currentPicture.author }}</h3>
                    </div>
                  </div>
                  <div
                    v-if="showHighlights && periodData && periodData.highlights"
                    class="period-highlights-content"
                  >
                      <div
                        class="ppd-container-content-flexbox-container-column-flexbox-title"
                      >
                        HIGHLIGHTS OF THIS PERIOD
                        <img
                          class="period-highlight-img"
                          :src="periodData.highlights.image"
                          alt="Highlight Image"
                        />
                      </div>
                        <div class="period-div-15">
                          <div class="period-highlight-text">
                            {{ periodData.highlights.text1 }}
                          </div>
                        </div>
                    <div class="period-div-18">
                      <div class="period-highlight-text">
                        {{ periodData.highlights.text2 }}
                      </div>
                      <div class="period-highlight-text">
                        {{ periodData.highlights.text3 }}
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="ppd-container-content-flexbox-container-column-2">
                <div
                  class="ppd-container-content-flexbox-container-column-2-flexbox"
                >
                  <v-list v-if="periodData" class="ppd-work-list-flexbox">
                    <v-list-item
                      v-for="work in periodData.works"
                      :key="work.id"
                      @mouseover="showPicture(work)"
                      @mouseout="hidePicture"
                    >
                      <div class="ppd-work-list-item-container">
                        <div class="ppd-work-list-work">
                          <h2>{{ work.name }}</h2>
                        </div>
                        <div class="ppd-work-list-year">
                          <h3>{{ work.date }}</h3>
                        </div>
                      </div>
                    </v-list-item>
                  </v-list>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";

export default {
  name: "PeriodPageDesktop",
  props: ["id"],
  setup(props) {
    const router = useRouter();
    const url = "https://art-database.onrender.com/data.json";
    const data = ref(null);
    const loading = ref(false);
    const error = ref(null);
    const periodData = ref(null);
    const currentPicture = ref(null);
    const showHighlights = ref(true);

    const fetchData = async () => {
      loading.value = true;
      try {
        const response = await axios.get(url);
        data.value = response.data;
        processData();
      } catch (err) {
        error.value = "Failed to fetch data. See console for details.";
        console.error("Error fetching data:", err);
      } finally {
        loading.value = false;
      }
    };

    const processData = () => {
      console.log("Period ID:", props.id);
      if (data.value && data.value.TimeLine) {
        const eras = Object.values(data.value.TimeLine);
        for (const era of eras) {
          const period = Object.values(era.Periods).find(
            (period) => period.Period === props.id
          );
          if (period) {
            periodData.value = {
              period: period.Period,
              highlights: {
                text1: period.Highlights["1"] || "",
                text2: period.Highlights["2"] || "",
                text3: period.Highlights["3"] || "",
                image: period.Highlights["4"] || "", // Assuming '4' is always an image URL
              },
              works: period.Works.map((work) => ({
                name: work.Name,
                author: work.Author,
                date: work.Date,
                image: work.Image,
                id: work.id,
              })),
            };
          }
        }
      } else {
        console.log("Invalid data format:", data.value);
      }
    };

    const showPicture = (work) => {
      currentPicture.value = {
        id: work.id,
        image: work.image,
        author: work.author,
      };
      showHighlights.value = false;
    };

    const hidePicture = () => {
      currentPicture.value = null;
      showHighlights.value = true;
    };

    const goBack = () => {
      router.back();
    };

    const goHome = () => {
      router.push("/");
    };

    onMounted(fetchData);
    return {
      data,
      loading,
      error,
      periodData,
      goBack,
      goHome,
      showPicture,
      hidePicture,
      currentPicture,
      showHighlights,
    };
  },
};
</script>

<style scoped>
.period-page-desktop {
  background-color: #fff;
  display: flex;
  flex-direction: column;
  justify-content: start;
  padding: 47px 49px;
  font-family: "Times New Roman", Times, serif;
  max-height: 1000px;
  overflow: scroll;
}
@media (max-width: 991px) {
  .period-page-desktop {
    padding: 0 20px;
  }
}
.ppd-container-frame {
  background-color: #322c2c;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 15px 23px;
}
@media (max-width: 991px) {
  .ppd-container-frame {
    max-width: 100%;
    padding: 0 20px;
  }
}
.ppd-container-frame2 {
  background-color: #fffafa;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 27px 25px;
}
@media (max-width: 991px) {
  .ppd-container-frame2 {
    max-width: 100%;
    padding: 0 20px;
  }
}
.ppd-container-flexbox {
  background-color: #322c2c;
  display: flex;
  flex-direction: column;
  flex-grow: column;
  padding: 38px 32px 80px;
  max-height: 720px;
}
@media (max-width: 991px) {
  .ppd-container-flexbox {
    max-width: 100%;
    padding: 0 20px;
  }
}
.ppd-container-header {
  display: flex;
  gap: 20px;
  font-size: 40px;
  color: #322c2c;
  font-weight: 700;
  line-height: 118%;
  justify-content: space-between;
}
@media (max-width: 991px) {
  .ppd-container-header {
    max-width: 100%;
    flex-wrap: wrap;
  }
}
.ppd-container-back {
  font-family: "Times New Roman", Times, serif;
  border-color: rgba(50, 44, 44, 1);
  border-style: solid;
  border-width: 6px;
  background-color: #fffafa;
  white-space: nowrap;
  letter-spacing: 8.4px;
  justify-content: center;
  padding: 31px 34px;
}
@media (max-width: 991px) {
  .ppd-container-back {
    white-space: initial;
    padding: 0 20px;
  }
}
.ppd-container-title {
  font-family: "Times New Roman", Times, serif;
  border-color: rgba(50, 44, 44, 1);
  text-transform: uppercase;
  border-style: solid;
  border-width: 8px;
  background-color: #fffafa;
  letter-spacing: 6px;
  max-width: 50%;
  white-space: nowrap;
  padding: 20px;
}
@media (max-width: 991px) {
  .ppd-container-title {
    max-width: 100%;
    padding: 0 23px 0 20px;
  }
}
.ppd-container-content-flexbox {
  margin: 39px 0 4px;
}
@media (max-width: 991px) {
  .ppd-container-content-flexbox {
    max-width: 100%;
  }
}
.ppd-container-content-flexbox-container {
  gap: 20px;
  display: flex;
}
@media (max-width: 991px) {
  .ppd-container-content-flexbox-container {
    flex-direction: column;
    align-items: stretch;
    gap: 0px;
  }

  .ppd-container-frame,
  .ppd-container-frame2,
  .ppd-container-flexbox,
  .ppd-container-content-flexbox {
    display: flex;
    flex-direction: column;
    flex-grow: 1;
    width: 100%; /* Ensure full width */
    height: 100%; /* Ensure full height */
  }
}
.ppd-container-content-flexbox-container-column {
  display: flex;
  flex-direction: column;
  line-height: normal;
  flex-grow: 1;
  width: 50%;
  left: 20px;
  height: 100%;
  overflow: hidden;
}
.ppd-container-content-flexbox-container-column-img {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  width: 100%;
  max-height: 400px;
  flex-grow: 1;
  overflow: visible;
}

.img {
  aspect-ratio: 1.05;
  object-fit: auto;
  object-position: center;
  width: 66px;
}

.ppd-img {
  object-fit: contain;
  object-position: top;
  height: 100%;
  width: 100%;
  max-height: 350px;
}

.ppd-work-list-author {
  font-family: "Times New Roman", Times, serif;
  text-align: left;
  margin: 10px;
  z-index: 2;
  overflow: visible;
  position: relative;
}

@media (max-width: 991px) {
  .ppd-container-content-flexbox-container-column {
    width: 100%;
  }
}
.ppd-container-content-flexbox-container-column-flexbox {
  background-color: #fffafa;
  display: flex;
  flex-grow: 1;
  flex-direction: column;
  font-size: 23px;
  color: #000;
  font-weight: 400;
  width: 100%;
  padding: 35px;
  max-height: 500px;
}
@media (max-width: 991px) {
  .ppd-container-content-flexbox-container-column-flexbox {
    max-width: 100%;
    margin-top: 35px;
    padding: 0 20px;
  }
}
.ppd-container-content-flexbox-container-column-2-flexbox-title {
  font-family: Roboto Serif, sans-serif;
  font-style: italic;
  font-weight: 900;
  line-height: 118%;
  letter-spacing: 9.2px;
  align-self: start;
  margin-left: 22px;
  flex: 1 1 100%;
}
@media (max-width: 991px) {
  .ppd-container-content-flexbox-container-column-2-flexbox-title {
    margin-left: 10px;
  }
}
.div-12 {
  font-family: Roboto Serif, sans-serif;
  line-height: 27px;
  margin-top: 35px;
}
@media (max-width: 991px) {
  .div-12 {
    max-width: 100%;
  }
}
.div-13 {
  color: #322c2c;
  letter-spacing: -3.2px;
  margin-top: 10px;
  font: 32px/41px Roboto Serif, sans-serif;
}
@media (max-width: 991px) {
  .div-13 {
    max-width: 100%;
  }
}
.ppd-container-content-flexbox-container-column-2 {
  background-color: #d9d9d9;
  display: flex;
  flex-grow: 1;
  flex-direction: column;
  color: #322c2c;
  font-weight: 700;
  line-height: 118%;
  width: 50%;
  max-height: 500px;
  overflow-y: auto;
}
@media (max-width: 991px) {
  .ppd-container-content-flexbox-container-column-2 {
    width: 100%;
  }
}
.ppd-container-content-flexbox-container-column-2-flexbox {
  background-color: #d9d9d9;
  display: flex;
  flex-grow: 1;
  flex-direction: column;
  color: #322c2c;
  font-weight: 700;
  line-height: 118%;
  width: 100%;
  padding: 16px 58px;
}
@media (max-width: 991px) {
  .ppd-container-content-flexbox-container-column-2-flexbox {
    max-width: 100%;
    margin-top: 35px;
    padding: 0 20px;
  }
}
.ppd-work-list-flexbox {
  border-color: rgba(50, 44, 44, 1);
  border-style: solid;
  border-width: 6px;
  background-color: #fffafa;
  display: flex;
  flex-direction: column;
  gap: 20px;
  padding: 15px 20px;
}
@media (max-width: 991px) {
  .ppd-work-list-flexbox {
    max-width: 100%;
    flex-wrap: wrap;
  }
}

.ppd-work-list-item-container {
  border: 4px solid #322c2c;
  padding: 4px 4px 4px 4px;
  background-color: #d9d9d9;
}
.ppd-work-list-work {
  letter-spacing: -1.8px;
  flex-grow: 1;
  flex-basis: auto;
  margin: auto 0;
  font: 18px "Times New Roman", Times, serif;
  white-space: nowrap;
  overflow-x: scroll;
}
.div-17 {
  display: flex;
  gap: 20px;
  font-size: 32px;
  letter-spacing: -3.2px;
  justify-content: space-between;
}
.ppd-work-list-year {
  font-family: "Times New Roman", Times, serif;
  margin: auto 0;
  text-align: right;
}

.div-19 {
  border-color: rgba(50, 44, 44, 1);
  border-style: solid;
  border-width: 6px;
  background-color: #fffafa;
  margin-top: 14px;
  align-items: start;
  white-space: nowrap;
  letter-spacing: -2.8px;
  justify-content: center;
  padding: 32px 18px;
  font: 40px Roboto, sans-serif;
}
@media (max-width: 991px) {
  .div-19 {
    max-width: 100%;
    padding-right: 20px;
    white-space: initial;
  }
}
.div-20 {
  border-color: rgba(50, 44, 44, 1);
  border-style: solid;
  border-width: 6px;
  background-color: #fffafa;
  margin-top: 21px;
  align-items: start;
  white-space: nowrap;
  letter-spacing: -2.8px;
  justify-content: center;
  padding: 32px 18px;
  font: 40px Roboto, sans-serif;
}
@media (max-width: 991px) {
  .div-20 {
    max-width: 100%;
    padding-right: 20px;
    white-space: initial;
  }
}
.div-21 {
  border-color: rgba(50, 44, 44, 1);
  border-style: solid;
  border-width: 6px;
  background-color: #fffafa;
  margin-top: 22px;
  align-items: start;
  white-space: nowrap;
  letter-spacing: -2.8px;
  justify-content: center;
  padding: 32px 18px;
  font: 40px Roboto, sans-serif;
}
@media (max-width: 991px) {
  .div-21 {
    max-width: 100%;
    padding-right: 20px;
    white-space: initial;
  }
}
.div-22 {
  border-color: rgba(50, 44, 44, 1);
  border-style: solid;
  border-width: 6px;
  background-color: #fffafa;
  margin-top: 25px;
  align-items: start;
  white-space: nowrap;
  letter-spacing: -2.8px;
  justify-content: center;
  padding: 32px 18px;
  font: 40px Roboto, sans-serif;
}
@media (max-width: 991px) {
  .div-22 {
    max-width: 100%;
    padding-right: 20px;
    white-space: initial;
  }
}
.period-highlights-title {
  color: #000;
  letter-spacing: 9.2px;
  font: italic 900 23px/118% "Times New Roman", Times, serif;
  padding-bottom: 8px;
  white-space: nowrap;
}

@media (max-width: 991px) {
  .period-highlights-title {
    max-width: 100%;
  }
}

.period-highlights-content {
  margin-top: 10px;
}

@media (max-width: 991px) {
  .period-highlights-content {
    max-width: 100%;
    margin-top: 40px;
  }
}

@media (max-width: 991px) {
  .period-highlights-content-flexbox {
    flex-direction: column;
    align-items: stretch;
    gap: 0px;
  }
}

.period-column-5 {
  display: flex;
  flex-direction: column;
  line-height: normal;
  width: 27%;
  margin-left: 0px;
}

@media (max-width: 991px) {
  .period-column-5 {
    width: 100%;
  }
}

.period-highlight-img {
    object-fit: contain;
    max-width: 100px;
    max-height: 100px;
    flex-grow: 1;
    position: absolute;
    top: 35%;
}

.period-column-6 {
  display: flex;
  flex-direction: column;
  line-height: normal;
  width: 73%;
  margin-left: 20px;
}

@media (max-width: 991px) {
  .period-column-6 {
    width: 100%;
  }
}

.period-div-15 {
  display: flex;
  margin-top: 9px;
  flex-direction: column;
  font-size: 23px;
  color: #000;
  font-weight: 400;
  line-height: 27px;
}

.period-highlight-text {
  font-family: "Times New Roman", Times, serif;
  align-self: flex-start;
  margin: 56px 37px 0 0;
}

@media (max-width: 991px) {
  .period-highlight-text {
    margin: 40px 10px 0 0;
  }
}

.period-div-18 {
  color: #000;
  letter-spacing: 0.92px;
  font: 400 23px/27px Roboto Serif, sans-serif;
}

@media (max-width: 991px) {
  .period-div-18 {
    max-width: 100%;
  }
}

.period-div-19 {
  color: #000;
  letter-spacing: 0.92px;
  margin-top: 33px;
  font: 400 23px/27px Roboto Serif, sans-serif;
}

@media (max-width: 991px) {
  .period-div-19 {
    max-width: 100%;
  }
}
</style>
