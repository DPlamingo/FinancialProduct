<template>
  <div class="title">
    <p>나의 정보</p>
  </div>
  <div class="container">
    <div v-if="user">
      <div class="info-item">
        <div>
          <p>아이디</p>
        </div>
        <div>
          {{ user.username }}
        </div>
      </div>

      <div class="info-item">
        <div>
          <p>이름</p>
        </div>
        <div>
          {{ user.first_name }}
        </div>
      </div>

      <div class="info-item">
        <div>
          <p>이메일</p>
        </div>
        <div>
          {{ user.email }}
        </div>
      </div>
      
      <div class="info-item">
        <div>
          <p>성별</p>
        </div>
        <div>
          {{ user.gender }}
        </div>
      </div>
      
      <div class="info-item">
        <div>
          <p>생년월일</p>
        </div>
        <div>
          {{ user.birth_date }}
        </div>
      </div>
    
    </div>
    <div>
      <button class="btn" @click="goToUpdatePage">비밀번호 변경</button>  <!-- 이 버튼을 누르면 정보 수정 페이지로 이동합니다. -->
      <button class="delete-btn" @click="deleteUser">회원 탈퇴</button>
    </div>
  </div>
</template>

<script>
import { useAuthStore } from '@/stores/auth.js'; // 경로는 auth store의 위치에 따라 다를 수 있습니다.
import { useRouter } from 'vue-router';
import { watchEffect, ref } from 'vue';


export default {
  setup() {
    const authStore = useAuthStore();
    const router = useRouter();
    let user = ref(null); // reactive reference


    const getUserInfo = async () => {
      try {
        await authStore.getUserInfo();
        user.value = authStore.user; // update user
      } catch (error) {
        // API 호출에 실패하면 사용자에게 메시지를 표시하거나 다른 적절한 조치를 취합니다.
      }
    };


    const goToUpdatePage = () => {
      router.push('/profile/updateuserinfo');  // 정보 수정 페이지의 경로를 적절하게 설정하세요.
    };

    
    // 회원탈퇴
    const deleteUser = async () => {
      try {
        await authStore.deleteUser();
      } catch (error) {
        console.log('========')
        console.log(error)
        // API 호출에 실패하면 사용자에게 메시지를 표시하거나 다른 적절한 조치를 취합니다.
      }
    };


    watchEffect(() => {
      user.value = authStore.user; // update user when authStore.user changes
    });
    
    return {
      user,
      goToUpdatePage,
      deleteUser,
      getUserInfo,
    }
  },
  

  created() {
    this.getUserInfo();  // 컴포넌트가 생성될 때 사용자 정보를 가져옵니다.
  }
};
</script >

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
  font-size: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
}


h1 {
  margin-bottom: 20px;
  text-align: center;
  color: #333;
}

.container {
  display: flex;
  flex-direction: column;
  /* justify-content: center; */
  /* align-items: center; */
  width: 300px;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  background-color: white;
  margin-bottom: 300px;
  margin-top: 20px;
  position: relative;
}

.info-item {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}

.container div p {
    margin: 0;
    color: #333;
  }

.btn {
  width: 100%;
  padding: 10px;
  border: none;
  border-radius: 5px;
  background-color: #ffeb00;
  color: black;
  margin-top: 20px;
  margin-bottom: 40px;
}

.btn:hover {
    background-color: #ffd700;
}

.delete-btn {
  width: auto;
  padding: 5px;
  margin-top: 20px;
  margin-left: auto; 
  color: red;  
  font-size: 12px; 
  background-color: transparent; 
  border: none;
  position: absolute;
  right: 20px; 
  bottom: 10px;
}

</style>
