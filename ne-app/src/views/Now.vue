<template>
  <div class="now">
    <h1>实时数据</h1>
    <v-btn depressed color="primary" @click="get_check"> 站点是否登记 </v-btn>
    <v-btn depressed color="primary" @click="get_neinfo"> 获取信息 </v-btn>
    <v-container>
          <v-card flex class="ma-3">
      <!-- <v-layout ma-6> -->
      <v-card-text xs12 md3>
        <div class="caption grey--text">主题</div>
        <div>基本管理控制框架 如果 NMS( 网管系统 )</div>
      </v-card-text>
      <v-card-text xs6 sm4 md6>
        <div class="caption grey--text">内容</div>
        <div>
          基本管理控制框架 如果 NMS( 网管系统 )
          需要查询被管理设备的状态，则需要通过 SNMP 的 get
          操作获得设备的状态信息
        </div>
      </v-card-text>
      <v-card-text xs6 sm4 md1>
        <h4 class="grey--text">主题</h4>
        <div>2020-01-12</div>
      </v-card-text>
      <v-card-text xs6 sm4 md2>
        <div class="caption grey--text">备注</div>
        <div>基本管理控制框架 如果 NMS( 网管系统 )</div>
      </v-card-text>
      <!-- </v-layout> -->
    </v-card>

    <v-card flex class="ma-3">
      <v-layout ma-6>
        <v-card-text xs12 sm4 md3>
          <div class="caption grey--text">主题</div>
          <div>基本管理控制框架 如果 NMS( 网管系统 )</div>
        </v-card-text>
        <v-card-text xs6 sm4 md6>
          <div class="caption grey--text">内容</div>
          <div>
            基本管理控制框架 如果 NMS( 网管系统 )
            需要查询被管理设备的状态，则需要通过 SNMP 的 get
            操作获得设备的状态信息
          </div>
        </v-card-text>
        <v-card-text xs6 sm4 md1>
          <h4 class="grey--text">主题</h4>
          <div>2020-01-12</div>
        </v-card-text>
        <v-card-text xs6 sm4 md2>
          <div class="caption grey--text">备注</div>
          <div>基本管理控制框架 如果 NMS( 网管系统 )</div>
        </v-card-text>
      </v-layout>
    </v-card>
    </v-container>
  </div>
</template>
    <p></p>
    <p></p>
    <p></p>
  </div>
</template>
<script>
export default {
  data() {
    return {
      msg: "工厂",
      query_fa: {
        point_name: "葛洁",
        addtime_start: "2021-01-01 00:00:00_2021-01-03 23:00:00",
      },
      sort_field: {
        addtime: "desc_1",
      },
      pageSize: 10,
      ne_info: [],
      paramsDetail: {
        query: {
          point_name: "葛洁",
          addtime_start: "2021-01-01 00:00:00_2021-01-03 23:00:00",
        },
        sort_field: {
          addtime: "desc_1",
        },
        index: "t_micro_5minute",
        pageSize: 10,
      },
      query: {
        point_name: "葛洁",
        addtime_start: "2021-01-01 00:00:00_2021-01-03 23:00:00",
      },
      sort_field: {
        addtime: "desc_1",
      },
      index: "t_micro_5minute",
      pageSize: 10,
    };
  },
  mounted() {
    let p1 = encodeURIComponent(JSON.stringify(this.query));
    let p2 = encodeURIComponent(JSON.stringify(this.sort_field));
    let p3 = encodeURIComponent(JSON.stringify(this.index));
    let p4 = encodeURIComponent(JSON.stringify(this.pageSize));
    let pt = p1 + p2 + p3 + p4;
    console.log(pt);
  },
  methods: {
    get_neinfo: function () {
      this.axios({
        headers: {
          "connection": "keep-alive",
          "content-encoding": "gzip",
          "content-type": "application/json;charset=utf-8",
          "keep-alive": "timeout=4",
          "proxy-connection": "keep-alive",
          "transfer-encoding": "chunked",
          "vary": "Accept-Encoding, User-Agent",
        },
        method: "get",
        url: "/data-center/nifc/queryPoint?pointName=%E8%91%9B%E6%B4%81",
      });
    },
    get_check: function () {
      this.axios
        .get("http://jsonplaceholder.typicode.com/posts")
        .then((body) => {
          this.ne_info = body.json();
        });
    },
  },
};
</script>