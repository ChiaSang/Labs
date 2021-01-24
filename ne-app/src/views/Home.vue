<template>
  <div class="home">
<<<<<<< HEAD
    <h1 class="display-1">主页</h1>
    <v-container class="my-5">
      <v-layout row>
        <v-flex>
          <v-flex xs12 md6>
            <v-btn outline block class="primary">TEST</v-btn>
          </v-flex>
          <br />
          <v-flex xs12 md6>
            <v-btn outline block class="primary">TEST</v-btn>
          </v-flex>
          本文讲解 SNMP Trap，在介绍 Trap 概念之前，首先认识一下 SNMP 吧。
          简单网络管理协议(Simple Network Management
          Protocol)是一种应用层协议，是TCP/IP协议族的一部分。它使网络设备之间能够方便地交换管理信息。能够让网络管理员管理网络的性能，发现和解决网络问题及进行网络的扩充。
          目前SNMP已成为网络管理领域中事实上的工
          业标准，并被广泛支持和应用，大多数网络管理系统和平台都是基于SNMP的。
          SNMP 管理控制框架 简而言之，SNMP
          协议是用来管理设备的协议，何谓管理呢？我斗胆将其归纳为两个基本点：监控（get）和配置（set）。也就是说：人们管理一个设备的基本手段可以归纳为
          get 和 set 两种操作。如图 1 所示。 图 1. SNMP 基本管理控制框架 图 1.
          SNMP 基本管理控制框架 如果 NMS( 网管系统 )
          需要查询被管理设备的状态，则需要通过 SNMP 的 get
          操作获得设备的状态信息；同样，如果 NMS
          需要修改或者配置被管理设备的参数，则需要通过 SNMP 的 set 操作来完成。
          什么是 MIB? MIB
          是描述被管理设备上的参数的数据结构。如前所述，管理一个设备，就是利用
          SNMP 协议，通过网络对被管理设备上的参数进行 get 和 set 操作。
        </v-flex>
      </v-layout>
      <br />

      <v-layout row wrap justify-space-around>
        <v-flex xs4 md3>
          <v-btn outline block class="success">Success</v-btn>
        </v-flex>
        <v-flex xs4 md3>
          <v-btn outline block class="success">Success</v-btn>
        </v-flex>
        <v-flex xs4 md3>
          <v-btn outline block class="success">Success</v-btn>
        </v-flex>
      </v-layout>
    </v-container>

    <v-container>
      <!-- <v-layout row wrap> -->
      <h1 class="subheading grey--text">{{ msg }}</h1>
      <v-card flat color="#eeeeee">
        <v-col xs12 md3>
          <div class="caption grey--text">主题</div>
          <div>发生地方是</div>
        </v-col>
        <v-col xs6 sm4 md6>
          <div class="caption grey--text">内容</div>
          <div>发生地方都是</div>
        </v-col>
        <v-col xs6 sm4 md1>
          <div class="caption grey--text">日期</div>
          <div>2020-01-12</div>
        </v-col>
        <v-col xs2 sm4 md2>
          <div class="caption grey--text">备注</div>
          <div>基本管理控打算</div>
        </v-col>
      </v-card>
      <!-- </v-layout> -->
    </v-container>
  </div>
</template>
=======
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
    HelloWorld
  }
}
</script>
>>>>>>> a96517be5f9a608192f6efc6fc960457dc596edd
