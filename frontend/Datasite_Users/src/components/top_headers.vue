<template>
    <header class="h-[50px] bg-[#1d1d1d] z-40 sticky top-0 shadow-xl w-full mx-auto flex items-center px-[10px]">
        <img @click="$genericStore.sidebar_closed=!$genericStore.sidebar_closed" src="@/assets/menu.svg" alt="" class="mr-[10px] hover:bg-[#2e2e2e] cursor-pointer rounded-full p-[5px] h-[65%] aspect-square">
        <RouterLink to="/" class="w-fit text-nowrap flex gap-[5px] h-[75%]">
            <img src="@/assets/logo.png" alt="" class="h-full aspect-square">
            <h1 class="text-[25px] font-bold text-[#fadb32]"><span class="text-gradient-yellow-rotated">Datasite</span> <span class="underline text-[21px] text-white">Academy</span></h1>
        </RouterLink>
        <RouterLink to="/sign-in/" class="ml-auto">
            <button class="bg-gradient-yellow text-[#1d1d1d] px-[10px] py-[5px] rounded-md">Login</button>
        </RouterLink>
    </header>
</template>

<script>

</script>

<style scoped>

</style>