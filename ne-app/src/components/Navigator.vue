<template>
  <div>
    <v-navigation-drawer v-model="drawer" app>
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="title"> 功能菜单 </v-list-item-title>
          <v-list-item-subtitle> 点击选择 </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list dense nav>
        <v-list-item
          v-for="item in items"
          :key="item.title"
          router-link
          :to="item.route"
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar app class="teal lighten-1">
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>无组织在线监测系统</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn text plain color="error"> 登出 </v-btn>
    </v-app-bar>
    <!-- <v-main> </v-main> -->
  </div>
</template>


<script>
export default {
  data() {
    return {
      drawer: false,
      items: [
        { title: "主页", icon: "mdi-view-dashboard", route: "/home" },
        { title: "实时数据", icon: "mdi-account-box", route: "/now" },
        { title: "工厂列表", icon: "mdi-gavel", route: "/factories" },
      ],
    };
  },
};
</script>