<template>
	<div 
		v-if="alertShow" 
		class="alert alert-dismissible fade show" 
		:class="alertType" 
		role="alert" 
		>
		{{ alertText }}
		<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
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
