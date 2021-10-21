<template>
	<nav class="navbar nav-tabs navbar-expand-lg border border-danger px-4 py-3 d-flex justify-content-between">
		<div class="navegation">
			<a 
				class="navbar-brand" 
				@click="$router.push('/')" 
				href="/"
				data-bs-toggle="tooltip" 
				data-bs-placement="bottom" 
				title="Tela de inicio"
			>
				<i class="bi bi-house-fill"></i>
				Inicio
			</a>
			<a 
				class="navbar-brand" 
				@click="$router.push('/funcionario')" 
				href="/funcionario"
				data-bs-toggle="tooltip" 
				data-bs-placement="bottom" 
				title="Tela de funcionários"
			>
				<i class="bi bi-people-fill"></i>
				Funcionários
			</a>
			<a 
				class="navbar-brand" 
				@click="$router.push('/bu')" 
				href="/bu"
				data-bs-toggle="tooltip" 
				data-bs-placement="bottom" 
				title="Tela de BUs"
			>
				<i class="bi bi-briefcase-fill"></i>
				BUs
			</a>
			<a 
				class="navbar-brand" 
				@click="$router.push('/orcamento')" 
				href="/orcamento"
				data-bs-toggle="tooltip" 
				data-bs-placement="bottom" 
				title="Tela de orçamentos"
			>
				<i class="bi bi-cash-stack"></i>
				Orçamentos
			</a>
		</div>
		<div class="user">
			<a class="navbar-brand" @click="$router.push('/orcamento')" href="/orcamento">
				<i class="bi bi-person-circle"></i>
				Usuário
			</a>
		</div>
	</nav>
</template>

<script>

export default {
    name: 'Navbar',
    data () {
        return {

        }
    },
}
</script>

<style scoped>
.bi {
	font-size: 28px;
}
.navbar {
  background-color: #dc3545;
}
.navbar-brand {
	color: white;
	padding: 5px; 
	border: #dc3545 solid 1px;
	border-radius: 7px;
}

.navbar-brand:hover, 
.navbar-brand:focus, 
.navbar-brand:active, 
.open .dropdown-toggle.navbar-brand {  
 background-color: #d04f5c; 
 border: white solid 1px;
} 
 
</style>