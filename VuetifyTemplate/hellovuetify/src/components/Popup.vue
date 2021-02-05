<template>
  <v-dialog max-width="600px">
    <template v-slot:activator="{ on }">
      <v-btn text color="#48b986" v-on="on">修改资料</v-btn>
    </template>
    <v-card class="mx-auto">
      <v-card-title class="headline"> Unlimited music now </v-card-title>
      <v-card-text>
        <v-form class="px-3">
          <v-text-field
            v-model="title"
            :rules="rules"
            hide-details="auto"
            label="Title"
            prepend-icon="mdi-folder"
          ></v-text-field>
          <v-textarea
            v-model="content"
            label="Information"
            prepend-icon="mdi-content-save-edit"
          ></v-textarea>

          <v-menu
            ref="menu"
            v-model="menu"
            :close-on-content-click="false"
            :return-value.sync="date"
            transition="scale-transition"
            offset-y
            min-width="auto"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                v-model="date"
                label="Picker in menu"
                prepend-icon="mdi-calendar"
                readonly
                v-bind="attrs"
                v-on="on"
              ></v-text-field>
            </template>
            <v-date-picker v-model="date" no-title scrollable>
              <v-spacer></v-spacer>
              <v-btn text color="primary" @click="menu = false"> Cancel </v-btn>
              <v-btn text color="primary" @click="$refs.menu.save(date)">
                OK
              </v-btn>
            </v-date-picker>
          </v-menu>

          <v-spacer></v-spacer>
          <v-btn
            text
            @click="submit"
            class="success mx-0 mt-3"
          >
            Add Project
          </v-btn>
        </v-form>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  data() {
    return {
      rules: [
        (value) => !!value || "Required.",
        (value) => (value && value.length >= 6) || "Min 6 characters",
      ],

      date: new Date().toISOString().substr(0, 10),
      menu: false,
      title: " ",
      content: " ",
    };
  },
  methods: {
    submit() {},
  },
};
</script>
