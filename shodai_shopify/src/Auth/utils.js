// auth/utils.js
export function isUserLoggedIn() {
  const token = localStorage.getItem('access_token')
  const user = localStorage.getItem('user')
  
  if (!token || !user) {
    return null
  }
  
  // Optional: Check if token is expired
  try {
    const payload = JSON.parse(atob(token.split('.')[1]))
    const currentTime = Date.now() / 1000
    
    if (payload.exp < currentTime) {
      // Token expired, clear storage
      localStorage.removeItem('access_token')
      localStorage.removeItem('refresh_token')
      localStorage.removeItem('user')
      return null
    }
  } catch (error) {
    // Invalid token format
    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')
    localStorage.removeItem('user')
    return null
  }
  
  return JSON.parse(user)
}