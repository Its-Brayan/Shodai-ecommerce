<script setup>
import HeaderComponent from '@/components/HeaderComponent.vue';
 import { ref } from 'vue'

  const desserts = [
    {
      name: 'Frozen Yogurt',
      calories: 159,
      fat: 6,
      carbs: 24,
      protein: 4,
      iron: '1',
    },
    {
      name: 'Jelly bean',
      calories: 375,
      fat: 0,
      carbs: 94,
      protein: 0,
      iron: '0',
    },
    {
      name: 'KitKat',
      calories: 518,
      fat: 26,
      carbs: 65,
      protein: 7,
      iron: '6',
    },
    {
      name: 'Eclair',
      calories: 262,
      fat: 16,
      carbs: 23,
      protein: 6,
      iron: '7',
    },
    {
      name: 'Gingerbread',
      calories: 356,
      fat: 16,
      carbs: 49,
      protein: 3.9,
      iron: '16',
    },
    {
      name: 'Ice cream sandwich',
      calories: 237,
      fat: 9,
      carbs: 37,
      protein: 4.3,
      iron: '1',
    },
    {
      name: 'Lollipop',
      calories: 392,
      fat: 0.2,
      carbs: 98,
      protein: 0,
      iron: '2',
    },
    {
      name: 'Cupcake',
      calories: 305,
      fat: 3.7,
      carbs: 67,
      protein: 4.3,
      iron: '8',
    },
    {
      name: 'Honeycomb',
      calories: 408,
      fat: 3.2,
      carbs: 87,
      protein: 6.5,
      iron: '45',
    },
    {
      name: 'Donut',
      calories: 452,
      fat: 25,
      carbs: 51,
      protein: 4.9,
      iron: '22',
    },
  ]
  const FakeAPI = {
    async fetch ({ page, itemsPerPage, sortBy }) {
      return new Promise(resolve => {
        setTimeout(() => {
          const start = (page - 1) * itemsPerPage
          const end = start + itemsPerPage
          const items = desserts.slice()
          if (sortBy.length) {
            const sortKey = sortBy[0].key
            const sortOrder = sortBy[0].order
            items.sort((a, b) => {
              const aValue = a[sortKey]
              const bValue = b[sortKey]
              return sortOrder === 'desc' ? bValue - aValue : aValue - bValue
            })
          }
          const paginated = items.slice(start, end === -1 ? undefined : end)
          resolve({ items: paginated, total: items.length })
        }, 500)
      })
    },
  }
  const itemsPerPage = ref(5)
  const headers = ref([
    {
      title: 'Dessert (100g serving)',
      align: 'start',
      sortable: false,
      key: 'name',
    },
    { title: 'Calories', key: 'calories', align: 'end' },
    { title: 'Fat (g)', key: 'fat', align: 'end' },
    { title: 'Carbs (g)', key: 'carbs', align: 'end' },
    { title: 'Protein (g)', key: 'protein', align: 'end' },
    { title: 'Iron (%)', key: 'iron', align: 'end' },
  ])
  const search = ref('')
  const serverItems = ref([])
  const loading = ref(true)
  const totalItems = ref(0)
  function loadItems ({ page, itemsPerPage, sortBy }) {
    loading.value = true
    FakeAPI.fetch({ page, itemsPerPage, sortBy }).then(({ items, total }) => {
      serverItems.value = items
      totalItems.value = total
      loading.value = false
    })
  }

</script>

<template>
 <v-card>
    <v-card-title>
     <HeaderComponent/>
    </v-card-title>
    <v-card-text class="pt-10">
        <v-row class="d-flex justify-center">
            <v-col cols="5">
                <v-card style="width:550px;">
              <v-card-title>
                <v-row>
                    <v-col cols="6">
                      
                        <v-icon size="large" class="rounded-circle pa-4 bg-green text-white mx-auto" style="width:64px;height:64px" >mdi-cash-multiple</v-icon>
                   
                    </v-col>
                    <v-col cols="6">
                          <v-icon size="large" class="float-right"  color="green">mdi-trending-up</v-icon>
                    </v-col>
                </v-row>

                    <div class="text-capitalize text-grey-lighten-1">Total Earning</div>
                    <div class="text-capitalize text-grey-lighten-1">
                       $44,722.88
                    </div>
               
              </v-card-title>
                </v-card>
            </v-col>
              <v-col cols="6">
                <v-card style="width:550px">
                      <v-card-title>
                <v-row>
                    <v-col cols="6">
                      
                        <v-icon size="large" class="rounded-circle pa-4 bg-indigo text-white mx-auto" style="width:64px;height:64px" >mdi-account-multiple-outline</v-icon>
                   
                    </v-col>
                    <v-col cols="6">
                          <v-icon size="large" class="float-right" color="indigo">mdi-trending-up</v-icon>
                    </v-col>
                </v-row>

                    <div class="text-capitalize text-grey-lighten-1">Total Customers</div>
                    <div class="text-capitalize text-grey-lighten-1">
                       $44,722.88
                    </div>
               
              </v-card-title>
                </v-card>
            </v-col>
          
        </v-row>
        <v-row class="d-flex justify-center">
            <v-col cols="5">
                <v-card style="width:550px;">
              <v-card-title>
                <v-row>
                    <v-col cols="6">
                      
                        <v-icon size="large" class="rounded-circle pa-4 bg-yellow text-white mx-auto" style="width:64px;height:64px" >mdi-receipt-text</v-icon>
                   
                    </v-col>
                    <v-col cols="6">
                          <v-icon size="large" class="float-right"  color="yellow">mdi-trending-up</v-icon>
                    </v-col>
                </v-row>

                    <div class="text-capitalize text-grey-lighten-1">Total Orders</div>
                    <div class="text-capitalize text-grey-lighten-1">
                       $44,722.88
                    </div>
               
              </v-card-title>
                </v-card>
            </v-col>
              <v-col cols="6">
                <v-card style="width:550px">
                      <v-card-title>
                <v-row>
                    <v-col cols="6">
                      
                        <v-icon size="large" class="rounded-circle pa-4 bg-blue text-white mx-auto" style="width:64px;height:64px" >mdi-cart-outline</v-icon>
                   
                    </v-col>
                    <v-col cols="6">
                          <v-icon size="large" class="float-right" color="blue">mdi-trending-up</v-icon>
                    </v-col>
                </v-row>

                    <div class="text-capitalize text-grey-lighten-1">Total Products</div>
                    <div class="text-capitalize text-grey-lighten-1">
                       $44,722.88
                    </div>
               
              </v-card-title>
                </v-card>
            </v-col>
        </v-row>
        <div class="pt-10 pl-15">
        <v-card style="width:1150px" >
            <v-card-title>
                <v-row>
                    <v-col>
                        <div class="text-capitalize text-h6">Recent orders</div>
                    </v-col>
                    <v-col>
                        <v-btn variant="outlined" class="bg-indigo float-right text-white text-capitalize">View More</v-btn>
                    </v-col>
                </v-row>
            </v-card-title>
            <v-card-text>
                 <v-data-table-server
    v-model:items-per-page="itemsPerPage"
    :headers="headers"
    :items="serverItems"
    :items-length="totalItems"
    :loading="loading"
    :search="search"
    item-value="name"
    @update:options="loadItems"
  ></v-data-table-server>
            </v-card-text>
        </v-card>
        </div>
    </v-card-text>
    </v-card>

</template>
