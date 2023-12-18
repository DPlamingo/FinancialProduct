<template>
    <div class="deposit-list-view">
      <div class="loading-content" v-if="isLoading">
        <div class="spinner-border" role="status">
          <span class="visually-hidden">Loading...</span>
          <!-- <img class="loading-img" :src="loadingImage" alt="Loading..."> -->
        </div>
      </div>
      <div class="depoosit-container" v-else>
        <div class="header">
          <h1>상품 전체 목록</h1>
          <router-link to="/selectdepsit">상품추천</router-link>
        </div>
        <div>
          <div class="product-card" v-for="(product, index) in products" :key="index">
            <p>{{ product.fin_prdt_nm }}</p>
            <p>{{ product.kor_co_nm }}</p>
            <button class="detail-button" @click="goToDetail(product.fin_prdt_cd)">상세페이지</button>
          </div>
        </div>
      </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router'
import axios from 'axios';
import loadingImage from '@/assets/images/loading.gif'

const products = ref([]);
const router = useRouter()
const isLoading = ref(false);

onMounted(async () => {
  isLoading.value = true;
  try {
    const response = await axios.get('http://127.0.0.1:8000/deposits/save');
    products.value = response.data;
  } catch (error) {
    console.error(error);
  } finally {
    isLoading.value = false;
  }
});

const goToDetail = (productCode) => {
  if (productCode) {
    router.push({ name: 'DepositDetailView', params: { productCode } })
  } else {
    console.log('productCode is missing')
  }
}

</script>

<style scoped>
.deposit-list-view {
  height: auto;
  background-color: #fcfcfc;
}

.loading-content {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.loading-img {
  width: 100px;
  height: 100px;
}

.depoosit-container{
  margin: 100px;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.header h1 {
  font-size: 2em;
}

.product-card {
  border-radius: 10px;
  padding: 20px;
  margin-bottom: 20px;
  background-color: #fff;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s ease-in-out;
}

.product-card:hover {
  box-shadow: 0 3px 20px rgba(0, 0, 0, 0.15);
}

.product-card h2 {
  margin-top: 0;
  color: #333;
}

.product-card p {
  color: #666;
}

.detail-button {
  background-color: #fee500; 
  color: #382200; 
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease-in-out;
}

.detail-button:hover {
  background-color: #fad200;
}

</style>