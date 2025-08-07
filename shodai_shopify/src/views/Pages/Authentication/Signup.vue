<template>
   
<v-card height="800px">
    <v-card-title>
        <v-row>
            <v-col cols="1">
                <v-img
                src="https://cdn.pixabay.com/photo/2023/03/06/13/56/icon-7833512_640.png"
                width="50px"
                height="50px"

                >

                </v-img>
            </v-col>
            <v-col cols="2" class="ml-n15 mt-2">
                <div class="text-h5 font-weight-bold">Shodai</div>
            </v-col>
        </v-row>
    </v-card-title>
    <v-card-text class="d-flex justify-center ml-16  " >
        <v-row>
        <v-col cols="5" class=" mt-16">
            <v-card class="pa-15 ml-16" height="700px" >
                <v-card-title>
         <div class="d-flex font-weight-medium text-h5 justify-start">
                    Create an Account
         </div>
         </v-card-title>
         <v-card-text>
         <div class="mt-3">
            <v-text-field label="Enter Your Name" :rules="[required]" v-model="form.fullname" variant="outlined" color="bg-grey">

            </v-text-field>
         </div>
          <div class="mt-3">
            <v-text-field label="Enter Your Email" :rules="[required]" v-model="form.email" variant="outlined" color="bg-grey">

            </v-text-field>
         </div>
          <div class="mt-3">
            <v-text-field label="Enter Your Password":rules="[required]" v-model="form.password" :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'" :type="visible ? 'text' : 'password'"  @click:append-inner="visible = !visible" variant="outlined">

            </v-text-field>
         </div>
           <div class="mt-3">
            <v-text-field label="Confirm Password" :rules="[required]" v-model="form.confirm_password" :append-inner-icon="visible1 ? 'mdi-eye-off' : 'mdi-eye'" :type="visible1 ? 'text' : 'password'"  @click:append-inner="visible1 = !visible1" variant="outlined">

            </v-text-field>
         </div>
           <div class="mt-3">
            <v-btn block size="large" :loading="loading" @click="registerUser" rounded="lg" variant="outlined" class="bg-indigo text-capitalize">
             Sign up
            </v-btn>
         </div>
         <div class=" mt-7 text-grey-lighten-1 d-flex justify-center">Or</div>
           <div class=" mt-3 text-grey-lighten-1 d-flex justify-center">Already have an account? <v-btn nav variant="text" class="text-capitalize mt-n2 text-indigo" to="/login">login</v-btn></div>
           </v-card-text>
           </v-card>
         </v-col>
         <v-col cols="5" class=" mt-16">
            <v-card class="bg-indigo ml-n6  pa-4 " height="700px">
                <v-card-title></v-card-title>
                <v-card-text>
            <v-img
            src="/Blog post-rafiki.png"
            width=""
            ></v-img>
            </v-card-text>
            </v-card>
         </v-col>
              </v-row>
</v-card-text>
                </v-card>
                
        
  

</template>

<script setup>
import {ref,watch} from 'vue'
import axiosInst from '@/services/api.js'
import { AuthStore } from '@/stores/authstore'
import { useRouter } from 'vue-router'
import { toast } from 'vue-sonner'
const router = useRouter()
const visible = ref(false)
const visible1 = ref(false)
 const loading = ref(false)
 const store = AuthStore()
  function required (v) {
    return !!v || 'Field is required'
  }
let form = ref({
    fullname : '',
    email:'',
    password:'',
    confirm_password:'',
   


})
function registerUser(){
    const formdata ={
        ...form.value,
        username : form.value.email
    }
    if (!form.value) return
    loading.value = true
    setTimeout(() => (loading.value = false), 2000)
    axiosInst.post(`api/register/`,formdata)
    .then( response =>{
        console.log("User register successfully", response.data)
        if (response.data.tokens) {
            localStorage.setItem('access_token', response.data.tokens.access)
            localStorage.setItem('refresh_token', response.data.tokens.refresh)
         
            // Optionally store user data
            localStorage.setItem('user', JSON.stringify(response.data.user))
              store.updateIsLoggedInToTrue(response.data.user)
            // Redirect to dashboard or home page
            router.push('/dashboard') 
            toast.success(`Welcome ${response.data.user.fullname}`)
    }
}

    ).catch(error=>{
        console.error("Failed to register user", error)
    }

    )
}
</script>