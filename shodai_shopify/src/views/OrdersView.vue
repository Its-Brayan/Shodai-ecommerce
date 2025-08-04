<template>
    <v-card>
        
        <HeaderComponent/>
        <v-card-text class="bg-grey-lighten-4">
         <v-card class=" mt-16" >
            <v-card-text>
                <v-row>
                    <v-col cols="5">
                        <v-tabs
                        bg-color="grey-lighten-4" v-model="selectedtab">
                         <v-tab value='' class="text-grey-darken-1 text-capitalize">All Orders
                        </v-tab>
                           <v-tab value="Draft" class="text-grey-darken-1 text-capitalize">Draft</v-tab>
                             <v-tab  value="Cancelled" class="text-grey-darken-1 text-capitalize">Cancelled</v-tab>
                               <v-tab value="Shipped" class="text-grey-darken-1 text-capitalize">Shipping</v-tab>
                                  <v-tab value="Completed"  class="text-grey-darken-1 text-capitalize">Completed</v-tab>
                               
                        </v-tabs>
                      
                    </v-col>
                    <v-col cols="5">
                         <v-btn 
                    prepend-icon="mdi-tray-arrow-down"
                  
                   
                    variant="outlined"
                    width="200px"
                     size="large"
                    class="text-capitalize float-right d-flex-justify-end "
                    >
                 Export as CSV
                        
                    </v-btn>
                    </v-col>
                    <v-col cols="2">
                    <v-btn 
                    prepend-icon="mdi-plus"
                    
                    @click="opendialog()"
                    variant="outlined"
                    width="200px"
                     size="large"
                    class="text-capitalize float-right d-flex-justify-end bg-indigo text-white"
                    >
                 Add Orders
                        
                    </v-btn>
                       </v-col>
                </v-row>
            </v-card-text>
         </v-card>
      
          <v-card class="mt-2">
               <v-card-title class="mt-3 pa-6">
                <v-row>
                         <v-col cols="3">
                        <v-text-field
                        variant="outlined"
                        prepend-inner-icon="mdi-magnify"
                        width="300px"
                        label="Search using OrderId"
                        v-model="search"
                        density="compact"
                        color="grey-darken-2"
                        class="text-grey-darken-2"></v-text-field>
                    </v-col>

                    <v-col cols="2">
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
    <template v-slot:item.actions="{item}">
     <v-btn prepend-icon="mdi-pencil" @click="opendialog(item)" variant="outlined" size="small" class="text-capitalize bg-indigo ma-3">Edit</v-btn>
    <v-icon size="small" @click="deleteorder(item.id)">mdi-trash-can-outline</v-icon>
  </template>
  <template v-slot:item.orderStatus="{item}">
    <v-chip variant="elevated"
     :color="item.orderStatus ==='Cancelled'? 'red' : item.orderStatus==='Completed' ? 'green'  : item.orderStatus==='Shipped' ? 'orange' : item.orderStatus ==='Draft' ? 'grey-darken-4' : '' "
    >{{ item.orderStatus }}</v-chip>
  </template>
  <template v-slot:item.datePurchased="{item}">
    {{formatdate(item.datePurchased)}}
  </template>
</v-data-table-server>
            </v-card-text>
          </v-card>

        </v-card-text>

    </v-card>
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
                label="Order ID*"
                required
                v-model="form.OrderId"
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
                label="Number of products*"
                required
                v-model="form.OrderNumber"
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
              <v-autocomplete
                label="Customer Email*"
                required
               
                v-model="form.CustomerName"
                :items="customerdetails"
                item-title="customerEmail"
                item-value="id"
              
                variant="outlined"
                color="grey-darken-2"
                density="compact"
              ></v-autocomplete>
            </v-col>
            </v-row>
             <v-row dense>
            <v-col
              cols="12"
              md="11"
              sm="10"
            >
               <v-date-input
                label="Date purchased*"
                  prepend-icon=""
                  prepend-inner-icon="mdi-calendar"
                required
                v-model="form.datePurchased"
                variant="outlined"
                color="grey-darken-2"
                density="compact"
              ></v-date-input>
            </v-col>
            </v-row>
             <v-row dense>
            <v-col
              cols="12"
              md="11"
              sm="10"
            >
              <v-select
                label="Payment Method*"
                required
                :items="['Mpesa','PayPal']"
                v-model="form.paymentMethod"
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
                label="Amount paid*"
                required
                v-model="form.amountPaid"
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
                label="Order Status*"
                required
                :items="['Draft','Cancelled','Shipped','Completed']"
                v-model="form.orderStatus"
                variant="outlined"
                color="grey-darken-2"
                density="compact"
              ></v-select>
            </v-col>
            </v-row>
          
        </v-card-text>

      

        <v-card-actions>
          <v-spacer></v-spacer>

     
          <v-btn
          
            :text="isediting ? 'update order' : 'create order'  "
             class="bg-indigo text-white text-capitalize"
            variant="tonal"
            @click="submitorder"
          ></v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
</template>

<script setup>
import dayjs from 'dayjs';
  import { onMounted, ref, watch} from 'vue'
  import axiosInst from '@/services/api.js' 
  import HeaderComponent from '@/components/HeaderComponent.vue'
  const dialog = ref(false)
  const isediting = ref(false)
  const orderid = ref(null)
  function opendialog(item){
    dialog.value = true
    if(item){
      orderid.value = item.id
      isediting.value = true
      form.value={
           OrderId : item.OrderId,
           OrderNumber:item.OrderNumber,
            CustomerName:item.CustomerName,
            datePurchased:item.datePurchased,
             paymentMethod:item.paymentMethod,
             amountPaid : item.amountPaid,
             orderStatus:item.orderStatus
      }
    }
    else{
      isediting.value = false
      form.value ={
  OrderId : '',
  OrderNumber:'',
  CustomerName:'',
  datePurchased:'',
  paymentMethod:'',
  amountPaid : '',
  orderStatus:''
    }
  }
}
 
  const itemsPerPage = ref(5)
  const headers = ref([
    {
      title: 'Order ID',
      align: 'start',
      sortable: false,
      key: 'OrderId',
    },
    { title: 'Number of Products', key: 'OrderNumber', align: 'start' },
    { title: 'Customer', key: 'customeremail', align: 'start' },
    { title: 'Date purchased', key: 'datePurchased', align: 'start' },
    { title: 'Payment', key: 'paymentMethod', align: 'start' },
    { title: 'Price',key:'amountPaid', align: 'end' },
     { title: 'Order Status',key:'orderStatus', align: 'end' },
     { title: 'actions',key:'actions', align: 'end' },
  ])
  const search = ref('')
  const serverItems = ref([])
  const loading = ref(true)
  const totalItems = ref(0)
  const selectedtab = ref('')
  function loadItems ({ page, itemsPerPage, sortBy }) {
    loading.value = true
      axiosInst.get('api/createorder/',{
        params:{
          page:page,
          itemsPerPage:itemsPerPage,
          search:search.value,
          status:selectedtab.value
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
  function formatdate(datestr){
    return dayjs(datestr).format('YYYY-MM-DD');
  }
  const customerdetails = ref({})
  let form = ref({
    OrderId : '',
    OrderNumber:'',
  CustomerName:'',
  datePurchased:'',
  paymentMethod:'',
  amountPaid : '',
  orderStatus:''
  })
  function submitorder(){
    const formdata = {
      ...form.value
    }
   if(isediting.value==false){
    axiosInst.post(`api/createorder/`, formdata)
    .then( response =>{
      console.log(response.data, "Order created successfully")
      loadItems ({ page:1, itemsPerPage:itemsPerPage.value })
       dialog.value=false
    }

    ).catch(error =>{
      console.error("error creating order", error)
    }

    )
  }
  else if(isediting.value==true){
    axiosInst.put(`api/updateorder/${orderid.value}/`, formdata)
    .then(response=>{
      console.log("Order edited successfully", response.data)
        loadItems ({ page:1, itemsPerPage:itemsPerPage.value })
        dialog.value=false
    }

    ).catch(error=>{
      console.error("Failed to edit order", error)
    }

    )
  }
}
async  function fetchcustomeremail(){
   await axiosInst.get(`api/createcustomer/`)
   .then(response =>{
    console.log("Fetched customer details successfully", response.data)
    customerdetails.value = response.data.results
   }

   ).catch(error =>{
    console.error("failed to fetch customer detail", error)
   }

   )
  }
  function deleteorder(id){
    axiosInst.delete(`api/updateorder/${id}/`)
    .then(response=>{
      console.log("deleted successfully", response.data)
        loadItems ({ page:1, itemsPerPage:itemsPerPage.value })
    }

    ).catch(error =>{
      console.error("Failed to delete order", error)
    }

    )
  }

  onMounted(() =>{
    fetchcustomeremail()

  }

  )
  watch(selectedtab, (newTab, oldTab) => {
  console.log('Tab changed from', oldTab, 'to', newTab)
  loadItems({ page: 1, itemsPerPage: itemsPerPage.value })
})
</script>