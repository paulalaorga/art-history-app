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
                <v-timeline v-if="foundEra" side="start" line-color="white" line-thickness="8px">
                  <v-timeline-item v-for="period in foundEra.periods" :key="period.period" dot-color="white">
                    <router-link :to="{ name: 'PeriodPage', params: { id: period.period } }">
                      <div class="timeline-content">
                        <h2>{{ period.period }}</h2>
                      </div>
                    </router-link>
                    <template v-slot:opposite>
                      <div class="timeline-content">
                        <h3>{{ period.years }}</h3>
                      </div>
                    </template>
                  </v-timeline-item>
                </v-timeline>
              </div>
              <div v-if="foundEra" class="picture-frame">
                <img :src="foundEra.picture" alt="Picture Frame" />
              </div>
            </div>
            <div class="info-column">
  <div class="info-column-flexbox">
    <div class="highlights-title">HIGHLIGHTS OF THIS ERA</div>
    <div v-if="foundEra && foundEra.highlights" class="highlights-content-flexbox">
      <div class="column-5">
      <img :src="foundEra.highlights.image" alt="Highlighted Art" class="highlight-img">
      </div>
      <div class="column-6">
        <div class="div-15">
      <div class="highlight-text">{{ foundEra.highlights.text1 }}</div>
      <div class="highlight-text">{{ foundEra.highlights.text2 }}</div>
      <div class="highlight-text">{{ foundEra.highlights.text3 }}</div>
    </div>
  </div>
 
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
              picture: era.Picture,
              highlights: {
                  text1: era.Highlights["1"] || "",
                  text2: era.Highlights["2"] || "",
                  text3: era.Highlights["3"] || "",
                  image: era.Highlights["4"] || ""  // Assuming '4' is always an image URL
                },
              periods: Object.values(era.Periods).map((period) => ({
                period: period.Period,
                years: period.Years,
                picture: period.Picture,
              })),
            }),
              console.log("Processed Era Data:", foundEra.value);
            console.log("Processed Highlights:", foundEra.value.highlights);

          }
        }
      };
      const isImageUrl = (str) => /\.(jpeg|jpg|gif|png)$/.test(str);

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
        isImageUrl,
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
    color: #322c2c;
    font-weight: 700;
    margin-right: 50px;
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
    letter-spacing: 22.4px;
    font-size: 40px;
    height: 60px;
    line-height: normal;


  }

  @media (max-width: 991px) {
    .periods-title {
      white-space: initial;
      padding: 0 20px;
    }
  }

  .timeline-content h2 {
    text-align: flex-start;
    text-transform: uppercase;
    font-family: "Times New Roman", Times, serif;
    font-weight: 700;
    background-color: #fffafa;
    color: #322c2c;
    white-space: nowrap;

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
    white-space: nowrap;
  }

  .picture-frame {
    bottom: 24px;
    height: 300px;
    border: 8px solid #322c2c;
    align-items: center;
    justify-self: center;
    filter: grayscale(50%) brightness(90%) contrast(110%) saturate(10%);
  }

  .picture-frame img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: top;
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
    font: italic 900 23px/118% "Times New Roman", Times, serif;
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
    .highlights-content-flexbox {
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

  .highlight-img {
    aspect-ratio: 0.72;
    object-fit: auto;
    object-position: center;
    width: 152px;
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


  .highlight-text {
    font-family: "Times New Roman", Times, serif;
    align-self: end;
    margin: 56px 37px 0 0;
  }

  @media (max-width: 991px) {
    .highlight-text  {
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
