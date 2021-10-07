<template>
	<div 
		v-if="alertShow" 
		class="alert" 
		:class="alertType" 
		role="alert" 
		>
		{{ alertText }}
	</div>
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
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>