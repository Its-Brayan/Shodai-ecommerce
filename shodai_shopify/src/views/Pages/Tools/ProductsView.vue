<template>
    <v-card>
        
        <v-card-title class="pt-5">
            
             
           <v-row>
            <v-col cols="8">
            <v-text-field
            variant="outlined"
            prepend-inner-icon="mdi-magnify"
            width="500px"
            rounded="pill"
            label="Search Products"
            density="compact"
            color="grey-darken-2"
            >

            </v-text-field>
            </v-col>
        
            <div class="d-flex justify-end ml-16">
                <v-col>
                    <v-icon style="cursor: pointer;" size="small">mdi-message-badge-outline</v-icon>
                </v-col>
                <v-col>
                    <v-icon style="cursor: pointer;" size="small">mdi-bell-badge-outline</v-icon>
                </v-col>
                <v-col  >
                    <v-img
                    :width="35"
                     aspect-ratio="16/9"
                    src="https://cdn-icons-png.flaticon.com/128/1999/1999625.png"
                    ></v-img>
                </v-col>
                <v-col>
                   
                    <p class="text-subtitle-1 mt-1">Brayan mwangi</p>
                   
                </v-col>
                <v-col class="ml-n5" >
                    <v-icon style="cursor: pointer;" size="small">mdi-menu-down</v-icon>
                </v-col>
                </div>
            </v-row>
          
        </v-card-title>
        <v-card-text class="bg-grey-lighten-4">
         <v-card class=" mt-16" >
            <v-card-text>
                <v-row>
                    <v-col cols="3">
                       <v-text-field
                        variant="outlined"
                        prepend-inner-icon="mdi-magnify"
                        width="300px"
                      
                        label="Search Products"
                        density="compact"
                        color="grey-darken-2"
                        class="text-grey-darken-2"></v-text-field>
                        
                    </v-col>
                    <v-col cols="2">
                        <v-select 
                        label="all products"
                        density="compact"
                        width="200px"
                        variant="outlined"></v-select>
                    </v-col>
                     <v-col cols="2">
                        <v-select 
                        label="Sort By"
                        color="grey-darken-2"
                        density="compact"
                        width="200px"
                        variant="outlined"></v-select>
                    </v-col>
                    <v-col>
                    <v-btn 
                    prepend-icon="mdi-plus"
                  
                   
                    variant="outlined"
                    width="200px"
                     size="large"
                    class="text-capitalize float-right d-flex-justify-end bg-indigo text-white"
                    >
                 Add product
                        
                    </v-btn>
                       </v-col>
                </v-row>
            </v-card-text>
         </v-card>
         <v-card class="mt-3">
            <v-card-text>
                <v-row>
                    <v-col cols="3">
                        <p class="text-subtitle-2">Category</p>
                    </v-col>
                      <v-col cols="3">
                        <p class="text-subtitle-2">Status</p>
                    </v-col>
                      <v-col cols="3">
                        <p class="text-subtitle-2">Price</p>
                    </v-col>
                      <v-col cols="3">
                        <p class="text-subtitle-2">Store</p>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="3">
                        <v-select 
                        label="Jackets(132)"
                        color="grey-darken-2"
                        density="compact"
                        width="200px"
                        variant="outlined"></v-select>
                    </v-col>
                       <v-col cols="3">
                        <v-select 
                        label="All Status"
                        color="grey-darken-2"
                        density="compact"
                        width="200px"
                        variant="outlined"></v-select>
                    </v-col>
                       <v-col cols="3">
                        <v-select 
                        label="$50-$100"
                        color="grey-darken-2"
                        density="compact"
                        width="200px"
                        variant="outlined"></v-select>
                    </v-col>
                       <v-col cols="3">
                        <v-select 
                        label="All Stores"
                        color="grey-darken-2"
                        density="compact"
                        width="200px"
                        variant="outlined"></v-select>
                    </v-col>
                </v-row>
            </v-card-text>
         </v-card>
          <v-card>
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

        </v-card-text>
    </v-card>
</template>

<script setup>
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