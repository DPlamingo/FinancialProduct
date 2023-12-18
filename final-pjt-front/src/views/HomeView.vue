<template>
  <div class="home">
    <!--첫 화면 (소개글) -->
    <div class="main-opening">
      <h1 class="fw-bold">"손쉽게 금융하다"</h1>
    </div>


    <!-- 설명글 -->
    <div class="main-description row d-flex flex-column align-items-center justify-content-center">
      <div class="description-img col">
        <img :src="finnectDescriptionImg" alt="그림">
      </div>
      <div class="description col">
        <p class="">
          여러 은행의 예금, 적금 상품을 <br>
          한번에 조회하고 <br>
          손쉽게 금융상품을 비교하는 서비스, <br>
          Finnect와 함께 해보세요.
        </p>
      </div>
    </div>


    <!-- 예적금 한번에 조회 -->
    <div class="main-productlist row">

      <!-- 왼쪽 -->
      <div class="col-md-6 d-flex flex-column align-items-center justify-content-center">
        <div class="productlist-text1">
          <p>일상의 모든</p>
          <p>예,적금</p>
          <p>한번에 조회</p>
        </div>
        <div class="productlistPhone1">
          <img :src="productlistPhone1" alt="긴 그림">
        </div>
      </div>

      <!-- 오른쪽 -->
      <div class="productlist-right col-md-6 d-flex flex-column justify-content-center align-items-center">
        <div class="productlistPhone2">
          <img :src="productlistPhone2" alt="그림">
        </div>
        <div class="productlist-text2">
          <p>finnect가 제공하는 <br> 금융상품조회를 해보세요.</p>
          <p>다양한 은행의 금융상품들의 <br>자세한 정보를 한번에 볼 수 있어요.</p>
        </div>
        <div class="productlist-link">
          <RouterLink to="/depositlist">예.적금 조회하러 가기</RouterLink>
        </div>
      </div>

    </div>


    <!-- 금융상품 추천 -->
    <div class="main-recommend d-flex flex-column align-items-center justify-content-center">

      <div class="recommend-text1 col">
        <p>내가 원하는 상품의 정보를 선택해서<br> 원하는 금융상품이 있는지 추천 받아 보세요. <br>
        선택한 조건에 따라 조건을 만족하는 <br> 상위 상품들을 보여줘요.</p>
      </div>

      <div class="recommend-img col">
        <img :src="depositRecommendImg" alt="그림">
      </div>

      <div class="recommend-text2 col">
        <p>
          나에게 맞는 <br>예적금 추천받기
        </p>
      </div>

      <div class="recommend-link col">
        <div class="recommend-link-button">
          <RouterLink to="/selectdepsit">추천받으러 가기</RouterLink>
        </div>
      </div>

    </div>


    <!-- 4 -->
    <!-- <div class="bg-black position-relative main-end">
      <h1>메인페이지 END</h1>
    </div> -->

    
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
// import depositMoveImg from '@/assets/images/deposit-move-img.gif'
import depositRecommendImg from '@/assets/images/deposit-recommend.gif'
import productlistPhone1 from '@/assets/images/productlist-phone1.png'
import productlistPhone2 from '@/assets/images/productlist-phone2.png'
import finnectDescriptionImg from '@/assets/images/finnect-description-img.png'

</script>

<style scoped>
.home {
  width: auto;
}

.main-opening {
  background-color: #ffd813;
  display: flex;
  justify-content: center;
  align-items: center;
  height: auto;
}

.main-opening h1 {
  font-size: 60px;
  color: rgb(23, 23, 23);
  margin-top: 500px;
  margin-bottom: 500px;
}



.main-description {
  background-color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  height: auto;
}

.description-img {
  display: flex;
  justify-content: center;
  margin-top: 400px;
  margin-bottom: 50px;
}

.description-img img {
  width: 400px;
  height: auto;
}

.description {
  text-align: center;
  font-size: 30px;
  margin-bottom: 500px;
}

.main-productlist {
  background-color: #FFFFFF;
  display: flex;
  justify-content: space-between;
  height: auto;
  /* margin-bottom: 500px; */
}

.productlist-right {
  min-width: 400px;
}

.productlist-text1 {
  font-size: 40px;
  padding-right: 150px;
  margin-top: 100px;
  margin-bottom: 80px;
  white-space: nowrap;
}

.productlistPhone1 img {
  width: 400px;
  height: auto;
  margin-top: 20px;
  margin-bottom: 100px;
}

.productlistPhone2 img {
  margin-top: 80px;
  margin-bottom: 50px;
  width: 400px;
  height: auto;
}

.productlist-check-text {
  font-size: 20px;
  color: blue;
}

.productlist-text2 {
  /* text-align: center; */
  padding-left: 30px;
  margin-top: 60px;
  margin-bottom: 10px;
  font-size: 20px;
  width: 400px;
}

.productlist-text2 p {
  margin-bottom: 10px;
}

.productlist-link {
  font-size: 20px;
  width: 400px;
  padding-left: 30px;
  margin-bottom: 300px;
}

.productlist-link a {
  text-decoration: none;
}

.main-recommend {
  height: auto;
  background-color: #FEFEFE;
}

.recommend-text1 {
  margin-top: 400px;
  margin-bottom: 400px;
  text-align: center;
  font-size: 30px;
}

.recommend-img {
  margin-bottom: 100px;
}

.recommend-text2 {
  text-align: center;
  font-size: 50px
}

.recommend-link {
  margin-bottom: 800px;
  text-align: center;
}

.recommend-link a {
  text-decoration: none;
  font-size: 20px;
}

</style>