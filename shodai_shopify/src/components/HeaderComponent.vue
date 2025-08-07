<template>
     <v-card-title class="pt-5">
     <v-row>
         
            <v-col cols="8">
            <v-text-field
            variant="outlined"
            prepend-inner-icon="mdi-magnify"
            width="500px"
            rounded="pill"
            label="Search..."
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
                   
                <v-menu
      transition="slide-x-transition"
    >
      <template v-slot:activator="{ props }">
        <v-btn
          color="primary"
          v-bind="props"
          class="text-capitalize"
        >
                  Brayan Mwangi
                <v-icon style="cursor: pointer;" size="small">mdi-menu-down</v-icon>
        </v-btn>
      </template>

      <v-list>
        <v-list-item>
            <v-btn nav to="/login" block prepend-icon="mdi-power" variant="text" color="red">
          <v-list-item-title prepend-icon="mdi-power">Sign out</v-list-item-title>
          
          </v-btn>
        </v-list-item>
      </v-list>
    </v-menu>

                   
                </v-col>
                <v-col class="ml-n5" >

              
                </v-col>
                </div>
            </v-row>
          
        </v-card-title>
</template>