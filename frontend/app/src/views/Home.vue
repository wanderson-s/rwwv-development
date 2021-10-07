<template>
  <div class="home">
    <p>Home</p>
  </div>
</template>

<script>
import checkLogin from '../js/checkLogin.js'
import redirectToLogin from '../js/redirectLogin'

export default {
  name: 'Home',
  async mounted (){
    try {
      const data = await checkLogin()
      if(!data){
        console.log("USER DOES NOT EXISTS.")
        redirectToLogin(this)
      } 
    } catch (error) {
      console.log("REQUEST ERROR")
      redirectToLogin(this)
    }
  }
}
</script>
