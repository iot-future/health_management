<template>
  <div>
    <div class="crumbs">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item>
          <i class="el-icon-video-camera"></i> 病房控制
        </el-breadcrumb-item>
      </el-breadcrumb>
    </div>

    <el-card shadow="hover">


      <!--动态将图片轮播图的容器高度设置成与图片一致-->
      <el-carousel :interval="4000" type="card" height="350px">
        <el-carousel-item v-for="item in imagebox" :key="item.id">
          <img :src="item.idView" class="image" alt/>
        </el-carousel-item>
      </el-carousel>

      <el-row style="height:100px">
        <el-col :span="16">
          <div v-if="auto.flag==1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <el-button type="primary" round
                       style="width:120px;height:30px;text-align: center;margin-top:10px">自动模式
            </el-button>
            <el-button type="primary" round plain
                       style="width:120px;height:30px;text-align: center;margin-top:10px" @click="set_autooff()">
              手动模式
            </el-button>
            <span class="word1">&nbsp;&nbsp;现在是自动模式，注意身边的电器哦~~</span>
          </div>
          <div v-else-if="auto.flag==0">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <el-button type="primary" round plain
                       style="width:120px;height:30px;text-align: center;margin-top:10px" @click="set_autoon()">
              自动模式
            </el-button>
            <el-button type="primary" round
                       style="width:120px;height:30px;text-align: center;margin-top:10px">手动模式
            </el-button>
            <span class="word1">&nbsp;&nbsp;现在是手动模式，可以自主调节开关，控制电器</span>
          </div>
        </el-col>

<!--        <el-col :span="2">-->
<!--          <el-button type="primary" @click="cimsInputClick"-->
<!--                     style="width:120px;height:30px;text-align: center;margin-top:10px;">语音控制-->
<!--          </el-button>-->
<!--          <el-dialog v-model="dialog1" title="语音控制" style="height: 400px;margin: 0 0 0 0;" center>-->
<!--            <div>-->
<!--              <iframe style="width:900px;height:320px" src="http://localhost:5000/main.html"></iframe>-->
<!--            </div>-->
<!--          </el-dialog>-->
<!--        </el-col>-->

<!--        <el-col :span="2">-->
<!--          <el-button type="primary" @click="cimsInputClick1"-->
<!--                     style="width:120px;height:30px;text-align: center;margin-top:10px;">打开监控-->
<!--          </el-button>-->
<!--          <el-dialog v-model="dialog2" title="打开监控" style="height: 400px;margin: 0 0 0 0;" center>-->
<!--            <div>-->
<!--              <iframe style="width:900px;height:320px" src="http://localhost:2000/main.html"></iframe>-->
<!--            </div>-->
<!--          </el-dialog>-->
<!--        </el-col>-->

<!--        <el-col :span="2">-->
<!--          <el-button type="primary" @click="cimsInputClick2"-->
<!--                     style="width:120px;height:30px;text-align: center;margin-top:10px;">自动拍摄-->
<!--          </el-button>-->
<!--          <el-dialog v-model="dialog3" title="自动拍摄" style="height: 400px;margin: 0 0 0 0;" center>-->
<!--            <div>-->
<!--              <iframe style="width:900px;height:320px" src="http://localhost:4000/main.html"></iframe>-->
<!--            </div>-->
<!--          </el-dialog>-->
<!--        </el-col>-->
<!--        &lt;!&ndash; 照片显示 &ndash;&gt;-->
<!--        <el-col :span="2">-->
<!--          <el-button type="primary" @click="imgshow"-->
<!--                     style="width:120px;height:30px;text-align: center;margin-top:10px;">获取图像-->
<!--          </el-button>-->
<!--          <el-dialog v-model="tupxs" title="获取图像" center>-->
<!--            <el-table :data="persons" style="width: 100%">-->
<!--              <el-table-column prop="id" label="ID" width="150"/>-->
<!--              <el-table-column prop="smoke" label="吸烟" width="150"/>-->
<!--              <el-table-column prop="age" label="年龄" width="150"/>-->
<!--              <el-table-column prop="gender" label="性别" width="150"/>-->
<!--              <el-table-column prop="face_mask" label="口罩" width="150"/>-->
<!--              <el-table-column prop="upper_color" label="上衣颜色" width="150"/>-->
<!--            </el-table>-->
<!--            <div class="fl" style="width:auto;height:auto">-->
<!--              <el-image :src="_img" alt=""/>-->
<!--            </div>-->
<!--          </el-dialog>-->
<!--        </el-col>-->
      </el-row>


      <div v-if="auto.flag==1">
        <el-row :gutter="20">
          <!-- 自动模式 -->
          <el-col :span="4" style="height:250px">
            <div v-if="switch1.fan==1">
              <el-row>
                <el-col :span="12">
                  <div class="el-row1">风扇控制</div>
                </el-col>
                <el-col :span="12">
                  <div class="el-row2">
                    <el-switch v-model="value1" @change="set_fanoff()" loading/>
                  </div>
                </el-col>
              </el-row>
              <div class="photo">
                <img src="../assets/img/fengshanonf.png"
                     style="margin: auto; width: 200px; height:200px"/>
              </div>

            </div>
            <div v-if="switch1.fan==0">
              <el-row>
                <el-col :span="12">
                  <div class="el-row1">风扇控制</div>
                </el-col>
                <el-col :span="12">
                  <div class="el-row2">
                    <el-switch v-model="value2" @change="set_fan()" loading/>
                  </div>
                </el-col>
              </el-row>
              <div class="photo">
                <img src="../assets/img/fengshanofff.png"
                     style="margin: auto; width: 200px; height:200px"/>
              </div>
            </div>
          </el-col>
          <el-col :span="4" style="height:250px">
            <div v-if="switch1.heat==1">
              <el-row>
                <el-col :span="12">
                  <div class="el-row1">加热控制</div>
                </el-col>
                <el-col :span="12">
                  <div class="el-row2">
                    <el-switch v-model="value3" @change="set_heatoff()" loading/>
                  </div>
                </el-col>
              </el-row>
              <div class="photo">
                <img src="../assets/img/jiareon_f.png"
                     style="margin: 30px 0 0 35px; width: 150px; height:150px"/>
              </div>
            </div>
            <div v-if="switch1.heat==0">
              <el-row>
                <el-col :span="12">
                  <div class="el-row1">加热控制</div>
                </el-col>
                <el-col :span="12">
                  <div class="el-row2">
                    <el-switch v-model="value4" @change="set_heat()" loading/>
                  </div>
                </el-col>
              </el-row>
              <div class="photo">
                <img src="../assets/img/jiareoff_f.png"
                     style="margin: 30px 0 0 35px; width: 150px; height:150px"/>
              </div>
            </div>
          </el-col>


          <el-col :span="4" style="height:250px">

            <el-row>
              <el-col :span="12">
                <div class="el-row1">灯光控制</div>
              </el-col>
              <el-col :span="12">
                <div v-if="switch1.light==0">
                  <el-select v-model="selectedlight" filterable placeholder="关闭" size="small"
                             style="margin: 0 0 0 50px;width:80px" disabled>
                    <el-option value="关闭" @click="set_lightoff()"></el-option>
                    <el-option value="一档" @click="set_light1()"></el-option>
                    <el-option value="二档" @click="set_light2()"></el-option>
                    <el-option value="三档" @click="set_light3()"></el-option>
                  </el-select>
                </div>
                <div v-else-if="switch1.light==1">
                  <el-select v-model="selectedlight" filterable placeholder="一档" size="small"
                             style="margin: 0 0 0 50px;width:80px" disabled>
                    <el-option value="关闭" @click="set_lightoff()"></el-option>
                    <el-option value="一档" @click="set_light1()"></el-option>
                    <el-option value="二档" @click="set_light2()"></el-option>
                    <el-option value="三档" @click="set_light3()"></el-option>
                  </el-select>
                </div>
                <div v-else-if="switch1.light==2">
                  <el-select v-model="selectedlight" filterable placeholder="二档" size="small"
                             style="margin: 0 0 0 50px;width:80px" disabled>
                    <el-option value="关闭" @click="set_lightoff()"></el-option>
                    <el-option value="一档" @click="set_light1()"></el-option>
                    <el-option value="二档" @click="set_light2()"></el-option>
                    <el-option value="三档" @click="set_light3()"></el-option>
                  </el-select>
                </div>
                <div v-else-if="switch1.light==3">
                  <el-select v-model="selectedlight" filterable placeholder="三档" size="small"
                             style="margin:0 0 0 50px;width:80px" disabled>
                    <el-option value="关闭" @click="set_lightoff()"></el-option>
                    <el-option value="一档" @click="set_light1()"></el-option>
                    <el-option value="二档" @click="set_light2()"></el-option>
                    <el-option value="三档" @click="set_light3()"></el-option>
                  </el-select>
                </div>
              </el-col>
            </el-row>
            <div v-if="switch1.light==0">
              <div class="photo">
                <img src="../assets/img/lightoff.png"
                     style="margin: 30px 0 0 40px; width: 150px; height:150px"/>
              </div>
            </div>

            <div v-else>
              <div class="photo">
                <img src="../assets/img/lighton.png"
                     style="margin: 30px 0 0 40px; width: 150px; height:150px"/>
              </div>
            </div>

          </el-col>
          <el-col :span="4" style="height:250px">
            <div v-if="switch1.curtain==1">
              <el-row>
                <el-col :span="12">
                  <div class="el-row1">窗帘控制</div>
                </el-col>
                <el-col :span="12">
                  <div class="el-row2">
                    <el-switch v-model="value7" @change="set_curoff()" loading/>
                  </div>
                </el-col>
              </el-row>
              <div class="photo">
                <img src="../assets/img/curtain-open.png"
                     style="margin: 25px 0 0 40px; width: 150px; height:150px"/>
              </div>
            </div>
            <div v-if="switch1.curtain==0">
              <el-row>
                <el-col :span="12">
                  <div class="el-row1">窗帘控制</div>
                </el-col>
                <el-col :span="12">
                  <div class="el-row2">
                    <el-switch v-model="value8" @change="set_cur()" loading/>
                  </div>
                </el-col>
              </el-row>
              <div class="photo">
                <img src="../assets/img/curtain.png"
                     style="margin: 15px 0 0 40px; width: 180px; height:180px"/>
              </div>
            </div>
          </el-col>

          <el-col :span="4" style="height:250px">
            <div v-if="switch1.lock_door==1">
              <el-row>
                <el-col :span="12">
                  <div class="el-row1">门锁控制</div>
                </el-col>
                <el-col :span="12">
                  <div class="el-row2">
                    <el-switch v-model="value9" @change="set_lockoff()" loading/>
                  </div>
                </el-col>
              </el-row>
              <div class="photo">
                <img src="../assets/img/unlock.png"
                     style="margin: 40px 0 0 40px; width: 180px; height:180px"/>
              </div>
            </div>
            <div v-if="switch1.lock_door==0">
              <el-row>
                <el-col :span="12">
                  <div class="el-row1">门锁控制</div>
                </el-col>
                <el-col :span="12">
                  <div class="el-row2">
                    <el-switch v-model="value10" @change="set_lock()" loading/>
                  </div>
                </el-col>
              </el-row>
              <div class="photo">
                <img src="../assets/img/lock.png"
                     style="margin: 40px 0 0 40px; width: 120px; height:120px"/>
              </div>
            </div>
          </el-col>
          <el-col :span="4" style="height:250px">
            <div v-if="switch1.door==1">
              <el-row>
                <el-col :span="12">
                  <div class="el-row1">房门状态</div>
                </el-col>
              </el-row>
              <div class="photo">
                <img src="../assets/img/door-open.png"
                     style="margin: 20px 0 0 20px; width: 150px; height:180px"/>
              </div>
            </div>
            <div v-if="switch1.door==0">
              <el-row>
                <el-col :span="12">
                  <div class="el-row1">房门状态</div>
                </el-col>
              </el-row>
              <div class="photo">
                <img src="../assets/img/door.png"
                     style="margin: 20px 0 0 20px; width: 150px; height:180px"/>
              </div>
            </div>
          </el-col>
        </el-row>
      </div>

      <div v-if="auto.flag==0">
        <el-row :gutter="20">
          <!-- 手动模式 -->

          <el-col :span="4" style="height:250px">
            <div v-if="this.motorState===1">
              <el-row>
                <el-col :span="12">
                  <div class="el-row1">风扇控制</div>
                </el-col>
                <el-col :span="12">
                  <div class="el-row2">
                    <el-switch v-model="value1" @change="set_fanoff()"/>
                  </div>
                </el-col>
              </el-row>
              <div class="photo">
                <img src="../assets/img/fengshanonf.png"
                     style="margin: auto; width: 200px; height:200px" @click="set_fanoff()"/>
              </div>
            </div>

            <div v-if="this.motorState===0">
              <el-row>
                <el-col :span="12">
                  <div class="el-row1">风扇控制</div>
                </el-col>
                <el-col :span="12">
                  <div class="el-row2">
                    <el-switch v-model="value2" @change="set_fan()"/>
                  </div>
                </el-col>
              </el-row>
              <div class="photo">
                <img src="../assets/img/fengshanofff.png"
                     style="margin: auto; width: 200px; height:200px" @click="set_fan()"/>
              </div>
            </div>
          </el-col>
          <el-col :span="4" style="height:250px">
            <div v-if="switch1.heat==1">
              <el-row>
                <el-col :span="12">
                  <div class="el-row1">加热控制</div>
                </el-col>
                <el-col :span="12">
                  <div class="el-row2">
                    <el-switch v-model="value3" @change="set_heatoff()"/>
                  </div>
                </el-col>
              </el-row>
              <div class="photo">
                <img src="../assets/img/jiareon_f.png"
                     style="margin: 25px 0 0 35px; width: 150px; height:150px" @click="set_heatoff()"/>
              </div>
            </div>
            <div v-if="switch1.heat==0">
              <el-row>
                <el-col :span="12">
                  <div class="el-row1">加热控制</div>
                </el-col>
                <el-col :span="12">
                  <div class="el-row2">
                    <el-switch v-model="value4" @change="set_heat()"/>
                  </div>
                </el-col>
              </el-row>
              <div class="photo">
                <img src="../assets/img/jiareoff_f.png"
                     style="margin: 25px 0 0 35px; width: 150px; height:150px" @click="set_heat()"/>
              </div>
            </div>
          </el-col>


          <el-col :span="4" style="height:250px">

            <el-row>
              <el-col :span="12">
                <div class="el-row1">灯光控制</div>
              </el-col>
              <el-col :span="12">
                <div v-if="this.lightState===0">
                  <el-select v-model="selectedlight" filterable placeholder="关闭" size="small"
                             style="margin: 0 0 0 50px;width:80px">
                    <el-option value="关闭" @click="set_lightoff()"></el-option>
                    <el-option value="一档" @click="set_light1()"></el-option>
                    <el-option value="二档" @click="set_light2()"></el-option>
                    <el-option value="三档" @click="set_light3()"></el-option>
                  </el-select>
                </div>
                <div v-else-if="this.lightState==1">
                  <el-select v-model="selectedlight" filterable placeholder="一档" size="small"
                             style="margin: 0 0 0 50px;width:80px">
                    <el-option value="关闭" @click="set_lightoff()"></el-option>
                    <el-option value="一档" @click="set_light1()"></el-option>
                    <el-option value="二档" @click="set_light2()"></el-option>
                    <el-option value="三档" @click="set_light3()"></el-option>
                  </el-select>
                </div>
                <div v-else-if="switch1.light==2">
                  <el-select v-model="selectedlight" filterable placeholder="二档" size="small"
                             style="margin: 0 0 0 50px;width:80px">
                    <el-option value="关闭" @click="set_lightoff()"></el-option>
                    <el-option value="一档" @click="set_light1()"></el-option>
                    <el-option value="二档" @click="set_light2()"></el-option>
                    <el-option value="三档" @click="set_light3()"></el-option>
                  </el-select>
                </div>
                <div v-else-if="switch1.light==3">
                  <el-select v-model="selectedlight" filterable placeholder="三档" size="small"
                             style="margin:0 0 0 50px;width:80px">
                    <el-option value="关闭" @click="set_lightoff()"></el-option>
                    <el-option value="一档" @click="set_light1()"></el-option>
                    <el-option value="二档" @click="set_light2()"></el-option>
                    <el-option value="三档" @click="set_light3()"></el-option>
                  </el-select>
                </div>
              </el-col>
            </el-row>
            <div v-if="switch1.light==0">
              <div class="photo">
                <img src="../assets/img/lightoff.png"
                     style="margin: 25px 0 0 40px; width: 150px; height:150px"/>
              </div>
            </div>

            <div v-else>
              <div class="photo">
                <img src="../assets/img/lighton.png"
                     style="margin: 25px 0 0 40px; width: 150px; height:150px"/>
              </div>
            </div>

          </el-col>
          <el-col :span="4" style="height:250px">
            <div v-if="switch1.curtain==1">
              <el-row>
                <el-col :span="12">
                  <div class="el-row1">窗帘控制</div>
                </el-col>
                <el-col :span="12">
                  <div class="el-row2">
                    <el-switch v-model="value7" @change="set_curoff()"/>
                  </div>
                </el-col>
              </el-row>
              <div class="photo">
                <img src="../assets/img/curtain-open.png"
                     style="margin: 25px 0 0 40px; width: 150px; height:150px" @click="set_curoff()"/>
              </div>
            </div>
            <div v-if="switch1.curtain==0">
              <el-row>
                <el-col :span="12">
                  <div class="el-row1">窗帘控制</div>
                </el-col>
                <el-col :span="12">
                  <div class="el-row2">
                    <el-switch v-model="value8" @change="set_cur()"/>
                  </div>
                </el-col>
              </el-row>
              <div class="photo">
                <img src="../assets/img/curtain.png"
                     style="margin: 15px 0 0 40px; width: 180px; height:180px" @click="set_cur()"/>
              </div>
            </div>
          </el-col>

          <el-col :span="4" style="height:250px">
            <div v-if="switch1.lock_door==1">
              <el-row>
                <el-col :span="12">
                  <div class="el-row1">门锁控制</div>
                </el-col>
                <el-col :span="12">
                  <div class="el-row2">
                    <el-switch v-model="value9" @change="set_lockoff()"/>
                  </div>
                </el-col>
              </el-row>
              <div class="photo">
                <img src="../assets/img/unlock.png"
                     style="margin: 40px 0 0 40px; width: 120px; height:120px" @click="set_lockoff()"/>
              </div>
            </div>
            <div v-if="switch1.lock_door==0">
              <el-row>
                <el-col :span="12">
                  <div class="el-row1">门锁控制</div>
                </el-col>
                <el-col :span="12">
                  <div class="el-row2">
                    <el-switch v-model="value10" @change="set_lock()"/>
                  </div>
                </el-col>
              </el-row>
              <div class="photo">
                <img src="../assets/img/lock.png"
                     style="margin: 40px 0 0 40px; width: 120px; height:120px" @click="set_lock()"/>
              </div>
            </div>
          </el-col>
          <el-col :span="4" style="height:250px">
            <div v-if="switch1.door==1">
              <el-row>
                <el-col :span="12">
                  <div class="el-row1">房门状态</div>
                </el-col>
              </el-row>
              <div class="photo">
                <img src="../assets/img/door-open.png"
                     style="margin: 20px 0 0 20px; width: 150px; height:180px"/>
              </div>
            </div>
            <div v-if="switch1.door==0">
              <el-row>
                <el-col :span="12">
                  <div class="el-row1">房门状态</div>
                </el-col>
              </el-row>
              <div class="photo">
                <img src="../assets/img/door.png"
                     style="margin: 20px 0 0 20px; width: 150px; height:180px"/>
              </div>
            </div>
          </el-col>
        </el-row>
      </div>
    </el-card>


  </div>
</template>

<script>
import axios from "axios"
import {ref} from 'vue'

export default {
  data() {
    return {

      persons: [],
      motorState: 0,
      lightState: 0,
      imagebox: [{id: 0, idView: 'src/assets/img/pic1.jpg'},
        {id: 1, idView: "src/assets/img/pic5.png"},
        {id: 2, idView: "src/assets/img/pic2.jpg"},
        {id: 3, idView: "src/assets/img/pic3.jpg"},
        {id: 4, idView: "src/assets/img/pic4.jpg"},

      ],

      _img: '',
      tupxs: false,
      downloadUrl: null,
      downloadfilename: null,

      dialog3: false,
      dialog1: false,
      dialog2: false,

      // 浏览器宽度
      screenWidth: 0,

      times: false,

      switch1: {
        id: "",
        fan: "",
        heat: "",
        light: "",
        curtain: "",
        door: "0",
        lock_door: ""
      },

      person: "1",

      alldata: {
        id: "",
        humidity: "",
        temperature: "",
        illumination: "",
        noise: "",
        smog: "",
        heartrate: "",
        bloodx: ""
      },

      auto: {
        id: "",
        flag: ""
      }
    };
  },
  setup() {
    const value1 = ref(true)
    const value2 = ref(false);
    const value3 = ref(true);
    const value4 = ref(false);
    const value5 = ref(true)
    const value6 = ref(false);
    const value7 = ref(true);
    const value8 = ref(false);
    const value9 = ref(true)
    const value10 = ref(false);
    const value11 = ref(true);
    const value12 = ref(false);
    const selectedlight = ref('')

    return {
      value1,
      value2,
      value3,
      value4,
      value5,
      value6,
      value7,
      value8,
      value9,
      value10,
      value11,
      value12,
      selectedlight,

    };
  },

  mounted() {
    this.newInterval(this.get_auto, 1000);
    this.newInterval(this.get_switch, 1000);
    this.newInterval(this.get_data, 1000);
    this.newInterval(this.all, 1000);

    // 首次加载时,需要调用一次
    this.screenWidth = window.innerWidth;
    this.setSize();
    // 窗口大小发生改变时,调用一次
    window.onresize = () => {
      this.screenWidth = window.innerWidth;
      this.setSize();
    }

  },

  methods: {
    cimsInputClick() {
      this.dialog1 = true

    },

    all() {
      // axios.get('http://119.3.16.162:8085/bodydata').then(res => {
      //   this.persons = res.data
      // }).catch(err => {
      //   console.log("获取数据失败" + err);
      // })
    },

    imgshow() {

    },
    //base64格式转换png
    downLoadImage(imgUrl) {
      let timestamp = new Date().getTime()
      let name = imgUrl.substring(22, 30) + timestamp + '.png'
      this.downloadUrl = imgUrl
      this.downloadfilename = name
    },

    setSize: function () {
      // 通过浏览器宽度(图片宽度)计算高度
      this.bannerHeight = 400 / 1920 * this.screenWidth;
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

    get_switch() {
    },
    get_data() {
      // axios.get('http://119.3.16.162:8085/data').then(res => {
      //   this.alldata = res.data[0]
      // }).catch(err => {
      //   console.log("获取数据失败" + err);
      // })
    },

    get_auto() {
      // axios.get('http://119.3.16.162:8085/auto').then(res => {
      //   this.auto = res.data[0]
      // }).catch(err => {
      //   console.log("获取数据失败" + err);
      // })
    },

    set_autoon() {
      // axios.get('http://119.3.16.162:8085/autoon').then(res => {
      // }).catch(err => {
      //   console.log("获取数据失败" + err);
      // })
    },

    set_autooff() {
      // axios.get('http://119.3.16.162:8085/autooff').then(res => {
      // }).catch(err => {
      //   console.log("获取数据失败" + err);
      // })
    },

    set_heat() {
      // axios.get('http://119.3.16.162:8085/heaton').then(res => {
      // }).catch(err => {
      //   console.log("获取数据失败" + err);
      // })
    },
    set_heatoff() {
      // axios.get('http://119.3.16.162:8085/heatoff').then(res => {
      // }).catch(err => {
      //   console.log("获取数据失败" + err);
      // })
    },

    set_fan() {
      this.motorState = 1
      this.value1 = true
      this.value2 = true
      console.log(this.value1)
      console.log(this.value2)

      axios.get('http://127.0.0.1:5000/openMotor').then(res => {
      }).catch(err => {
        console.log("获取数据失败" + err);
      })
    },
    set_fanoff() {
      this.motorState = 0
      this.value1 = true
      this.value2 = false
      console.log(this.value1)
      console.log(this.value2)

      axios.get('http://127.0.0.1:5000/closeMotor').then(res => {
      }).catch(err => {
        console.log("获取数据失败" + err);
      })
    },

    set_cur() {
      // axios.get('http://119.3.16.162:8085/curtainon').then(res => {
      // }).catch(err => {
      //   console.log("获取数据失败" + err);
      // })
    },
    set_curoff() {
      // axios.get('http://119.3.16.162:8085/curtainoff').then(res => {
      // }).catch(err => {
      //   console.log("获取数据失败" + err);
      // })
    },

    set_light1() {
      this.lightState=1
      axios.get('http://127.0.0.1:5000/openLight').then(res => {
      }).catch(err => {
        console.log("获取数据失败" + err);
      })
    },
    set_light2() {
      // axios.get('http://119.3.16.162:8085/lighton2').then(res => {
      // }).catch(err => {
      //   console.log("获取数据失败" + err);
      // })
    },
    set_light3() {
      // axios.get('http://119.3.16.162:8085/lighton3').then(res => {
      // }).catch(err => {
      //   console.log("获取数据失败" + err);
      // })
    },

    set_lightoff() {
      this.lightState=0
      axios.get('http://127.0.0.1:5000/closeLight').then(res => {
      }).catch(err => {
        console.log("获取数据失败" + err);
      })
    },

    set_lock() {
      // axios.get('http://119.3.16.162:8085/lockon').then(res => {
      // }).catch(err => {
      //   console.log("获取数据失败" + err);
      // })
    },

    set_lockoff() {
      // axios.get('http://119.3.16.162:8085/lockoff').then(res => {
      // }).catch(err => {
      //   console.log("获取数据失败" + err);
      // })
    },


  },
  beforeDestroy() {
    this.times = true;
  }
};
</script>

<style scoped>

.mgb20 {
  margin-bottom: 20px;
}

.el-row1 {
  margin-left: 30px;
}

.el-row2 {

  margin-left: 70px;
}

.grid-content {
  display: flex;
  align-items: center;
  height: 50px;
}

.grid-con-1 .grid-con-icon {
  background: rgb(45, 140, 240);
}

.grid-con-1 .grid-num {
  color: rgb(45, 140, 240);
}

.grid-con-icon {
  font-size: 50px;
  width: 100px;
  height: 100px;
  text-align: left;
  line-height: 100px;
  color: #fff;
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

.photo {
  margin-top: 10px;
  text-align: center;
}

.button_c {
  text-align: center;
  align-items: center;
}

.word1 {
  text-align: center;
  color: #999;
}

.el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n+1) {
  background-color: #d3dce6;
}

img {
  /*设置图片宽度和浏览器宽度一致*/
  width: 100%;
  height: inherit;
}

.fl {
  display: flex;
  justify-content: space-around;

}

</style>