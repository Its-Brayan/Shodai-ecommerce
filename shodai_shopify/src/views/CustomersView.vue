<template>
    <v-card>
        
        <HeaderComponent/>
        <v-card-text class="bg-grey-lighten-4">
         <v-card class=" mt-16" >
            <v-card-text>
                <v-row>
                    <v-col cols="6">
                        <v-tabs
                        bg-color="grey-lighten-4">
                         <v-tab class="text-grey-darken-1 text-capitalize">All Customers</v-tab>
                           <v-tab class="text-grey-darken-1 text-capitalize">New Customers</v-tab>
                             <v-tab  class="text-grey-darken-1 text-capitalize">From Europe</v-tab>
                               <v-tab  class="text-grey-darken-1 text-capitalize">Asia</v-tab>
                                  <v-tab  class="text-grey-darken-1 text-capitalize">Others</v-tab>
                               
                        </v-tabs>
                    </v-col>
                    <v-col cols="4">
                         <v-btn 
                    prepend-icon="mdi-tray-arrow-down"
                  
                   
                    variant="outlined"
                    width="200px"
                     size="large"
                    class="text-capitalize float-right d-flex-justify-end "
                    >
                 Export
                        
                    </v-btn>
                    </v-col>
                    <v-col cols="2">
                    <v-btn 
                 
                  
                   @click="openDialog"
                    variant="outlined"
                    width="200px"
                     size="large"
                    class="text-capitalize float-right d-flex-justify-end bg-indigo text-white"
                    >
                 Add Customer
                        
                    </v-btn>
                       </v-col>
                </v-row>
            </v-card-text>
         </v-card>
      
          <v-card class="mt-2">
            <v-card-title class="mt-3 pa-6">
                <v-row>
                    <v-col cols="1">
                 <v-btn 
                    prepend-icon="mdi-filter-outline"
                  
                   
                    variant="outlined"
                    width="120px"
                     size="large"
                    class="text-capitalize  d-flex-justify-start bg-grey-lighten-3"
                    >
                 Filter
                        
                    </v-btn>
                    </v-col>
                    <v-col cols="2">
                        <v-text-field
                        variant="outlined"
                        prepend-inner-icon="mdi-magnify"
                        width="300px"
                        label="Search Customers"
                        density="compact"
                        color="grey-darken-2"
                        class="text-grey-darken-2"></v-text-field>
                    </v-col>

                    </v-row>
            </v-card-title>
              <v-dialog
      v-model="dialog"
      max-width="600"
    >
     
      <v-card>
        <v-card-title>
          <span><v-icon>mdi-account-outline</v-icon></span>
          <span> Customer</span>
        <span class="float-right"><v-icon @click="dialog=false">mdi-close-circle</v-icon></span>
        </v-card-title>
        <v-card-text>
          <v-row dense>
            <v-col
              cols="12"
              md="11"
              sm="10"
            >
              <v-text-field
                label="Customer Name*"
                required
                v-model="form.customerName"
                variant="outlined"
                color="grey-darken-2"
                density="compact"
              ></v-text-field>
            </v-col>
            </v-row>
              <v-row dense>
            <v-col
              cols="12"
              md="11"
              sm="10"
            >
              <v-text-field
                label="Customer Email*"
                required
                v-model="form.customerEmail"
                variant="outlined"
                color="grey-darken-2"
                density="compact"
              ></v-text-field>
            </v-col>
            </v-row>
             <v-row dense>
            <v-col
              cols="12"
              md="11"
              sm="10"
            >
              <v-select
                label="Customer Location*"
                required
                :items="['Europe', 'Asia']"
                v-model="form.customerLocation"
                item-title="categoryName"
                item-value="id"
              
                variant="outlined"
                color="grey-darken-2"
                density="compact"
              ></v-select>
            </v-col>
            </v-row>
             <v-row dense>
            <v-col
              cols="12"
              md="11"
              sm="10"
            >
              <v-text-field
                label="Number of orders*"
                required
                v-model="form.customerOrders"
                variant="outlined"
                color="grey-darken-2"
                density="compact"
              ></v-text-field>
            </v-col>
            </v-row>
             <v-row dense>
            <v-col
              cols="12"
              md="11"
              sm="10"
            >
              <v-text-field
                label="Total Paid*"
                required
                v-model="form.cashSpent"
                variant="outlined"
                color="grey-darken-2"
                density="compact"
              ></v-text-field>
            </v-col>
            </v-row>
          
        </v-card-text>

      

        <v-card-actions>
          <v-spacer></v-spacer>

     
          <v-btn
          
            :text="isediting ? 'update customer' : 'create customer'  "
             class="bg-indigo text-white text-capitalize"
            variant="tonal"
            @click="submitcustomer"
          ></v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
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
  >
  <template v-slot:item.actions="{item}">
     <v-btn prepend-icon="mdi-pencil" @click="openDialog(item)" variant="outlined" size="small" class="text-capitalize bg-indigo ma-3">Edit</v-btn>
    <v-icon size="small" @click="deletecustomer(item.id)">mdi-trash-can-outline</v-icon>
  </template>
  
</v-data-table-server>
            </v-card-text>
          </v-card>

        </v-card-text>
    </v-card>
</template>

<script setup>
  import { ref } from 'vue'
  import HeaderComponent from '@/components/HeaderComponent.vue'
  import axiosInst from '@/services/api.js' 
  const dialog = ref(false)
  const isediting = ref(false)
  const customerid = ref(null)
  function openDialog(item){
    dialog.value = true
    if(item){
       isediting.value = true
       customerid.value = item.id
      form.value.customerName = item.customerName
      form.value.customerEmail = item.customerEmail
      form.value.customerLocation = item.customerLocation
      form.value.customerOrders = item.customerOrders
      form.value.cashSpent = item.cashSpent

    }
    else{
      isediting.value = false
      form.value = {
        customerName : '',
        customerEmail : '',
        customerLocation:'',
        customerOrders: '',
        cashSpent:''
      }
    }
  }
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
   
    { title: 'Customer Name', key: 'customerName', align: 'start' },
    { title: 'Email', key: 'customerEmail', align: 'start' },
    { title: 'Location', key: 'customerLocation', align:'start' },
    { title: 'Orders', key: 'customerOrders', align: 'start' },
    { title: 'Spent',key:'cashSpent', align: 'start' },
     { title: 'Action',key:'actions', align: 'start' },
    ])
  const search = ref('')
  const serverItems = ref([])
  const loading = ref(true)
  const totalItems = ref(0)
  async function  loadItems ({ page, itemsPerPage, sortBy }) {
    loading.value = true
     await  axiosInst.get(`api/createcustomer/`,{
      params:{
      page:page,
      itemsPerPage:itemsPerPage,
      search:search.value
      }
     }
     ).then(response =>{
      serverItems.value = response.data
      totalItems.value = response.data.count 
      loading.value = false
     }
     ).catch(error =>{
      console.error("Error fetching data", error)
      loading.value = false
     }

     )

    
  }
let form = ref({
  customerName:'',
  customerEmail:'',
  customerLocation:'',
  customerOrders:'',
  cashSpent:''
})
  function submitcustomer(){
    const formdata = {
      ...form.value
    }
    if(isediting.value==false){
  axiosInst.post(`api/createcustomer/`,formdata)
  .then(response =>{
    console.log(response.data)
  }

  ).catch( error =>{
    console.error(error)
  }
     
  )
}
else{
  axiosInst.put(`api/updatecustomer/${customerid.value}/`, formdata)
  .then(response =>{
    console.log(response.data)
  }

  ).catch(error=>{
    console.error(error)
  }

  )
}
  }
  function deletecustomer(id){
    axiosInst.delete(`api/updatecustomer/${id}/`)
    .then(response =>{
      console.log('Customer deleted successfully', response.data)
    }

    ).catch(error =>{
      console.error("Error deleting customer", error)
    }

    )
  }
</script>