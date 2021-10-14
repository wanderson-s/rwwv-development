<template>
	<transition name="fade">
		<div 
			v-if="alertShow" 
			class="alert" 
			:class="alertType" 
			role="alert" 
			>
			{{ alertText }}
		</div> 
	</transition>
</template>

<script>
export default {
	props: {
		alertText: {
			type: String,
			default: ''
		},
		alertShow: {
			type: Boolean,
			default: false
		},
		alertType: {
			type: String,
			default: 'alert-danger'
		}
	}
}
</script>

<style scoped>
.fade-enter-active, .fade-leave-active {
  transition: opacity .7s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>