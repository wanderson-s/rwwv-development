<template>
    <div class="nav-bar">
        <div class="menu-bar">
            <b-button class="button-menu" variant="secondary">Funcionário</b-button>
            <b-button class="button-menu" variant="secondary">Orçamento</b-button>
            <b-button class="button-menu" variant="secondary">Sobre</b-button>
        </div>
        <div class="user">
            <p>
                user {{ user }}
            </p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Navbar',
    data(){
        return {
            user: null
        }
    }
}
</script>

<style scoped>
    .nav-bar {
        display: flex;
        justify-content: space-between;
        padding: 10px;
        background-color: aqua;
    }
    .menu-bar {
        align-items: stretch;
    }
    .button-menu {
        margin-right: 5px;
    }
    
</style>