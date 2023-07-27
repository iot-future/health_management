<template>
  <div>
    <div v-if='alldata.smog>140'>
      <el-dialog v-model="dialogVisible1" title="提醒" width="30%">
        <span>【烟雾提醒】病房内的烟雾过高!请注意提醒！</span>
        <template #footer>
                <span class="dialog-footer">
                    <el-button @click="dialogVisible1 = false">取消</el-button>
                    <el-button type="primary" @click="dialogVisible1 = false;set_s()">确定</el-button>
                </span>
        </template>
      </el-dialog>
    </div>
    <div v-if='(alldata.noise-440)>500'>
      <el-dialog v-model="dialogVisible2" title="提醒" width="30%">
        <span>【噪音提醒】病房内的噪音过高！请注意提醒!</span>
        <template #footer>
                <span class="dialog-footer">
                    <el-button @click="dialogVisible2 = false">取消</el-button>
                    <el-button type="primary" @click="dialogVisible2 = false;set_n()">确定</el-button>
                </span>
        </template>
      </el-dialog>
    </div>
    <div v-if='alldata.heartrate>120'>
      <el-dialog v-model="dialogVisible3" title="提醒" width="30%">
        <span>【心率告警】病人心率异常，请及时检查病人情况！</span>
        <template #footer>
                <span class="dialog-footer">
                    <el-button @click="dialogVisible3 = false">取消</el-button>
                    <el-button type="primary" @click="dialogVisible3 = false;set_h()">确定</el-button>
                </span>
        </template>
      </el-dialog>
    </div>
    <div v-if='alldata.bloodx<89&alldata.bloodx>1'>
      <el-dialog v-model="dialogVisible4" title="提醒" width="30%">
        <span>【血氧告警】病人血氧异常，请及时检查病人情况！</span>
        <template #footer>
                <span class="dialog-footer">
                    <el-button @click="dialogVisible4 = false">取消</el-button>
                    <el-button type="primary" @click="dialogVisible4 = false;set_b()">确定</el-button>
                </span>
        </template>
      </el-dialog>
    </div>
    <div>
      <el-row :gutter="20">
        <el-col :span="8">
          <el-card shadow="hover" class="mgb20" style="height:250px;">
            <div class="user-info">
              <img src="../assets/img/1.jpg" class="user-avator" alt/>
              <div class="user-info-cont">
                <div class="user-info-name">{{ name }}</div>
                <div>{{ role }}</div>
              </div>
            </div>
            <div class="user-info-list">
              登录时间：
              <span>{{ nowtime }}</span>
            </div>
            <div class="user-info-list">
              登录地点：
              <span>青岛</span>
            </div>
          </el-card>
          <el-card shadow="hover" style="height:380px">
            <div class="data_word" style="font-size: 15px;">
              <el-container style="height:500px;">
                <el-main style="height: 350px;">
                  <div class="word" style="font-size: 16px">
                    室内烟雾:&nbsp;
                    <span class="word1" style="font-size: 18px;font-weight: bold">{{
                        this.dataEnvironment.MQ2
                      }}</span>
                    &nbsp;PPM
                  </div>
                  <div id="smog" style="width: 100%; height: 85%; text-align: center; margin: auto"></div>
                </el-main>
              </el-container>
            </div>
          </el-card>
        </el-col>
        <el-col :span="16">
          <el-row class="mgb20">
            <el-card shadow="hover" style="height:270px;">
              <el-col :span="12">
                <div id="temp" style="width:500px;height:300px;text-align: center; margin:10px 0 0 0"></div>
              </el-col>
              <el-col :span="12">
                <div id="humidity" style="width:500px;height:300px;text-align: center; margin:10px 0 0 50px">
                </div>
              </el-col>
            </el-card>
          </el-row>
          <el-row class="mgb20">
            <el-card shadow="hover" style="height:360px;">
              <el-col :span="4" style="width:300px;height:300px;">
                <div class="photo" style="margin-top: 30px;">
                  <img src="../assets/img/xinlv1.gif" style="margin: auto; width: 60px; height:60px">
                  <div class="word" style="font-size: 16px">
                    病人心率:&nbsp;
                    <span class="word1" style="font-size: 18px;font-weight: bold">{{
                        this.dataEnvironment.Humidity
                      }}</span>
                    &nbsp;BPM
                  </div>
                </div>
                <div class="photo" style="margin-top: 80px;">
                  <img src="../assets/img/bloodx.png" style="margin: auto; width: 60px; height:60px">
                  <div class="word" style="font-size: 16px">
                    病人血氧:&nbsp;
                    <span class="word2" style="font-size: 18px;font-weight: bold">{{
                        this.dataEnvironment.Temperature
                      }}</span>
                    &nbsp;%
                  </div>
                </div>
              </el-col>
              <el-col :span="15" style="width:600px;height:300px;">
                <div id="heart_blood" style="width:500px;height:300px;text-align: center; margin:0 0 60px 0"></div>
              </el-col>
              <el-col :span="4" style="width:400px;height:300px;">
                <el-row style="width:300px;height:50px;">
                  <div class="photo" style="margin:0 0 0 35px;">
                    <img src="../assets/img/sun.gif" style="margin: auto; width: 50px; height:50px">
                    <div class="word" style="font-size: 16px">
                      光照强度:&nbsp;
                      <span class="word1"
                            style="font-size: 18px;font-weight: bold">{{ this.dataEnvironment.Luminance }}</span>
                      &nbsp;Lx
                    </div>
                  </div>
                </el-row>
                <el-row style="width:300px;height:200px;">
                  <div id="Luminance" style="width:180px;height:280px;text-align: center; margin:15px 0 0 0"></div>
                </el-row>
              </el-col>
            </el-card>
          </el-row>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>


import axios from "axios"
import 'echarts-liquidfill';
import {ref} from 'vue';
import * as echarts from 'echarts';

export default {
  data() {
    let yy = new Date().getFullYear();
    let mm = new Date().getMonth() + 1;
    let dd = new Date().getDate();
    let hh = new Date().getHours();
    let mf = new Date().getMinutes() < 10 ? '0' + new Date().getMinutes() : new Date().getMinutes();
    let ss = new Date().getSeconds() < 10 ? '0' + new Date().getSeconds() : new Date().getSeconds();
    return {
      nowtime: yy + '/' + mm + '/' + dd + ' ' + hh + ':' + mf + ':' + ss,
      patient: "0",
      num: "0",
      person: "0",
      times: false,
      flag: "8400000",
      alldata: {
        id: "1",
        humidity: "",
        temperature: "",
        illumination: "",
        noise: "520",
        smog: "",
        heartrate: "",
        bloodx: "",
        pressure: "8400000",
      },
      dataEnvironment: {
        time: "20230711T083047Z",
        Temperature: 28,
        Humidity: 46,
        Luminance: 148,
        MQ2: 10
      },
      listTime: "",
      listTemperature: "",
      listHumidity: "",
      listLuminance: "",
      listMQ2: "",
      listSpO2:""
    }
  },
  setup() {
    const name = localStorage.getItem("ms_username");
    const role = name === "admin" ? "超级管理员" : "普通用户";
    const dialogVisible = ref(true);
    const dialogVisible1 = ref(true);
    const dialogVisible2 = ref(true);
    const dialogVisible3 = ref(true);
    const dialogVisible4 = ref(true);
    return {
      name,
      role,
      dialogVisible,
      dialogVisible1,
      dialogVisible2,
      dialogVisible3,
      dialogVisible4
    }
  },
  mounted() {
    this.draw();
    this.draw_tem();
    // this.newInterval(this.get_data, 1000);
    setInterval(this.Draw, 2000);
    setInterval(this.DrawMax, 2000);
  },
  methods: {
    Draw() {
      var data_temp = [];
      var data_humi = [];
      var data_mq = [];
      var data_Luminance = [];
      var data_time = [];

      axios.get('http://127.0.0.1:5000/askDataEnvironment').then(res => {
        // console.log("1")
        this.dataEnvironment = res.data[11] //取最后一个数据
        console.log(this.dataEnvironment)
        //存数据列表
        for (var i = 0; i < 12; i++) {
          //时间转换
          let timeString = res.data[i].time
          let year = timeString.slice(0, 4)
          let month = timeString.slice(4, 6)
          let day = timeString.slice(6, 8)
          let hour = timeString.slice(9, 11)
          let minute = timeString.slice(11, 13)
          let second = timeString.slice(13, 15)
          // let date = new Date(`${year}-${month}-${day}T${hour}:${minute}:${second}Z`)
          let date = new Date(`${year}-${month}-${day}T${hour}:${minute}:${second}Z`)
          let formattedTime = date.toLocaleString('zh-CN', {hour12: false})
          // 数据转储
          data_time.push(formattedTime.slice(10, 19))
          data_temp.push(res.data[i].Temperature);
          data_humi.push(res.data[i].Humidity);
          data_mq.push(res.data[i].MQ2);
          data_Luminance.push(res.data[i].Luminance);
        }
        this.listTemperature = data_temp;
        this.listMQ2 = data_mq;
        this.listHumidity = data_humi;
        this.listLuminance = data_Luminance;
        this.listTime = data_time;

        // console.log(this.listTime)
        //温度
        var myChartTemp = echarts.init(document.getElementById("temp"))
        var optionTemp = {
          title: {
            text: '病房温度'
          },
          series: [
            {
              type: 'gauge',
              startAngle: 200,
              endAngle: -20,
              min: 0,
              max: 40,
              splitNumber: 8,
              itemStyle: {
                color: '#FFAB91'
              },
              progress: {
                show: true,
                width: 20,
              },
              pointer: {
                show: false
              },
              axisLine: {
                lineStyle: {
                  width: 20
                }
              },
              axisTick: {
                distance: -28,
                splitNumber: 5,
                lineStyle: {
                  width: 2,
                  color: '#999'
                }
              },
              splitLine: {
                distance: -32,
                length: 10,
                lineStyle: {
                  width: 2,
                  color: '#999'
                }
              },
              axisLabel: {
                distance: -5,
                color: '#999',
                fontSize: 10
              },
              anchor: {
                show: false
              },
              title: {
                show: false
              },
              detail: {
                valueAnimation: true,
                width: '100%',
                lineHeight: 20,
                borderRadius: 8,
                offsetCenter: [0, '-10%'],
                fontSize: 25,
                fontWeight: 'bolder',
                formatter: '{value} °C',
                color: '#FD7347'
              },
              data: [
                {
                  value: this.dataEnvironment.Temperature
                }
              ]
            },
          ]
        };
        myChartTemp.setOption(optionTemp);
        //湿度
        var myChartHumidity = echarts.init(document.getElementById("humidity"))
        var optionHumidity = {
          title: {
            text: '病房湿度'
          },
          series: [
            {
              startAngle: 200,
              endAngle: -20,
              type: 'gauge',
              axisLine: {
                lineStyle: {
                  width: 18,
                  color: [
                    [0.3, '#67e0e3'],
                    [0.7, '#37a2da'],
                    [1, '#fd666d']
                  ]
                }
              },
              pointer: {
                itemStyle: {
                  color: 'auto'
                }
              },
              axisTick: {
                distance: -18,
                length: 8,
                lineStyle: {
                  color: '#fff',
                  width: 2
                }
              },
              splitLine: {
                distance: -18,
                length: 18,
                lineStyle: {
                  color: '#fff',
                  width: 2
                }
              },
              axisLabel: {

                distance: -15,
                fontSize: 12
              },
              detail: {
                valueAnimation: true,
                fontSize: 22,
                formatter: '{value} %',
                color: 'inherit'

              },
              data: [
                {
                  value: this.dataEnvironment.Humidity
                }
              ]
            }
          ]
        };
        myChartHumidity.setOption(optionHumidity);
        //光强
        var myChartLuminance = echarts.init(document.getElementById("Luminance"))
        var optionLuminance = {
          animationDuration: false,
          tooltip: {
            trigger: "axis",
            axisPointer: {
              type: "cross",
              label: {
                backgroundColor: "#283b56",
              },
            },
          },
          grid: [
            {
              left: '15%',
              right: '20%',
              top: '10%',
            },
          ],
          xAxis: [
            {
              type: "category",
              boundaryGap: true,
              data: (function () {
                var now = new Date();
                var res = [];
                var len = 1;
                while (len--) {
                  res.unshift(now.toLocaleTimeString().replace(/^\D*/, ""));
                  now = new Date(now - 2000);
                }
                return res;
              })(),
              axisTick: {
                show: false // 不显示坐标轴刻度线
              },
            },
          ],
          yAxis: [
            {
              animationDuration: false,
              type: 'value',
              scale: true,
              name: '光照强度',
              axisLabel: {
                formatter: '{value}'
              },
              boundaryGap: [0.2, 0.2]
            }
          ],
          series: [
            {
              name: "光照强度",
              type: "bar",
              barWidth: 25,
              data: [this.dataEnvironment.Luminance]
            },
          ],
        };
        myChartLuminance.setOption(optionLuminance);
        //烟雾
        var myChartMQ2 = echarts.init(document.getElementById("smog"))
        var optiontMQ2 = {
          xAxis: {
            type: 'category',
            boundaryGap: false,
            data: this.listTime
          },
          yAxis: {
            type: 'value'
          },
          series: [
            {
              data: this.listMQ2,
              type: 'line',
              areaStyle: {}
            }
          ]
        };
        myChartMQ2.setOption(optiontMQ2);
      }).catch(err => {
        console.log("获取数据失败" + err);
      })
    },
    DrawMax() {
      var data_time = [];
      var data_SpO2 = [];
      axios.get('http://127.0.0.1:5000/askDataEnvironment').then(res => {
        for (var i = 0; i < 12; i++) {
          console.log(res.data)
          //时间转换
          let timeString = res.data[i].time
          let year = timeString.slice(0, 4)
          let month = timeString.slice(4, 6)
          let day = timeString.slice(6, 8)
          let hour = timeString.slice(9, 11)
          let minute = timeString.slice(11, 13)
          let second = timeString.slice(13, 15)
          // let date = new Date(`${year}-${month}-${day}T${hour}:${minute}:${second}Z`)
          let date = new Date(`${year}-${month}-${day}T${hour}:${minute}:${second}Z`)
          let formattedTime = date.toLocaleString('zh-CN', {hour12: false})
          // 数据转储
          data_time.push(formattedTime.slice(10, 19))
          data_SpO2.push(res.data[i].SpO2);
        }
        this.listSpO2=data_SpO2
        var myChart2 = echarts.init(document.getElementById("heart_blood"))
        var option2 = {
          color: ['rgb(230, 46, 0)', 'rgb(38, 115, 76)'],
          tooltip: {
            trigger: 'axis',
            axisPointer: {
              animation: false
            }
          },

          axisPointer: {
            link: [
              {
                xAxisIndex: 'all'
              }
            ]
          },

          grid: [
            {
              left: '5%',
              right: '5%',
              top: '10%',
              height: '34%'
            },
            {
              left: '5%',
              right: '5%',
              top: '60%',
              height: '34%'
            }
          ],
          xAxis: [
            {
              type: 'category',
              boundaryGap: false,
              axisLine: {onZero: true},
              data: this.listTime,
            },
            {
              gridIndex: 1,
              type: 'category',
              boundaryGap: false,
              axisLine: {onZero: true},
              data: this.listTime,
            }
          ],
          yAxis: [
            {
              name: '心率',
              type: 'value',

            },
            {
              gridIndex: 1,
              name: '血氧',
              type: 'value',
            }
          ],
          series: [
            {
              name: '心率',
              type: 'line',
              showSymbol: false,
              data: [70, 68, 82, 78, 75, 80, 69, 79, 70, 68, 82, 78]
            },
            {
              name: '血氧',
              type: 'line',
              xAxisIndex: 1,
              yAxisIndex: 1,
              showSymbol: false,
              data: [95, 98, 97, 96, 99, 98, 97, 96, 95, 98, 97, 96]
            }
          ]
        };
        myChart2.setOption(option2);
      })
    },
    newInterval(fn, delay) {
      if (this.times == true) {
        return
      }
      setTimeout(() => {
        fn()
        this.newInterval(fn, delay)
      }, delay)
    },
    draw() {
      var alldata_1 = {
        "time": "",
        "Temperature": "",
        "Humidity": "",
        "Luminance": "",
      }


      axios.get('http://119.3.16.162:8085/data').then(res => {
        alldata_1 = res.data[0]
      }).catch(err => {
        console.log("获取数据失败" + err);
      })
      setInterval(function () {
        axios.get('http://127.0.0.1:5000/askData').then(res => {
          alldata_1 = res.data[0]
        }).catch(err => {
          console.log("获取数据失败" + err);
        })
        var axisData = new Date().toLocaleTimeString().replace(/^\D*/, "");
        var data0 = option.series[0].data;


        data0.shift();
        data0.push(alldata_1.noise - 440);
        option.xAxis[0].data.shift();
        option.xAxis[0].data.push(axisData);


        var data1 = option1.series[0].data;
        data1.shift();
        data1.push(alldata_1.smog);
        option1.xAxis[0].data.shift();
        option1.xAxis[0].data.push(axisData);


        var data2 = option2.series[0].data;
        var data3 = option2.series[1].data;
        data2.shift();
        data2.push(alldata_1.heartrate);
        data3.shift();
        data3.push(alldata_1.bloodx);
        option2.xAxis[0].data.shift();
        option2.xAxis[0].data.push(axisData);
        myChart2.setOption(option2);


        var data4 = option3.series[0].data;
        data4.shift();
        data4.push(alldata_1.illumination);
        option3.xAxis[0].data.shift();
        option3.xAxis[0].data.push(axisData);
        myChart3.setOption(option3);

        myChart.setOption(option);
        myChart1.setOption(option1);
        myChart2.setOption(option2);
        myChart3.setOption(option3);

      }, 500000);
    },


    draw_tem() {


      // axios.get('http://119.3.16.162:8085/data').then(res => {
      //   alldata_1 = res.data[0]
      //   if (res.data[0].pressure > 8180000) {
      //     alldata_1.pressure = res.data[0].pressure
      //     this.flag = res.data[0].pressure
      //   } else {
      //     alldata_1.pressure = this.flag
      //   }
      //
      // }).catch(err => {
      //   console.log("获取数据失败" + err);
      // })
      /*setInterval(function () {*/
      /*  axios.get('http://119.3.16.162:8085/data').then(res => {*/
      /*    alldata_1 = res.data[0]*/
      /*    if (res.data[0].pressure > 8170000) {*/
      /*      alldata_1.pressure = res.data[0].pressure*/
      /*      this.flag = res.data[0].pressure*/
      /*    } else {*/
      /*      alldata_1.pressure = this.flag*/
      /*    }*/
      /*  }).catch(err => {*/
      /*    console.log("获取数据失败" + err);*/
      /*  })*/
      /*  myChart.setOption({*/
      /*    series: [*/
      /*      {*/
      /*        data: [*/
      /*          {*/
      /*            value: alldata_1.temperature*/
      /*          }*/
      /*        ]*/
      /*      },*/
      /*      {*/
      //         data: [
      //           {
      //             value: alldata_1.temperature
      //           }
      //         ]
      //       }
      //     ]
      //   });
      //
      //   myChart2.setOption({
      //     series: [
      //       {
      //         data: [
      //           {
      //             value: alldata_1.humidity
      //           }
      //         ]
      //       }
      //     ]
      //   });
      //   var data1 = option1.series.data;
      //   data1[0] = (alldata_1.pressure - 8170000) / 220000;
      //   data1[1] = data1[0] - 0.2;
      //   data1[2] = data1[1] - 0.2;
      //   myChart1.setOption(option1);
      //
      // }, 500);
    },

  },

  beforeDestroy() {
    this.times = true
  }
};
</script>

<style scoped>
.el-row {
  margin-bottom: 20px;
}

.data_word {
  text-align: center;
}

.grid-content {
  display: flex;
  align-items: center;
  height: 100px;
}

.grid-cont-right {
  flex: 1;
  text-align: center;
  font-size: 14px;
  color: #999;
}

.grid-num {
  font-size: 30px;
  font-weight: bold;
}

.grid-con-icon {
  font-size: 50px;
  width: 100px;
  height: 100px;
  text-align: center;
  line-height: 100px;
  color: #fff;
}

.grid-con-1 .grid-con-icon {
  background: rgb(45, 140, 240);
}

.grid-con-1 .grid-num {
  color: rgb(45, 140, 240);
}

.grid-con-2 .grid-con-icon {
  background: rgb(100, 213, 114);
}

.grid-con-2 .grid-num {
  color: rgb(100, 213, 114);
}

.grid-con-3 .grid-con-icon {
  background: rgb(242, 94, 67);
}

.grid-con-3 .grid-num {
  color: rgb(242, 94, 67);
}

.user-info {
  display: flex;
  align-items: center;
  padding-bottom: 20px;
  border-bottom: 2px solid #ccc;
  margin-bottom: 20px;
}

.user-avator {
  width: 120px;
  height: 120px;
  border-radius: 50%;
}

.user-info-cont {
  padding-left: 50px;
  flex: 1;
  font-size: 14px;
  color: #999;
}

.user-info-cont div:first-child {
  font-size: 30px;
  color: #222;
}

.user-info-list {
  font-size: 14px;
  color: #999;
  line-height: 25px;
}

.user-info-list span {
  margin-left: 70px;
}

.mgb20 {
  margin-bottom: 20px;
}

.todo-item {
  font-size: 14px;
}

.todo-item-del {
  text-decoration: line-through;
  color: #999;
}

.dialog-footer button:first-child {
  margin-right: 10px;
}

.photo {
  margin-top: 30px;
  text-align: center;
}

.word {
  text-align: center;
}

.word1 {
  text-align: center;
  color: rgb(230, 46, 0);
}

.word2 {
  text-align: center;
  color: rgb(38, 115, 76);
}
</style>
