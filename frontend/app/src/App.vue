<template>
  <div class="div-main">
    <Navbar />
    <router-view class="div-body shadow" />
  </div>
</template>

<script>
import "bootstrap/dist/css/bootstrap.min.css";
import checkLogin from "./js/checkLogin.js";
import Navbar from "./components/Navbar.vue";

export default {
  components: {
    Navbar,
  },
  methods: {
    redirectToLogin: function () {
      console.log("REDIRECT TO LOGIN");
      this.$router.push("/login");
    },
  },
  data() {
    return {
      user: null,
    };
  },
  async mounted() {
    try {
      const data = await checkLogin();
      if (!data) {
        console.log("USER DOES NOT EXISTS.");
        this.redirectToLogin();
      }
    } catch (error) {
      console.log("REQUEST ERROR");
      this.redirectToLogin();
    }
  },
};
</script> 

<style scoped>
.div-body {
  margin: 5px 3px !important;
  padding: 20px;
  min-height: calc(100vh - 75px);
  min-width: 100vh;
  bottom: 0;
  
	display: flex;
	flex-direction: row;
	flex-wrap: wrap;
	justify-content: flex-start;
	align-items: stretch;
	align-content: flex-start;
}
</style>
<style>
.col-12.required .form-label:after {
  content:"*";color:red;
}
</style>