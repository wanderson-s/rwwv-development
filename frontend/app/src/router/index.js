import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/funcionario',
    name: 'Funcionario',
    component: () => import('../views/Funcionario.vue')
  },
  {
    path: '/orcamento',
    name: 'Orçamento',
    component: () => import('../views/Orcamento.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
