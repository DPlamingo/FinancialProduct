<template>
    <div class="detail-view">
      <div class="header d-flex justify-content-between align-items-center">
        <h1>상세페이지</h1>
        <router-link to="/selectdepsit">상품추천</router-link>
      </div>
      <div class="detail-card" v-if="product.deposit_detail && product.deposit_detail_options">
        
        <div class="detail-name">
          <div>
            <p>은행명</p>
          </div>
          <div>
            <p>상품명</p>
          </div>
          <div>
            <p>가입방법</p>
          </div>
          <div>
            <p>이자율</p>
          </div>
          <div>
            <p>가입조건</p>
          </div>
        </div>

        <div class="detail-value">
          <div>
            <p>{{ product.deposit_detail.kor_co_nm }}</p>
          </div>
          <div>
            <p>{{ product.deposit_detail.fin_prdt_nm }}</p>
          </div>
          <div>
            <p>{{ product.deposit_detail.join_way }}</p>
          </div>
          <div>
            <p>{{ product.deposit_detail_options.intr_rate}}</p>
          </div>
          <div>
            <p>{{ product.deposit_detail.etc_note}}</p>
          </div>
        </div>

      </div>
      <button class="back-button" @click="goToDepositList">전체 상품 보기</button>
      <!-- <button @click="like">좋아요</button> -->
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useAuthStore  } from '@/stores/auth';
import { useRoute, useRouter, } from 'vue-router';
import axios from 'axios';

const store = useAuthStore ();

const route = useRoute();
const router = useRouter();
const product = ref([]);
console.log(store.user)
onMounted(async () => {
  const productCode = route.params.productCode;
  const response = await axios.get(`http://127.0.0.1:8000/deposits/detail/${productCode}/`);
  product.value = response.data;
  // console.log(product.value)
});

const goToDepositList = () => {
  router.push('/depositlist');
};

// 좋아요 기능
// const like = async () => {
//   try {
//     // 좋아요 정보를 저장하는 API에 요청을 보냅니다.
//     // 이때, 사용자 ID와 상품 코드를 함께 전송해야 합니다.
//     // 사용자 ID는 로그인 세션 등에서 가져올 수 있습니다.
//     // 상품 코드는 현재 페이지의 URL에서 가져올 수 있습니다.
//     const response = await axios.post('http://127.0.0.1:8000/accounts/likes/', {
//       user_id: store.user,
//       product_code: route.params,
//     },{
//     headers: {
//      Authorization: `Token ${store.token}`  // 'Authorization' 헤더를 추가합니다.
//     }
//     });


//     if (response.status === 200 || response.status === 201) {
//       alert('좋아요를 눌렀습니다.');
//     } else {
//       alert('좋아요를 누르는 데 실패했습니다.');
//     }
//   } catch (error) {
//     console.error(error);
//     alert('좋아요를 누르는 데 실패했습니다.');
//   }
// };

</script>

<style scoped>
.detail-view {
height: auto;
margin-top: 100px;
margin-bottom: 300px;
}

.header {
  padding: 20px;
  font-size: 1.5em;
}

.header h1 {
  font-size: 2em;
}

.detail-card {
  display: flex;
  background-color: #fff;
  border-radius: 10px;
  padding: 20px;
  margin: 20px ;
  box-shadow: 0 5px 5px rgba(0, 0, 0, 0.1);
  /* max-width: 800px; */
}

.detail-name {
  width: 10%; /* 각각의 너비를 50%로 설정 */
  min-width: 100px;
}

.detail-value {
  width: 90%;
}

.detail-value p {
  width: 100%;
}

.detail-card p {
  margin-bottom: 10px;
  color: #333;
}

.back-button {
  background-color: #fee500; /* Kakao Yellow */
  color: #382200; /* Kakao Brown */
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease-in-out;
  margin: 20px;
}

.back-button:hover {
  background-color: #fad200;
}

</style>