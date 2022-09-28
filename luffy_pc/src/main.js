import Vue, {set} from 'vue'
import App from './App'
import router from './router'
import settings from "./settings";
Vue.config.productionTip = false
Vue.prototype.$settings = settings
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(ElementUI);
//导入css初始化文件
import '../static/css/reset.css'
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
