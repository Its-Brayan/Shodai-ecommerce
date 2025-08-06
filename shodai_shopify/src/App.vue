<script setup>
import {ref, onMounted} from 'vue'
import MenuComponent from './components/MenuComponent.vue';
import { RouterView,useRoute,useRouter } from 'vue-router';


const route = useRoute()
const router = useRouter()
const routerready = ref(false)
onMounted(async ()=>{
  await router.isReady()
  routerready.value=true
})
</script>

<template>
  <v-app>
    <v-layout>
      <MenuComponent v-if="routerready && !route.meta.hideNavigation"/>
  <v-main>
     <RouterView />
    </v-main>
    </v-layout>
  </v-app>
 
 </template>