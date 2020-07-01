<template>
  <v-card-text>
    <v-list v-if="players.length" class>
      <v-list-item v-for="(player, index) in players" :key="`players-${index}`">
        <v-list-item-icon>
          <v-icon>mdi-account-check-outline</v-icon>
        </v-list-item-icon>
        <v-list-item-text>{{ player }}</v-list-item-text>
      </v-list-item>
    </v-list>

    <v-form @submit.prevent="addPlayer" id="WriteForm" method="post" v-if="!confirmed">
      <v-text-field
        class="mx-16 mt-4"
        name="name"
        v-model="name"
        v-bind="name"
        label="Name"
        required
      ></v-text-field>
      <v-btn
        class="ma-2 ml-16"
        color="primary"
        rounded
        outlined
        type="submit"
        form="WriteForm"
      >Add Player</v-btn>
      <v-btn class="ma-2" @click="removeLastPlayer" rounded outlined color="red">Remove player</v-btn>
    </v-form>

    <v-form @submit.prevent="confirmForm" id="confirmForm1" method="post" v-if="!confirmed">
      <v-btn
        class="ma-6 ml-16"
        color="yellow accent-2"
        rounded
        outlined
        type="submit"
        form="confirmForm1"
        @click="confirmForm"
        :disabled="!players.length"
      >Confirm Players</v-btn>
    </v-form>

    <v-btn
      v-if="confirmed && !sent"
      class="ma-6 ml-16"
      color="green accent-4"
      rounded
      outlined
      @click="sendForm"
    >Send players</v-btn>
  </v-card-text>
</template>

<script>
const axios = require('axios')

export default {
  data() {
    return {
      name: "",
      players: [],
      confirmed: false,
      sent: false
    };
  },
  mounted() {},
  methods: {
    addPlayer: function() {
      this.players.push(this.name);
      console.log(this.players);
      this.name = "";
    },
    removeLastPlayer: function() {
      this.players.pop();
    },
    confirmForm: function() {
      if (this.players.length) {
        this.confirmed = true;
      }
    },
    sendForm: function() {
      let formdata = this.players;
      console.log(formdata);
      this.sent = true;
      formdata = JSON.stringify(formdata);
      var config = {
        method: "post",
        url: `http://127.0.0.1:8000/giveMePlayerData/?data=${formdata}`,
        headers: {}
      };

      axios(config)
        .then(function(response) {
          console.log(JSON.stringify(response.data));
        })
        .catch(function(error) {
          console.log(error);
        });
    }
  }
};
</script>


<style>
</style>