<template>
  <div>
    <Navbar class="Navbar" />
    <Footer class="Footer"></Footer>
  </div>
</template>


<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Navbar from '../components/Navbar.vue'
import Footer from '../components/Footer.vue';
</script>

<style>
@font-face {
  font-family: 'JalnanGothic'; /* 원하는 폰트 이름 */
  src: url('/fonts/JalnanGothic.otf') format('opentype'), /* 폰트 파일 경로 */
}
body {
  font-family: 'JalnanGothic', sans-serif; /* 폰트 적용 */
  min-width: 600px;
  background-color: #fcfcfc;
}

.navbar {
  margin-bottom: 150px;
}

.Footer {
  /* margin-top: 300px; */
}
</style>

<style scoped>

</style>
