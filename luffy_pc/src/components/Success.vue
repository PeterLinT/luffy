<template>
  <div class="success">
    <Header/>
    <div class="main">
        <div class="title">
          <div class="success-tips">
              <p class="tips1">您已成功购买 {{course_list.length}} 门课程！</p>
              <p class="tips2">你还可以加入QQ群 <span>747556033</span> 学习交流</p>
          </div>
        </div>
        <div class="order-info">
            <p class="info1"><b>付款时间：</b><span>{{pay_time | timeformat}}</span></p>
            <p class="info2"><b>付款金额：</b><span >{{real_price.toFixed(2)}}</span></p>
            <p class="info3"><b>课程信息：</b><span v-for="course in course_list">《<router-link :to="'/course/detail/'+course.id">{{course.name}}</router-link>》</span></p>
        </div>
        <div class="wechat-code">
<!--          <img src="../../static/image/server.cf99f78.png" alt="" class="er">-->
<!--          <p><img src="../../static/image/tan.svg" alt="">重要！微信扫码关注获得学习通知&amp;课程更新提醒！否则将严重影响学习进度和课程体验！</p>-->
        </div>
        <div class="study">
          <router-link to="/user/learn">立即学习</router-link>
        </div>
    </div>
    <Footer/>
  </div>
</template>

<script>
  import Header from "./common/Header"
  import Footer from "./common/Footer"
  export default{
    name:"Success",
    data(){
      return {
        pay_time: "",
        course_list:[],
        real_price:0,
      };
    },
    created(){
      // 把地址栏上面的支付结果，转发给后端
      this.alipayResultHander();
    },
    filters:{
        timeformat(value){
            let datetime = new Date(value);
            let Y = datetime.getFullYear(); // 年
            let m = datetime.getMonth()+1;
            let d = datetime.getDate();
            let H = datetime.getHours();
            let M = datetime.getMinutes();
            let S = datetime.getSeconds();
            m = m<10?'0'+m:m;
            d = d<10?'0'+d:d;
            H = H<10?'0'+H:H;
            M = M<10?'0'+M:M;
            S = S<10?'0'+S:S;
            return `${Y}-${m}-${d} ${H}:${M}`;
        }
    },
    methods:{
        alipayResultHander(){
            // 转发支付结果给后端服务器
            this.$axios.get(`${this.$settings.HOST}/payments/alipay/result/`+location.search).then(response=>{
                this.$message.success(response.data.message);
                localStorage.user_credit = response.data.credit;
                this.real_price = response.data.real_price;
                this.pay_time = response.data.pay_time;
                this.course_list = response.data.course_list;
            }).catch(error=>{
                this.$message.error(error.response.data.message);
                // this.$router.go(-1);
            })
        }
    },
    components:{
      Header,
      Footer,
    }
  }
</script>

<style scoped>
.success{
  padding-top: 80px;
}
.main{
    height: 100%;
    padding-top: 25px;
    padding-bottom: 25px;
    margin: 0 auto;
    width: 1200px;
    background: #fff;
}
.main .title{
    display: flex;
    -ms-flex-align: center;
    align-items: center;
    padding: 25px 40px;
    border-bottom: 1px solid #f2f2f2;
}
.main .title .success-tips{
    box-sizing: border-box;
}
.title img{
    vertical-align: middle;
    width: 60px;
    height: 60px;
    margin-right: 40px;
}
.title .success-tips{
    box-sizing: border-box;
}
.title .tips1{
    font-size: 22px;
    color: #000;
}
.title .tips2{
    font-size: 16px;
    color: #4a4a4a;
    letter-spacing: 0;
    text-align: center;
    margin-top: 10px;
}
.title .tips2 span{
    color: #ec6730;
}
.order-info{
    padding: 25px 48px;
    padding-bottom: 15px;
    border-bottom: 1px solid #f2f2f2;
}
.order-info p{
    display: -ms-flexbox;
    display: flex;
    margin-bottom: 10px;
    font-size: 16px;
}
.order-info p b{
  font-weight: 400;
  color: #9d9d9d;
  white-space: nowrap;
}
.wechat-code{
    display: flex;
    -ms-flex-align: center;
    align-items: center;
    padding: 25px 40px;
    border-bottom: 1px solid #f2f2f2;
}
.wechat-code>img{
    width: 100px;
    height: 100px;
    margin-right: 15px;
}
.wechat-code p{
    font-size: 14px;
    color: #d0021b;
    display: -ms-flexbox;
    display: flex;
    -ms-flex-align: center;
    align-items: center;
}
.wechat-code p>img{
    width: 16px;
    height: 16px;
    margin-right: 10px;
}
.study{
      padding: 25px 40px;
}
.study span{
  display: block;
  width: 140px;
  height: 42px;
  text-align: center;
  line-height: 42px;
  cursor: pointer;
  background: #ffc210;
  border-radius: 6px;
  font-size: 16px;
  color: #fff;
}
</style>
