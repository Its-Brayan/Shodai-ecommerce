import axios from 'axios'
const axiosInst = axios.create({
  baseURL: ' http://127.0.0.1:8000/',
  headers: {
     
    'Content-Type': 'application/json',
  },
});  
axiosInst.interceptors.request.use(
  (config) =>{
    const token = localStorage.getItem('access_token')
    if (token){
      config.headers.Authorization =`Bearer ${token}`
    }
    return config
  },
  (error)=>{
    return Promise.reject(error)
  }
)   
axiosInst.interceptors.response.use(
  (response) => response,
  async (error) =>{
    if(error.response?.status===401){
      const refreshToken = localStorage.getItem('refresh_token')
      if(refreshToken){
        try{
          const response = await axiosInst.post(`http://localhost:8000/token/refresh/`,{
            refresh:refreshToken
          }
          )
          const newAccessToken = response.data.access
          localStorage.setItem('access_token',newAccessToken)
          error.config.headers.Authorization = `Bearer ${newAccessToken}`
          return axios.request(error.config)
        }catch(refresherror){
          localStorage.clear()
          window.location.href="/login"
        }
      }
    }
        return Promise.reject(error)
  }
)

export default axiosInst;