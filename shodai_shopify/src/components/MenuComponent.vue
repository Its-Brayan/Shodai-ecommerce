<template>
  <v-card>
    <v-layout>
      <v-navigation-drawer
        location="left"
        permanent
      >
        <template v-slot:prepend>
          <v-list-item
          class="ml-6"
            lines="two"
            prepend-avatar="https://cdn.pixabay.com/photo/2023/03/06/13/56/icon-7833512_640.png"
           
            title="Shodai"
          ></v-list-item>
        </template>

        <v-divider></v-divider>

        <v-list  nav>
          <v-list-item class="text-subtitle-2" prepend-icon="mdi-home-variant-outline" title="Dashboard" to="/dashboard" value="home"></v-list-item>
          <v-list-item class="text-subtitle-2" prepend-icon="mdi-shopping-outline" title="Orders"  to="/orders" value="account"></v-list-item>
          <v-list-item class="text-subtitle-2" prepend-icon="mdi-account-multiple-outline" to="/customers" title="Customers" value="users"></v-list-item>
          <v-list-item class="text-subtitle-2" prepend-icon="mdi-chat-outline" title="Messages" to="/chat" value="users"></v-list-item>

        </v-list>
        <v-list nav>
            <v-list-subheader>TOOLS</v-list-subheader>
            <v-list-item class="text-subtitle-2" prepend-icon="mdi-home-variant-outline" title="Products" to="/products" value="home"></v-list-item>
          <v-list-item class="text-subtitle-2" prepend-icon="mdi-shopping-outline" title="Categories" to="/categories" value="account"></v-list-item>
          <v-list-item class="text-subtitle-2" prepend-icon="mdi-account-multiple-outline" title="Analytics" to="/analytics" value="users"></v-list-item>
         
        </v-list>
         <v-list nav>
            <v-list-subheader>SETTINGS</v-list-subheader>
            <v-list-item class="text-subtitle-2" prepend-icon="mdi-home-variant-outline" title="Settings" to="/settings" value="home"></v-list-item>
          <v-list-item class="text-subtitle-2" prepend-icon="mdi-shopping-outline" title="Help" to="/help" value="account"></v-list-item>
           <v-list-item class="text-subtitle-2" prepend-icon="mdi-shopping-outline" title="Help" to="/help" value="account"></v-list-item>
         
        </v-list>
        
      </v-navigation-drawer>
      <v-main style="height: 100vh"></v-main>
    </v-layout>
  </v-card>
</template>