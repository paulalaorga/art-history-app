<template>
  <div class="era-page-desktop">
    <div class="epd-header">
      <div class="epd-header-flexbox">
        <div class="epd-title-frame" @click="goBack">
          <div class="epd-title-frame2">
            <div class="epd-title-frame3">
              <div class="epd-title-text">ART HISTORY</div>
            </div>
          </div>
        </div>

        <div v-if="foundEra" class="epd-era-text">
          {{ foundEra.era }}
        </div>
      </div>
    </div>
    <div class="epd-container-frame1">
      <div class="epd-container-frame2">
        <div class="epd-container">
          <div class="epd-container-flexbox">
            <div class="periods-column">
              <div class="periods-column-flexbox">
                <div class="periods-title">PERIODS</div>
                <v-timeline
                  v-if="foundEra"
                  side="start"
                  line-color="white"
                  line-thickness="8px"
                >
                  <v-timeline-item
                    v-for="period in foundEra.periods"
                    :key="period.period"
                    dot-color="white"
                    :years="period.years"
                    @mouseover="showPicture(period.picture)"
                    @mouseleave="hidePicture"
                  >
                    <router-link
                      :to="{
                        name: 'PeriodPage',
                        params: { id: period.period },
                      }"
                    >
                      <div class="timeline-content">
                        <h2>
                          {{ period.period }}
                        </h2>
                      </div>
                    </router-link>
                    <template v-slot:opposite>
                      <!--               <router-link  :to="{ name: 'PeriodPage', params: { id: period.period }}">
   -->
                      <div class="timeline-content">
                        <h3>
                          {{ period.years }}
                        </h3>
                      </div>
                    </template>
                  </v-timeline-item>
                </v-timeline>
              </div>
            </div>
            <div class="info-column">
              <div class="info-column-flexbox">
                <div class="highlights-title">HIGHLIGHTS OF THIS ERA</div>
                <div class="highlights-content">
                  <div class="highlights-content-flexbox">
                    <div class="column-5">
                      <img loading="lazy" srcSet="..." class="img-3" />
                    </div>
                    <div class="column-6">
                      <div class="div-15">
                        <div class="div-16">
                          History, mythology, literature and phylosophy are
                          interconected
                        </div>
                        <div class="div-17">
                          The Original Works are
                          <span style="font-weight: 600"
                            >Surviving Artifacts</span
                          >
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="div-18">
                  To analise this era we have to pay attention to
                  <span style="font-weight: 700"
                    >iconography, styles, form, function, meaning, technique and
                    symbolism
                  </span>
                </div>
                <div class="div-19">
                  It starts at the flourishing of Greek civilization and ends
                  with the decline of the Roman Empire Centuries
                  <span style="font-weight: 800">V b.c. to IV c.e</span>
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
import { useRouter } from "vue-router";
import axios from "axios";

export default {
  name: "EraPageDesktop",
  props: ["id"],
  setup(props) {
    const router = useRouter();
    const url = "https://art-database.onrender.com/data.json";
    const data = ref(null);
    const loading = ref(false);
    const error = ref(null);
    const foundEra = ref(null);

    const fetchData = async () => {
      loading.value = true;
      try {
        const response = await axios.get(url);
        data.value = response.data;
        console.log("Data received:", data.value);
        processData();
      } catch (error) {
        console.error("Error fetching data:", error);
        error.value = "Failed to fetch data. See console for details.";
      } finally {
        loading.value = false;
      }
    };

    const processData = () => {
      console.log("Processing data:", data.value);
      console.log("Era ID:", props.id);
      if (data.value && data.value.TimeLine) {
        const eras = Object.values(data.value.TimeLine);
        const era = eras.find((era) => era.Era === props.id);
        if (era) {
          (foundEra.value = {
            era: era.Era,
            periods: Object.values(era.Periods).map((period) => ({
              period: period.Period,
              years: period.Years,
              picture: period.Picture,
            })),
          }),
            console.log("Processed Era Data:", foundEra.value);
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
      error,
      foundEra,
      goBack,
    };
  },
};
</script>

<style scoped>
.era-page-desktop {
  background-color: #fff;
  display: flex;
  flex-direction: column;
  padding: 32px 49px 59px;
}
@media (max-width: 991px) {
  .era-page-desktop {
    padding: 0 20px;
  }
}
.epd-header {
  align-self: center;
  width: 100%;
  max-width: 1151px;
}
@media (max-width: 991px) {
  .epd-header {
    max-width: 100%;
  }
}
.epd-header-flexbox {
  gap: 20px;
  display: flex;
}
@media (max-width: 991px) {
  .epd-header-flexbox {
    flex-direction: column;
    align-items: stretch;
    gap: 0px;
  }
}
.epd-title-frame {
  background-color: #322c2c;
  display: flex;
  width: 100%;
  flex-direction: column;
  box-height: 58px;
  color: #322c2c;
  font-weight: 700;
  justify-content: center;
  padding: 7px 12px;
}
.epd-title-frame2 {
  background-color: #fffafa;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 4px 7px;
  box-sizing: border-box;
  height: 100%;
}
.epd-title-frame3 {
  background-color: #322c2c;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 6px 13px;
  display: flex;
  width: 100%;
  height: 100%;
}
.epd-title-text {
  font-family: "Times New Roman", Times, serif;
  background-color: #fffafa;
  text-align: center;
  text-transform: uppercase;
  font-size: 45px;
  height: 100%;
  align-content: center;
  text-overflow: ellipsis;
  letter-spacing: clamp(0.05em, 0.1vw, 0.2em);
}

.epd-era-text {
  border-color: rgba(50, 44, 44, 1);
  border-style: solid;
  border-width: 8px;
  background-color: #fffafa;
  color: #322c2c;
  white-space: nowrap;
  letter-spacing: 20.2px;
  justify-content: center;
  padding: 31px 34px;
  text-transform: uppercase;
  font: 700 40px/118% "Times New Roman", Times, serif;
}
@media (max-width: 991px) {
  .epd-era-text {
    max-width: 100%;
    margin-top: 40px;
    white-space: initial;
    padding: 0 20px;
  }
}
.epd-container {
  background-color: #322c2c;
  display: flex;
  margin-top: 20px;
  flex-direction: column;
  justify-content: center;
  padding: 13px 23px;
}
@media (max-width: 991px) {
  .epd-container-frame1 {
    max-width: 100%;
    padding: 0 20px;
  }
}
.epd-container-frame2 {
  background-color: #fffafa;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 23px 25px;
}
@media (max-width: 991px) {
  .epd-container-frame2 {
    max-width: 100%;
    padding: 0 20px;
  }
}
.epd-container {
  background-color: #322c2c;
  padding: 34px 74px 34px 27px;
}
@media (max-width: 991px) {
  .epd-container {
    max-width: 100%;
    padding: 0 20px;
  }
}
.epd-container-flexbox {
  gap: 20px;
  display: flex;
}
@media (max-width: 991px) {
  .epd-container-flexbox {
    flex-direction: column;
    align-items: stretch;
    gap: 0px;
  }
}
.periods-column {
  display: flex;
  flex-direction: column;
  line-height: normal;
  width: 41%;
  margin-left: 0px;
}
@media (max-width: 991px) {
  .periods-column {
    width: 100%;
  }
}
.periods-column-flexbox {
  display: flex;
  flex-grow: 1;
  flex-direction: column;
  font-size: 40px;
  color: #322c2c;
  font-weight: 700;
  white-space: nowrap;
  letter-spacing: 22.4px;
  line-height: 118%;
}
@media (max-width: 991px) {
  .periods-column-flexbox {
    margin-top: 40px;
    white-space: initial;
  }
}
.periods-title {
  font-family: "Times New Roman", Times, serif;
  border-color: rgba(50, 44, 44, 1);
  border-style: solid;
  border-width: 8px;
  background-color: #fffafa;
  justify-content: center;
  align-self: center;
}
@media (max-width: 991px) {
  .periods-title {
    white-space: initial;
    padding: 0 20px;
  }
}
.timeline-content h2 {
  justify-content: start;
  text-align: center;
  padding: 8px 16px 8px 16px;
  text-transform: uppercase;
  font-family: "Times New Roman", Times, serif;
  font-weight: 700;
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
  font-family: "Times New Roman", Times, serif;
  font-weight: 500;
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
.img-2 {
  aspect-ratio: 0.69;
  object-fit: auto;
  object-position: center;
  width: 100%;
  border-color: rgba(50, 44, 44, 1);
  border-style: solid;
  border-width: 10px;
}
.info-column {
  display: flex;
  flex-direction: column;
  line-height: normal;
  width: 59%;
  margin-left: 20px;
}
@media (max-width: 991px) {
  .info-column {
    width: 100%;
  }
}
.info-column-flexbox {
  background-color: #fff;
  display: flex;
  flex-direction: column;
  align-self: stretch;
  width: 100%;
  margin: auto 0;
  padding: 59px 42px;
}
@media (max-width: 991px) {
  .info-column-flexbox {
    max-width: 100%;
    margin-top: 40px;
    padding: 0 20px;
  }
}
.highlights-title {
  color: #000;
  letter-spacing: 9.2px;
  font: italic 900 23px/118% Roboto Serif, -apple-system, Roboto, Helvetica,
    sans-serif;
}
@media (max-width: 991px) {
  .highlights-title {
    max-width: 100%;
  }
}
.highlights-content {
  margin-top: 51px;
}
@media (max-width: 991px) {
  .highlights-content {
    max-width: 100%;
    margin-top: 40px;
  }
}
.highlights-content-flexbox {
  gap: 20px;
  display: flex;
}
@media (max-width: 991px) {
  . .highlights-content-flexbox {
    flex-direction: column;
    align-items: stretch;
    gap: 0px;
  }
}
.column-5 {
  display: flex;
  flex-direction: column;
  line-height: normal;
  width: 27%;
  margin-left: 0px;
}
@media (max-width: 991px) {
  .column-5 {
    width: 100%;
  }
}
.img-3 {
  aspect-ratio: 0.72;
  object-fit: auto;
  object-position: center;
  width: 152px;
  max-width: 100%;
  flex-grow: 1;
}
.column-6 {
  display: flex;
  flex-direction: column;
  line-height: normal;
  width: 73%;
  margin-left: 20px;
}
@media (max-width: 991px) {
  .column-6 {
    width: 100%;
  }
}
.div-15 {
  display: flex;
  margin-top: 9px;
  flex-direction: column;
  font-size: 23px;
  color: #000;
  font-weight: 400;
  line-height: 27px;
}
.div-16 {
  font-family: Roboto Serif, sans-serif;
}
.div-17 {
  font-family: Roboto Serif, sans-serif;
  align-self: end;
  margin: 56px 37px 0 0;
}
@media (max-width: 991px) {
  .div-17 {
    margin: 40px 10px 0 0;
  }
}
.div-18 {
  color: #000;
  letter-spacing: 0.92px;
  font: 400 23px/27px Roboto Serif, sans-serif;
}
@media (max-width: 991px) {
  .div-18 {
    max-width: 100%;
  }
}
.div-19 {
  color: #000;
  letter-spacing: 0.92px;
  margin-top: 33px;
  font: 400 23px/27px Roboto Serif, sans-serif;
}
@media (max-width: 991px) {
  .div-19 {
    max-width: 100%;
  }
}
</style>
