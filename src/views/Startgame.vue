<template>
  <v-card-text class="ma-3">
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
      .get('http://127.0.0.1:8000/getPlayerNames/')
      .then(response => (this.players = response.data))
  }
};
</script>