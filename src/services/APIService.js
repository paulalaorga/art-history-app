import axios from 'axios';

// Base configuration for the axios instance
const API = axios.create({
  baseURL: 'https://art-database.onrender.com/data.json',
  headers: {
    'Content-Type': 'application/json',
    // Add other headers here
  }
});

// Handling Interceptors
API.interceptors.response.use(
  response => response,
  error => {
    // Handle errors
    console.error('API error:', error);
    return Promise.reject(error);
  }
);

// API methods
export default {
  // Fetch data method
  fetchData(endpoint) {
    return API.get(endpoint)
      .then(response => response.data)
      .catch(error => {
        throw error;
      });
  },

  // Post data method
  postData(endpoint, data) {
    return API.post(endpoint, data)
      .then(response => response.data)
      .catch(error => {
        throw error;
      });
  },

  // Update data method
  updateData(endpoint, data) {
    return API.put(endpoint, data)
      .then(response => response.data)
      .catch(error => {
        throw error;
      });
  },

  // Delete data method
  deleteData(endpoint) {
    return API.delete(endpoint)
      .then(response => response.data)
      .catch(error => {
        throw error;
      });
  }
};
