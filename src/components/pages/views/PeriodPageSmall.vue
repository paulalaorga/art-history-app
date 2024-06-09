<template>
  <div class="pp-sm-light">
    <div class="pp-sm-header-frame">
      <div class="pp-sm-header-frame2">
        <div class="pp-sm-header-frame3">
          <div v-if="periodData" class="pp-sm-art-history" @click="goBack">
            {{ periodData.period }}
          </div>
        </div>
      </div>
    </div>
    <div class="pp-sm-timeline-frame">
      <div class="pp-sm-timeline-frame1">
        <div class="pp-sm-timeline-frame2">
          <div class="pp-sm-timeline-frame3">
            <div class="pp-sm-timeline-frame4">
              <div class="pp-sm-info-column">
              <div class="pp-sm-info-column-flexbox">
                <div class="pp-sm-highlights-title">HIGHLIGHTS OF THIS ERA</div>
                <div v-if="foundEra && foundEra.highlights" class="highlights-content">
                  <div class="pp-sm-highlights-content-flexbox">

                    <div class="pp-sm-column-5">
                      <img :src="foundEra.highlights.image" alt="Highlighted Art" class="highlight-img">
                    </div>
                    <div class="pp-sm-column-6">
                      <div class="pp-sm-div-15">
                        <div class="pp-sm-highlight-text">{{ foundEra.highlights.text1 }}</div>
                      </div>
                    </div>
                  </div>
                  <div class="pp-sm-div-18">
                    <div class="pp-sm-highlight-text">{{ foundEra.highlights.text2 }}</div>
                    <div class="pp-sm-highlight-text">{{ foundEra.highlights.text3 }}</div>
                  </div>

                </div>
              </div>
            </div>
            <v-list v-if="periodData" class="pp-sm-timeline-content-list">
              <v-list-item
                v-for="work in periodData.works"
                :key="work.id"
                :picture="work.image"
              >
                <div class="pp-sm-timeline-period">{{ work.name }}</div>
                <img
                  class="pp-sm-period-image"
                  :src="work.image"
                  alt="Picture Frame"
                />
              </v-list-item>
            </v-list>
          </div>
         </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";

export default {
  name: "PeriodPageSmall",
  props: ["id"],
  setup(props) {
    const router = useRouter();
    const url = "https://art-database.onrender.com/data.json";
    const data = ref(null);
    const loading = ref(false);
    const fetchError = ref(null);
    const periodData = ref(null);

    const fetchData = async () => {
      loading.value = true;
      try {
        const response = await axios.get(url);
        data.value = response.data;
        processData();
      } catch (err) {
        fetchError.value = "Failed to fetch data. See console for details.";
      } finally {
        loading.value = false;
      }
    };

    const processData = () => {
      console.log("Processing data", data.value);
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
              works: period.Works.map((work) => ({
                name: work.Name,
                date: work.Date,
                image: work.Image,
              })),
            };
            console.log("Found Period:", periodData.value);
            return;
          }
        }
      }
    };

    const goBack = () => {
      router.back();
    };

    onMounted(fetchData);

    return {
      data,
      loading,
      fetchError,
      periodData,
      goBack,
    };
  },
};
</script>

<style scoped>
.pp-sm-light {
  background-color: #fff;
  display: flex;
  max-width: 480px;
  min-width: 375px;
  width: 100%;
  flex-direction: column;
  margin: 0 auto;
  font-family: "Times New Roman", Times, serif;
}
.pp-sm-header-frame {
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
.pp-sm-header-frame2 {
  background-color: #fffafa;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 4px 7px;
}
.pp-sm-header-frame3 {
  background-color: #322c2c;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 6px 13px;
}
.pp-sm-art-history {
  font-family: "Times New Roman", Times, serif;
  background-color: #fffafa;
  text-align: center;
  text-transform: uppercase;
  letter-spacing: 2vw;
  font-size: calc(3vw + 3vh + 3vmin);
}
.pp-sm-timeline-frame2 {
  background-color: #322c2c;
  display: flex;
  width: 100%;
  flex-direction: column;
  justify-content: center;
  padding: 0 12px;
}
.pp-sm-timeline-frame3 {
  background-color: #fffafa;
  display: flex;
  flex-direction: column;
  padding: 7px 6px 0;
}
.pp-sm-timeline-content-list {
  background-color: #322c2c;
  display: flex;
  flex-direction: column;
}
.pp-sm-timeline-period {
  margin-top: 8px;
  margin-bottom: 8px;
  border: solid 8px #322c2c;
  background-color: #fffafa;
  color: #322c2c;
  padding: 8px;
  text-transform: uppercase;
  text-align: center;
  font-family: "Times New Roman", Times, serif;
  font-weight: 700;
  font-size: calc(2vw + 2vh + 2vmin);
  overflow-y: hidden;
}
.pp-sm-period-image {
  margin-top: 8px;
  border: solid 8px #322c2c;
  display: flex;
  flex-direction: column;
  max-width: 412px;
  height: 500px;
  filter: brightness(90%) contrast(110%) saturate(50%);
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

.pp-sm-info-column {
  display: flex;
  flex-direction: column;
  line-height: normal;
  width: 59%;
  margin-left: 20px;
}

@media (max-width: 991px) {
  .pp-sm-info-column {
    width: 100%;
  }
}

.pp-sm-info-column-flexbox {
  background-color: #fff;
  display: flex;
  flex-direction: column;
  align-self: stretch;
  width: 100%;
  margin: auto 0;
  padding: 59px 42px;
}

@media (max-width: 991px) {
  .pp-sm-info-column-flexbox {
    max-width: 100%;
    margin-top: 40px;
    padding: 0 20px;
  }
}

.pp-sm-highlights-title {
  color: #000;
  letter-spacing: 9.2px;
  font: italic 900 23px/118% "Times New Roman", Times, serif;
  padding-bottom: 8px;
  white-space: nowrap;
}

@media (max-width: 991px) {
  .pp-sm-highlights-title {
    max-width: 100%;
  }
}

.pp-sm-highlights-content {
  margin-top: 10px;
}

@media (max-width: 991px) {
  .pp-sm-highlights-content {
    max-width: 100%;
    margin-top: 40px;
  }
}

.pp-sm-highlights-content-flexbox {
  gap: 20px;
  display: flex;
}

@media (max-width: 991px) {
  .pp-sm-highlights-content-flexbox {
    flex-direction: column;
    align-items: stretch;
    gap: 0px;
  }
}

.pp-sm-column-5 {
  display: flex;
  flex-direction: column;
  line-height: normal;
  width: 27%;
  margin-left: 0px;
}

@media (max-width: 991px) {
  .pp-sm-column-5 {
    width: 100%;
  }
}

.pp-sm-highlight-img {
  object-fit: contain;
  object-position: center;
  width: 152px;
  flex-grow: 1;
}

.pp-sm-column-6 {
  display: flex;
  flex-direction: column;
  line-height: normal;
  width: 73%;
  margin-left: 20px;
}

@media (max-width: 991px) {
  .pp-sm-column-6 {
    width: 100%;
  }
}

.pp-sm-div-15 {
  display: flex;
  margin-top: 9px;
  flex-direction: column;
  font-size: 23px;
  color: #000;
  font-weight: 400;
  line-height: 27px;
}


.pp-sm-highlight-text {
  font-family: "Times New Roman", Times, serif;
  align-self: end;
  margin: 56px 37px 0 0;
}

@media (max-width: 991px) {
  .pp-sm-highlight-text {
    margin: 40px 10px 0 0;
  }
}

.pp-sm-div-18 {
  color: #000;
  letter-spacing: 0.92px;
  font: 400 23px/27px Roboto Serif, sans-serif;
}

@media (max-width: 991px) {
  .pp-sm-div-18 {
    max-width: 100%;
  }
}

.pp-sm-div-19 {
  color: #000;
  letter-spacing: 0.92px;
  margin-top: 33px;
  font: 400 23px/27px Roboto Serif, sans-serif;
}

@media (max-width: 991px) {
  .pp-sm-div-19 {
    max-width: 100%;
  }
}

</style>
