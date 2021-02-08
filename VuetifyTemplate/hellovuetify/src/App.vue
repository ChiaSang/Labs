<template>
  <v-app id="inspire">
    <Navbar />
    <v-main class="mx-4 mb-4">
      <router-view></router-view>
    </v-main>
  </v-app>
</template>
<script>
import Navbar from "./components/NavBar";

export default {
  name: "App",
  components: { Navbar },
  data() {
    return {};
  },
};
</script>