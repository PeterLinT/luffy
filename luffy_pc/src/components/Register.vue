<template>
  <div class="box">
    <img src="../../static/image/Loginbg.3377d0c.jpg" alt="">
    <div class="register">
      <div class="register_box">
        <div class="register-title">注册路飞学城</div>
        <div class="inp">
          <input v-model="username" type="text" placeholder="请输入用户名" class="user">
          <!--          <div id="geetest"></div>-->
          <input v-model="password" type="text" placeholder="请输入密码" class="user">
          <input v-model="password2" type="text" placeholder="请重复密码" class="user">
          <button class="register_btn" @click="registerclick">注册</button>
          <p class="go_login">已有账号
            <router-link to="/login">直接登录</router-link>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Register',
  data() {
    return {
      password: "",
      password2: "",
      username: "",
      validateResult: false,
    }
  },
  created() {
  },
  methods: {
    registerclick() {
      this.$axios.post(`${this.$settings.HOST}/user/register/`, {
        username: this.username, password: this.password, password2: this.password2
      }, {
        responseType: "json",
      }).then(res => {
        console.log(res.data)
        localStorage.removeItem("token");
        let data = res.data;
        sessionStorage.token = data.token;
        sessionStorage.id = data.id;
        sessionStorage.username = data.username;
        // 注册成功以后默认表示已经登录了,跳转用户中心的页面
        this.$router.push("/");
        alert("注册成功!");
      }).catch(err => {
        let data = err.response.data
        let mss = ''
        for (let i in data) {
          mss = data[i]
        }
        this.$message.error(`对不起注册失败!${mss}`)
      })
    }
  },

};
</script>

<style scoped>
.box {
  width: 100%;
  height: 100%;
  position: relative;
  overflow: hidden;
}

.box img {
  width: 100%;
  min-height: 100%;
}

.box .register {
  position: absolute;
  width: 500px;
  height: 500px;
  top: 0;
  left: 0;
  margin: auto;
  right: 0;
  bottom: 0;
  top: -338px;
}

.register .register-title {
  width: 100%;
  font-size: 24px;
  text-align: center;
  padding-top: 30px;
  padding-bottom: 30px;
  color: #4a4a4a;
  letter-spacing: .39px;
}

.register-title img {
  width: 190px;
  height: auto;
}

.register-title p {
  font-family: PingFangSC-Regular;
  font-size: 18px;
  color: #fff;
  letter-spacing: .29px;
  padding-top: 10px;
  padding-bottom: 50px;
}

.register_box {
  width: 400px;
  height: auto;
  background: #fff;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, .5);
  border-radius: 4px;
  margin: 0 auto;
  padding-bottom: 40px;
}

.register_box .title {
  font-size: 20px;
  color: #9b9b9b;
  letter-spacing: .32px;
  border-bottom: 1px solid #e6e6e6;
  display: flex;
  justify-content: space-around;
  padding: 50px 60px 0 60px;
  margin-bottom: 20px;
  cursor: pointer;
}

.register_box .title span:nth-of-type(1) {
  color: #4a4a4a;
  border-bottom: 2px solid #84cc39;
}

.inp {
  width: 350px;
  margin: 0 auto;
}

.inp input {
  border: 0;
  outline: 0;
  width: 100%;
  height: 45px;
  border-radius: 4px;
  border: 1px solid #d9d9d9;
  text-indent: 20px;
  font-size: 14px;
  background: #fff !important;
}

.inp input.user {
  margin-bottom: 16px;
}

.inp .rember {
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: relative;
  margin-top: 10px;
}

.inp .rember p:first-of-type {
  font-size: 12px;
  color: #4a4a4a;
  letter-spacing: .19px;
  margin-left: 22px;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  /*position: relative;*/
}

.inp .rember p:nth-of-type(2) {
  font-size: 14px;
  color: #9b9b9b;
  letter-spacing: .19px;
  cursor: pointer;
}

.inp .rember input {
  outline: 0;
  width: 30px;
  height: 45px;
  border-radius: 4px;
  border: 1px solid #d9d9d9;
  text-indent: 20px;
  font-size: 14px;
  background: #fff !important;
}

.inp .rember p span {
  display: inline-block;
  font-size: 12px;
  width: 100px;
  /*position: absolute;*/
  /*left: 20px;*/

}

#geetest {
  margin-top: 20px;
}

.register_btn {
  width: 100%;
  height: 45px;
  background: #84cc39;
  border-radius: 5px;
  font-size: 16px;
  color: #fff;
  letter-spacing: .26px;
  margin-top: 30px;
}

.inp .go_login {
  text-align: center;
  font-size: 14px;
  color: #9b9b9b;
  letter-spacing: .26px;
  padding-top: 20px;
}

.inp .go_login span {
  color: #84cc39;
  cursor: pointer;
}
</style>
