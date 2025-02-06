<template>
    <div @click="this.$emit('select')" tabindex="0" :class="`w-[18px] aspect-square outline-none transition-all rounded-[5px] border-[1px] border-solid cursor-pointer ${checked?'bg-[#fadb32] border-[#fadb32]':'bg-black border-[#525252]'}`">
        <img src="@/assets/check.svg" alt="">
    </div>
</template>

<script>
export default {
    props: ['checked']
}

</script>

<style lang="scss" scoped>

</style>