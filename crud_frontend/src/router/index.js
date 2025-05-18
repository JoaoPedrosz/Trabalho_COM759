import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login.vue'
import CarList from '@/components/CarList.vue'
import CarForm from '@/components/CarForm.vue'
import Register from '@/components/Register.vue'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes: [
    { path: '/', redirect: '/login' },
    { path: '/login', component: Login },
    { path: '/carros', component: CarList },
    { path: '/novo', component: CarForm },
    { path: '/editar/:id', component: CarForm, meta: { requiresAuth: true } },
    { path: '/register', component: Register },
    { path: '*', redirect: '/login' }
  ]
})

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token')
  if (to.matched.some(record => record.meta.requiresAuth) && !token) {
    next('/login')
  } else {
    next()
  }
})

export default router
