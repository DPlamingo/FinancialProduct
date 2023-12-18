<template>
  <footer>
    <div class="row flex-column">

      <!-- 프로젝트 이름 -->
      <div class="footer-title col-12">
        <p>Finnect</p>
        <hr>
      </div>

      <!-- 지도, 설명, 링크 -->
      <div class="col-12 row justify-content-center">
        <div class="map col-12 col-md-auto">
          <p class="map-title">Head Office</p>
          <img src="@/assets/images/our-office.png" alt="Our office">
          <p class="map-text">Address : 부산 강서구 녹산산업중로 333</p>
        </div>

        <div class="say col-12 col-md-auto">
          <div class="say-title">
            <p>Contact US</p>
          </div>
          <div class="say-text">
            <p style="white-space: nowrap;">
              안녕하세요. <br>
              Finnect 제작자 <br>
              김지수, 신현기 입니다. <br>
              문의 사항이 있으시면, <br>
              이곳으로 연락을 주세요.
            </p>
          </div>
          <div class="say-email">
            <p style="white-space: nowrap;">Email : lement38641@gmail.com</p>
            <p style="white-space: nowrap;">Email : humankim800@gmail.com</p>
          </div>
        </div>

        <div class="sub col-12 col-md-auto">
          <div>
            <p style="white-space: nowrap;">
              Subscribe US
            </p>
          </div>
          <div class="icon row">
            <div class="col-4">
              <a href="https://lab.ssafy.com/muffin3864/final-pjt">
                <img class="github-icon" src="@/assets/images/github-icon.png" alt="github">
              </a>
            </div>
            <div class="col-4">
              <a href="https://www.notion.so/Team-Project-Template-62d1685767474ae69f350c958b7a70d1">
                <img class="notion-icon" src="@/assets/images/notion-icon.png" alt="github">
              </a>
            </div>
            <div class="col-4">
              <a href="https://www.figma.com/file/Jk5Qj1doS7AbZFgLhRw0cc/final_project?type=design&node-id=0-1&mode=design&t=CD5WmfYBGNoQspHk-0">
                <img class="figma-icon" src="@/assets/images/figma-icon.png" alt="github">
              </a>
            </div>
          </div>
        </div>
      </div>

      <!-- 목록, 카피라이트 -->
      <div class="nav col-12 row">

        <div class="row col-8">
          <div class="col">
            <router-link :to="{ name: 'HomeView' }">Home</router-link>
          </div>
          <div class="col">
            <router-link :to="{ name: 'UserProfile' }">내 정보</router-link>
          </div>
          <div class="col">
            <router-link :to="{ name: 'SelectDepsitView' }">상품추천</router-link>
          </div>
          <div class="col">
            <router-link :to="{ name: 'DepositListView' }">전체상품</router-link>
          </div>
        </div>

        <div class="copyright col-4 text-end">
          <p>(C) 2023. Finnect all right reserved.</p>
        </div>

      </div>

    </div>
  </footer>
</template>

<script setup>

</script>

<style scoped>
@font-face {
  font-family: 'MBC1961GulimM';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2304-01@1.0/MBC1961GulimM.woff2') format('woff2');
  font-weight: normal;
  font-style: normal;
}

footer {
background-color: #111111;
height: auto;
/* margin-top: 300px; */
/* padding: 20px; */
font-family: 'MBC1961GulimM';
letter-spacing: 1px;

}

body {
font-family: 'Roboto', sans-serif;

}

.footer-title {
color: white;
padding: 20px;
font-size: 2em;
}

.footer-title p {
padding-left: 40px;
}

.map {
padding-left: 60px;
padding-bottom: 20px;
margin-bottom: 50px;
min-width: 400px;
}

.map-title {
color: white;
font-size: 30px;
}

.map img {
width: 300px;
height: auto;
}

.map-text {
color: white;
font-size: 15px;
margin-top: 5px;
}

.say {
color: white;
padding-left: 60px;
margin-bottom: 50px;
min-width: 400px;
}

.say-title {
font-size: 30px;
}

.say-text {
font-size: 16px;
margin-bottom: 30px;
}

.say-email {
font-size: 13px;
}

.say-email p {
margin-bottom: 5px;
}

.sub {
color: white;
padding-left: 60px;
margin-bottom: 20px;
font-size: 30px;
min-width: 400px;
}
.icon {
max-width: 150px;
}

.github-icon {
width: 40px;
height: auto;
/* margin: 10px; */
}

.notion-icon {
width: 40px;
height: auto;
/* margin: 10px; */
margin-left: 20px;
}

.figma-icon {
width: 40px;
height: auto;
/* margin: 10px; */
margin-left: 40px;
}

.nav {
background-color: #333333;
color: #6D6D6D;
padding-left: 30px;
padding-top: 20px;
white-space: nowrap;
}

.nav a {
color: #6D6D6D;
text-decoration: none;
}

.copyright {
font-size: 12px;
}


</style>