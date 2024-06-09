<template>
  <div class="era-sm-light">
    <div class="era-sm-header-frame">
      <div class="era-sm-header-frame2">
        <div class="era-sm-header-frame3">
          <div v-if="foundEra" class="era-sm-art-history" @click="goBack">
            {{ foundEra.era }}
          </div>
        </div>
      </div>
    </div>
    <div class="era-sm-timeline-frame">
      <div class="era-sm-timeline-frame1">
        <div class="era-sm-timeline-frame2">
          <div class="era-sm-timeline-frame3">
            <v-list v-if="foundEra" class="sm-timeline-content-list">
              <v-list-item
                v-for="period in foundEra.periods"
                :key="period.period"
                :picture="period.picture"
              >
                <router-link
                  :to="{ name: 'PeriodPage', params: { id: period.period } }"
                >
                  <div class="era-sm-timeline-period">{{ period.period }}</div>
                  <img
                    class="era-sm-period-image"
                    :src="period.picture"
                    alt="Picture Frame"
                /></router-link>
              </v-list-item>
            </v-list>
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
  name: "EraPageSmall",
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

<style>
.era-sm-light {
  background-color: #fff;
  display: flex;
  max-width: 480px;
  min-width: 375px;
  width: 100%;
  flex-direction: column;
  margin: 0 auto;
  font-family: "Times New Roman", Times, serif;
}
.era-sm-header-frame {
  background-color: #322c2c;
  display: flex;
  width: 100%;
  flex-direction: column;
  color: #322c2c;
  font-weight: 700;
  justify-content: center;
  padding: 7px 12px;
}
.era-sm-header-frame2 {
  background-color: #fffafa;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 4px 7px;
  box-sizing: border-box;
}
.era-sm-header-frame3 {
  background-color: #322c2c;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 6px 13px;
  display: flex;
  width: 100%;
  height: 100%;
}
.era-sm-art-history {
  font-family: "Times New Roman", Times, serif;
  background-color: #fffafa;
  text-align: center;
  text-transform: uppercase;
  font-size: 45px;
  text-overflow: ellipsis;
  letter-spacing: clamp(0.05em, 0.1vw, 0.2em);
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
  border: solid 8px #322c2c;
  background-color: #fffafa;
  color: #322c2c;
  padding: 8px;
  text-transform: uppercase;
  text-align: center;
  font-size: 35px;
  font-family: "Times New Roman", Times, serif;
  font-weight: 700;
  font-size: calc(2vw + 2vh + 2vmin);
  overflow-y: hidden;
}
.era-sm-period-image {
  margin-top: 8px;
  display: flex;
  flex-direction: column;
  max-width: 400px;
  max-height: 250px;
  filter: grayscale(50%) brightness(90%) contrast(110%) saturate(10%);
  overflow: hidden;
  object-position: center;
  align-items: center;
  object-fit: contain;
  border: solid 8px #322c2c;
}
img {
  width: auto;
  height: auto;
  object-position: center;
  position: relative;
}
a {
  text-decoration: none;
  text-align: -webkit-center;

}
</style>
