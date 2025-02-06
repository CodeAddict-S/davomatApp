<template>
    <div :class="`flex fixed z-40 top-[70px] transition-all h-full ${$genericStore.sidebar_closed?'translate-x-[-200%]':''}`">
        <div ref="sidebar" :class="`w-[330px] bg-[#222222] shrink-0 h-[80%] scrollbar-dark rounded-[12px] overflow-auto max-h-[1000px] shadow-xl border-solid border-[#cfcfcf] shadow-[#555555]`">
            <div ref="sidebar_inside" class="px-[20px] py-[20px] overflow-auto">
                <div class="flex items-center gap-[5px] mb-[10px]">
                    <img src="@/assets/group.svg" alt="">
                    <p class="font-semibold text-[17px] select-none">USERS</p>
                </div>
                <div :class="`z-[9] relative transition-all overflow-hidden mb-[10px]`">
                    <RouterLink :to="item.link" v-for="item in user_links">
                        <div :class="`text-light rounded py-[10px] pl-[20px] opacity-90 shrink-0 ${current_link==item.link?'bg-[#626262]':'hover:bg-[rgba(51,51,51,.9)]'}`">
                            <p>{{ item.name }}</p>
                        </div>
                    </RouterLink>
                </div>
                <div class="flex items-center gap-[5px] mb-[10px]">
                    <img src="@/assets/notebook.svg" alt="">
                    <p class="font-semibold text-[17px] select-none">COURSES</p>
                </div>
                <div :class="`z-[9] relative transition-all overflow-hidden mb-[10px]`">
                    <RouterLink :to="item.link" v-for="item in course_links">
                        <div :class="`text-light rounded py-[10px] pl-[20px] opacity-90 shrink-0 ${current_link==item.link?'bg-[#626262]':'hover:bg-[rgba(51,51,51,.9)]'}`">
                            <p>{{ item.name }}</p>
                        </div>
                    </RouterLink>
                </div>
                <div class="flex items-center gap-[5px] mb-[10px]">
                    <img src="@/assets/account.svg" alt="">
                    <p class="font-semibold text-[17px] select-none">ACCOUNTS</p>
                </div>
                <div :class="`z-[9] relative transition-all overflow-hidden mb-[10px]`">
                    <RouterLink :to="item.name!=='Logout'?item.link:''" v-for="item in account_links">
                        <div v-if="item.name!=='Logout'" :class="`text-light rounded py-[10px] pl-[20px] opacity-90 shrink-0 ${current_link==item.link?'bg-[#626262]':'hover:bg-[rgba(51,51,51,.9)]'}`">
                            <p>{{ item.name }}</p>
                        </div>
                        <div @click="logout" v-else-if="item.name==='Logout'" :class="`text-light rounded py-[10px] pl-[20px] opacity-90 shrink-0 ${current_link==item.link?'bg-[#626262]':'hover:bg-[rgba(51,51,51,.9)]'}`">
                            <p>{{ item.name }}</p>
                        </div>
                    </RouterLink>
                </div>
            </div>
        </div>
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
        }
    },
    watch: {
        $route(to, from) {
            this.current_link = to.path;
        },
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
    },
    methods: {
        logout(){
            this.$genericStore.confirm_popup("Are you sure you want to logout?").then((response)=>{
                if(response){
                    localStorage.removeItem('token')
                    location.reload()
                }
            })
        }
    }
}
</script>

<style scoped>

</style>