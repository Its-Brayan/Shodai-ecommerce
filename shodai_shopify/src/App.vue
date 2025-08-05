<script setup>
import MenuComponent from './components/MenuComponent.vue';
import { RouterView,useRoute } from 'vue-router';
const route=useRoute()
</script>

<template>
  <v-app>
    <v-layout>
      <MenuComponent v-if="!route.meta.hideNavigation"/>
  <v-main>
     <RouterView />
    </v-main>
    </v-layout>
  </v-app>
 
 </template>