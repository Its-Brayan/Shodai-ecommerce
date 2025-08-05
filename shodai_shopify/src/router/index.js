import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/DashboardView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/dashboard',
      name: 'home',
      component:import('../views/DashboardView.vue'),
    },
    {
      path: '/customers',
      name: 'customers',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: import('../views/CustomersView.vue'),
    },
    {
      path: '/orders',
      name: 'orders',
      component: () => import('../views/OrdersView.vue'),
    },
  
    {
      path: '/products',
      name: 'products',
      component: () => import('../views/Pages/Tools/ProductsView.vue'),
    },
   
    
    {
      path:'/analytics',
      name: 'Analytics',
      component: () => import('../views/Pages/Tools/AnalysisView.vue'),
    },
    {
      path:'/settings',
      name: 'Settings',
      component: () => import('../views/Pages/Settings/SettingsView.vue'),
    },
    {
      path:'/chat',
      name: 'Chat',
      component: () => import('../views/MessagesView.vue'),
    },
    {
      path:'/categories',
      name: 'Categories',
      component: () => import('../views/Pages/Tools/CategoryView.vue'),
    },
    {
      path:'/help',
      name: 'Help',
      component: () => import('../views/Pages/Settings/HelpView.vue'),
    },
     {
      path:'/signup',
      name: 'Help',
      component: () => import('../views/Pages/Authentication/Signup.vue'),
    },
     {
      path:'/login',
      name: 'Login',
      component: () => import('../views/Pages/Authentication/Login.vue'),
    }
  ],
})

export default router
