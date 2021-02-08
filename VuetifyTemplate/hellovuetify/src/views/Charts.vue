<template>
  <div class="Charts">
    <v-container fluid class="text-center">
      <h1>Charts</h1>
      <v-row>
        <v-col cols="6" class="text-center">
          <Chart />
        </v-col>
        <v-col cols="6" class="text-center">
          <v-sheet
            class="v-sheet--offset mx-auto"
            color="cyan"
            elevation="12"
            max-width="calc(100% - 32px)"
          >
            <v-sparkline
              :labels="labels"
              :value="value"
              color="white"
              line-width="2"
              padding="16"
            ></v-sparkline>
          </v-sheet>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import Chart from "../components/Chart.vue";
export default {
  components: { Chart },
  data: () => ({
    labels: ["12am", "3am", "6am", "9am", "12pm", "3pm", "6pm", "9pm"],
    value: [200, 675, 410, 390, 310, 460, 250, 240],
  }),
};
</script>