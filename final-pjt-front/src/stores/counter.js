import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'


export const useStore = defineStore({
  id: 'mainStore',
  state: () => ({
    token: null,
    articles: [],
    comments: [],
    depositData: null,
    currentDetail: null,
    userInfo: null,
    product: '', // 금융상품 추천 
    period: 0 // 금융상품 추천 
  }),
  getters: {
    isLogin(state){
      return state.token ? true : false
    },
  },
  actions: {
    // async getArticles(){
    //   const response = await axios.get(`${API_URL}/articles/`)
    //   this.articles = response.data
    // },
    // async getComments(){
    //   const response = await axios.get(`${API_URL}/articles/comments/`)
    //   this.comments = response.data
    // },
    // async signUp(payload) {
    //   const response = await axios.post('http://127.0.0.1:8000/accounts/signup/', payload)
    //   this.token = response.data.key
    // },
    // async login(payload){
    //   const response = await axios.post('http://127.0.0.1:8000/accounts/login/', payload)
    //   this.token = response.data.key
    // },
    // async getUserInfo() {
    //   const response = await axios.get('http://127.0.0.1:8000/accounts/user/', {
    //     headers: {
    //       Authorization: `Token ${this.token}`
    //     }
    //   })
    //   this.userInfo = response.data
    // },
    // logOut() {
    //   this.token = null
    // },
    // 금융상품 추천 ==============
    selectProduct(product) {  
      this.product = product
    },
    enterPeriod(period) {     
      this.period = period
    },
    selectInterestType(interest_type) { 
      this.interest_type = interest_type
    },
    resetState() {  
      this.product = null
    },
    
    // ===========================
  },



})
