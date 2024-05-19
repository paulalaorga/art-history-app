<template>
    <div class="ppd-period-page-desktop">
      <div class="ppd-header">
        <div class="ppd-h-frame1"></div>
        <div class="ppd-h-frame2"></div>
        <div class="ppd-h-frame3"></div>
        <div class="ppd-h-frame4"></div>
        <b class="ppd-art-history">ART HISTORY</b>
      </div>
      <div class="ppd-timeline-frame">
        <div class="ppd-timeline-frame1"></div>
        <div class="ppd-timeline-frame2"></div>
        <div class="ppd-timeline-frame3">
        <v-list v-if="periodData" class="ppd-list-content">
        
          <div class="ppd-era-title">
            {{ periodData.period }}
          </div>
          <v-list-item
              v-for="work in periodData.works"
              :key="work.id"
            >
              <div class="ppd-list-content">
                <h2>{{ work.name }}</h2>
                <h3>{{ work.date }}</h3>
            </div>
        </v-list-item>
        </v-list>
    <div class="ppd-picture-frame" v-if="currentPicture">
        <img :src="currentPicture" alt="Picture Frame" />
      </div>
    </div>
    </div>
    </div>
  </template>
  
  <script>
  import { ref, onMounted } from 'vue';
  import axios from 'axios';
  
  export default {
    name: 'PeriodPageDesktop',
    props: ['id'],
    setup(props) {
      const url = 'https://art-database.onrender.com/data.json';
      const data = ref(null);
      const loading = ref(false);
      const error = ref(null);
      const periodData = ref(null);
  
      const fetchData = async () => {
        loading.value = true;
        try {
          const response = await axios.get(url);
          data.value = response.data;
          console.log('Data received:', data.value);
          processData();
        } catch (err) {
          error.value = 'Failed to fetch data. See console for details.';
          console.error('Error fetching data:', err);
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
            }
            }
            console.log('Period not found');
        } else {
            console.log("Invalid data format:", data.value);
      }
    };

  onMounted(fetchData);
  return {
    data,
    loading,
    error,
    periodData,
    };
    }
    };

  </script>
  
  <style scoped>
  .ppd-period-page-desktop {
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
  .ppd-header {
    position: absolute;
    top: 13px;
    left: 7px;
    width: 621px;
    height: 329px;
    flex: 1;
  }
  .ppd-h-frame1 {
    position: absolute;
    top: 0px;
    left: 0px;
    background-color: #322c2c;
    width: 100%;
    height: 100%;
  }
  .ppd-h-frame2 {
    position: absolute;
    top: calc(50% - 152.2px);
    left: 11px;
    background-color: #fffafa;
    width: 596.8px;
    height: 305.7px;
  }
  .ppd-h-frame3 {
    position: absolute;
    top: 21.77px;
    left: 20.17px;
    background-color: #322c2c;
    width: 579.4px;
    height: 285.8px;
  }
  .ppd-h-frame4 {
    position: absolute;
    top: calc(50% - 132.5px);
    left: 31px;
    background-color: #fffafa;
    width: 557px;
    height: 263px;
  }
  .ppd-art-history {
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
  
  .ppd-timeline-frame {
    position: absolute;
    top: 0px;
    left: 638px;
    width: 100vw;
    height: 832px;
    justify-content: space-around;
    display: flex;
    flex-direction: column;
  }
  .ppd-timeline-frame1 {
    position: absolute;
    top: 0px;
    left: 0px;
    background-color: #322c2c;
    width: 100vw;
    height: 100vw;
    margin: 12px;
  }
  .ppd-timeline-frame2 {
    position: absolute;
    top: 24px;
    left: 24px;
    right: 24px;
    background-color: #fffafa;
    width: 100vw;
    height: 805px;
  }
  .ppd-timeline-frame3 {
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
  
   .ppd-era-title {
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
  
  .ppd-list-content h2 {
    justify-content: start;
    text-align: center;
    padding: 8px 16px 8px 16px;
    text-transform: uppercase;
    font-family: 'Times New Roman', Times, serif;
    font-weight: 700;
    font-size: large;
    border-width: 8px;
    background-color: #fffafa;
    color: #322c2c;
    padding: 8px 16px 8px 16px;
    width: 323px; 
    height: 70px; 
    justify-content: left;
  } 
  .ppd-list-content h3 {
    justify-content: flex-start;
    text-align: justify;
    padding: 8px 16px 8px 16px;
    text-transform: capitalize;
    font-family: 'Times New Roman', Times, serif;
    font-weight: 500;
    font-size: x-large;
    border-width: 8px;
    color: #0a0a0a;
    padding: 8px 16px 8px 16px;
  }
  
  
  .ppd-picture-frame {
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
  .ppd-picture-frame img {
    width: 100%;
    height: 100%;
    object-fit: cover; /* Ensures the image covers the frame */
    object-position: top;
    /* Adjust the values to achieve the desired effect */
  }
  </style>
  