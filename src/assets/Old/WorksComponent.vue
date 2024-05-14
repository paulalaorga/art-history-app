<template>
    <div class="works-container">
      <div v-for="work in works" :key="work.id" class="work">
        <h2>{{ work.Author }} - {{ work.Date }}</h2>
        <img :src="work.Image" :alt="work.Description" />
        <p>{{ work.Description }}</p>
        <p><strong>Museum:</strong> {{ work.Museum }}</p>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'WorksDisplay',
    data() {
      return {
        works: []
      };
    },
    methods: {
      fetchWorks() {
        axios.get('http://127.0.0.1:5000/api/items')
          .then(response => {
            const worksData = response.data.TimeLine.ClassicalEra[0].AncientGreece.Works;
            this.works = Object.values(worksData); // Transforming the object into an array
          })
          .catch(error => {
            console.error('There was an error fetching the works: ', error);
          });
      }
    },
    mounted() {
      this.fetchWorks();
    }
  };
  </script>
  
  <style>
  .work {
    border: 1px solid #ccc;
    padding: 10px;
    margin-bottom: 20px;
  }
  
  .work h2 {
    color: #333;
  }
  
  .work img {
    max-width: 100%;
    height: auto;
  }
  
  .works-container {
    max-width: 800px;
    margin: 0 auto;
  }
  </style>
  