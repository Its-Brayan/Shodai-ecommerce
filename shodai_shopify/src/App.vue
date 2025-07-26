<script setup>
import MenuComponent from './components/MenuComponent.vue';
import { RouterView } from 'vue-router';
</script>

<template>
  <v-app>
    <v-layout>
      <MenuComponent/>
  <v-main>
     <RouterView />
    </v-main>
    </v-layout>
  </v-app>
 
 </template>