<template>
  <div class="home darken-2 text-center">
    <v-container>
      <p class="green lighten-1 white--text">
        One should give up anger; one should abandon pride; one should overcome
        all fetters. I’ll never befall him who clings not to mind and body and
        is passionless.
      </p>
      <p>
        一个人应该舍弃愤怒，拔除傲慢，超越所有的束缚。不执着心灵和物质的人，内心可以得到真正的安宁，而不受外在的影响。
      </p>

      <Panel />

      <div>
        <v-layout row wrap class="pa-3">
          <v-flex xs12 md6>
            <v-btn outlined block class="primary">1</v-btn>
          </v-flex>
          <v-flex xs4 md2>
            <v-btn outlined block class="primary">2</v-btn>
          </v-flex>
          <v-flex xs4 md2>
            <v-btn outlined block class="primary">3</v-btn>
          </v-flex>
          <v-flex xs4 md2>
            <v-btn outlined block class="primary">4</v-btn>
          </v-flex>
        </v-layout>
      </div>
      <div id="nav">
        <v-layout row wrap justify-space-around>
          <v-flex xs4 md3>
            <v-btn outlined block class="success">1</v-btn>
          </v-flex>
          <v-flex xs4 md3>
            <v-btn outlined block class="success">2</v-btn>
          </v-flex>
        </v-layout>
      </div>

      <v-main>
        <v-row row justify-start class="mb-3">
          <v-tooltip top>
            <template v-slot:activator="{ on }">
              <v-btn
                small
                depressed
                class="grey--text"
                @click="sortBy('title')"
                v-on="on"
              >
                <v-icon left small> mdi-folder </v-icon>
                <span class="caption text-lowercase">By project name</span>
              </v-btn>
            </template>
            <span>Sort projects by project name</span>
          </v-tooltip>

          <v-tooltip top>
            <template v-slot:activator="{ on }">
              <v-btn
                small
                depressed
                class="grey--text"
                @click="sortBy('person')"
                v-on="on"
              >
                <v-icon left small>mdi-account</v-icon>
                <span class="caption text-lowercase">By project name</span>
              </v-btn>
            </template>
            <span>Sort projects by author name</span>
          </v-tooltip>
        </v-row>

        <div v-for="project in projects" :key="project.title">
          <v-card flat :class="`pa-3 project ${project.status}`">
            <v-row>
              <v-col cols="12" md="6">
                <div class="caption grey--text">Project Title</div>
                <div>{{ project.title }}</div>
              </v-col>
              <v-col cols="6" sm="4" md="2">
                <div class="caption grey--text">Person</div>
                <div>{{ project.person }}</div>
              </v-col>
              <v-col cols="6" sm="4" md="2">
                <div class="caption grey--text">Due By</div>
                <div>{{ project.due }}</div>
              </v-col>
              <v-col cols="2" sm="4" md="2">
                <div class="right">
                  <v-chip
                    small
                    :color="`${project.status}`"
                    :class="`v-chip--active white--text caption my-2`"
                  >
                    {{ project.status }}
                  </v-chip>
                </div>
              </v-col>
            </v-row>
          </v-card>
          <v-divider class="mx-1"></v-divider>
        </div>
      </v-main>
    </v-container>
  </div>
</template>

<script>
import Panel from "../components/Panel";

export default {
  components: { Panel },
  data() {
    return {
      projects: [
        {
          title: "Design a new website",
          person: "The Net Ninja",
          due: "1st Jan 2019",
          status: "ongoing",
          content:
            "Lorem ipsum dolor sit amet consectetur adipisicing elit. Sunt consequuntur eos eligendi illum minima adipisci deleniti, dicta mollitia enim explicabo fugiat quidem ducimus praesentium voluptates porro molestias non sequi animi!",
        },
        {
          title: "Code up the homepage",
          person: "Chun Li",
          due: "10th Jan 2019",
          status: "complete",
          content:
            "Lorem ipsum dolor sit amet consectetur adipisicing elit. Sunt consequuntur eos eligendi illum minima adipisci deleniti, dicta mollitia enim explicabo fugiat quidem ducimus praesentium voluptates porro molestias non sequi animi!",
        },
        {
          title: "Design video thumbnails",
          person: "Ryu",
          due: "20th Dec 2018",
          status: "overdue",
          content:
            "Lorem ipsum dolor sit amet consectetur adipisicing elit. Sunt consequuntur eos eligendi illum minima adipisci deleniti, dicta mollitia enim explicabo fugiat quidem ducimus praesentium voluptates porro molestias non sequi animi!",
        },
        {
          title: "Create a community forum",
          person: "Gouken",
          due: "20th Oct 2018",
          status: "complete",
          content:
            "Lorem ipsum dolor sit amet consectetur adipisicing elit. Sunt consequuntur eos eligendi illum minima adipisci deleniti, dicta mollitia enim explicabo fugiat quidem ducimus praesentium voluptates porro molestias non sequi animi!",
        },
      ],
    };
  },
  methods: {
    sortBy(prop) {
      this.projects.sort((a, b) => (a[prop] < b[prop] ? -1 : 1));
    },
  },
};
</script>

<style>
.project.complete {
  border-left: 4px solid #3cd1c2;
}
.project.ongoing {
  border-left: 4px solid orange;
}
.project.overdue {
  border-left: 4px solid tomato;
}
.v-chip.complete {
  background: #3cd1c2;
}
.v-chip.ongoing {
  background: #ffaa2c;
}
.v-chip.overdue {
  background: #f83e70;
}
</style>