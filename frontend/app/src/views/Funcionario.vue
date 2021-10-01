<template>
  <p>funcionario</p>
</template>

<script>
import checkLogin from '../js/checkLogin.js'
export default {
  name: 'Employee',
  methods: {
    redirectToLogin: function () {
      console.log("REDIRECT TO LOGIN")
      this.$router.push("/login")
    }
  },
  async mounted (){
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
  }
}
</script>

<style>

</style>