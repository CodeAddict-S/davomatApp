<template>
    <div>
        <div class="flex flex-col gap-[5px] mx-auto w-full max-w-full h-full min-w-[300px] justify-center">
            <div class="h-fit w-full shrink-1 mx-auto">
                <div class="bg-[#2b2b2b] w-[98%] mx-auto max-w-[1200px] h-fit py-[30px] rounded-[20px] mt-[20px] overflow-auto scrollbar-dark"
                    v-if="request_success">
                    <div
                        class="flex gap-[5px] w-[calc(100%-40px)] py-[15px] px-[20px] mx-auto border-[2px] rounded-[12px] border-solid border-[#757575] mb-[15px] h-fit">
                        <button @click="openAddPopup" ref="add_student_button"
                            class="h-[40px] w-[80px] flex rounded-[10px] bg-[#555555] hover:bg-[#646464] transition-all">
                            <div class="mx-auto overflow-hidden flex items-center relative top-[50%] translate-y-[-50%]">
                                <img src="@/assets/plus.svg" alt="" class="h-[22px]">
                                <p class="relative">New</p>
                            </div>
                        </button>
                        <button @click="deleteSelected" ref="delete_student_button"
                            :class="`h-[40px] w-[100px] flex rounded-[10px] bg-[#555555] ${count_selected_items() > 0 ? 'hover:bg-[#646464]' : 'opacity-50 cursor-default'} transition-all`">
                            <div class="mx-auto overflow-hidden flex items-center relative top-[50%] translate-y-[-50%]">
                                <img src="@/assets/delete.svg" alt="" class="h-[22px]">
                                <p class="relative">Remove</p>
                            </div>
                        </button>
                    </div>
                    <div
                        class="flex md:flex-row flex-col md:gap-0 gap-[8px] w-full md:px-[35px] px-[10px] justify-between mb-[10px]">
                        <h1 class="text-[18px] truncate relative top-[5px]">Manage {{ name }}s</h1>
                        <div class="h-[38px] flex shrink-0 gap-[15px] items-center relative">
                            <img src="@/assets/search.svg" alt=""
                                class="absolute left-[10px] top-[50%] translate-y-[-50%] z-20 scale-95 opacity-80">
                            <input @input="searchTable(default_filter)" v-model="search" type="text"
                                class="bg-black border-[#acacac] pl-[38px] transition-all border-[2px] border-solid w-full md:w-[250px] rounded-[8px] h-full outline-none focus:border-[#fadb32] px-[10px]"
                                placeholder="filter...">
                        </div>
                    </div>
                    <div class="w-[calc(100%-30px)] mx-auto overflow-auto">
                        <table ref="table" class="w-[1250px] mx-auto relative">
                            <tbody class="w-full">
                                <tr class="relative h-[50px] cursor-pointer select-none">
                                    <th class="w-[50px]">
                                        <checkBox ref="check_all" @select="select_all()"
                                            :checked="are_all_selected()"/>
                                    </th>
                                    <th @click="order['by'] === 'id' ? order['asc'] = !order['asc'] : order['by'] = 'id'; order_table()"
                                        class="text-center wmin--[46px ] hover:bg-[rgba(81,81,81,0.6)]">
                                        <div class="flex gap-[5px]">
                                            <p>ID</p>
                                            <img src="@/assets/swap.svg" alt="" v-if="order['by'] !== 'id'"
                                                class="h-[20px] aspect-auto relative top-[3px]">
                                            <div v-else>
                                                <img v-if="order['asc'] === true" src="@/assets/north.svg" alt=""
                                                    class="h-[20px] aspect-auto relative top-[3px]">
                                                <img v-else src="@/assets/south.svg" alt=""
                                                    class="h-[20px] aspect-auto relative top-[3px]">
                                            </div>
                                        </div>
                                    </th>
                                    <th @click="order['by'] === item ? order['asc'] = !order['asc'] : order['by'] = item; order_table()"
                                        class="text-center select-none px-[40px] hover:bg-[rgba(81,81,81,0.6)]"
                                        v-for="item in values">
                                        <div class="flex gap-[5px]">
                                            <p>{{ item }}</p>
                                            <img src="@/assets/swap.svg" alt="" v-if="order['by'] !== item"
                                                class="h-[20px] aspect-auto relative top-[3px]">
                                            <div v-else>
                                                <img v-if="order['asc'] === true" src="@/assets/north.svg" alt=""
                                                    class="h-[20px] aspect-auto relative top-[3px]">
                                                <img v-else src="@/assets/south.svg" alt=""
                                                    class="h-[20px] aspect-auto relative top-[3px]">
                                            </div>
                                        </div>
                                    </th>
                                    <th class="w-[150px]"></th>
                                </tr>
                                <tr class="relative hover:bg-[#333] h-[50px]" v-for="student in items_table"
                                    :key="student['id']">
                                    <td class="w-[50px]">
                                        <checkBox type="checkbox" @select="select_item(student['id'])"
                                            :checked="is_selected(student['id'])"/>
                                    </td>
                                    <td class="truncate min-w-[60px]">
                                        <div class="flex">
                                            <p class="min-w-full truncate">{{ student['id'] }}</p>
                                        </div>
                                    </td>
                                    <td v-for="(value, index) in values" :key="value"
                                        :class="`relative ${value === 'description' ? 'view-description' : ''}`">
                                        <input v-if="value !== 'description'" type="text" readonly
                                            :value="getValue(student, value)"
                                            class="bg-transparent outline-none readonly readonly-1">
                                        <div v-else @click="toggleDescription(student['description'], student['id'])"
                                            class="flex w-[120px] items-center cursor-pointer select-none">
                                            <p readonly
                                                class="bg-transparent cursor-pointer w-[35px] relative bottom-[1px] font-medium outline-none readonly readonly-1">
                                                view</p>
                                            <svg class="w-[20px] h-[20px] relative top-[1px]"
                                                v-if="!(description_open && student['id'] === student_description_open_id)"
                                                xmlns="http://www.w3.org/2000/svg" height="24px"
                                                viewBox="0 -960 960 960" width="24px" fill="currentColor">
                                                <path
                                                    d="M480-320q75 0 127.5-52.5T660-500q0-75-52.5-127.5T480-680q-75 0-127.5 52.5T300-500q0 75 52.5 127.5T480-320Zm0-72q-45 0-76.5-31.5T372-500q0-45 31.5-76.5T480-608q45 0 76.5 31.5T588-500q0 45-31.5 76.5T480-392Zm0 192q-146 0-266-81.5T40-500q54-137 174-218.5T480-800q146 0 266 81.5T920-500q-54 137-174 218.5T480-200Zm0-300Zm0 220q113 0 207.5-59.5T832-500q-50-101-144.5-160.5T480-720q-113 0-207.5 59.5T128-500q50 101 144.5 160.5T480-280Z" />
                                            </svg>
                                            <svg v-else class="w-[20px] h-[20px] relative top-[1px]"
                                                xmlns="http://www.w3.org/2000/svg" height="24px"
                                                viewBox="0 -960 960 960" width="24px" fill="currentColor">
                                                <path
                                                    d="m644-428-58-58q9-47-27-88t-93-32l-58-58q17-8 34.5-12t37.5-4q75 0 127.5 52.5T660-500q0 20-4 37.5T644-428Zm128 126-58-56q38-29 67.5-63.5T832-500q-50-101-143.5-160.5T480-720q-29 0-57 4t-55 12l-62-62q41-17 84-25.5t90-8.5q151 0 269 83.5T920-500q-23 59-60.5 109.5T772-302Zm20 246L624-222q-35 11-70.5 16.5T480-200q-151 0-269-83.5T40-500q21-53 53-98.5t73-81.5L56-792l56-56 736 736-56 56ZM222-624q-29 26-53 57t-41 67q50 101 143.5 160.5T480-280q20 0 39-2.5t39-5.5l-36-38q-11 3-21 4.5t-21 1.5q-75 0-127.5-52.5T300-500q0-11 1.5-21t4.5-21l-84-82Zm319 93Zm-151 75Z" />
                                            </svg>
                                        </div>
                                    </td>
                                    <td class="relative">
                                        <div class="flex absolute top-0 h-full right-[50px]">
                                            <button @click="openEditPopup(student['id'])"
                                                class="h-[60%] aspect-square mr-[5px] rounded-full relative top-[50%] translate-y-[-50%] text-blue-800 shrink-0 border-blue-800 border-[1px] border-solid hover:text-black hover:bg-blue-800 transition-all">
                                                <svg class="w-[60%] aspect-square mx-auto object-contain"
                                                    xmlns="http://www.w3.org/2000/svg" height="24px"
                                                    viewBox="0 -960 960 960" width="24px" fill="currentColor">
                                                    <path
                                                        d="M200-200h57l391-391-57-57-391 391v57Zm-80 80v-170l528-527q12-11 26.5-17t30.5-6q16 0 31 6t26 18l55 56q12 11 17.5 26t5.5 30q0 16-5.5 30.5T817-647L290-120H120Zm640-584-56-56 56 56Zm-141 85-28-29 57 57-29-28Z" />
                                                </svg>
                                            </button>
                                            <button @click="removeStudent(student['id'])"
                                                class="h-[60%] aspect-square mr-[5px] rounded-full relative top-[50%] translate-y-[-50%] text-red-700 shrink-0 border-red-700 border-[1px] border-solid hover:text-black hover:bg-red-700 transition-all">
                                                <svg class="w-[60%] aspect-square mx-auto object-contain"
                                                    xmlns="http://www.w3.org/2000/svg" height="24px"
                                                    viewBox="0 -960 960 960" width="24px" fill="currentColor">
                                                    <path
                                                        d="m376-300 104-104 104 104 56-56-104-104 104-104-56-56-104 104-104-104-56 56 104 104-104 104 56 56Zm-96 180q-33 0-56.5-23.5T200-200v-520h-40v-80h200v-40h240v40h200v80h-40v520q0 33-23.5 56.5T680-120H280Zm400-600H280v520h400v-520Zm-400 0v520-520Z" />
                                                </svg>
                                            </button>
                                        </div>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
                <div v-else class="mt-[50px]" v-show="!request_success">
                    <h1 class="text-center font-medium text-[35px]">¯\_(ツ)_/¯</h1>
                    <p class="text-center">couldn't fetch server, status: {{ status }}</p>
                </div>
            </div>
        </div>
        <div ref="add_student_popup"
            class="bg-[#474747] text-white w-[550px] z-50 px-[25px] py-[30px] max-w-full duration-[600ms] mx-auto fixed right-0 left-0 top-0 translate-y-[-200%] transition-all rounded-[20px] shadow-2xl h-fit">
            <div @click="closeAddPopup" class="absolute right-[10px] top-[10px] w-fit cursor-pointer">
                <img src="@/assets/close.svg" alt="">
            </div>
            <h1 class="font-semibold text-[20px]">Add {{ startsWithVowel(name) ? 'an ' + name : 'a ' + name }}</h1>
            <form @submit.prevent="addStudent(); closeAddPopup()">
                <div v-for="key in keys" :key="key">
                    <input v-if="key.type === 'text' && key.name !== 'description'" v-model="add_values[key.name]" type="text"
                        required minlength="3" :placeholder="key.name"
                        class="w-full h-[40px] bg-[#555555] outline-[#fadb32] border-white border-[1px] border-solid px-[15px] py-[10px] rounded mt-[15px]">
                    <textarea v-else-if="key.type === 'text' && key.name === 'description'" rows=2
                        v-model="add_values[key.name]" type="text" required minlength="3" :placeholder="key.name"
                        class="w-full bg-[#555555] outline-[#fadb32] border-white border-[1px] border-solid px-[15px] py-[10px] rounded mt-[15px]"></textarea>
                    <select v-else-if="key.type === 'choices'" v-model="add_values[key.name]" required minlength="3"
                        class="w-full h-[40px] bg-[#555555] outline-[#fadb32] border-white border-[1px] border-solid px-[15px] rounded mt-[15px]">
                        <option :value="key_choices_choice.value" v-for="(key_choices_choice, index) in key.value"
                            :key="index">{{ key_choices_choice.name }}</option>
                    </select>
                    <select v-else-if="key.type === 'multi_choices' && !isObject(add_values[key.name])" multiple
                        v-model="add_values[key.name]" required minlength="3"
                        class="w-full h-[80px] bg-[#555555] outline-[#fadb32] border-white border-[1px] border-solid px-[15px] py-[10px] rounded mt-[15px]">
                        <option :value="key_choices_choice.value" v-for="key_choices_choice in key.value">{{
                            key_choices_choice.name }}</option>
                    </select>
                    <select v-else-if="key.type === 'multi_choices' && isObject(add_values[key.name])" multiple
                        v-model="add_values[key.name]['value']" required minlength="3"
                        class="w-full h-[80px] bg-[#555555] outline-[#fadb32] border-white border-[1px] border-solid px-[15px] py-[10px] rounded mt-[15px]">
                        <option :value="key_choices_choice.value" v-for="key_choices_choice in key.value">{{
                            key_choices_choice.name }}</option>
                    </select>
                    <input v-else-if="key.type === 'number'" v-model="add_values[key.name]" type="number" required
                        minlength="3" :placeholder="key.name"
                        class="w-full h-[40px] bg-[#555555] outline-[#fadb32] border-white border-[1px] border-solid px-[15px] rounded mt-[15px]">
                    <input v-else-if="key.type === 'time'" v-model="add_values[key.name]" type="time" required
                        minlength="3" :placeholder="key.name"
                        class="w-full h-[40px] bg-[#555555] outline-[#fadb32] border-white border-[1px] border-solid px-[15px] rounded mt-[15px]">
                </div>
                <button type="submit"
                    class="bg-[#006bba] bg-gradient-yellow-rotated px-[45px] h-[40px] mt-[30px] rounded hover:bg-[#005aa0] text-white">Submit</button>
            </form>
        </div>
        <div ref="edit_student_popup"
            class="bg-[#474747] text-white z-50 w-[550px] px-[25px] py-[30px] max-w-full duration-[600ms] mx-auto fixed right-0 left-0 top-0 translate-y-[-200%] transition-all rounded-[20px] shadow-2xl h-fit">
            <div @click="closeEditPopup" class="absolute right-[10px] top-[10px] w-fit cursor-pointer">
                <img src="@/assets/close.svg" alt="">
            </div>
            <h1 class="font-semibold text-[20px]">Editing {{ edit_values['full_name'] }}</h1>
            <form @submit.prevent="editStudent(); closeEditPopup()">
                <div v-for="key in keys" :key="key">
                    <input v-if="key.type === 'text' && key.name !== 'description'" v-model="edit_values[key.name]"
                        type="text" required minlength="3" :placeholder="key.name"
                        class="w-full h-[40px] bg-[#555555] outline-[#fadb32] border-white border-[1px] border-solid px-[15px] py-[10px] rounded mt-[15px]">
                    <textarea v-else-if="key.type === 'text' && key.name === 'description'" rows=2
                        v-model="edit_values[key.name]" type="text" required minlength="3" :placeholder="key.name"
                        class="w-full bg-[#555555] outline-[#fadb32] border-white border-[1px] border-solid px-[15px] py-[10px] rounded mt-[15px]"></textarea>
                    <select v-else-if="key.type === 'choices'" v-model="edit_values[key.name]" required minlength="3"
                        class="w-full h-[40px] bg-[#555555] outline-[#fadb32] border-white border-[1px] border-solid px-[15px] rounded mt-[15px]">
                        <option :value="key_choices_choice.value" v-for="(key_choices_choice, index) in key.value"
                            :key="index">{{ key_choices_choice.name }}</option>
                    </select>
                    <select v-else-if="key.type === 'multi_choices' && !isObject(edit_values[key.name])" multiple
                        v-model="edit_values[key.name]" required minlength="3"
                        class="w-full h-[80px] bg-[#555555] outline-[#fadb32] border-white border-[1px] border-solid px-[15px] py-[10px] rounded mt-[15px]">
                        <option :value="key_choices_choice.value" v-for="key_choices_choice in key.value">{{
                            key_choices_choice.name }}</option>
                    </select>
                    <select v-else-if="key.type === 'multi_choices' && isObject(edit_values[key.name])" multiple
                        v-model="edit_values[key.name]['value']" required minlength="3"
                        class="w-full h-[80px] bg-[#555555] outline-[#fadb32] border-white border-[1px] border-solid px-[15px] py-[10px] rounded mt-[15px]">
                        <option :value="key_choices_choice.value" v-for="key_choices_choice in key.value">{{
                            key_choices_choice.name }}</option>
                    </select>
                    <input v-else-if="key.type === 'number'" v-model="edit_values[key.name]" type="number" required
                        minlength="3" :placeholder="key.name"
                        class="w-full h-[40px] bg-[#555555] outline-[#fadb32] border-white border-[1px] border-solid px-[15px] rounded mt-[15px]">
                    <input v-else-if="key.type === 'time'" v-model="edit_values[key.name]" type="time" required
                        minlength="3" :placeholder="key.name"
                        class="w-full h-[40px] bg-[#555555] outline-[#fadb32] border-white border-[1px] border-solid px-[15px] rounded mt-[15px]">
                </div>
                <button type="submit"
                    class="bg-[#006bba] bg-gradient-yellow-rotated px-[45px] h-[40px] mt-[30px] rounded hover:bg-[#005aa0] text-white">Submit</button>
            </form>
        </div>
        <div ref="description"
            :class="`bg-[#363636] shadow-white scrollbar-dark overflow-ellipsis max-h-[400px] overflow-y-auto duration-200 z-50 w-[550px] px-[25px] py-[10px] max-w-full ease-out mx-auto fixed right-0 left-0 top-0 ${description_open ? 'translate-y-[20px]' : 'translate-y-[-200%]'} transition-all rounded-[20px] shadow-2xl h-fit`">
            <div @click="closeDescription" class="right-[10px] fixed top-[10px] w-fit cursor-pointer">
                <img src="@/assets/close-white.svg" alt="">
            </div>
            <p class="min-h-[25px] max-w-[550px]">{{ description }}</p>
        </div>
    </div>
</template>

<script>
import checkBox from '@/components/checkbox.vue'

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
    components: {
        checkBox
    },
    data() {
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
            order: {
                by: 'id',
                asc: true
            },
            selected_items: []
        }
    },
    mounted() {
        for (let i of this.items) {
            this.selected_items.push({
                id: i.id,
                selected: false
            })
        }
        // detect outside click
        document.addEventListener('click', (event) => {
            const target = event.target;
            const add_popup = this.$refs['add_student_popup'];
            const button = this.$refs['add_student_button'];
            const description = this.$refs['description']
            const view_description_buttons = document.getElementsByClassName('view-description')

            try {
                if (!add_popup.contains(target) && !button.contains(target)) {
                    this.closeAddPopup()
                }
                let clicked_view_button = true
                for (const view_description_button of view_description_buttons) {
                    if (view_description_button.contains(target)) {
                        clicked_view_button = false
                        break
                    }
                }
                if (clicked_view_button && !description.contains(target)) {
                    this.closeDescription()
                }
            } catch { }
        });
    },
    methods: {
        removeStudent(id) {
            this.$genericStore.confirm_popup("Are you sure you want to delete an element with id: " + id + "?").then((response) => {
                if (response) {
                    this.$api.delete(this.api_link + id + '/').then(() => {
                        this.items_table = this.items.filter(student => student['id'] !== id);
                    })
                    this.$emit('refetch')
                }
            })
        },
        openAddPopup() {
            let popup = this.$refs['add_student_popup'];
            popup.style.transform = "translateY(20px)";
            this.closeEditPopup()
        },
        closeAddPopup() {
            let popup = this.$refs['add_student_popup'];
            popup.style.transform = "translateY(-200%)";
        },
        openEditPopup(id) {
            const student = this.items.find(student => student['id'] === id);
            this.edit_values = {
                "id": student['id']
            }
            for (let value in this.values) {
                this.edit_values[this.values[value]] = student[this.values[value]]
            }
            let popup = this.$refs['edit_student_popup'];
            popup.style.transform = "translateY(20px)";
            this.closeAddPopup()
        },
        closeEditPopup() {
            this.edit_values = this.saved_edit_value
            let popup = this.$refs['edit_student_popup'];
            popup.style.transform = "translateY(-200%)";
        },
        editStudent() {
            let filteredObject = {};
            for (const entry of Object.entries(this.edit_values)) {
                if (entry[0] !== 'id') {
                    if (this.isObject(entry[1])) {
                        filteredObject[entry[0]] = entry[1]['value']
                    } else {
                        filteredObject[entry[0]] = entry[1]
                    }
                }
            }
            this.$api.put(this.api_link + this.edit_values['id'] + '/', filteredObject).then(response => {
                console.log(response)
                this.$emit('refetch')
            })
        },
        addStudent() {
            this.$api.post(this.api_link, this.add_values).then(response => {
                console.log(response)
                this.add_values = this.default_add_values
                let forms = document.getElementsByTagName('form')
                for (const form of forms) {
                    form.reset()
                }
                this.$emit('refetch')
            })
        },
        openDescription(description, id) {
            this.student_description_open_id = id
            this.description = description
            this.description_open = true
        },
        closeDescription() {
            this.description = ''
            this.description_open = false
        },
        toggleDescription(description, id) {
            this.description = description
            if (this.description_open) {
                if (this.student_description_open_id !== id) {
                    this.student_description_open_id = id
                    this.closeDescription()
                    setTimeout(() => {
                        this.openDescription(description, id)
                    }, 200)
                } else {
                    this.closeDescription()
                }
            } else {
                this.openDescription(description, id)
            }
        },
        getValue(student, value) {
            return (typeof student[value] === 'object' && !Array.isArray(student[value]) && student[value] !== null) ? student[value]['show'] : student[value]
        },
        isObject(value) {
            return (typeof value === 'object' && !Array.isArray(value) && value !== null)
        },
        startsWithVowel(word) {
            return ['a', 'e', 'i', 'o'].includes(word[0].toLowerCase())
        },
        searchTable(value) {
            this.items_table = this.items.filter(saved_item => String(saved_item[value]).toLowerCase().match(this.search.toLowerCase()))
        },
        order_table() {
            let sort = () => {
                let is_a_bigger_than_b = (itemA, itemB) => {
                    if(typeof(itemA[this.order['by']])==='object'){
                        if(itemA[this.order['by']].value > itemB[this.order['by']].value){
                            return true
                        }
                        else if(itemA[this.order['by']].value === itemB[this.order['by']].value && itemA['id']>itemB['id']){
                            return true
                        }
                        return false
                    }
                    if (itemA[this.order['by']] > itemB[this.order['by']]) {
                        return true
                    }
                    else if(itemA['id'] > itemB['id'] && itemA[this.order['by']] === itemB[this.order['by']]){
                        return true
                    }
                    return false
                };
                let is_sorted = (arr) => {
                    for (let index = 0; index < arr.length; index++) {
                        if (index < arr.length - 1) {
                            if (is_a_bigger_than_b(arr[index], arr[index + 1])) {
                                return false
                            }
                        }
                    }
                    return true
                }
                while (!is_sorted(this.items_table)) {
                    for (let index = 0; index < this.items_table.length; index++) {
                        if (index < this.items_table.length - 1) {
                            if (is_a_bigger_than_b(this.items_table[index], this.items_table[index + 1])) {
                                let saved_item_a = this.items_table[index]
                                this.items_table[index] = this.items_table[index + 1]
                                this.items_table[index + 1] = saved_item_a
                            }
                        }
                    }
                }
            }

            sort()

            if (!this.order['asc']) {
                this.items_table.reverse()
            }
        },
        select_item(id) {
            for (let i = 0; i < this.selected_items.length; i++) {
                if (this.selected_items[i]['id'] === id) {
                    this.selected_items[i]['selected'] = !this.selected_items[i]['selected']
                    break
                }
            }
        },
        select_all() {
            const value = !this.$refs['check_all'].checked
            for (let i = 0; i < this.selected_items.length; i++) {
                this.selected_items[i]['selected'] = value
            }
        },
        is_selected(id) {
            for (let i = 0; i < this.selected_items.length; i++) {
                if (this.selected_items[i]['id'] === id) {
                    return this.selected_items[i]['selected']
                }
            }
        },
        are_all_selected() {
            if(this.selected_items.length === 0){
                return false
            }
            for (let i = 0; i < this.selected_items.length; i++) {
                if (this.selected_items[i]['selected'] === false) {
                    return false
                }
            }
            return true
        },
        count_selected_items() {
            let count = 0
            for (let i = 0; i < this.selected_items.length; i++) {
                if (this.selected_items[i]['selected']) {
                    count++
                }
            }
            return count
        },
        deleteSelected(){
            this.$genericStore.confirm_popup("Are you sure you want to delete all selected items?").then((response)=>{
                if(response){
                    for(let selected_item of this.selected_items){
                        if(selected_item.selected){
                            this.$api.delete(this.api_link+selected_item.id+'/')
                        }
                    }
                }
                this.$emit("refetch")
            })
        }
    },
    watch: {
        items(new_items) {
            this.items_table = new_items
            for (let i of this.items) {
                this.selected_items.push({
                    id: i.id,
                    selected: false
                })
            }
        }
    }
}
</script>

<style lang="css" scoped>
tr,
td,
th,
table {
    border-top: 1px solid #555555;
    border-bottom: 1px solid #555555;
}

input {
    width: 100%;
}

td,
th {
    padding-left: 10px;
    padding-right: 10px;
}
</style>