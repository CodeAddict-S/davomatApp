<template>
    <top_headers/>
    <div class="flex h-screen w-full mx-auto">
        <sidebar/>
        <div :style="{width: $genericStore.sidebar_open?'calc(100% - 150px)':'100%'}" :class="`shrink-1 overflow-auto`" >
            <RouterView/>
        </div>
    </div>
</template>

<script>
import sidebar from './components/sidebar.vue'
import top_headers from './components/top_headers.vue'
import { inject } from 'vue';

export default {
    name: 'App',
    components: {
        sidebar,
        top_headers
    },
}
</script>

<style>
.bg-gradient-yellow{
    background: linear-gradient(-90deg, rgba(250,234,50,1) 0%, rgba(250,219,50,1) 42%, rgba(250,181,50,1) 100%);
}
.hover\:bg-gradient-yellow:hover{
    background-image: linear-gradient(-90deg, rgba(250,234,50,1) 0%, rgba(250,219,50,1) 42%, rgba(250,181,50,1) 100%);
    color: transparent;
    background-clip: text;
}
.bg-gradient-yellow-rotated{
    background: linear-gradient(90deg, rgba(250,234,50,1) 0%, rgba(250,219,50,1) 42%, rgba(250,181,50,1) 100%);
}
.hover\:bg-gradient-yellow-rotated:hover{
    background-image: linear-gradient(90deg, rgba(250,234,50,1) 0%, rgba(250,219,50,1) 42%, rgba(250,181,50,1) 100%);
    color: transparent;
    background-clip: text;
}
.text-gradient-yellow{
    background-image: linear-gradient(-90deg, rgba(250,234,50,1) 0%, rgba(250,219,50,1) 42%, rgba(250,181,50,1) 100%);
    color: transparent;
    background-clip: text;
}
.hover\:text-gradient-yellow:hover{
    background-image: linear-gradient(-90deg, rgba(250,234,50,1) 0%, rgba(250,219,50,1) 42%, rgba(250,181,50,1) 100%);
    color: transparent;
    background-clip: text;
}
.text-gradient-yellow-rotated{
    background-image: linear-gradient(90deg, rgba(250,234,50,1) 0%, rgba(250,219,50,1) 42%, rgba(250,181,50,1) 100%);
    color: transparent;
    background-clip: text;
}
.hover\:text-gradient-yellow-rotated:hover{
    background-image: linear-gradient(90deg, rgba(250,234,50,1) 0%, rgba(250,219,50,1) 42%, rgba(250,181,50,1) 100%);
    color: transparent;
    background-clip: text;
}
.text-yellow{
    color: #fadb32
}
.bg-yellow{
    background-color: #fadb32;
}
.shadow-custom-yellow{
    box-shadow: 0px 0px 10px 0px rgba(250,220,50,1);
}
.shadow-custom-yellow-focus:focus{
    box-shadow: 0px 0px 10px 0px rgba(250,220,50,1);
}
.scrollbar-dark {
    scrollbar-width: initial;
    scrollbar-color: #2e2e2e #1e1e1e;
}

.scrollbar-dark::-webkit-scrollbar {
    width: 8px;
}

.scrollbar-dark::-webkit-scrollbar-track {
    background: #1e1e1e;
}

.scrollbar-dark::-webkit-scrollbar-thumb {
    background-color: #2e2e2e;
    border-radius: 10px;
    border: 2px solid #1e1e1e;
}
input[type="time"]::-webkit-calendar-picker-indicator {
    filter: invert(100%);
}
</style>