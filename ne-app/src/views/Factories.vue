<template>
  <div class="factories">
    <v-container>
      <v-card
        flat
        color="#eeeeee"
        v-for="comment in comments"
        :key="comment.id"
      >
        <v-layout wrap :class="`pa-1 card-${comment.id}`">
          <v-flex xs3 sm4 md2 pa-2>
            <h4 class="grey--text">主题</h4>
            <div>{{ comment.name }}</div>
          </v-flex>
          <v-flex xs5 sm4 md6 pa-2>
            <h4 class="grey--text">内容</h4>
            <div>
              {{ comment.body }}
            </div>
          </v-flex>
          <v-flex xs2 sm4 md2 pa-2>
            <h4 class="grey--text">邮箱</h4>
            <div>{{ comment.email }}</div>
          </v-flex>
          <v-flex xs2 sm4 md2 pa-2>
            <h4 class="grey--text">序号</h4>
            <div>{{ comment.id }}</div>
          </v-flex>
        </v-layout>
      </v-card>
    </v-container>
  </div>
</template>
<script>
export default {
  data() {
    return {
      msg: "工厂列表",
      comments: {
        postId: "",
        id: "",
        name: "",
        email: "",
        body: "",
      },
    };
  },
  mounted() {
    axios
      .get("http://jsonplaceholder.typicode.com/posts/1/comments")
      .then((body) => {
        this.comments = body.data;
      });
  },
};
</script>
<style>
.card-1 {
  border-left: 4px solid #3cd1c2;
}
.card-2 {
  border-left: 4px solid #f7ad2d;
}
.card-3 {
  border-left: 4px solid #ee6e69;
}
.card-4 {
  border-left: 4px solid #98c379;
}
.card-5 {
  border-left: 4px solid #c678dd;
}
</style>