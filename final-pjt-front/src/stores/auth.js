import axios from 'axios'
import { computed, ref } from 'vue'
import { useRouter } from 'vue-router'
import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', () => {
  const user = ref({})
  const router = useRouter()
  const token = ref('')
  const isAuthenticated = ref(false)
  
  const signUp = async function (username, first_name, gender, birth_date, password1, password2, email) {
    // console.log(username, password1, password2, email)
    // const res = axios({
    //   method: 'post',
    //   url: 'http://127.0.0.1:8000/dj-rest-auth/registration/',
    //   data: {
    //     username : username,
    //     password1 : password1,
    //     password2 : password2,
    //     email : email,
    //   }
    // }).then((res) => {
    //   console.log(res)
    // }).catch((err) => {
    //   console.log(err)
    // })
    try {
      const res = await axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/dj-rest-auth/registration/',
        data: {
          username,
          first_name,
          gender,
          birth_date,
          password1,
          password2,
          email,
        }
      })

      if (res.status === 200||201) {
        // 회원가입 성공
        console.log('회원가입 성공');
        // 여기에 추가 작업을 작성하세요. 예를 들어, 새로운 사용자 정보를 저장하거나 사용자를 인증하는 등의 작업을 수행할 수 있습니다.
      } else {
        // 회원가입 실패
        console.log('회원가입 실패');
      }

      
      token.value = res.data.key
      isAuthenticated.value = true
      localStorage.setItem('auth_token', res.data.key)
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/dj-rest-auth/user/',
        headers: {
          Authorization: `Token ${token.value}`
        }
      })
      user.value = res.data
      router.push({name: 'HomeView'})
      return res;

    } catch (error) {
      // console.error(error)
      return error;

    }
  }

  const logIn = async function ({ username, password }) {
    try {
      const res = await axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/dj-rest-auth/login/',
        data: {
          username,
          password,
        }
      })

      // console.log(res.data) // 응답 체크

      token.value = res.data.key
      isAuthenticated.value = true

      // 로그인 성공 후 토큰을 로컬 스토리지에 저장
      localStorage.setItem('auth_token', res.data.key)

      await axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/dj-rest-auth/user/',
        headers: {
          Authorization: `Token ${token.value}`
        }
      })
      user.value = res.data
      router.push({ name: 'HomeView' })
      return res;
    } catch (error) {
      console.error(error)
      return error;
    }
  }


  // const logOut = function () {
  //   axios({
  //     method: 'post',
  //     url: 'http://127.0.0.1:8000/dj-rest-auth/logout/',
  //     headers: {
  //       Authorization: `Token ${token.value}`
  //     }
  //   })
  //   token.value = ''
  //   user.value = {}
  //   isAuthenticated.value = false

  //   // 로그아웃 시 로컬 스토리지의 토큰 제거
  //   localStorage.removeItem('auth_token')

  //   router.push({ name: 'login' })
  // }

  
  const logOut = async function () {
    try {
      const response = await axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/dj-rest-auth/logout/',
        headers: {
          Authorization: `Token ${token.value}`
        }
      });
  
      if (response.status === 200) { // 로그아웃 API 호출이 성공했을 때의 HTTP 상태 코드를 확인하세요.
        // 로그아웃 성공
        token.value = ''
        user.value = {}
        isAuthenticated.value = false
        localStorage.removeItem('auth_token')
        router.push({ name: 'HomeView' })
      } else {
        // 로그아웃 실패
        console.error('로그아웃에 실패했습니다.');
      }
    } catch (error) {
      console.error(error);
    }
  }


  const getUserInfo = async function () {
    try {
      const res = await axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/accounts/detail/',
        headers: {
          Authorization: `Token ${token.value}`
        }
      })
      user.value = res.data
      return res
    } catch (error) {
      console.error(error)
      throw error 
    }
  }
  

  const updateUserInfo = async function (new_password) {
    try {
      const res = await axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/update/',
        headers: {
          Authorization: `Token ${token.value}`
        },
        data: {
          new_password,
        }
      
      })
      console.log(res)
      user.value = res.data
      return res
    } catch (error) {
      console.error(error)
      throw error 
    }
  }

  const deleteUser = async function () {
    if (window.confirm('정말로 탈퇴하시겠습니까?')) {  
      try {
        const res = await axios({
          method: 'delete',
          url: 'http://127.0.0.1:8000/accounts/user/delete/', // 회원 탈퇴 API 주소를 확인하고, 필요하다면 수정하세요.
          headers: {
            Authorization: `Token ${token.value}`
          }
        });
      
        if (res.status === 204 || 200) { // 서버에서 반환하는 상태 코드에 따라 조건을 수정하세요.
          // 회원 탈퇴 성공
          token.value = '';
          user.value = {};
          isAuthenticated.value = false;
          router.push({ name: 'HomeView' });
          alert('회원 탈퇴하셨습니다.');

        } else {
          // 회원 탈퇴 실패
          console.error('회원 탈퇴에 실패했습니다.');
        }
      } catch (error) {
        console.error(error);
      }
    }
  }
  // 앱 로드 시 로그인 상태 확인
  const loadAuthStatus = function() {
    const savedToken = localStorage.getItem('auth_token')
    if (savedToken) {
      token.value = savedToken
      isAuthenticated.value = true
    }
  }

  loadAuthStatus()

  return {
    signUp, logIn, logOut, getUserInfo, updateUserInfo, deleteUser, 
    user,
    router,
    token,
    isAuthenticated
  }
}, { persist: true })