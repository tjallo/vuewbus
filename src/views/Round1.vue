<template>
  <v-app>
    <v-btn @click="getInfo">getInfo</v-btn>
    <h1>Player: {{player}}</h1>
    <h1>Round: {{round}}</h1>
    <h1>Cardname: {{cardname}}</h1>
  </v-app>
</template>

<script>
const axios = require("axios");

export default {
  data() {
    return {
      player: "",
      round: 0,
      cardname: ""
    };
  },
  methods: {
    getInfo: function() {
      var player, round, cardname;

      var config = {
        method: "get",
        url: "http://localhost:8000/round1/1/",
        headers: {}
      };

      axios(config)
        .then(function(response) {
          const data = response.data;
          console.log(data);
          this.player = data[0];
          this.round = data[1];
          this.cardname = data[2];
          console.log(player, round, cardname);
        })
        .catch(function(error) {
          console.log(error);
        });

      console.log(this.player);
    }
  }
};
</script>