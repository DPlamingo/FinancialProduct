<template>
  <div class="container text-center">
      <div>
        <h1 class="title">금융상품 선택</h1>
      </div>
      <div class="row justify-content-center">
        <div class="col-sm-12 col-md-6">
          <button @click="selectProduct('예금')" class="btn btn-warning deposit_button">예금</button>
        </div>
        <div class="col-sm-12 col-md-6">
          <button @click="selectProduct('적금')" class="btn btn-warning deposit_button">적금</button>
        </div>
      </div>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { useStore } from '@/stores/counter';

const store = useStore()
const router = useRouter()

const selectProduct = (product) => {
  store.selectProduct(product)
  router.push('/savedepositterm')
}

</script>


<style scoped>
.container {
  margin-top: 150px;
  margin-bottom: 300px;
}

.title {
  padding: 20px; /* 제목 패딩 */
  font-size: 2.5em; /* 제목 크기 */
}

.deposit_button {
  margin: 50px;
  width: 300px;
  height: 300px;
  font-size: 2em;
  color: black; /* 텍스트 색상 */
  border: none; /* 테두리 제거 */
  border-radius: 10px; /* 둥근 모서리 */
  background-color: #ffd700; /* 카카오뱅크의 대표 색상 */
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s ease-in-out;
}
.deposit_button:hover {
  background-color: #e5bf03;
  box-shadow: 0 3px 20px rgba(0, 0, 0, 0.15);
}
</style>