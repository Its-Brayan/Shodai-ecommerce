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
    <v-card-text class="d-flex justify-center">
        <v-row>
        <v-col cols="5" class=" mt-16">
            <v-card class="pa-15" height="600px" >
                <v-card-title>
         <div class="d-flex font-weight-medium text-h5 justify-start">
                    Create an Account
         </div>
         </v-card-title>
         <v-card-text>
         <div class="mt-3">
            <v-text-field label="Enter Your Name" variant="outlined" color="bg-grey">

            </v-text-field>
         </div>
          <div class="mt-3">
            <v-text-field label="Enter Your Email" variant="outlined" color="bg-grey">

            </v-text-field>
         </div>
          <div class="mt-3">
            <v-text-field label="Enter Your Password" :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'" :type="visible ? 'text' : 'password'"  @click:append-inner="visible = !visible" variant="outlined">

            </v-text-field>
         </div>
           <div class="mt-3">
            <v-btn block size="large" rounded="lg" variant="outlined" class="bg-indigo text-capitalize">
             Sign up
            </v-btn>
         </div>
         <div class=" mt-7 text-grey-lighten-1 d-flex justify-center">Or</div>
           <div class=" mt-3 text-grey-lighten-1 d-flex justify-center">Already have an account? <v-btn nav variant="text" class="text-capitalize mt-n2 text-indigo" to="/login">login</v-btn></div>
           </v-card-text>
           </v-card>
         </v-col>
         <v-col cols="5" class=" mt-16">
            <v-card class="bg-indigo ml-n6" height="600px">
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
const visible = ref(false)

</script>