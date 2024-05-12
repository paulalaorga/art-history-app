const { defineConfig } = require('@vue/cli-service');

module.exports = {
  publicPath: process.env.NODE_ENV === 'production'
    ? '/repository-name/'  // replace 'repository-name' with your GitHub repository name
    : '/'
}
