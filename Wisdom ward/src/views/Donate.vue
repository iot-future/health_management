<template>
 <div>
    <div class="crumbs">
        <el-breadcrumb separator="/">
            <el-breadcrumb-item>
                <i class="el-icon-pie-chart"></i> 人工智能
            </el-breadcrumb-item>
        </el-breadcrumb>
    </div>

    <el-button type="primary" @click="cimsInputClick">语音控制</el-button>
    <el-button type="primary" @click="cccc">打开监控</el-button>

    <!-- 照片显示 -->
    <el-button type="info" plain size="mini" @click="imgshow">点击展示后台传的base64图片</el-button>
    
    	

    <el-dialog v-model="tupxs" title="获取图像"  center>
    <div class="fl" style="width:auto;height:auto">
      <el-image :src="_img" alt="" />
    </div>
    </el-dialog>
    
</div>
 
</template>

<script>
import axios from "axios"
export default {

  data() {
    return {
      _img: '',
      tupxs: false,
      downloadUrl: null,
      downloadfilename: null
    }
  },

  setup(){

    	const _this = this
			axios.get('http://119.3.16.162:8085/bodynum').then(function(res) {
			  var image = res.data[0].data; //后台返回的base64文件
			  _img= 'data:image/png;base64,' + image//在base64文件前加“'data:image/png;base64,' ”可以在页面上显示图片，但是文件仍然不是png格式
			  downLoadImage(_img)//这一步，将文件转成png格式
			_tupxs = true
			})
      return{

      }

  },
  
  
  methods: {
    cimsInputClick () {
      window.open('http://localhost:5000/main.html')

    },
    cccc () {
      window.open('http://localhost:5000/main.html')

    },

    imgshow() {
				const _this = this
				axios.get('http://119.3.16.162:8085/bodynum').then(function(res) {
						var image = res.data[0].data; //后台返回的base64文件
						_this._img= 'data:image/png;base64,' + image//在base64文件前加“'data:image/png;base64,' ”可以在页面上显示图片，但是文件仍然不是png格式
						_this.downLoadImage(_this._img)//这一步，将文件转成png格式
						_this.tupxs = true

					})
			},
      //base64格式转换png
			downLoadImage(imgUrl) {
				let timestamp = new Date().getTime()
				let name = imgUrl.substring(22, 30) + timestamp + '.png'
				this.downloadUrl = imgUrl
				this.downloadfilename = name
			},

  }
 
}
</script>


<style scoped>
.fl{
    display: flex;
    justify-content: space-around;
   
  }

</style>


