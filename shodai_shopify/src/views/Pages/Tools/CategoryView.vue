<template>
    <v-card>
        
        <HeaderComponent/>
        <v-card-text class="bg-grey-lighten-4">
         <v-card class=" mt-16" >
            <v-card-text>
            
                    <v-btn 
                    prepend-icon="mdi-plus"
                  
                    @click="opendialog()"
                    variant="outlined"
                    width="200px"
                     size="large"
                    class="text-capitalize float-right mb-4 d-flex-justify-end bg-indigo text-white"
                    >
                 Add Category
                        
                    </v-btn>
                      <div class="pa-4 text-center">
    <v-dialog
      v-model="dialog"
      max-width="600"
    >
     
      <v-card>
       
      <v-card-title>
        <span class="text-indigo">
        Category</span>
        <span class="float-right"><v-icon @click="closedialog">mdi-close-circle</v-icon></span>

      </v-card-title>
      
        <v-card-text>
          <v-row dense>
            <v-col
              cols="12"
              md="11"
              sm="10"
            >
              <v-text-field
                label="Category name*"
                variant="outlined"
                color="grey-darken-2"
                v-model="form.categoryName"
                required
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
            v-model="form.categoryStatus"
  label="Select"
  :items="['Active', 'Inactive']"
  variant="outlined"
></v-select>
            </v-col>
            <v-row>
                <v-col
              cols="12"
              md="11"
              sm="10"
            >
               <v-container fluid>
    <v-textarea
      autocomplete="email"
      v-model="form.categoryDescription"
      label="Category description"
      clearable
      variant="outlined"
    ></v-textarea>
  </v-container>
            </v-col>
            </v-row>
         </v-row>
          <v-row dense>
            <v-col
              cols="12"
              md="11"
              sm="10"
            >
          <v-file-upload  v-model="form.categoryImage" clearable density="compact" title="Drag and drop Category Image"
          ><div v-if="form.categoryImagePreview && !form.categoryImage" class="mt-2">
            Hii
  <v-img :src="getImageUrl(form.categoryImagePreview)" max-width="100" max-height="100" />
</div>
        </v-file-upload>
            </v-col>
            
         </v-row>
        </v-card-text>
           

        <v-card-actions>
          <v-spacer></v-spacer>

         
          <v-btn
             class="bg-indigo text-white text-capitalize"
            :text="isediting ? 'Update Category' : 'Create Category'"
            variant="tonal"
            @click="submitCategory"
          ></v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
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
                    class="text-capitalize   d-flex-justify-start bg-grey-lighten-3"
                    >
                 Filter
                        
                    </v-btn>
                    </v-col>
                    <v-col cols="2">
                        <v-text-field
                        variant="outlined"
                        prepend-inner-icon="mdi-magnify"
                        width="300px"
                        label="Search Categories"
                        density="compact"
                        color="grey-darken-2"
                        class="text-grey-darken-2"></v-text-field>
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
  <template v-slot:item.categoryImage="{ item }">
    <v-img :src="getImageUrl(item.categoryImage)" max-width="70" max-height="70"></v-img>
  </template>
  <template v-slot:item.categoryStatus="{item}">
    <v-chip :color="item.categoryStatus == 'Active' ? 'green' : 'red'"
            class="text-capitalize"
            variant="outlined"
            size="small">
      {{ item.categoryStatus}}
    </v-chip>
  </template>
  <template v-slot:item.actions="{ item,value }">

   <v-btn prepend-icon="mdi-pencil" @click="opendialog(item)" variant="outlined" size="small" class="text-capitalize bg-indigo ma-3">Edit</v-btn>
    <v-icon size="small" @click="deletecategory(item.id)">mdi-trash-can-outline</v-icon>
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
    import { toast } from 'vue-sonner';
import axiosInst from '@/services/api.js'
  const dialog = ref(false)
  const categoryid = ref(null)
  function opendialog(item){
    dialog.value = true
    if(item){
      isediting.value = true
      categoryid.value = item.id
    form.value.categoryName = item.categoryName 
     form.value.categoryDescription= item.categoryDescription
    form.value.categoryStatus = item.categoryStatus
    form.value.categoryImage = null
    form.value.categoryImagePreview = item.categoryImage
    }else{
      isediting.value = false
      form.value.categoryName = ''
      form.value.categoryDescription = ''
      form.value.categoryStatus = ''
      form.value.categoryImage = null
      form.value.categoryImagePreview = ''

    }
}
  function closedialog(){
    dialog.value = false
  }


const BASE_URL = 'http://localhost:8000'; // Change to your backend URL

function getImageUrl(path) {
  if (!path) return '';
  // If path is already absolute, return as is
  if (path.startsWith('http')) return path;
  return BASE_URL + path;
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
let form = ref({
  categoryName:'',
  categoryStatus:'',
  categoryDescription:'',
  categoryImage:null,
  categoryImagePreview:'',
}
  
)
const isediting = ref(false)
  function submitCategory(){
    const formdata = new FormData();
formdata.append('categoryName', form.value.categoryName);
formdata.append('categoryStatus', form.value.categoryStatus);
formdata.append('categoryDescription', form.value.categoryDescription);
if (form.value.categoryImage) {
  formdata.append('categoryImage', form.value.categoryImage);
}
  if(!isediting.value){

axiosInst.post(`api/categories/`,formdata,{
  headers: {
    'Content-Type': 'multipart/form-data',
  },
})
.then(response => {
  toast.success('Category created successfully!');
  console.log('Category created successfully:', response.data);
  dialog.value = false; // Close the dialog after successful submission
   loadItems({page:1,itemsPerPage:itemsPerPage})
})
.catch(error => {
  console.error('Error creating category:', error);

    toast.error('Failed to create category. Please try again.');

}); 
  }else{
      axiosInst.put(`api/categorydetail/${categoryid.value}/`,formdata,{
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      })
      .then(response => {
        toast.success('Category updated successfully!');
        console.log('Category updated successfully:', response.data);
        
        dialog.value = false; 
        // Close the dialog after successful submission
        loadItems({page:1,itemsPerPage:itemsPerPage})
      })
      .catch(error => {
        console.error('Error updating category:', error);     
        toast.error('Failed to update category. Please try again.');
      });
  }
  }
  const itemsPerPage = ref(5)
  const headers = ref([
    {
      title: 'Image',
      align: 'start',
      sortable: false,
      key: 'categoryImage',
    },
    { title: 'Category Name', key: 'categoryName', align: 'end' },
    { title: 'Category Status', key: 'categoryStatus', align: 'end' },
    { title: 'Category Description', key: 'categoryDescription', align: 'end' },
     { title: 'Action',key:'actions', align: 'end' },
    ])
  const search = ref('')
  const serverItems = ref([])
  const loading = ref(true)
  const totalItems = ref(0)
  function loadItems ({ page, itemsPerPage, sortBy }) {
    loading.value = true
    axiosInst.get(`api/categories/`, {
        params: {
          page:1,
          itemsPerPage:itemsPerPage,
       
        },
      })
      .then(response => {
        serverItems.value = response.data.results || response.data;
        totalItems.value = response.data.total;
        loading.value = false;
      })
      .catch(error => {
        console.error('Error fetching items:', error);
        loading.value = false;
      });
     
  }
 function deletecategory(item){
  try{
  axiosInst.delete(`api/categorydetail/${item}/`)
  
    toast.success('Category deleted successfully!');
    loadItems({ page: 1, itemsPerPage: 10, sortBy: [] });
  }catch (error) {

    console.error('Error deleting category:', error);
    toast.error('Failed to delete category. Please try again.');
  }

 }
 
 
</script>