import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignUpView from '../views/SignUpView.vue'
import LogInView from '../views/LogInView.vue'
import LogOutView from '../views/LogOutView.vue'
import UserProfile from '../views/UserProfile.vue'
import UpdateUserInfo from '../../components/UpdateUserInfo.vue'
import { useAuthStore } from '../stores/auth.js'

import SelectDepsitView from '../views/Deposit/SelectDepsitView.vue'
import SaveDepositTermView from '../views/Deposit/SaveDepositTermView.vue'
import InterestTypeView from '../views/Deposit/InterestTypeView.vue'
import RecommendProductsView from '../views/Deposit/RecommendProductsView.vue'
import DepositDetailView from '../views/Deposit/DepositDetailView.vue'
import DepositListView from '../views/Deposit/DepositListView.vue'



const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'HomeView',
      component: HomeView
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView,
      beforeEnter: (to, from, next) => {
        const store = useAuthStore()
        if (store.isAuthenticated) {
          next({ name: 'HomeView' });  // 로그인이 된 상태에서 회원가입 페이지로 접근하려고 할 때 메인 페이지로 리다이렉트
        } else {
          next();  // 로그인이 안 된 상태에서 회원가입 페이지로 접근하려고 할 때 이동을 허용
        }
      }
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView,
      beforeEnter: (to, from) => {
        const store = useAuthStore()
        if (from.name !== 'HomeView' && store.isAuthenticated) {
          return false
        }
      }
    },
    {
      path: '/logout',
      name: 'LogOutView',
      component: LogOutView
    },
    
    {
      path: '/profile',
      name: 'UserProfile',
      component: UserProfile,
      beforeEnter: (to, from, next) => {
        const authStore = useAuthStore()
        if (authStore.isAuthenticated.value) {
          next({ name: 'LogInView' });  // 로그인이 안 된 상태에서 프로필 페이지로 접근하려고 할 때 로그인 페이지로 리다이렉트
        } else {
          next();  // 로그인이 된 상태에서 프로필 페이지로 접근하려고 할 때 이동을 허용
        }
      }
    },
    {
      path: '/profile/updateuserinfo',  // 경로는 원하는 대로 설정하세요.
      name: 'UpdateUserInfo',
      component: UpdateUserInfo,
    },

    {
      path: '/selectdepsit',
      name: 'SelectDepsitView',
      component: SelectDepsitView,
      beforeEnter: (to, from, next) => {
        const authStore = useAuthStore()
        if (authStore.isAuthenticated.value) {
          next({ name: 'LogInView' });  // 로그인이 안 된 상태에서 프로필 페이지로 접근하려고 할 때 로그인 페이지로 리다이렉트
        } else {
          next();  // 로그인이 된 상태에서 프로필 페이지로 접근하려고 할 때 이동을 허용
        }
      }
    },
    {
      path: '/savedepositterm',
      name: 'SaveDepositTermView',
      component: SaveDepositTermView,
    },
    {
      path: '/interesttype',
      name: 'InterestTypeView',
      component: InterestTypeView
    },
    {
      path: '/recommendproducts',
      name: 'RecommendProductsView',
      component: RecommendProductsView
    },
    {
      path: '/depositdetail/:productCode',
      name: 'DepositDetailView',
      component: DepositDetailView,
      props: true
    },
    {
      path: '/depositlist',
      name: 'DepositListView',
      component: DepositListView,
      props: true
    },
  ],
  scrollBehavior() {
    // 페이지 이동 시 스크롤을 맨 위로 이동
    return { top: 0 };
  },
})

router.beforeEach((to, from) => {
  const store = useAuthStore()
  const publicPages = ['LogInView', 'SignUpView', 'UserProfile', 'HomeView', 'SelectDepsitView', 'SaveDepositTermView', 'InterestTypeView', 'RecommendProductsView', 'DepositDetailView', 'DepositListView'];
  if (publicPages.includes(to.name) || store.isAuthenticated) {
    return true
  }
  return { name: 'LogInView' } // 로그인이 필요한 페이지를 요청했지만 로그인이 안된 상태일 때 로그인 뷰로 리디렉션
})


export default router
