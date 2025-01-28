<template>
    <div>

    </div>
</template>

<script>
export default {
    mounted(){
        if(confirm("Are you sure you want to logout?")){
            localStorage.removeItem('token')
            history.back()
        }else{
            this.$router.push('/')
        }
    }
}
</script>

<style lang="css" scoped>

</style>