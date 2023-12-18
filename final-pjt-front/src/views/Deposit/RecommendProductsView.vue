<template>
  <div class="container text-center py-5">

    <div class="header row justify-content-between align-items-center">
      <div class="col-6 col-md-5 text-left">
        <h1 class="title m-0">추천 금융 상품</h1>
      </div>
      <div class="col-6 col-md-2 text-right">
        <router-link to="/selectdepsit" class="back-link">상품추천</router-link>
      </div>
    </div>

    <div v-if="depositProducts.length > 0" class="row justify-content-center">
      <div v-for="product in depositProducts" :key="product.product_code" @click="goToDetail(product.product_code)" class="col-lg-4 col-md-6 py-3 d-flex justify-content-center">
        <div class="product-card card">
          <div class="card-body d-flex flex-column justify-content-center align-items-center">
            <h2 class="product-company">{{ product.company_name }}</h2>
            <p class="product-name">{{ product.product_name }}</p>
          </div>
        </div>
      </div>
    </div>

    <div v-else class="no-match">{{ noMatchMessage }}</div>

  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useStore } from '@/stores/counter';
import { useRouter } from 'vue-router'
import axios from 'axios';

const store = useStore()
const products = ref([])
const depositProducts = ref([])
const router = useRouter()
const noMatchMessage = ref('')

onMounted(async () => {
  const response_options = await axios.get('http://127.0.0.1:8000/deposits/recommend_products_options/')
  const apiProductsOptions = response_options.data

  products.value = apiProductsOptions.filter(apiProductsOptions =>
  apiProductsOptions.period === store.period &&
  (store.interest_type === '전체' || apiProductsOptions.interest_type === store.interest_type)
  )
  products.value.sort((a, b) => b.interest_rate - a.interest_rate)
  if (products.value.length > 3) {
    products.value = products.value.slice(0, 3)
  }

  const response_product = await axios.get('http://127.0.0.1:8000/deposits/recommend_products/')
  const apiProducts = response_product.data
  
  
  for (const product of products.value) {
    const matchedProduct = apiProducts.find(apiProduct => 
    apiProduct.product_code === product.product_code
    )
    
    if (matchedProduct && store.product === matchedProduct.product_type) {
      depositProducts.value.push(matchedProduct)
    }
  }  
  console.log(products)

  // 일치하는 상품이 없을 때 메시지 설정
  if (depositProducts.value.length === 0) {
    noMatchMessage.value = '일치하는 상품이 없습니다.'; 
  }
  
})


const goToDetail = (productCode) => {
  if (productCode) {
    router.push({ name: 'DepositDetailView', params: { productCode } })
  } else {
    console.log('productCode is missing')
  }
}


</script>

<style scoped>
.container {
  font-family: 'JalnanGothic', sans-serif;
  margin-top: 100px;
  margin-bottom: 300px;
}

.title {
  font-size: 2.5em;
  white-space: nowrap;
}

.back-link { 
  font-size: 1.2em; 
}

.product-card {
  width: 250px;
  height: 150px;
  background-color: #ffd700;
  color: black;
  transition: background-color 0.3s ease-in-out;
}

.product-card:hover {
  background-color: #d8b401;
}

.product-company {
  font-size: 1.5em;
}

.no-match {
  margin-top: 200px;
  font-size: 2em;
  color: red;
}
</style>