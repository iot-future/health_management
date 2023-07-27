<template>
  <div class="right_one_box">
    <div class="box_con">
      <div class="con">
        <canvas id="video-canvas" style="height: 1000px; wight:1404px"></canvas>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  mounted () {
    var canvas = document.getElementById('video-canvas')

    var player = new JSMpeg.Player(this.path, {canvas: canvas})

  },

  data(){
    return{
      path:'ws://127.0.0.1:8082',   //你拉取视频源地址

    }
  },
  methods:{


  }
};
</script>