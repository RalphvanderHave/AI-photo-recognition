import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/Home.vue'
import PowerBIDashboard from '../components/PowerBIDashboard.vue'
import PhotoAnalysis from '../components/PhotoAnalysis.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: PowerBIDashboard
    },
    {
      path: '/photo-analysis',
      name: 'photo-analysis',
      component: PhotoAnalysis
    }
  ]
})

export default router 