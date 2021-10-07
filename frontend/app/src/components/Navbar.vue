<template>
    <nav class="navbar navbar-expand-lg">
        <div class="item-pages">
            <a v-for="item in menuItem" :key=item.title class="navbar-brand" @click="$router.push(item.url)" :href="item.url">
                <img src="../assets/employee.png" width="30" height="30" class="d-inline-block align-top" alt="">
                {{ item.title }}
            </a>
        </div>
    </nav>
</template>

<script>

export default {
    name: 'Navbar',
    data () {
        return {
            menuItem: [
                {
                    title: 'Inicio',
                    url: '/',
                    //img:  "../assets/home.png"
                },
                {
                    title: 'Funcionários',
                    url: '/funcionario',
                    //img: "../assets/employee.png"
                },
                {
                    title: 'Orçamentos',
                    url: '/orcamento',
                    //img: "../assets/budget.png"
                }
            ]
        }
    },
    async mounted (){
        
    }
}
</script>

<style scoped>
.item-pages {
    padding: 10px 25px 10px;

}
.navbar {
    margin: 0px 4px;
    background-color: #dc3545;
    border-bottom-left-radius: 7px;
    border-bottom-right-radius: 7px;
}
.navbar-brand {
    color: white;
}
</style>