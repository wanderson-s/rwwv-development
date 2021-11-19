<template>
  <div class="container g-0 p-1 m-0 d-flex justify-content-center">
		<p class="card-title pb-0 pt-0" style="font-size: 22px;">
			<i class="bi" :class="titleIcon" style="font-size: 28px;"></i>
			{{ titleText }}
		</p>
	</div>
</template>

<script>
export default {
	props: {
		titleText: {
			type: String,
			required: true
		},
		titleIcon: {
			type: String,
			required: 'bi-briefcase-fill'
		}
	}
}
</script>

<style scoped>
.container {
	width: 100%;
	border-top-left-radius: 7px;
	border-top-right-radius: 7px;
	background-color: black;
	color: white;
	border: black solid 1px;
}

</style>