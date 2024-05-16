module.exports = {
  publicPath: process.env.NODE_ENV === 'production' ? '/art-history-app/' : '/',
  devServer: {
    proxy: 'http://localhost:3000',
  },
  configureWebpack: {
    // configurations for webpack
  }
};
