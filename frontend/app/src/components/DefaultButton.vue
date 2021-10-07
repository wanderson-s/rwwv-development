<template>
    <button :disabled="buttonActive" :type="buttonType" :class="buttonColor"> 
        <i 
            :class="buttonIcon" 
            style="font-size: 1.2rem;" 
        ></i> 
        {{ buttonText }} 
    </button>
</template>

<script>
export default {
    name: 'DefaultButton',
    props:{
        buttonText: {
            type: String,
            default: ''},
        buttonColor: {
            type: String,
            default: 'btn btn-primary'
        },
        buttonIcon: {
            type: String,
            default: ''
        },
        buttonActive: {
            type: Boolean,
            default: false
        },
        buttonType: {
            type: String,
            default: 'submit'
        }
    }
}
</script>


<style scoped>

.btn-primary{
    color: #fff;
}
</style>