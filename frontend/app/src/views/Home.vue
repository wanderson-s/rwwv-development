<template>
  <div class="main-container">
    <Navbar :user="user"/>
    <p> Home - {{ user }} </p>
  </div>
</template>

<script>
import checkLogin from '../js/checkLogin'
import Navbar from '../components/Navbar.vue'

export default {
  name: 'Home',
  data() {
    return {
      user: null
    }
  },
  components: {
    Navbar
  },
  async created(){
    if (!this.user){
      const data = await checkLogin()
      if(data){
        console.log("USER EXISTS.")
        this.user = data
        this.$emit('resetuser', this.user)
      }else{
        console.log("USER DOES NOT EXISTS.")
        this.$router.push({ 
          name: 'Login', 
          path: '/login', 
        })
      }
    }
  }
}
</script>
