<template>
  <v-app id="inspire">
    <Navbar />
    <v-main class="mx-4 mb-4">
      <div id="app">
        <div id="nav">
          <h1>
            <router-link to="/">Home</router-link> |
            <router-link to="/about">About</router-link> |
            <router-link to="/hello">HelloWorld</router-link>
          </h1>
        </div>
      </div>
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

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>

