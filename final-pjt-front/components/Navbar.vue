<template>
  <header>
    <nav class="navbar fixed-top navbar-expand-lg navbar-light bg-white">
      <div class="container-fluid">
        <RouterLink class="navbar-brand text-dark " :to="{ name: 'HomeView' }" style="font-size:26px;">FINNECT</RouterLink>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav ms-auto text-dark fs-5">
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'HomeView' }">Home</RouterLink>
            </li>
            <li class="nav-item" v-if="!store.isAuthenticated">
              <RouterLink class="nav-link" :to="{ name: 'SignUpView' }">회원가입</RouterLink> 
            </li>
            <li class="nav-item" v-if="!store.isAuthenticated">
              <RouterLink class="nav-link" :to="{ name: 'LogInView' }">로그인</RouterLink> 
            </li>
            <li class="nav-item" v-if="store.isAuthenticated">
              <RouterLink class="nav-link" :to="{ name: 'LogOutView' }">로그아웃</RouterLink> 
            </li>
            <li class="nav-item" v-if="store.isAuthenticated">
              <RouterLink class="nav-link" :to="{ name: 'UserProfile' }">내 정보</RouterLink> 
            </li>
            <li class="nav-item" v-if="store.isAuthenticated">
              <RouterLink class="nav-link" :to="{ name: 'SelectDepsitView' }">상품 추천</RouterLink> 
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'DepositListView' }">전체 상품</RouterLink> 
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
  <RouterView class="router-view" />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { reactive } from 'vue'

const store = reactive(useAuthStore())
</script>

<style scoped>
.navbar {
  margin-bottom: 150px;
}

.navbar-brand {
  font-size: 2em;
}

.router-view {
  padding-top: 60px; 
}

.navbar-nav {
  display: flex;
  flex-direction: row;
}

.navbar-nav .nav-item {
  list-style: none;
  margin-right: 15px; 
  font-size: 1em;
  white-space: nowrap;
}
</style>