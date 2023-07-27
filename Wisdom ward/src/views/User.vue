<template>
  <div>
    <div class="crumbs">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item>
          <i class="el-icon-user"></i> 关于我们
        </el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <el-row :gutter="20">
      <el-col :span="12">
        <el-card shadow="hover">
          <template #header>
            <div class="clearfix">
              <span>智慧病房</span>
            </div>
          </template>
          <div class="info">
            <div class="info-image" @click="showDialog">
              <img :src="avatarImg"/>
              <span class="info-edit">
                                <i class="el-icon-lx-camerafill"></i>
                            </span>
            </div>
            <div class="info-name">{{ name }}</div>
            <div class="info-desc">致力于打造最顶尖的智慧病房系统！</div>
          </div>
        </el-card>
        <el-card shadow="hover">
          <el-image src="src/assets/img/pic5.png"/>
        </el-card>

      </el-col>
      <el-col :span="12">
        <el-card shadow="hover">
          <el-calendar v-model="value"/>
        </el-card>
      </el-col>
    </el-row>
    <el-dialog title="裁剪图片" v-model="dialogVisible" width="600px">
      <vue-cropper ref="cropper" :src="imgSrc" :ready="cropImage" :zoom="cropImage" :cropmove="cropImage"
                   style="width: 100%; height: 400px"></vue-cropper>

      <template #footer>
                <span class="dialog-footer">
                    <el-button class="crop-demo-btn" type="primary">选择图片
                        <input class="crop-input" type="file" name="image" accept="image/*" @change="setImage"/>
                    </el-button>
                    <el-button type="primary" @click="saveAvatar">上传并保存</el-button>
                </span>
      </template>
    </el-dialog>


  </div>
</template>

<script>
import {reactive, ref} from "vue";
import VueCropper from "vue-cropperjs";
import "cropperjs/dist/cropper.css";
import avatar from "../assets/img/1.jpg";

export default {
  components: {
    VueCropper,
  },


  setup() {
    const name = localStorage.getItem("ms_username");
    const value = ref(new Date())
    const form = reactive({
      old: "",
      new: "",
      desc: "致力于打造最顶尖的智慧病房系统!",
    });
    const onSubmit = () => {
    };

    const avatarImg = ref(avatar);
    const imgSrc = ref("");
    const cropImg = ref("");
    const dialogVisible = ref(false);
    const cropper = ref(null);

    const showDialog = () => {
      dialogVisible.value = true;
      imgSrc.value = avatarImg.value;
    };

    const setImage = (e) => {
      const file = e.target.files[0];
      if (!file.type.includes("image/")) {
        return;
      }
      const reader = new FileReader();
      reader.onload = (event) => {
        dialogVisible.value = true;
        imgSrc.value = event.target.result;
        cropper.value && cropper.value.replace(event.target.result);
      };
      reader.readAsDataURL(file);
    };

    const cropImage = () => {
      cropImg.value = cropper.value.getCroppedCanvas().toDataURL();
    };

    const saveAvatar = () => {
      avatarImg.value = cropImg.value;
      dialogVisible.value = false;
    };

    return {
      name,
      form,
      onSubmit,
      cropper,
      avatarImg,
      imgSrc,
      cropImg,
      showDialog,
      dialogVisible,
      setImage,
      cropImage,
      saveAvatar,
      value
    };
  },
};
</script>

<style scoped>
.info {
  text-align: center;
  padding: 22px 0;
}

.info-image {
  position: relative;
  margin: auto;
  width: 100px;
  height: 100px;
  background: #f8f8f8;
  border: 1px solid #eee;
  border-radius: 50px;
  overflow: hidden;
}

.info-image img {
  width: 100%;
  height: 100%;
}

.info-edit {
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.info-edit i {
  color: #eee;
  font-size: 25px;
}

.info-image:hover .info-edit {
  opacity: 1;
}

.info-name {
  margin: 15px 0 10px;
  font-size: 24px;
  font-weight: 500;
  color: #262626;
}

.crop-demo-btn {
  position: relative;
}

.crop-input {
  position: absolute;
  width: 100px;
  height: 40px;
  left: 0;
  top: 0;
  opacity: 0;
  cursor: pointer;
}

</style>