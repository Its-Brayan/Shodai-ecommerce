<template>
    <v-card>
        
        <HeaderComponent/>
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
                        v-model="search"
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
                  
                   @click="openDialog()"
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
               <div class="pa-4 text-center">
    <v-dialog
      v-model="dialog"
      max-width="600"
    >
     
      <v-card>
        <v-card-title>
          <span><v-icon>mdi-cart-outline</v-icon></span>
          <span> Product</span>
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
                label="Product Name*"
                required
                v-model="form.productName"
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
                label="Product SKU*"
                required
                v-model="form.ProductSku"
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
                label="Product Category*"
                required
                :items="fetchedcategories"
                v-model="form.productCategory"
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
                label="Purchase unit price*"
                required
                v-model="form.productPrice"
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
                v-model="form.ProductNumber"
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
                label="Status*"
                :items="['Active', 'Inactive']"
                required
                v-model="form.productStatus"
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
              <v-file-upload density="compact" v-model="form.productImage"></v-file-upload>

            </v-col>
            </v-row>
        </v-card-text>

      

        <v-card-actions>
          <v-spacer></v-spacer>

     
          <v-btn
          
            :text="isediting ? 'update product' : 'submit product'  "
             class="bg-indigo text-white text-capitalize"
            variant="tonal"
            @click="submitproducts"
          ></v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
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
  >
  <template v-slot:item.actions="{ item,value }">
   <v-btn prepend-icon="mdi-pencil" @click="openDialog(item)" variant="outlined" size="small" class="text-capitalize bg-indigo ma-3">Edit</v-btn>
    <v-icon size="small" @click="deleteproduct(item.id)">mdi-trash-can-outline</v-icon>
  </template>
  <template v-slot:item.productStatus="{ item }">
    <v-chip
      :color="item.productStatus == 'Active' ? 'green' : 'red'"
      text-color="white"
    >
      {{ item.productStatus }}
    </v-chip>
    
  </template>
  <template v-slot:item.productPrice="{item}">
    ksh {{item.productPrice}}
  </template>
  <template v-slot:item.productImage="{ item }">
    <v-img
      :src="getImageUrl(item.productImage)"
      max-width="50"
      max-height="50"
      contain
    ></v-img>
  </template>
</v-data-table-server>
            </v-card-text>
          </v-card>

        </v-card-text>
    </v-card>
  
</template>

<script setup>

  import { onMounted, ref, watch } from 'vue'
import HeaderComponent from '@/components/HeaderComponent.vue'
import axiosInst from '@/services/api.js'
const dialog = ref(false)
function openDialog(item) {
  dialog.value=true
  if(item){
      isediting.value = true
       productid.value = item.id
      form.value.productName = item.productName
      form.value.productPrice = item.productPrice
      form.value.ProductNumber = item.ProductNumber
      form.value.productStatus = item.productStatus
      form.value.ProductSku = item.ProductSku
      form.value.productCategory = item.productCategory  
      form.value.productImage = null
      
    }
    else {
        dialog.value=true
      isediting.value = false
    form.value.productName = ''
     form.value.productName= ''
      form.value.productPrice=''
      form.value.ProductNumber=''
     form.value.productStatus=''
    form.value.productCategory= ''
     form.value.ProductSku=''
     form.value.productImage= null
     }
    

  
 
   
} 

     
  const itemsPerPage = ref(5)
  const headers = ref([
     {title:'product Image', key:'productImage', align:'start'},
    { title: 'Product name', key: 'productName', align: 'start' },
     {title: 'SKU', key: 'ProductSku', align: 'start' },
    { title: 'Purchase Unit Price', key: 'productPrice', align: 'start' },
    { title: 'Number of Products', key: 'ProductNumber', align: 'start' },
    { title: 'Category', key: 'categoryName', align: 'start' },
    { title: 'Status', key: 'productStatus', align: 'start' },
    { title: 'actions',key:'actions', align: 'start' },
  ])
  const search = ref('')
  const serverItems = ref([])
  const loading = ref(true)
  const totalItems = ref(0)
  function loadItems ({ page, itemsPerPage, sortBy }) {
    loading.value = true
      axiosInst.get('/api/products/', {
      params: {
        page: page, 
        itemsPerPage: itemsPerPage,
        search:search.value
       
      },
    }).then(response => {
      serverItems.value =Array.isArray(response.data.results) ? response.data.results : [];
      totalItems.value = response.data.count  
      loading.value = false
    }).catch(error => {
      console.error('Error fetching products:', error);
      loading.value = false
    })
  }
  let form = ref({
    productName: '',
    productPrice: '',
    ProductNumber: '',
    productStatus: '',
    productCategory: '',
    ProductSku: '',
    productImage: null,
  })
  const isediting = ref(false)
  const productid = ref(null)
  function submitproducts(){
 const formdata = new FormData();
 formdata.append('productName', form.value.productName);
 formdata.append('productPrice', form.value.productPrice);
  formdata.append('ProductSku', form.value.ProductSku);
 formdata.append('ProductNumber', form.value.ProductNumber);
  formdata.append('productCategory', form.value.productCategory);
 formdata.append('productStatus', form.value.productStatus);
 formdata.append('productImage', form.value.productImage);
 // Here you can send formdata to your API
if(isediting){
 axiosInst.post('/api/products/', formdata, {
   headers: {
     'Content-Type': 'multipart/form-data'
   }
 }).then(response => {
   console.log('Product submitted successfully:', response.data); 
    dialog.value = false; // Close the dialog after submission
    loadItems({page:1, itemsPerPage:itemsPerPage.value});
  }).catch(error => {
    console.error('Error submitting product:', error);
  });
}
else{
  axiosInst.put(`api/productdetail/${productid.value}/`, formdata,{
    headers:{
      'Content-Type':'multipart/form-data'
    }
  }).then(response =>{
    console.log("product edit successfully",response.data)
     dialog.value=false
        loadItems({page:1, itemsPerPage:itemsPerPage.value});

  }

  ).catch(error =>{
    console.error("Failed to edit product:",error);
  }

  )
}
 
  }
  const BASE_URL = 'http://localhost:8000';
function getImageUrl(path) {
  if (!path) return '';
  // If path is already absolute, return as is
  if (path.startsWith('http')) return path;
  return BASE_URL + path;
}
  const fetchedcategories = ref([]);
  function fetchcategories() {
    axiosInst.get('/api/categories/')
      .then(response => {
        // Handle the response data
        console.log('Categories fetched successfully:', response.data);
         fetchedcategories.value = response.data;
      })
      .catch(error => {
        console.error('Error fetching categories:', error);
      });
  }
  onMounted(() => {
    fetchcategories();
    loadItems({page:1, itemsPerPage:itemsPerPage.value} )
    
  });
  function deleteproduct(id) {
    axiosInst.delete(`/api/productdetail/${id}/`)
      .then(response => {
        console.log('Product deleted successfully:', response.data);
        loadItems({ page: 1, itemsPerPage: itemsPerPage.value, sortBy: [] }); // Refresh the product list
        // Optionally, refresh the product list or handle UI updates
      })
      .catch(error => {
        console.error('Error deleting product:', error);
      });
  }
  watch(search,()=>{
    loadItems({page:1,itemsPerPage:itemsPerPage.value})
  }

  )
  
</script>