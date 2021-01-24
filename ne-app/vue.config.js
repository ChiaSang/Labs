module.exports = {
  "transpileDependencies": [
    "vuetify"
<<<<<<< HEAD
  ],
  publicPath: '/',
  outputDir: "dist",
  devServer: {
    proxy: {
      '/posts': { //访问路径，可以自己设置，
        target: 'http://jsonplaceholder.typicode.com/', //代理接口，即后端运行所在的端口
        changeOrigin: true, //设置是否跨域
        ws: true,
        pathRewrite: { //访问路径重写
          '^/posts': ''
        }
      }
    }
  }
=======
  ]
>>>>>>> a96517be5f9a608192f6efc6fc960457dc596edd
}