<template>
  <div class="">
    <div class="crumbs">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item><i class="el-icon-lx-copy"></i> 系统提醒</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <div class="container">
      <el-tabs v-model="message">
        <el-tab-pane :label="`提示消息(${state.unread.length})`" name="first">
          <el-col :span="22" style="width:100%">
            <el-table :data="state.unread" :show-header="false" style="width: 100%">
              <el-table-column>
                <template #default="scope">
                  <span class="message-title">{{ scope.row.title }}</span>
                </template>
              </el-table-column>
              <el-table-column prop="date" width="180"></el-table-column>
            </el-table>
          </el-col>
          <el-col :span="2" style="width:100%">
            <el-button size="small" @click="del_p()" style="margin:8px 0 0 10px">已处理</el-button>
            <el-button size="small" @click="del_s()" style="margin:16px 0 0 10px">已处理</el-button>
            <el-button size="small" @click="del_n()" style="margin:16px 0 0 10px">已处理</el-button>
            <el-button size="small" @click="del_h()" style="margin:16px 0 0 10px">已处理</el-button>
            <el-button size="small" @click="del_b()" style="margin:16px 0 0 10px">已处理</el-button>
          </el-col>

        </el-tab-pane>


      </el-tabs>
    </div>
  </div>
</template>

<script>
import axios from "axios"
import {ref, reactive} from "vue";

export default {

  data() {
    return {
      times: true
    }
  },

  setup() {
    const message = ref("first");
    let yy = new Date().getFullYear();
    let mm = new Date().getMonth() + 1;
    let dd = new Date().getDate();
    let hh = new Date().getHours();
    let mf = new Date().getMinutes() < 10 ? '0' + new Date().getMinutes() : new Date().getMinutes();
    let ss = new Date().getSeconds() < 10 ? '0' + new Date().getSeconds() : new Date().getSeconds();
    const state = reactive({
      unread: [
        {
          date: yy + '/' + mm + '/' + dd + ' ' + hh + ':' + mf + ':' + ss,
          title: "",
        },
        {
          date: yy + '/' + mm + '/' + dd + ' ' + hh + ':' + mf + ':' + ss,
          title: "",
        },
        {
          date: yy + '/' + mm + '/' + dd + ' ' + hh + ':' + mf + ':' + ss,
          title: "",
        },
        {
          date: yy + '/' + mm + '/' + dd + ' ' + hh + ':' + mf + ':' + ss,
          title: "",
        },
        {
          date: yy + '/' + mm + '/' + dd + ' ' + hh + ':' + mf + ':' + ss,
          title: "",
        },
      ],

    });

    return {
      message,
      state,
    };
  },

  mounted() {
    this.newInterval(this.read_info, 500);
  },

  methods: {
    newInterval(fn, delay) {
      if (this.times == false) {
        return
      }
      setTimeout(() => {
        fn()
        this.newInterval(fn, delay)
      }, delay)
    },

    read_info() {
      axios.get('http://119.3.16.162:8085/warning').then(res => {
        this.state.unread[0].title = res.data[0].pressure_info
        this.state.unread[1].title = res.data[0].smog_info
        this.state.unread[2].title = res.data[0].noise_info
        this.state.unread[3].title = res.data[0].heart_info
        this.state.unread[4].title = res.data[0].blood_info
      }).catch(err => {
        console.log("获取数据失败" + err);
      })
    },

    //处理液位

    del_p() {
      axios.get('http://119.3.16.162:8085/dpwarning').then(res => {
      }).catch(err => {
        console.log("获取数据失败" + err);
      })
    },

    //处理烟雾

    del_s() {
      axios.get('http://119.3.16.162:8085/dswarning').then(res => {
      }).catch(err => {
        console.log("获取数据失败" + err);
      })
    },

    //处理噪声

    del_n() {
      axios.get('http://119.3.16.162:8085/dnwarning').then(res => {
      }).catch(err => {
        console.log("获取数据失败" + err);
      })
    },

    //处理心率

    del_h() {
      axios.get('http://119.3.16.162:8085/dhwarning').then(res => {
      }).catch(err => {
        console.log("获取数据失败" + err);
      })
    },

    //处理血氧
    del_b() {
      axios.get('http://119.3.16.162:8085/dbwarning').then(res => {
      }).catch(err => {
        console.log("获取数据失败" + err);
      })
    },

  },
  beforeDestroy() {
    this.times = true
  }

};
</script>

<style>
.message-title {
  cursor: pointer;
}

.handle-row {
  margin-top: 30px;
}
</style>

