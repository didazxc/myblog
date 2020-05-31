import Vue from "vue";
import Vuex from "vuex";
import AuthApi from "../api/auth";
import router from "@/router";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    token: localStorage.token ? localStorage.token : null,
    user: localStorage.user ? JSON.parse(localStorage.user) : null
  },
  mutations: {
    setToken(state, token) {
      state.token = token;
      localStorage.token = token;
    },
    delToken(state) {
      state.token = null;
      localStorage.clear();
    },
    setUser(state, user) {
      state.user = user;
      localStorage.user = JSON.stringify(user);
    }
  },
  actions: {
    login(context, form) {
      return AuthApi.login(form.username, form.password).then(res => {
        context.commit("setToken", res.data.token);
        context.commit("setUser", res.data.user);
        //context.commit("setProject", null);
      });
    },
    logout(context) {
      context.commit("delToken");
      router.push("/login");
    }
  },
  modules: {}
});
