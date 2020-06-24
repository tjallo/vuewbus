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

    <v-form @submit.prevent="addPlayer" id="WriteForm" method="post">
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
  </v-card-text>
</template>

<script>
export default {
  data() {
    return {
      name: "",
      players: []
    };
  },
  methods: {
    addPlayer: function() {
      this.players.push(this.name);
      console.log(this.players);
      this.name = "";
    },
    removeLastPlayer: function() {
      this.players.pop();
    }
  }
};
</script>


<style>
</style>