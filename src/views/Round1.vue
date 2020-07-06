<template>
  <v-app>
    <v-container>
      <v-btn @click="incrementRound">getPlayerAndRound</v-btn>
      <v-text-field
        class="centered-input text--darken-3 mt-3"
        :value="playerTurn"
        color="grey lighten-43"
        readonly
      />
      <v-text-field
        v-if="round != 0"
        class="centered-input text--darken-3 mt-3"
        :value="cardName"
        color="grey lighten-43"
        readonly
      />
    </v-container>
    <v-container v-if="!start">
      <v-card>
        <v-card-title primary-title class="justify-center">
          <v-card-actions class="justify-center">
            <v-btn
              large
              rounded
              flat
              color="primary"
              class="btn px-5 py-7"
              @click="disableStart"
            >Start</v-btn>
          </v-card-actions>
        </v-card-title>
      </v-card>
    </v-container>
    <v-container class="my-5 round1" v-if="round == 0 && start">
      <v-card>
        <v-card-title primary-title class="justify-center">
          <h3 class="headline red--text text--accent-2">Rood</h3>
          <h3 class="headline white--text text--accent-2">¿</h3>
          <h3 class="headline secondary--text text--accent-2">Zwart</h3>
        </v-card-title>
        <v-card-actions class="justify-center">
          <v-btn large rounded flat color="red" class="btn px-5 py-7" @click="incrementRound">
            <v-icon>mdi-cards-heart</v-icon>
          </v-btn>
          <v-btn large rounded flat color="zwart" class="btn px-5 py-7" @click="incrementRound">
            <v-icon>mdi-cards-spade</v-icon>
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
    <v-container class="my-5 round2" v-if="round == 1">
      <v-card>
        <v-card-title primary-title class="justify-center">
          <h3 class="headline blue--text text--accent-2">Hoger</h3>
          <h3 class="headline white--text text--accent-2">¿</h3>
          <h3 class="headline red--text text--accent-2">Lager</h3>
        </v-card-title>
        <v-card-actions class="justify-center">
          <v-btn large rounded flat color="blue" class="btn px-5 py-7" @click="incrementRound">
            <v-icon>mdi-arrow-up</v-icon>
          </v-btn>
          <v-btn large rounded flat color="red" class="btn px-5 py-7" @click="incrementRound">
            <v-icon>mdi-arrow-down</v-icon>
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
    <v-container class="my-5 round3" v-if="round == 2">
      <v-card>
        <v-card-title primary-title class="justify-center">
          <h3 class="headline blue--text text--accent-2">Binnen</h3>
          <h3 class="headline white--text text--accent-2">¿</h3>
          <h3 class="headline red--text text--accent-2">Buiten</h3>
        </v-card-title>
        <v-card-actions class="justify-center">
          <v-btn
            large
            rounded
            flat
            color="blue"
            class="btn px-5 py-7"
            dense
            @click="incrementRound"
          >
            <v-icon>mdi-arrow-right</v-icon>
            <v-icon>mdi-arrow-left</v-icon>
          </v-btn>
          <v-btn large rounded flat color="red" class="btn px-5 py-7" @click="incrementRound">
            <v-icon>mdi-arrow-left</v-icon>
            <v-icon>mdi-arrow-right</v-icon>
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
    <v-container class="my-5 round4" v-if="round == 3">
      <v-card>
        <v-card-title primary-title class="justify-center">
          <h3 class="headline blue--text text--accent-2">Wel Hebben</h3>
          <h3 class="headline white--text text--accent-2">¿</h3>
          <h3 class="headline red--text text--accent-2">Niet Hebben</h3>
        </v-card-title>
        <v-card-actions class="justify-center">
          <v-btn
            large
            rounded
            flat
            color="blue"
            class="btn px-5 py-7"
            dense
            @click="incrementRound"
          >
            <v-icon>mdi-check</v-icon>
          </v-btn>
          <v-btn large rounded flat color="red" class="btn px-5 py-7" @click="incrementRound">
            <v-icon>mdi-minus-box-outline</v-icon>
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
  </v-app>
</template>

<script>
const axios = require("axios");
export default {
  data() {
    return {
      player: "",
      cardName: "Hier moeten de kaarten komen die de speler al heeft",
      round: 0,
      cardround: 0,
      start: false
    };
  },
  mounted: function() {
    this.playerTurn = `${this.player}'s turn:`;
  },
  methods: {
    incrementRound: function() {
      this.round++;
      var playername, cardround, cardname;

      var config = {
        method: "get",
        url: "http://localhost:8000/round1/1/",
        headers: {}
      };

      axios(config)
        .then(function(response) {
          var data = response.data;
          playername = data[0];
          cardround = data[1];
          cardname = data[2];
        })
        .catch(function(error) {
          console.log(error);
        });
      this.round = cardround;
      this.player = playername;
      this.cardName = cardname;
    },
    disableStart() {
      this.start = true;
    }
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