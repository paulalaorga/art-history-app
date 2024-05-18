<template>
    <div class="era-sm-light">
      <div class="era-sm-header-frame">
        <div class="era-sm-header-frame2">
          <div class="era-sm-header-frame3">
            <div v-if="foundEra" class="era-sm-art-history">{{ foundEra.era }}</div>
          </div>
        </div>
      </div>
      <div class="era-sm-timeline-frame">
        <div class="era-sm-timeline-frame1">
          <div class="era-sm-timeline-frame2">
            <div class="era-sm-timeline-frame3">
              <v-list v-if= "foundEra" class="sm-timeline-content-list">
                <v-list-item
                  v-for="period in foundEra.periods"
                  :key="period.period"
                  :picture="period.picture"
                >
                <router-link  :to="{ name: 'PeriodPage', params: { id: period.period }}">
                  <div class="era-sm-timeline-period">{{ period.period }}</div>
                  <img  class="era-sm-period-image" :src="period.picture" alt="Picture Frame"/></router-link>
                </v-list-item>
              </v-list>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
import { ref, onMounted } from 'vue';
import axios from "axios";

export default {
    name: "EraPageSmall",
    props: ["id"],
    setup(props) {
      const url = "https://art-database.onrender.com/data.json";
      const data = ref(null);
      const loading = ref(false);
      const error = ref(null);
      const foundEra = ref(null);
      const currentPicture = ref(null);
  
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
            foundEra.value = {
              era: era.Era,
              periods: Object.values(era.Periods).map(period => ({
                period: period.Period,
                years: period.Years,
                picture: period.Picture,
              })),
            };
          console.log("Processed Era Data:", foundEra.value);
          } else {
            console.log("Era not found for id:", props.id);
          }
        } else {
          console.log("Invalid data format:", data.value);
        }
    };
  
    onMounted(fetchData);
  
    return {
      data,
      loading,
      error,
      foundEra,
  };
    },
  };
  </script>
  
  <style>
  
  .era-sm-light {
    background-color: #fff;
    display: flex;
    max-width: 480px;
    min-width: 375px;
    width: 100%;
    flex-direction: column;
    margin: 0 auto;
    font-family: 'Times New Roman', Times, serif;
  }
  .era-sm-header-frame {
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
  .era-sm-header-frame2 {
    background-color: #fffafa;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 4px 7px;
  }
  .era-sm-header-frame3 {
    background-color: #322c2c;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 6px 13px;
  }
  .era-sm-art-history {
    font-family: 'Times New Roman', Times, serif;
    background-color: #fffafa;
    text-align: justify;
    font-size: 1.2em;
    text-transform: uppercase;
  }
  .era-sm-timeline-frame2 {
    background-color: #322c2c;
    display: flex;
    width: 100%;
    flex-direction: column;
    justify-content: center;
    padding: 0 12px;
  }
  .era-sm-timeline-frame3 {
    background-color: #fffafa;
    display: flex;
    flex-direction: column;
    padding: 7px 6px 0;
  }
  .era-sm-timeline-content-list {
    background-color: #322c2c;
    display: flex;
    flex-direction: column;
  }
  .era-sm-timeline-period {
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
  .era-sm-period-image {
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
  