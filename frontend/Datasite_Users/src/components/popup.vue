<template>
    <div :class="`fixed ${$genericStore.popup.shown?'sclae-100':'scale-0'} transition-all pointer-events-auto select-text px-[15px] py-[10px] top-[50%] translate-y-[calc(-50%-100px)] border-[1px] border-solid border-[#7e7e7e] rounded-[12px] bg-[#3d3d3d] w-[400px] max-w-[90%] mx-auto right-0 left-0 h-[190px] z-50 shadow-[#5f5f5f] shadow-xl`">
        <h1 class="text-[20px] text-gradient-yellow w-fit">Confirm</h1>
        <p class="opacity-90 h-[100px] overflow-hidden">{{ $genericStore.popup.message }}</p>
        <div class="ml-auto w-fit flex gap-[5px]">
            <button @click="$genericStore.decline_current_popup" class="w-[70px] h-[40px] hover:bg-[#dc262642] transition-all rounded py-[5px] justify-center flex items-center gap-[2px]">
                <img src="@/assets/close.svg" alt="" class="h-[60%] aspect-auto">
                <p>No</p>
            </button>
            <button @click="$genericStore.confirm_current_popup" class="w-[70px] h-[40px] hover:bg-[#fadb32] text-[#fadb32] items-center flex justify-center hover:text-black border-solid border-[2px] border-[#fadb32] transition-all rounded py-[5px]">
                <svg class="h-[70%] aspect-auto relative top-[2px]" xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="currentColor"><path d="M382-240 154-468l57-57 171 171 367-367 57 57-424 424Z"/></svg>
                <p>Yes</p>
            </button>
        </div>
    </div>
</template>

<script>
export default {

}
</script>

<style lang="css" scoped>

</style>