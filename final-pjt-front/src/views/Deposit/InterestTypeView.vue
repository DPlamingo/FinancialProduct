<template>
  <div class="container text-center py-5">
    <div class="header d-flex justify-content-between align-items-center">
      <h1 class="title m-0">이자 계산 방식 선택</h1>
      <router-link to="/selectdepsit" class="back-link">상품추천</router-link>
    </div>

    <div class="row">
      <div class="col-lg-4 col-12 py-3">
        <button @click="selectInterestType('전체')" class="button btn btn-block"><h1>전체</h1></button>    
      </div>
      <div class="col-lg-4 col-12 py-3">
        <button @click="selectInterestType('단리')" class="button btn btn-block"><h1>단리</h1></button>
      </div>
      <div class="col-lg-4 col-12 py-3">
        <button @click="selectInterestType('복리')" class="button btn btn-block"><h1>복리</h1></button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { useStore } from '@/stores/counter';

const store = useStore()
const router = useRouter()

const selectInterestType = (interest_type) => {
  store.selectInterestType(interest_type)
  router.push('/recommendproducts') //다음 페이지로 이동
}
// console.log(store.period)

</script>

<style scoped>
.container {
  font-family: 'JalnanGothic', sans-serif;
  margin-top: 100px;
  margin-bottom: 250px;
}

.title {
  font-size: 2.5em;
  white-space: nowrap;
}

.back-link { 
  font-size: 1.2em; 
}

.button {
  width: 200px;
  height: 200px;
  background-color: #ffd700;
  color: black;
  transition: background-color 0.3s ease-in-out;
}

.button h1 {
  font-size: 1.5em;
}

.button:hover {
  background-color: #d8b401;
}
</style>