<template>
  <div class="title">
    <h1>로그인</h1>
  </div>
  <div class="container">
    <div>
      <form @submit.prevent="onSubmit">
        <div>
          <label for="username">아이디</label>
          <input class="form-control" type="text" id="username" v-model="username">
        </div>
        <div>
          <label for="password">비밀번호</label>
          <input class="form-control" type="password" id="password" v-model="password">
        </div>
        <button type="submit">로그인</button>
      </form>
    </div>
    
  </div>
</template>

<script setup>
import { useAuthStore } from '@/stores/auth';
import { ref } from 'vue';
import { useRouter } from 'vue-router';


const store = useAuthStore();
const router = useRouter();
const username = ref('');
const password = ref('');

const onSubmit = async () => {
  const res = await store.logIn({username: username.value,password: password.value });
  console.log(res)
  
  // res가 undefined인 경우에 대한 처리를 제거하고,
  // res.status가 200 또는 201인 경우에만 로그인 성공으로 판단
  if (res && (res.status === 200 || res.status === 201)) {
    // 로그인 성공
    router.push('/');
    console.log('로그인 성공')
    alert(`${username.value}님 어서오십시오.`)
  } else {
    // 로그인 실패
    console.log('로그인 실패')
    alert('로그인에 실패했습니다.');
  }
};
</script>

<style scoped>
body {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-color: #f5f6f7;
}

.title {
  margin-top: 200px;
  margin-bottom: 30px;
}

.container {
  margin-bottom: 300px;
  display: flex;
  justify-content: center;
  align-items: center;
}

form {
  width: 300px;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  background-color: white;
}

h1 {
  text-align: center;
  color: #333;
  font-size: 30px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input {
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
}

input:focus, select:focus {
  border-color: #FFD700 !important; /* 카카오 노란색 */
  box-shadow: 0 0 0 0.2rem rgba(255, 235, 0, 0.25) !important; /* 카카오 노란색으로 약간 흐릿한 테두리 효과 */
}

button {
  width: 100%;
  padding: 10px;
  border: none;
  border-radius: 5px;
  background-color: #ffeb00;
  color: black;
  margin-top: 20px;
}

button:hover {
  background-color: #FFD700; /* 호버 효과로 색상을 약간 어둡게 변경 */
}
</style>
