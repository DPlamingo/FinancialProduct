<template>
  <div class="title">
    <p>회원 가입</p>
  </div>
  <div class="container">
    <form @submit.prevent="onSubmit">
      <div>
        <label for="username">아이디</label>
        <input class="form-control" type="text" id="username" v-model="username">
      </div>
      <div>
        <label for="first_name">이름</label>
        <input class="form-control" type="first_name" id="first_name" v-model="first_name">
      </div>
      <div>
        <label for="password1">비밀번호</label>
        <input class="form-control" type="password" id="password1" v-model="password1">
      </div>
      <div>
        <label for="password2">비밀번호 확인</label>
        <input class="form-control" type="password" id="password2" v-model="password2">
      </div>
      <div>
        <label for="email">E-mail</label>
        <input class="form-control" type="email" id="email" v-model="email">
      </div>
      <div class="form-group">
        <label for="gender">성별</label>
        <select class="form-control" id="gender" v-model="gender">
          <option value="male">남성</option>
          <option value="female">여성</option>
        </select>
      </div>
      <div>
        <label for="birth_date">생년월일</label>
        <input class="form-control" type="date" id="birth_date" v-model="birth_date">
      </div>
      <div class="submit-button">
        <button type="submit">회원 가입</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { useAuthStore } from '@/stores/auth';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const store = useAuthStore();
const username = ref('');
const first_name = ref('');
const gender = ref('');
const birth_date = ref('');

const password1 = ref('');
const password2 = ref('');
const email = ref('');

const router = useRouter();

const onSubmit = async () => {
  if (!username.value || !password1.value || !password2.value || !email.value) {
    alert('모든 필수 항목을 입력해주세요.');
    return;
  }

  try {
    // const { username, password1, password2, Email } = this;
    const res = await store.signUp(username.value, first_name.value, gender.value, birth_date.value, password1.value, password2.value, email.value );
    // const res = await store.signUp({username :username.value, first_name:first_name.value, gender:gender.value, birth_date:birth_date.value, password1:password1.value, password2:password2.value, email:email.value });
    console.log(res)
    console.log(res.data)
    console.log(res.status)
    if (res.status === 200 || res.status === 201) {
      // 회원 가입 성공
      console.log('회원가입 성공')
      alert(`${username.value}님 환영합니다.`)
      router.push('/');
    } else {
      // 회원 가입 실패
      console.log('회원가입 실패')

      alert('회원 가입에 실패했습니다.');
    } 
} catch (error) {
    console.log('오류 발생: ', error);
    alert('중복된 ID거나, E-mail입니다. 다시 시도 해주십시오.');
  }
}; 

</script>

<style scoped>
.title {
  margin-top: 200px;
  text-align: center;
}
.title p {
  font-size: 40px;
}

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin: 50px auto;
  max-width: 600px;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
  background-color: white;
  margin-bottom: 300px;
}

form {
  width: 100%;
}

form div {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 10px;
}

input, select {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-sizing: border-box;
}

input:focus, select:focus {
  border-color: #FFD700 !important; /* 카카오 노란색 */
  box-shadow: 0 0 0 0.2rem rgba(255, 235, 0, 0.25) !important; /* 카카오 노란색으로 약간 흐릿한 테두리 효과 */
}

.submit-button button {
  margin-top: 20px;
  width: 100%;
  padding: 15px;
  border: none;
  border-radius: 5px;
  background-color: #FFE812; /* 카카오뱅크의 주 색상인 노란색 */
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.submit-button button:hover {
  background-color: #FFD700; /* 호버 효과로 색상을 약간 어둡게 변경 */
}
</style>
