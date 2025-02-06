import All_users from '@/views/all_users.vue'
import Employees from '@/views/employees.vue'
import Students from '@/views/students.vue'
import Courses from '@/views/courses.vue'
import Sign_in from '@/views/sign_in.vue'
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: All_users,
    },
    {
      path: '/employees/',
      name: 'employees',
      component: Employees
    },
    {
      path: '/students/',
      name: 'students',
      component: Students
    },
    {
      path: '/courses/',
      name: 'courses',
      component: Courses
    },
    {
      path: '/sign-in/',
      name: 'sign-in',
      component: Sign_in
    }
  ],
})

export default router
