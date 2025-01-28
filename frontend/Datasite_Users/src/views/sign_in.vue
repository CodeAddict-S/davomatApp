<template>
    <div class="container mx-auto max-w-[600px] relative top-[-50px] text-white">
        <form ref="form" v-on:submit.prevent="getToken" method="post" class="relative top-[75px] bg-[#242424] rounded-[20px] shadow-2xl shadow-white py-[25px] px-[20px] ">
            <h1 class="text-[30px] mb-[20px] text-gradient-yellow w-fit font-bold">Sign in</h1>
            <div class="gap-[10px] flex flex-col">
                <div class="flex flex-col gap-[10px]">
                    <label for="username" class="w-[100px] font-medium">Username: </label>
                    <input v-model="username" placeholder="User101" type="text" name="username" id="username" class="rounded-[12px] bg-[#5f5f5f] shadow-custom-yellow-focus h-[50px] w-full font-medium outline-none px-[20px] transition-all duration-700">
                </div>
                <div class="flex flex-col gap-[10px] relative z-10">
                    <label for="password" class="w-[100px] font-medium">Password: </label>
                    <input v-model="password" placeholder="********" type="password" name="username" id="password" class="rounded-[12px] bg-[#5f5f5f] shadow-custom-yellow-focus font-medium h-[50px] w-full outline-none px-[20px] transition-all duration-700">
                </div>
                <h1 :class="`absolute ${operation===0?'hidden':'block'} bottom-[100px] transition-all z-0 px-[20px] rounded-b-[12px] pt-[10px] w-[calc(100%-40px)]`" :style="{background: operation===1?'green':'red'}">{{ operation===1?'Success!':'Something went wrong' }}</h1>
                <button class="w-fit px-[30px] text-white font-semibold py-[10px] rounded mx-auto mt-[40px] bg-gradient-yellow-rotated active:opacity-80 transition-all">Submit</button>
            </div>
        </form>
    </div>
</template>

<script>
export default {
    data(){
        return {
            username: '',
            password: '',
            operation: 0,
        }
    },
    methods: {
        getToken(){
            this.$api.post('token/', {
                username: this.username,
                password: this.password
            }).then(response=>{
                if(response.status===200){
                    localStorage.setItem('token', JSON.stringify(response.data))
                    this.operation = 1
                    setTimeout(()=>{
                        location.href = '/'
                    }, 2000)
                }else{
                    this.operation = 2
                }
            }).catch(()=>{
                this.operation = 2
            })
            this.$refs['form'].reset()
        }
    }
}
</script>

<style lang="css" scoped>
</style>