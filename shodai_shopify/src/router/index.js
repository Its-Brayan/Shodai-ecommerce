import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/DashboardView.vue'
import { isUserLoggedIn } from '@/Auth/utils'
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
       meta:{
        requiresAuth:true
      }
    },
    {
      path: '/orders',
      name: 'orders',
      component: () => import('../views/OrdersView.vue'),
       meta:{
        requiresAuth:true
      }
    },
  
    {
      path: '/products',
      name: 'products',
      component: () => import('../views/Pages/Tools/ProductsView.vue'),
       meta:{
        requiresAuth:true
      }
    },
   
    
    {
      path:'/analytics',
      name: 'Analytics',
      component: () => import('../views/Pages/Tools/AnalysisView.vue'),
       meta:{
        requiresAuth:true
      }
    },
    {
      path:'/settings',
      name: 'Settings',
      component: () => import('../views/Pages/Settings/SettingsView.vue'),
       meta:{
        requiresAuth:true
      }
    },
    {
      path:'/chat',
      name: 'Chat',
      component: () => import('../views/MessagesView.vue'),
       meta:{
        requiresAuth:true
      }
    },
    {
      path:'/categories',
      name: 'Categories',
      component: () => import('../views/Pages/Tools/CategoryView.vue'),
       meta:{
        requiresAuth:true
      }
    },
    {
      path:'/help',
      name: 'Help',
      component: () => import('../views/Pages/Settings/HelpView.vue'),
      meta:{
        requiresAuth:true
      }
    },
     {
      path:'/signup',
      name: 'signup',
      component: () => import('../views/Pages/Authentication/Signup.vue'),
      meta:{
        hideNavigation:true,
        requiresGuest:true,

      }
    },
    
     {
      path:'/login',
      name: 'login',
      component: () => import('../views/Pages/Authentication/Login.vue'),
      meta:{
        hideNavigation:true,
        requiresGuest:true
      }
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'not-found',
      redirect: (to) => {
        const user = isUserLoggedIn()
        return user ? '/' : '/login'
      }
    },
    
    
  ]

})
router.beforeEach((to, from, next) => {
  const user = isUserLoggedIn()
  const isAuthenticated = user !== null
  
  console.log(`Navigating to: ${to.path}, Authenticated: ${isAuthenticated}`)
  
  // Handle protected routes
  if (to.meta?.requiresAuth) {
    if (!isAuthenticated) {
      console.log('Redirecting to login - not authenticated')
      return next('/login')
    }
  }
  
  // Handle guest-only routes (login/signup)
  if (to.meta?.requiresGuest) {
    if (isAuthenticated) {
      console.log('Redirecting to dashboard - already authenticated')
      return next('/dashboard')
    }
  }
  
  // Continue navigation
  next()
})

export default router
