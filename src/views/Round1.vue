<template>
  <v-app>
    <v-container class="my-5 round1">
      <v-card>
        <v-card-title primary-title class="justify-center">
          <h3 class="headline blue--text text--accent-2">Hoger</h3>
          <h3 class="headline white--text text--accent-2">¿</h3>
          <h3 class="headline red--text text--accent-2">Lager</h3>
        </v-card-title>
        <v-card-actions class="justify-center">
          <v-btn large rounded flat color="blue" class="btn px-5 py-7"><v-icon>mdi-arrow-up</v-icon></v-btn>
          <v-btn large rounded flat color="red" class="btn px-5 py-7"><v-icon>mdi-arrow-down</v-icon></v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
  </v-app>
</template>

<style>
.btn{
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    font-size: 40;
}
</style>