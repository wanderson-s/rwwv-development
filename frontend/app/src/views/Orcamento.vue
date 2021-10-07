<template>
  <p>orcamento</p>
</template>

<script>
import checkLogin from '../js/checkLogin.js'
import redirectToLogin from '../js/redirectLogin'

export default {
  name: 'Budget',
  data () {
    user: null
  },
  async mounted (){
    try {
      const data = await checkLogin()
      if(!data){
        console.log("USER DOES NOT EXISTS.")
        redirectToLogin(this)
        this.user = data
      }
    } catch (error) {
      console.log("REQUEST ERROR")
      redirectToLogin(this)
    }
  }
}
</script>

<style>

</style>