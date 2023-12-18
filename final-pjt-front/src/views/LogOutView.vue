<template>
  <div>
    <p>..</p>
  </div>
</template>

<script>
import { useAuthStore } from '../stores/auth.js'; // 경로는 auth store의 위치에 따라 다를 수 있습니다.
import { useRouter } from 'vue-router';
import HomeView from '../views/HomeView.vue';

export default {
  setup() {
    const authStore = useAuthStore();
    const router = useRouter();

    const logout = async () => {
      await authStore.logOut();
      router.push({ name: 'HomeView' });
      alert(`조심히 가십시오.`)

    }

    logout(); // 컴포넌트가 로드될 때 로그아웃 함수를 호출합니다.

    return {};
  }
};
</script>

<style>
  /* Your styles here */
</style>
