const { defineConfig } = require('@vue/cli-service');

module.exports = defineConfig({
  publicPath: process.env.NODE_ENV === 'production'
    ? '/art-history-app/'  
    : '/',
  devServer: {
    https: false, // Set true if you need HTTPS
    port: 8080, // Default is 8080, change it if necessary
    host: 'localhost',
    open: true, // Open the browser after server had been started
    client: {
      webSocketURL: 'ws://0.0.0.0:8080/ws',
    },
  },
});
