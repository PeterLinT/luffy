import Vue, {set} from 'vue'
import App from './App'
import router from './router'
import settings from "./settings";
Vue.config.productionTip = false
Vue.prototype.$settings = settings
require('video.js/dist/video-js.css')
require('vue-video-player/src/custom-theme.css')
import VideoPlayer from 'vue-video-player'
Vue.use(VideoPlayer);
// vuex 的 store
import store from './store/index';
// element-ui 初始化加载
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(ElementUI);
//导入css初始化文件
import '../static/css/reset.css'

// 从node_modules目录中导入包
import axios from 'axios';
// 允许ajax发送请求时附带cookie
axios.defaults.withCredentials = false;
// 把对象挂载vue中
Vue.prototype.$axios = axios;
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
})
