<script setup>
import HeaderComponent from '@/components/HeaderComponent.vue';
import axiosInst from '@/services/api';
import dayjs from 'dayjs';
 import { ref,onMounted } from 'vue'

  
  const itemsPerPage = ref(5)
  const headers = ref([
    {
      title: 'OrderID',
      align: 'start',
      sortable: false,
      key: 'OrderId',
    },
    { title: 'Customer', key: 'customeremail', align: 'end' },
    { title: 'Date Purchased', key: 'datePurchased', align: 'end' },
    { title: 'Price', key: 'amountPaid', align: 'end' },
    { title: 'Status', key: 'orderStatus', align: 'end' },
   
  ])
  const search = ref('')
  const serverItems = ref([])
  const loading = ref(true)
  const totalItems = ref(0)
  const limit=ref(2)
  function loadItems ({ page, itemsPerPage, sortBy }) {
    loading.value = true
     axiosInst.get('api/getrecentorders/',{
        params:{
          page:page,
          itemsPerPage:itemsPerPage,
          search:search.value,
          limit:limit.value
       
        }
      }


      )
      .then(response=>{
      serverItems.value = response.data.results
      totalItems.value = response.data.count
      loading.value = false
      }
  ).catch(error=>{
    console.error("Could fetch the orders", error)
    loading.value=false
  }

  )
   
  
  }
  const allorders=ref()
  function formatdate(datestr){
    return dayjs(datestr).format('YYYY-MM-DD');
  }
  function getorders(){
    axiosInst.get(`api/getallorders/`)
    .then(response=>{
        allorders.value = response.data.count || response.data.length
        console.log("Fetched all orders")
    
  }
)
  .catch(error=>{
    console.log("error fetching orders",error)
  }
)

  }
  const allproducts = ref()
  function getproducts(){
    axiosInst.get(`api/getallproducts/`)
    .then(response=>{
        allproducts.value = response.data.count || response.data.length
        console.log("Fetched all orders")
    
  }
)
  .catch(error=>{
    console.log("error fetching orders",error)
  }
)

  }
  const allcustomers = ref()
  function getcustomers(){
    axiosInst.get(`api/getallcustomers/`)
    .then(response=>{
        allcustomers.value = response.data.count || response.data.length
        console.log("Fetched all Customers")
    
  }
)
  .catch(error=>{
    console.log("error fetching customers",error)
  }
)

  }
  onMounted(()=>{
    getorders()
    getproducts()
    getcustomers()
  }
  )

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
                       {{ allcustomers }}
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
                       {{ allorders }}
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
                       {{ allproducts }}
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
                        <v-btn to="/orders" variant="outlined" class="bg-indigo float-right text-white text-capitalize">View More</v-btn>
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
  >
  <template v-slot:item.datePurchased="{item}">
    {{ formatdate(item.datePurchased) }}
    </template>
    <template v-slot:item.orderStatus="{item}">
  <v-chip variant="elevated"
     :color="item.orderStatus ==='Cancelled'? 'red' : item.orderStatus==='Completed' ? 'green'  : item.orderStatus==='Shipped' ? 'orange' : item.orderStatus ==='Draft' ? 'grey-darken-4' : '' "
    >{{ item.orderStatus }}</v-chip>
    </template>
</v-data-table-server>
            </v-card-text>
        </v-card>
        </div>
    </v-card-text>
    </v-card>

</template>
