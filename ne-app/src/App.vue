<template>
<<<<<<< HEAD
  <v-app id="inspire">
    <Navigator />
    <!-- <router-view></router-view> -->
    <v-main class="mx-4 my-3">
      <router-view></router-view>
       </v-main>
=======
  <v-app>
    <!-- <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
          transition="scale-transition"
          width="40"
        />

        <v-img
          alt="Vuetify Name"
          class="shrink mt-1 hidden-sm-and-down"
          contain
          min-width="100"
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-name-dark.png"
          width="100"
        />
      </div>

      <v-spacer></v-spacer>

      <v-btn
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
        text
      >
        <span class="mr-2">Latest Release</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar> -->

    <AppBar />

    <v-main>
      <HelloWorld />
    </v-main>
>>>>>>> a96517be5f9a608192f6efc6fc960457dc596edd
  </v-app>
</template>

<script>
<<<<<<< HEAD
import Navigator from "./components/Navigator";
=======
import HelloWorld from "./components/HelloWorld";
import AppBar from "./components/AppBar";
>>>>>>> a96517be5f9a608192f6efc6fc960457dc596edd

export default {
  name: "App",

  components: {
<<<<<<< HEAD
    Navigator,
=======
    HelloWorld,
>>>>>>> a96517be5f9a608192f6efc6fc960457dc596edd
  },

  data: () => ({
    //
  }),
};
</script>
