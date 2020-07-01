<template>
  <v-card-text class="ma-3">
    <h2 class="ma-2 title">Current players:</h2>
    <v-list-item-group v-if="players">
      <v-list-item v-for="player in players" :key="player">
        <v-list-item-icon>
          <v-icon>mdi-account-check-outline</v-icon>
        </v-list-item-icon>
        <v-list-item-text>{{ player }}</v-list-item-text>
      </v-list-item>
    </v-list-item-group>
  </v-card-text>
</template>

<script>
let axios = require("axios");

export default {
  data() {
    return {
      players: [null]
    };
  },
  mounted() {
    axios
      .get("http://127.0.0.1:8000/getPlayerNames/")
      .then(response => (this.players = response.data));
  }
};
</script>

<style>
.title{
  font-weight: 100;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  color: whitesmoke;
}

</style>