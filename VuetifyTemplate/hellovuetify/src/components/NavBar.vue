<template>
  <nav>
    <v-snackbar top v-model="snackbar" :timeout="4000">
      <span>Awesome! New project added.</span>
      <template v-slot:action="{ attrs }">
        <v-btn color="success" text v-bind="attrs" @click="snackbar = false"
          >Close</v-btn
        >
      </template>
    </v-snackbar>

    <v-navigation-drawer app v-model="drawer">
      <v-sheet color="grey lighten-4" class="pa-4">
        <v-avatar class="mb-4" color="grey darken-1" size="64"></v-avatar>
        <Popup />
        <div>chiachia@example.com</div>
      </v-sheet>
      <v-divider></v-divider>

      <v-list>
        <v-list-item
          v-for="link in links"
          :key="link.text"
          router
          :to="link.route"
        >
          <v-list-item-icon>
            <v-icon>{{ link.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>
              {{ link.text }}
            </v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar color="#42b983" dense app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>
        <span color="#2c3e50">在线综合管理系统</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon color="white">
        <v-icon icon>mdi-invert-colors</v-icon>
      </v-btn>
      <div class="text-center">
        <v-menu offset-y>
          <template v-slot:activator="{ on, attrs }">
            <v-btn color="white" text v-bind="attrs" v-on="on">
              <v-icon icon>mdi-dots-vertical</v-icon>
              <!-- <span>Menu</span> -->
            </v-btn>
          </template>
          <v-list>
            <v-list-item
              v-for="link in links"
              :key="link.title"
              router
              :to="link.route"
            >
              <v-list-item-title>{{ link.text }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </div>
      <v-btn depressed text color="white">
        <!-- <span class="font-weight-light">Sign Out</span> -->
        <v-icon icon>mdi-exit-to-app</v-icon>
      </v-btn>
    </v-app-bar>
  </nav>
</template>

<script>
import Popup from "../components/Popup";

export default {
  components: { Popup },
  data() {
    return {
      drawer: false,
      snackbar: false,
      links: [
        { icon: "mdi-view-dashboard", text: "Dashboard", route: "/" },
        { icon: "mdi-account", text: "About", route: "/about" },
        { icon: "mdi-folder", text: "HelloWorld", route: "/hello" },
      ],
    };
  },
};
</script>