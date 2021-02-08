<template>
  <div class="helloworld">
    <v-container class="mx-auto text-center">
      <h1>Live Bitcoin Price Index</h1>
      <v-row class="text-center my-4">
        <v-col cols="4" v-for="currency in info" :key="currency.code">
          <v-card class="mx-auto" max-width="344">
            <v-card-text>
              <div>{{ currency.description }}</div>
              <div class="display-1 text--primary">
                <span v-html="currency.symbol"></span>
                <span>{{ currency.rate_float | currencydecimal }}</span>
              </div>
              <div class="text--primary">
                {{ currency.code }}
              </div>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      info: null,
    };
  },
  mounted() {
    this.axios
      .get("https://api.coindesk.com/v1/bpi/currentprice.json")
      .then((response) => {
        this.info = response.data.bpi;
      });
  },
  filters: {
    currencydecimal(value) {
      return value.toFixed(2);
    },
  },
};
</script>