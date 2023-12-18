UpdateUserInfo.vue
<template>
  <div>
    <div class="title">
      <p>비밀번호 변경</p>
    </div>
    <div class="container">
      <form @submit.prevent="updateUserInfo">

        <div>
          <label>
            비밀번호
          </label>
          <input class="form-control" v-model="form.password" type="password" required>
        </div>
        
        <div>
          <label>
            비밀번호 확인
          </label>
          <input class="form-control" v-model="form.passwordConfirm" type="password" required>
        </div>

        <div>
          <button type="submit">비밀번호 변경</button>
        </div>

      </form>
    </div>
  </div>
</template>

<script>
import { useAuthStore } from '@/stores/auth.js'; // 경로는 auth store의 위치에 따라 다를 수 있습니다.
import { useRouter } from 'vue-router';
import { ref } from 'vue';

export default {
  setup() {
    const authStore = useAuthStore();
    const router = useRouter();
    const form = ref({
      password: '',
      passwordConfirm: '',
    });

    const updateUserInfo = async () => {
      if (form.value.password !== form.value.passwordConfirm) {
        alert('비밀번호와 비밀번호 확인이 일치하지 않습니다.');
        return;
      }

      try {
        const response = await authStore.updateUserInfo(form.value.password);
        alert('비밀번호가 정상적으로 변경되었습니다. \n 재로그인 해주시길 바랍니다.');

        await authStore.logOut();
    
        router.push({ name: 'LogInView' });
        
      } catch (error) {
        // API 호출에 실패하면 사용자에게 메시지를 표시하거나 다른 적절한 조치를 취합니다.
        console.error(error);
        alert('비밀번호 변경에 실패하였습니다.');
      }
    };

    return {
      form,
      updateUserInfo,
    };
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
  font-size: 30px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.container {
  display: flex;
  flex-direction: column;
  width: 300px;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  background-color: white;
  margin-bottom: 300px;
  margin-top: 20px;
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

.container div label {
  margin-right: 10px;
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
    background-color: #ffd700;
}

</style>