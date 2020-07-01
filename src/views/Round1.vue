<template>
  <v-app>
    <v-container>
      <v-text-field
        class="centered-input text--darken-3 mt-3"
        :value="playerTurn"
        color="grey lighten-43"
        
        readonly
      />
    </v-container>
    <v-container class="my-5 round1">
      <v-card>
        <v-card-title primary-title class="justify-center">
          <h3 class="headline red--text text--accent-2">Rood</h3>
          <h3 class="headline white--text text--accent-2">¿</h3>
          <h3 class="headline secondary--text text--accent-2">Zwart</h3>
        </v-card-title>
        <v-card-actions class="justify-center">
          <v-btn large rounded flat color="red" class="btn px-5 py-7">
            <v-icon>mdi-cards-heart</v-icon>
          </v-btn>
          <v-btn large rounded flat color="zwart" class="btn px-5 py-7">
            <v-icon>mdi-cards-spade</v-icon>
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
    <v-container class="my-5 round2">
      <v-card>
        <v-card-title primary-title class="justify-center">
          <h3 class="headline blue--text text--accent-2">Hoger</h3>
          <h3 class="headline white--text text--accent-2">¿</h3>
          <h3 class="headline red--text text--accent-2">Lager</h3>
        </v-card-title>
        <v-card-actions class="justify-center">
          <v-btn large rounded flat color="blue" class="btn px-5 py-7">
            <v-icon>mdi-arrow-up</v-icon>
          </v-btn>
          <v-btn large rounded flat color="red" class="btn px-5 py-7">
            <v-icon>mdi-arrow-down</v-icon>
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
    <v-container class="my-5 round3">
      <v-card>
        <v-card-title primary-title class="justify-center">
          <h3 class="headline blue--text text--accent-2">Binnen</h3>
          <h3 class="headline white--text text--accent-2">¿</h3>
          <h3 class="headline red--text text--accent-2">Buiten</h3>
        </v-card-title>
        <v-card-actions class="justify-center">
          <v-btn large rounded flat color="blue" class="btn px-5 py-7" dense>
            <v-icon>mdi-arrow-right</v-icon>
            <v-icon>mdi-arrow-left</v-icon>
          </v-btn>
          <v-btn large rounded flat color="red" class="btn px-5 py-7">
            <v-icon>mdi-arrow-left</v-icon>
            <v-icon>mdi-arrow-right</v-icon>
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
    <v-container class="my-5 round4">
      <v-card>
        <v-card-title primary-title class="justify-center">
          <h3 class="headline blue--text text--accent-2">Wel Hebben</h3>
          <h3 class="headline white--text text--accent-2">¿</h3>
          <h3 class="headline red--text text--accent-2">Niet Hebben</h3>
        </v-card-title>
        <v-card-actions class="justify-center">
          <v-btn large rounded flat color="blue" class="btn px-5 py-7" dense>
            <v-icon>mdi-check</v-icon>
          </v-btn>
          <v-btn large rounded flat color="red" class="btn px-5 py-7">
            <v-icon>mdi-minus-box-outline</v-icon>
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      player: "Tjalle",
      playerTurn: '',
    };
  },
  mounted: function() {
    this.playerTurn = `${this.player}'s turn:`
  }
};
  
</script>

<style>
.btn {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  font-size: 40;
}
.centered-input input {
  text-align: center;
  font-size: 1.5em;
}
</style>