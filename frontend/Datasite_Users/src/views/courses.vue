<template>
    <table_users 
     :default_filter="'name'"
     @refetch="fetchCourses" 
     :name="'Course'" 
     :api_link="'courses/'" 
     :items="courses" 
     :request_success="request_success" 
     :status="status" 
     :default_add_values="add_values" 
     :default_edit_values="edit_values" 
     :values="values" 
     :keys="keys">
     </table_users>
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
            request_success: true,
            status: 0,
            add_values: {
                "name": "",
                "description": "",
                "price": "",
                "start_time": "",
                "end_time": "",
                "days": [],
                "telegram_group_id": ""
            },
            edit_values: {
                "id": 0,
                "name": "",
                "description": "",
                "price": "",
                "start_time": "",
                "end_time": "",
                "days": [],
                "telegram_group_id": ""
            },
            values: [
                "name",
                "price",
                "start_time",
                "end_time",
                "days",
                "telegram_group_id",
                "description",
            ],
            keys: [
                {
                    name: "name",
                    type: "text",
                },
                {
                    name: "description",
                    type: "text",
                },
                {
                    name: "price",
                    type: "number",
                },
                {
                    name: "start_time",
                    type: "time",
                },
                {
                    name: "end_time",
                    type: "time",
                },
                {
                    name: "days",
                    type: "multi_choices",
                    value: [
                        {
                            name: "Monday",
                            value: "mon"
                        },
                        {
                            name: "Tuesday",
                            value: "tue"
                        },
                        {
                            name: "Wednesday",
                            value: "wed"
                        },
                        {
                            name: "Thursday",
                            value: "thu"
                        },
                        {
                            name: "Friday",
                            value: "fri"
                        },
                        {
                            name: "Saturday",
                            value: "sat"
                        },
                        {
                            name: "Sunday",
                            value: "sun"
                        }
                    ]
                },
                {
                    name: "telegram_group_id",
                    type: "number",
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
            let result = []
            for(const id of idArray){
                let course = this.courses.filter(course=>course.id===id)
                result.push(course[0].name)
            }
            return result
        },
    },
    mounted() {
        this.fetchCourses()
    },
}
</script>

<style lang="scss" scoped>

</style>