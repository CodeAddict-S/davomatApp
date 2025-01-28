<template>
<div>
    <div class="flex flex-col gap-[5px] mx-auto w-full max-w-full justify-center">
        <div class="h-fit w-full shrink-1 mx-auto">
            <div style="box-shadow: 0px 1px 16px 0px darkgray;" class="flex flex-row z-[39] py-[5px] px-[10px] bg-[#505050] fixed justify-between gap-[5px] w-[calc(100%)] left-0">
                <button @click="openAddPopup" ref="add_student_button" class="w-full md:w-[250px] justify-center px-[10px] h-[30px] bg-gradient-yellow bg-[#006bba] text-white flex items-center rounded-[8px] gap-[5px] hover:bg-[#005aa0] transition-all duration-200">
                    <img src="@/assets/add.svg" alt="" class="h-[20px] object-contain">
                    <p class="text-[12px] truncate">Add {{ startsWithVowel(name)?'an '+name:'a '+name }}</p>
                </button>
                <div class="h-[30px] flex gap-[15px] items-center">
                    <input @input="searchTable(default_filter)" v-model="search" type="text" class="bg-[#555555] border-white border-[1px] border-solid w-full md:w-[250px] rounded-[12px] h-full outline-[#fadb32] px-[10px]" placeholder="filter">
                </div>
            </div>
            <div class="px-[10px] mt-[90px] md:mt-[50px] overflow-auto scrollbar-dark pb-[10px]" v-if="items_table.length>0&&request_success">
                <table ref="table" class="w-[calc(100%-50px)] ml-[50px] max-w-full relative">
                    <tbody class="w-full">
                        <tr class="relative">
                            <th>ID</th>
                            <th v-for="item in values">{{ item }}</th>
                        </tr>
                        <tr class="even:bg-[#222222] relative hover:bg-[#fadb32] hover:text-black" v-for="student in items_table" :key="student['id']">
                            <td class="text-right truncate">
                                <div class="flex">
                                    <!-- id -->
                                    <p class="text-right w-full truncate pl-[10px]">{{ student['id'] }}</p>
                                </div>
                                <div class="flex absolute top-0 left-[-50px]">
                                    <button @click="openEditPopup(student['id'])" class="h-[20px] mr-[5px] mt-[2px] shrink-0 rounded w-[20px] bg-[#006bba] hover:bg-[#1b5580] transition-all">
                                        <img src="@/assets/edit.svg" class="w-[80%] h-[80%] mx-auto object-contain">
                                    </button>
                                    <button @click="removeStudent(student['id'])" class="h-[20px] mt-[2px] shrink-0 rounded w-[20px] bg-red-600 hover:bg-[#9c3636] transition-all">
                                        <img src="@/assets/delete.svg" class="w-[80%] h-[80%] mx-auto object-contain">
                                    </button>
                                </div>
                            </td>
                            <td v-for="(value, index) in values" :key="value" :class="`relative ${value==='description'?'view-description':''}`">
                                <input v-if="value!=='description'" type="text" readonly :value="getValue(student, value)" class="bg-transparent outline-none readonly readonly-1">
                                <div v-else @click="toggleDescription(student['description'], student['id'])" class="flex w-[120px] items-center cursor-pointer select-none">
                                    <p readonly class="bg-transparent cursor-pointer w-[35px] relative bottom-[1px] font-medium outline-none readonly readonly-1">view</p>
                                    <svg class="w-[20px] h-[20px] relative top-[1px]" v-if="!(description_open&&student['id']===student_description_open_id)" xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="currentColor"><path d="M480-320q75 0 127.5-52.5T660-500q0-75-52.5-127.5T480-680q-75 0-127.5 52.5T300-500q0 75 52.5 127.5T480-320Zm0-72q-45 0-76.5-31.5T372-500q0-45 31.5-76.5T480-608q45 0 76.5 31.5T588-500q0 45-31.5 76.5T480-392Zm0 192q-146 0-266-81.5T40-500q54-137 174-218.5T480-800q146 0 266 81.5T920-500q-54 137-174 218.5T480-200Zm0-300Zm0 220q113 0 207.5-59.5T832-500q-50-101-144.5-160.5T480-720q-113 0-207.5 59.5T128-500q50 101 144.5 160.5T480-280Z"/></svg>
                                    <svg v-else class="w-[20px] h-[20px] relative top-[1px]" xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="currentColor"><path d="m644-428-58-58q9-47-27-88t-93-32l-58-58q17-8 34.5-12t37.5-4q75 0 127.5 52.5T660-500q0 20-4 37.5T644-428Zm128 126-58-56q38-29 67.5-63.5T832-500q-50-101-143.5-160.5T480-720q-29 0-57 4t-55 12l-62-62q41-17 84-25.5t90-8.5q151 0 269 83.5T920-500q-23 59-60.5 109.5T772-302Zm20 246L624-222q-35 11-70.5 16.5T480-200q-151 0-269-83.5T40-500q21-53 53-98.5t73-81.5L56-792l56-56 736 736-56 56ZM222-624q-29 26-53 57t-41 67q50 101 143.5 160.5T480-280q20 0 39-2.5t39-5.5l-36-38q-11 3-21 4.5t-21 1.5q-75 0-127.5-52.5T300-500q0-11 1.5-21t4.5-21l-84-82Zm319 93Zm-151 75Z"/></svg>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p v-else-if="request_success" class="text-center mt-[50px] mx-auto text-[20px] font-semibold">Nothing found</p>
            <div v-else class="mt-[50px]" v-show="!request_success">
                <h1 class="text-center font-medium text-[35px]">¯\_(ツ)_/¯</h1>
                <p class="text-center">couldn't fetch server, status: {{ status }}</p>
            </div>
        </div>
    </div>
    <div ref="add_student_popup" class="bg-[#474747] text-white w-[550px] z-50 px-[25px] py-[30px] max-w-full duration-[600ms] mx-auto fixed right-0 left-0 top-0 translate-y-[-200%] transition-all rounded-[20px] shadow-2xl h-fit">
        <div @click="closeAddPopup" class="absolute right-[10px] top-[10px] w-fit cursor-pointer">
            <img src="@/assets/close.svg" alt="">
        </div>
        <h1 class="font-semibold text-[20px]">Add {{ startsWithVowel(name)?'an '+name:'a '+name }}</h1>
        <form @submit.prevent="addStudent(); closeAddPopup()">
            <div v-for="key in keys" :key="key">
                <input v-if="key.type==='text'&&key.name!=='description'" v-model="add_values[key.name]" type="text" required minlength="5" :placeholder="key.name" class="w-full h-[40px] bg-[#555555] outline-[#fadb32] border-white border-[1px] border-solid px-[15px] py-[10px] rounded mt-[15px]">
                <textarea v-else-if="key.type==='text'&&key.name==='description'" rows=2 v-model="add_values[key.name]" type="text" required minlength="5" :placeholder="key.name" class="w-full bg-[#555555] outline-[#fadb32] border-white border-[1px] border-solid px-[15px] py-[10px] rounded mt-[15px]"></textarea>
                <select v-else-if="key.type==='choices'" v-model="add_values[key.name]" required minlength="5" class="w-full h-[40px] bg-[#555555] outline-[#fadb32] border-white border-[1px] border-solid px-[15px] rounded mt-[15px]">
                    <option :value="key_choices_choice.value" v-for="(key_choices_choice, index) in key.value" :key="index">{{ key_choices_choice.name }}</option>
                </select>
                <select v-else-if="key.type==='multi_choices'&&!isObject(add_values[key.name])" multiple v-model="add_values[key.name]" required minlength="5" class="w-full h-[80px] bg-[#555555] outline-[#fadb32] border-white border-[1px] border-solid px-[15px] py-[10px] rounded mt-[15px]">
                    <option :value="key_choices_choice.value" v-for="key_choices_choice in key.value">{{ key_choices_choice.name }}</option>
                </select>
                <select v-else-if="key.type==='multi_choices'&&isObject(add_values[key.name])" multiple v-model="add_values[key.name]['value']" required minlength="5" class="w-full h-[80px] bg-[#555555] outline-[#fadb32] border-white border-[1px] border-solid px-[15px] py-[10px] rounded mt-[15px]">
                    <option :value="key_choices_choice.value" v-for="key_choices_choice in key.value">{{ key_choices_choice.name }}</option>
                </select>
                <input v-else-if="key.type==='number'" v-model="add_values[key.name]" type="number" required minlength="5" :placeholder="key.name" class="w-full h-[40px] bg-[#555555] outline-[#fadb32] border-white border-[1px] border-solid px-[15px] rounded mt-[15px]">
                <input v-else-if="key.type==='time'" v-model="add_values[key.name]" type="time" required minlength="5" :placeholder="key.name" class="w-full h-[40px] bg-[#555555] outline-[#fadb32] border-white border-[1px] border-solid px-[15px] rounded mt-[15px]">
            </div>
            <button type="submit" class="bg-[#006bba] bg-gradient-yellow-rotated px-[45px] h-[40px] mt-[30px] rounded hover:bg-[#005aa0] text-white">Submit</button>
        </form>
    </div>
    <div ref="edit_student_popup" class="bg-[#474747] text-white z-50 w-[550px] px-[25px] py-[30px] max-w-full duration-[600ms] mx-auto fixed right-0 left-0 top-0 translate-y-[-200%] transition-all rounded-[20px] shadow-2xl h-fit">
        <div @click="closeEditPopup" class="absolute right-[10px] top-[10px] w-fit cursor-pointer">
            <img src="@/assets/close.svg" alt="">
        </div>
        <h1 class="font-semibold text-[20px]">Editing {{ edit_values['full_name'] }}</h1>
        <form @submit.prevent="editStudent(); closeEditPopup()">
            <div v-for="key in keys" :key="key">
                <input v-if="key.type==='text'&&key.name!=='description'" v-model="edit_values[key.name]" type="text" required minlength="5" :placeholder="key.name" class="w-full h-[40px] bg-[#555555] outline-[#fadb32] border-white border-[1px] border-solid px-[15px] py-[10px] rounded mt-[15px]">
                <textarea v-else-if="key.type==='text'&&key.name==='description'" rows=2 v-model="edit_values[key.name]" type="text" required minlength="5" :placeholder="key.name" class="w-full bg-[#555555] outline-[#fadb32] border-white border-[1px] border-solid px-[15px] py-[10px] rounded mt-[15px]"></textarea>
                <select v-else-if="key.type==='choices'" v-model="edit_values[key.name]" required minlength="5" class="w-full h-[40px] bg-[#555555] outline-[#fadb32] border-white border-[1px] border-solid px-[15px] rounded mt-[15px]">
                    <option :value="key_choices_choice.value" v-for="(key_choices_choice, index) in key.value" :key="index">{{ key_choices_choice.name }}</option>
                </select>
                <select v-else-if="key.type==='multi_choices'&&!isObject(edit_values[key.name])" multiple v-model="edit_values[key.name]" required minlength="5" class="w-full h-[80px] bg-[#555555] outline-[#fadb32] border-white border-[1px] border-solid px-[15px] py-[10px] rounded mt-[15px]">
                    <option :value="key_choices_choice.value" v-for="key_choices_choice in key.value">{{ key_choices_choice.name }}</option>
                </select>
                <select v-else-if="key.type==='multi_choices'&&isObject(edit_values[key.name])" multiple v-model="edit_values[key.name]['value']" required minlength="5" class="w-full h-[80px] bg-[#555555] outline-[#fadb32] border-white border-[1px] border-solid px-[15px] py-[10px] rounded mt-[15px]">
                    <option :value="key_choices_choice.value" v-for="key_choices_choice in key.value">{{ key_choices_choice.name }}</option>
                </select>
                <input v-else-if="key.type==='number'" v-model="edit_values[key.name]" type="number" required minlength="5" :placeholder="key.name" class="w-full h-[40px] bg-[#555555] outline-[#fadb32] border-white border-[1px] border-solid px-[15px] rounded mt-[15px]">
                <input v-else-if="key.type==='time'" v-model="edit_values[key.name]" type="time" required minlength="5" :placeholder="key.name" class="w-full h-[40px] bg-[#555555] outline-[#fadb32] border-white border-[1px] border-solid px-[15px] rounded mt-[15px]">
            </div>
            <button type="submit" class="bg-[#006bba] bg-gradient-yellow-rotated px-[45px] h-[40px] mt-[30px] rounded hover:bg-[#005aa0] text-white">Submit</button>
        </form>
    </div>
    <div ref="description" :class="`bg-[#363636] shadow-white scrollbar-dark overflow-ellipsis max-h-[400px] overflow-y-auto duration-200 z-50 w-[550px] px-[25px] py-[10px] max-w-full ease-out mx-auto fixed right-0 left-0 top-0 ${description_open?'translate-y-[20px]':'translate-y-[-200%]'} transition-all rounded-[20px] shadow-2xl h-fit`">
        <div @click="closeDescription" class="right-[10px] fixed top-[10px] w-fit cursor-pointer">
            <img src="@/assets/close-white.svg" alt="">
        </div>
        <p class="min-h-[25px] max-w-[550px]">{{ description }}</p>
    </div>
</div>
</template>

<script>
export default {
    props: {
        items: Array,
        request_success: Boolean,
        status: Number,
        default_add_values: Object,
        default_edit_values: Object,
        values: Array,
        keys: Array,
        api_link: String,
        name: String,
        default_filter: String
    },
    data(){
        return {
            description_open: false,
            description: 'description',
            student_description_open_id: 0,
            add_values: this.default_add_values,
            edit_values: this.default_edit_values,
            saved_edit_value: this.default_edit_values,
            saved_add_value: this.default_add_values,
            search: '',
            items_table: this.items,
        }  
    },
    mounted(){
        // detect outside click
        document.addEventListener('click', (event) => {
            const target = event.target;
            const add_popup = this.$refs['add_student_popup'];
            const button = this.$refs['add_student_button'];
            const description = this.$refs['description']
            const view_description_buttons = document.getElementsByClassName('view-description')
            
            try{
                if (!add_popup.contains(target)&&!button.contains(target)) {
                    this.closeAddPopup()
                }
                let clicked_view_button = true
                for(const view_description_button of view_description_buttons){
                    if (view_description_button.contains(target)){
                        clicked_view_button = false
                        break
                    }
                }
                if(clicked_view_button && !description.contains(target)){
                    this.closeDescription() 
                }
            }catch{}
        });
    },
    methods: {
        removeStudent(id){
            if(confirm("Are you sure you want to delete an element with id: "+id + "?")){
                this.$api.delete(this.api_link+id+'/').then(()=>{
                    this.items_table = this.items.filter(student => student['id'] !== id);
                })
                this.$emit('refetch')
            }
        },
        openAddPopup(){
            let popup = this.$refs['add_student_popup'];
            popup.style.transform = "translateY(20px)";
            this.closeEditPopup()
        },
        closeAddPopup(){
            let popup = this.$refs['add_student_popup'];
            popup.style.transform = "translateY(-200%)";
        },
        openEditPopup(id){
            const student = this.items.find(student => student['id'] === id);
            this.edit_values = {
                "id": student['id']
            }
            for(let value in this.values){
                this.edit_values[this.values[value]] = student[this.values[value]]
            }
            let popup = this.$refs['edit_student_popup'];
            popup.style.transform = "translateY(20px)";
            this.closeAddPopup()
        },
        closeEditPopup(){
            this.edit_values = this.saved_edit_value
            let popup = this.$refs['edit_student_popup'];
            popup.style.transform = "translateY(-200%)";
        },
        editStudent(){
            let filteredObject = {};
            for(const entry of Object.entries(this.edit_values)){
                if(entry[0] !== 'id'){
                    if(this.isObject(entry[1])){
                        filteredObject[entry[0]] = entry[1]['value']
                    }else{
                        filteredObject[entry[0]] = entry[1]
                    }
                }
            }
            this.$api.put(this.api_link+this.edit_values['id']+'/', filteredObject).then(response=>{
                console.log(response)
                this.$emit('refetch')
            })
        },
        addStudent(){
            this.$api.post(this.api_link, this.add_values).then(response=>{
                console.log(response)
                this.add_values = this.default_add_values
                let forms = document.getElementsByTagName('form')
                for(const form of forms){
                    form.reset()
                }
                this.$emit('refetch')
            })
        },
        openDescription(description, id){
            this.student_description_open_id = id
            this.description = description
            this.description_open = true
        },
        closeDescription(){
            this.description = ''
            this.description_open = false
        },
        toggleDescription(description, id){
            this.description = description
            if(this.description_open){
                if(this.student_description_open_id !== id){
                    this.student_description_open_id = id
                    this.closeDescription()
                    setTimeout(()=>{
                        this.openDescription(description, id)
                    }, 200)
                }else{
                    this.closeDescription()
                }
            }else{
                this.openDescription(description, id)
            }
        },
        getValue(student, value){
            return (typeof student[value] === 'object' && !Array.isArray(student[value]) && student[value] !== null)?student[value]['show']:student[value]
        },
        isObject(value){
            return (typeof value === 'object' && !Array.isArray(value) && value !== null)
        },
        startsWithVowel(word){
            return ['a', 'e', 'i', 'o'].includes(word[0].toLowerCase())
        },
        searchTable(value){
            this.items_table = this.items.filter(saved_item=>String(saved_item[value]).toLowerCase().match(this.search.toLowerCase()))
        },
        advancedSearchTable(value){}
    },
    watch: {
        items(new_items){
            this.items_table = new_items
        }
    }
}
</script>

<style lang="css" scoped>
tr, td , th, table{
    border: 1px solid lightgray;
}
td, th{
    padding-right: 10px;
    padding-left: 10px;
}
tr{
    height: 25px;
}
input{
    width: 100%;
}
</style>