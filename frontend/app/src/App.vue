<template>
  <div class="div-main">
    <Navbar/>
    <router-view class="div-body" />
  </div>

</template>

<script>
import "bootstrap/dist/css/bootstrap.min.css";
import checkLogin from './js/checkLogin.js'
import Navbar from './components/Navbar.vue'

export default {
  components: {
    Navbar, 
  },
  methods: {
    redirectToLogin: function () {
      console.log("REDIRECT TO LOGIN")
      this.$router.push("/login")
    }
  },
  data() {
    return { 
      }
  },
  async created (){
    try {
      const data = await checkLogin()
      if(!data){
        console.log("USER DOES NOT EXISTS.")
        this.redirectToLogin()
      }
    } catch (error) {
      console.log("REQUEST ERROR")
      this.redirectToLogin()
    }
    console.log(this.showMenu)
  }
}
</script> 

<style scoped>
.div-body {
  margin: 5px 3px;
  padding: 20px;
  border: 2px solid red;
  border-radius: 10px;
  height: calc(100vh - 75px);
  bottom: 0;
  }

</style>