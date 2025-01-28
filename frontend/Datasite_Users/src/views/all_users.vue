<template>
    <table_users :default_filter="'full_name'" @refetch="fetchCourses" :name="'User'" :api_link="'users/'" :items="students" :request_success="request_success" :status="status" :default_add_values="add_values" :default_edit_values="edit_values" :values="values" :keys="keys"></table_users>
</template>

<script>
import table_users from '@/components/table_users.vue'

export default {
    name: 'App',
    components: {
        table_users,
    },
    data(){
        return {
            courses: [],
            students: [],
            request_success: true,
            status: 0,
            add_values: {
                "full_name": "",
                "username": "",
                "type_user": "student",
                "description": "",
                "courses": []
            },
            edit_values: {
                "id": 0,
                "full_name": "",
                "username": "",
                "type_user": "",
                "description": "",
                "courses": []
            },
            values: [
                "full_name",
                "username",
                "type_user",
                "description",
                "courses"
            ],
            keys: [
                {
                    name: "full_name",
                    type: "text",
                },
                {
                    name: "username",
                    type: "text",
                },
                {
                    name: "type_user",
                    type: "choices",
                    value: [
                        {
                            name: "student",
                            value: "student"
                        },
                        {
                            name: "employee",
                            value: "employee"
                        }
                    ]
                },
                {
                    name: "description",
                    type: "text",
                },
                {
                    name: "courses",
                    type: "multi_choices",
                    value: []
                }
            ]
        }
    },
    methods: {
        fetchCourses(){
            this.$api.get('courses/').then(response=>{
                this.courses = response.data
                this.keys[4].value = this.courses.map(course=>{
                    return {
                        name: course.name,
                        value: course.id
                    }
                })
                this.fetchStudents()
            }).catch((error)=>{
                console.log(error)
                this.request_success = false
                try{
                    this.status = error.response.status
                }catch{
                    this.status = 400
                }
            }) 
        },
        fetchStudents() {
            // Fetch students from the database
            this.$api.get('users/').then(response => {
                this.students = response.data
                this.parseStudents()
            }).catch((error)=>{
                console.log(error)
                this.request_success = false
                try{
                    this.status = error.response.status
                }catch{
                    this.status = 400
                }
            })
        },
        parseStudents(){
            for(let i = 0; i < this.students.length; i++){
                this.students[i]['courses'] = this.renderCourses(this.students[i].courses)
            }
        },
        renderCourses(idArray){
            let what_to_show = []
            let value = []
            for(const id of idArray){
                let course = this.courses.filter(course=>course.id===id)
                what_to_show.push(course[0].name)
                value.push(course[0].id)
            }
            return {
                show: what_to_show,
                value: value
            }
        },
    },
    mounted() {
        this.fetchCourses()
    },
}
</script>

<style lang="scss" scoped>

</style>