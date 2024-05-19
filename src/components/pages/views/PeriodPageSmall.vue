<template>
    <div class="pp-sm-light">
      <div class="pp-sm-header-frame">
        <div class="pp-sm-header-frame2">
          <div class="pp-sm-header-frame3">
            <div v-if="periodData" class="pp-sm-art-history">{{ periodData.period }}</div>
          </div>
        </div>
      </div>
      <div class="pp-sm-timeline-frame">
        <div class="pp-sm-timeline-frame1">
          <div class="pp-sm-timeline-frame2">
            <div class="pp-sm-timeline-frame3">
              <v-list v-if= "periodData" class="pp-sm-timeline-content-list">
                <v-list-item
                  v-for="work in periodData.works"
                  :key="work.id"
                  :picture="work.image"
                >
                  <div class="pp-sm-timeline-period">{{ work.name }}</div>
                  <img  class="pp-sm-period-image" :src="work.image" alt="Picture Frame"/>
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
    name: "PeriodPageSmall",
    props: ["id"],
    setup(props) {
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
        console.log('Processing data', data.value);
        console.log('Period ID:', props.id);
        if (data.value && data.value.TimeLine) {
          const eras = Object.values(data.value.TimeLine);
          for (const era of eras) {
            const period = Object.values(era.Periods).find((period) => period.Period === props.id);
            if (period) {
              periodData.value = {
                period: period.Period,
                works: period.Works.map(work => ({
                  name: work.Name,
                  date: work.Date,
                  image: work.Image,
                }))
              };
              console.log('Found Period:', periodData.value);
              return;
            };
            };
        };
        };
  
    onMounted(fetchData);
  
    return {
      data,
      loading,
      fetchError,
      periodData
  };
    },
  };
  </script>
  
  <style>
  
  .pp-sm-light {
    background-color: #fff;
    display: flex;
    max-width: 480px;
    min-width: 375px;
    width: 100%;
    flex-direction: column;
    margin: 0 auto;
    font-family: 'Times New Roman', Times, serif;
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
    font-family: 'Times New Roman', Times, serif;
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
    border-style: solid;
    background-color: #fffafa;
    color: #322c2c;
    padding: 8px;
    text-transform: uppercase;
    text-align: center;
    font-family: 'Times New Roman', Times, serif;
    font-weight: 700;
    font-size: calc(2vw + 2vh + 2vmin);
    overflow-y: hidden;
  }
  .pp-sm-period-image {
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
  