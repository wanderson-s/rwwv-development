
module.exports = {
    devServer: {
      proxy: process.env.PROXY_URL || 'http://localhost:8001',
      disableHostCheck: true
    }
  }