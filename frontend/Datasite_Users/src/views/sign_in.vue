<template>
    <div :class="`${operation!==0?'opacity-100':'opacity-0'} transition-all duration-[300ms] z-50`">
        <div v-if="operation===1" class="fixed top-[60px] px-[10px] py-[5px] right-[20px] w-[250px] max-w-full rounded-[12px] z-50 bg-[#13aa1b] overflow-hidden h-[57px] text-white">
            Success! Signed in as {{ username }}
        </div>
        <div v-else class="fixed top-[60px] px-[10px] py-[5px] right-[20px] w-[250px] max-w-full rounded-[12px] z-50 bg-red-700 overflow-hidden h-[57px] text-white">
            Failed, username or password might be wrong
        </div>
    </div>
    <div class="container mx-auto max-w-[600px] relative top-[-50px] text-white">
        <form ref="form" v-on:submit.prevent="getToken" method="post" class="relative top-[75px] bg-[#242424] rounded-[20px] shadow-2xl shadow-[#222] py-[25px] px-[20px] ">
            <h1 class="text-[30px] mb-[20px] text-gradient-yellow w-fit font-bold">Sign in</h1>
            <div class="gap-[10px] flex flex-col">
                <div class="flex flex-col gap-[10px]">
                    <label for="username" class="w-[100px] font-medium">Username: </label>
                    <input v-model="username" type="text" name="username" id="username" class="rounded-[12px] border-[#888] focus:border-[#fadb32] border-[2px] border-solid bg-[#111] shadow-custom-yellow-focus h-[50px] w-full font-medium outline-none px-[20px] transition-all duration-700">
                </div>
                <div class="flex flex-col gap-[10px] relative z-10">
                    <label for="password" class="w-[100px] font-medium">Password: </label>
                    <input v-model="password" type="password" name="username" id="password" class="rounded-[12px] border-[#888] focus:border-[#fadb32] border-[2px] border-solid bg-[#111] shadow-custom-yellow-focus font-medium h-[50px] w-full outline-none px-[20px] transition-all duration-700">
                </div>
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
            this.operation = 0
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