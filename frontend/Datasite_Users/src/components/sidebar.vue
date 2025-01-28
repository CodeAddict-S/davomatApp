<template>
    <div class="flex">
        <div ref="sidebar" :style="{borderRightWidth: held_mouse?'3px':'1px'}" :class="`w-[200px] shrink-0 bg-[#222222] shadow-xl border-solid border-[#cfcfcf] shadow-[#555555] h-full`">
            <div ref="sidebar_inside">
                <div style="box-shadow: -4px 8px 8px -8px darkgray;" :class="`z-[10] relative border-t-[3px] border-solid border-[#fadb32] ${current_link=='/sign-in/'?'mt-[2px]':'mt-[48px]'} cursor-pointer flex justify-between px-[10px] bg-[#4d4d4d]`">
                    <p class="font-semibold text-[17px] select-none">Users</p>
                </div>
                <div :class="`h-[${user_links.length*30}px] z-[9] relative transition-all overflow-hidden`">
                    <RouterLink :to="item.link" v-for="item in user_links">
                        <div class="text-light h-[30px] pl-[20px] opacity-90 shrink-0 py-[2px]" :style="{ 'background-color': current_link == item.link ? '#636363' : '#525252' }">
                            <p>{{ item.name }}</p>
                        </div>
                        <hr class="opacity-80">
                    </RouterLink>
                </div>
                <div style="box-shadow: -4px 8px 8px -8px darkgray;" class="z-[11] relative border-t-[3px] border-solid border-[#fadb32] mt-[2px] cursor-pointer flex justify-between px-[10px] bg-[#4d4d4d]">
                    <p class="font-semibold text-[17px] select-none">Courses</p>
                </div>
                <div :class="`h-[${course_links.length*30}px] z-[7] relative transition-all overflow-hidden`">
                    <RouterLink :to="item.link" v-for="item in course_links">
                        <div class="text-light h-[30px] pl-[20px] opacity-90 shrink-0 py-[2px]" :style="{ 'background-color': current_link == item.link ? '#636363' : '#525252' }">
                            <p>{{ item.name }}</p>
                        </div>
                        <hr class="opacity-80">
                    </RouterLink>
                </div>
                <div style="box-shadow: -4px 8px 8px -8px darkgray;" class="z-[11] relative border-t-[3px] border-solid border-[#fadb32] mt-[2px] cursor-pointer flex justify-between px-[10px] bg-[#4d4d4d]">
                    <p class="font-semibold text-[17px] select-none">Account</p>
                </div>
                <div :class="`h-[${account_links.length*30}px] z-[7] relative transition-all overflow-hidden`">
                    <RouterLink :to="item.link" v-for="item in account_links">
                        <div class="text-light h-[30px] pl-[20px] opacity-90 shrink-0 py-[2px]" :style="{ 'background-color': current_link == item.link ? '#636363' : '#525252' }">
                            <p>{{ item.name }}</p>
                        </div>
                        <hr class="opacity-80">
                    </RouterLink>
                </div>
            </div>
        </div>
        <div ref="drag_sidebar" class="h-full w-[20px] fixed cursor-w-resize" :style="{left: sidebar_closed?'10px':'190px'}" @pointerdown="held_mouse=true" @mousedown="held_mouse=true"></div>
    </div>
</template>

<script>
import { RouterLink } from 'vue-router';

export default {
    name: 'Sidebar',
    data() {
        return {
            user_links: [
                {
                    "name": "All Users",
                    "link": "/"
                },
                {
                    "name": "Employees",
                    "link": "/employees/"
                },
                {
                    "name": "Students",
                    "link": "/students/"
                }
            ],
            course_links: [
                {
                    "name": "All Courses",
                    "link": "/courses/"
                }
            ],
            account_links: [
                {
                    "name": "Login",
                    "link": "/sign-in/"
                },
                {
                    "name": "Logout",
                    "link": "/logout/"
                }
            ],
            current_link: this.$route.path,
            held_mouse: false,
            sidebar_closed: false,
        }
    },
    watch: {
        $route(to, from) {
            this.current_link = to.path;
        },
        held_mouse(new_held_mouse){
            if(new_held_mouse){
                document.body.style.userSelect = 'none'
            }else{
                document.body.style.userSelect = 'auto'
            }
        },
        sidebar_closed(new_sidebar){
            this.$genericStore.sidebar_open = !new_sidebar
        }
    },
    mounted(){
        document.addEventListener('touchend', (event)=>{
            if(this.held_mouse && !this.sidebar_closed){
                event.changedTouches[0].pageX<150?this.$refs['sidebar'].style.width='20px':'';
                event.changedTouches[0].pageX<150?this.$refs['sidebar_inside'].style.display='none':'';
                if(event.changedTouches[0].pageX<150){
                    this.sidebar_closed = true  
                }
            }
            else if(this.held_mouse && this.sidebar_closed){
                event.changedTouches[0].pageX>100?this.$refs['sidebar'].style.width='200px':'';
                event.changedTouches[0].pageX>100?this.$refs['sidebar_inside'].style.display='initial':'';
                if(event.changedTouches[0].pageX>100){
                    this.sidebar_closed = false
                }
            }            
            this.held_mouse = false
        })  
        document.addEventListener('mouseup', (event)=>{
            if(this.held_mouse && !this.sidebar_closed){
                event.clientX<150?this.$refs['sidebar'].style.width='20px':'';
                event.clientX<150?this.$refs['sidebar_inside'].style.display='none':'';
                if(event.clientX<150){
                    this.sidebar_closed = true  
                }
            }
            else if(this.held_mouse && this.sidebar_closed){
                event.clientX>100?this.$refs['sidebar'].style.width='200px':'';
                event.clientX>100?this.$refs['sidebar_inside'].style.display='initial':'';
                if(event.clientX>100){
                    this.sidebar_closed = false
                }
            }            
            this.held_mouse = false
        })  
        this.$refs.drag_sidebar.addEventListener('touchmove', (event)=>{
            event.preventDefault()
        })
    },
}
</script>

<style scoped>

</style>