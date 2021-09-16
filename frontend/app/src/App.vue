<template>
  <div id="app">
    
    <router-view></router-view>

    <Footer v-show="true"/>
  </div>
</template>

<script>
import Footer from './components/Footer.vue'


export default {
  name: 'App',
  data(){
    return {
      showNavbarFooter: false
    }
  },
  components: {
    Footer
  },
  beforeCreate(){
    
  }
}
</script>


<style>
  body {
    display: flex;
    flex-direction: column;
    min-height: 100%;
  }
  .main-container {
    margin: 50px;
    min-height: 500px;
    max-height: 1200px;
  }
  .div-footer {
    position:fixed;
    bottom:0;
  }
  
</style>
