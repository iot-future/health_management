<template>
  <div>
    <video controls :title="videoTitle">
      <source :src="videoPath" type="video/mp4">
    </video>
  </div>
</template>

<script>
export default {
  data() {
    return {
      videoPath: "src/assets/fall_video.mp4",
      videoTitle: "My Video"
    };
  }
};
</script>
