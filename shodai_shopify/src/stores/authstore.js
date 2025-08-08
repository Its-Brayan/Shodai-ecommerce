// stores/authstore.js
import { ref } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import { isUserLoggedIn } from '@/Auth/utils'
import { toast } from 'vue-sonner'

export const AuthStore = defineStore("authstore", () => {
  const router = useRouter()
  const loggedIn = ref(false)
  const user = ref(null)
  
  // Initialize authentication state
  const initializeAuth = () => {
    const userData = isUserLoggedIn()
    if (userData) {
      loggedIn.value = true
      user.value = userData
    } else {
      loggedIn.value = false
      user.value = null
    }
  }
  
  // Initialize on store creation
  initializeAuth()

  function updateIsLoggedInToTrue(userData = null) {
    loggedIn.value = true
    if (userData) {
      user.value = userData
    }
  }
  
  function updateIsLoggedInToFalse() {
    loggedIn.value = false
    user.value = null
  }

  function logout() {
    // Remove all auth data from localStorage
    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')
    localStorage.removeItem('user')
    
    // Update store state
    updateIsLoggedInToFalse()
    
    // Redirect to login page
    router.push({ name: "login" }).then(() => {
      toast.success(
        "You have successfully logged out.",
        {
          timeout: 2000,
        }
      )
    })
  }

  // Login function
//   async function login(credentials) {
//     try {
//       // Your login logic here
//       // After successful login, update state
//       const userData = isUserLoggedIn()
//       if (userData) {
//         updateIsLoggedInToTrue(userData)
//         return true
//       }
//     } catch (error) {
//       console.error('Login failed:', error)
//       return false
//     }
//   }

//   // Register function
//   async function register(userData) {
//     try {
//       // Your register logic here
//       // After successful registration, update state
//       const newUserData = isUserLoggedIn()
//       if (newUserData) {
//         updateIsLoggedInToTrue(newUserData)
//         return true
//       }
//     } catch (error) {
//       console.error('Registration failed:', error)
//       return false
//     }
//   }

  return {
    loggedIn,
    user,
    updateIsLoggedInToTrue,
    updateIsLoggedInToFalse,
    logout,
    // login,
    // register,
    initializeAuth
  }
})