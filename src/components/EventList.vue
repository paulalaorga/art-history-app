<template>
    <div>
      <h2>Events List</h2>
      <ul>
        <li v-for="event in events" :key="event.id">
          {{ event.name }} - {{ event.date }}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'EventList',
    data() {
      return {
        events: []
      }
    },
    mounted() {
      this.fetchEvents();
    },
    methods: {
      fetchEvents() {
        axios.get('/api/events')
          .then(response => {
            this.events = response.data;
          })
          .catch(error => {
            console.error("There was an error fetching the events:", error);
          });
      }
    }
  }
  </script>
  
  <style>
  /* Add your CSS styling here */
  </style>
  