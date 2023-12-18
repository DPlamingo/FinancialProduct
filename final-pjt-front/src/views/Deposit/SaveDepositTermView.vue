<template>
    <div class="container-fluid text-center py-5">
      
      <div class="header row justify-content-between align-items-center">
        <div class="col-6 col-md-5 text-left">
          <h1 class="title m-0">저축 예정 기간</h1>
        </div>
        <div class="col-6 col-md-2 text-right">
          <router-link to="/selectdepsit" class="back-link">상품추천</router-link>
        </div>
      </div>

      <div class="row">
        <div class="col-lg-3 col-md-6 py-3">
            <button @click="enterPeriod(6)" class="period_button btn btn-block">6개월</button>
        </div>
        <div class="col-lg-3 col-md-6 py-3">
            <button @click="enterPeriod(12)" class="period_button btn btn-block">12개월</button>
        </div>
        <div class="col-lg-3 col-md-6 py-3">
            <button @click="enterPeriod(24)" class="period_button btn btn-block">24개월</button>
        </div>
        <div class="col-lg-3 col-md-6 py-3">
            <button @click="enterPeriod(36)" class="period_button btn btn-block">36개월</button>
        </div>
      </div>

    </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { useStore } from '@/stores/counter'

const store = useStore()
const router = useRouter()

const enterPeriod = (period) => {
  store.enterPeriod(period)
  router.push('/interesttype')
}
// console.log(store.product)


</script>

<style scoped>
.container-fluid {
  font-family: 'JalnanGothic', sans-serif;
  margin-top: 100px;
  margin-bottom: 250px;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.title {
  font-size: 2.5em;
  white-space: nowrap;
}

.back-link { 
  font-size: 1.2em; 
}

/* .button-container {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
  width: 100%;
} */

.period_button {
  width: 200px;
  color: #382200;
  border: none;
  border-radius: 10px;
  background-color: #ffd700;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s ease-in-out;
  min-height: 200px;
}
.period_button:hover {
  background-color: #d8b401;
  box-shadow: 0 3px 20px rgba(0, 0, 0, 0.15);
}

</style>