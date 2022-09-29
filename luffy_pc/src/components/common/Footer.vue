<template>
  <div class="footer">
    <ul >
      <li v-for="nav in nav_list">
        <span v-if="nav.is_site"><a :href="nav.link">{{ nav.title }}</a></span>
        <span v-else><router-link :to="nav.link">{{ nav.title }}</router-link></span>
      </li>
    </ul>
    <p>Copyright © peterl.top版权所有 | 京ICP备17072161号-1</p>
  </div>
</template>

<script>
export default {
  name: "Footer",
  data() {
    return {
      nav_list: [],

    }
  },
  created() {
    this.get_nav()
  },
  methods: {
    get_nav() {
      this.$axios.get(`${this.$settings.HOST}/nav/footer/`, {})
        .then(res => {
          this.nav_list = res.data
        }).catch(err => {
        console.log(err)
      })
    }
  }

}
</script>

<style scoped>
.footer {
  width: 100%;
  height: 128px;
  background: #25292e;
  color: #fff;
}

.footer ul {
  margin: 0 auto 16px;
  padding-top: 38px;
  width: 810px;
}

.footer ul li {
  float: left;
  width: 112px;
  margin: 0 10px;
  text-align: center;
  font-size: 14px;
}

.footer ul::after {
  content: "";
  display: block;
  clear: both;
}

.footer p {
  text-align: center;
  font-size: 12px;
}
a{
  color: white;
}
</style>
