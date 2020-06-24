  
<template>
  <nav>
    <v-navigation-drawer v-model="drawer" app clipped dark>
      <v-list dense>
        <v-list-item v-for="link in links" :key="link.text" router :to="link.route">
          <v-list-item-action class="item-tile-icon">
            <v-icon>{{ link.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title class="font">{{ link.text }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar app clipped-left flat dark>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>
        <span class="wired font uppercase pa-auto">hallo</span>
        <span class="upload font uppercase">daar</span>
      </v-toolbar-title>
    </v-app-bar>

    <v-footer app dark flat>
      <span class="wired font">&copy; Tjalle Wolterink 2020</span>
    </v-footer>
  </nav>
</template>

<script>
export default {
  props: {
    source: String
  },
  data: () => ({
    drawer: true,
    links: [
      { icon: "mdi-view-dashboard", text: "Dashboard", route: "/" },
      { icon: "mdi-folder", text: "Upload", route: "/upload" },
      { icon: "mdi-rotate-3d", text: "Render", route: "/render" }
    ]
  }),
  created() {}
};
</script>

<style>
* {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}
.font {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
}
.uppercase {
  text-transform: uppercase;
}
.wired {
  font-weight: 400;
}
.upload {
  font-weight: 200;
  color: grey;
}
.item-tile-icon {
    color: black;
}
</style>