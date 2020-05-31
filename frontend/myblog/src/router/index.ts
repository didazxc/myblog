import Vue from "vue";
import VueRouter, { Route, RouteConfig } from "vue-router";
import axios from "axios";
import store from "../store";
import Layout from "../views/Layout.vue";
import Login from "../views/Login.vue";

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  {
    path: "/login",
    name: "login",
    component: Login
  },
  {
    path: "/",
    redirect: "/home",
    component: Layout,
    meta: {
      requireAuth: true
    },
    children: [
      {
        path: "/home",
        components: require("../views/Home.vue"),
        meta: {
          title: "主页",
          fa: "fa-home"
        }
      },
      {
        path: "/about",
        component: () =>
          import(/* webpackChunkName: "about" */ "../views/About.vue")
      }
    ]
  }
];

const router = new VueRouter({
  routes
});

// axios拦截器，401状态时跳转登录页并清除token
axios.interceptors.response.use(
  response => {
    //在header检测新token
    return response;
  },
  error => {
    if (error.response) {
      switch (error.response.status) {
        case 401:
          store.commit("delToken");
          router.push("/login");
      }
    }
    return Promise.reject(error);
  }
);

//登陆验证
router.beforeEach((to: Route, from: Route, next: Function) => {
  if (to.matched.some(record => record.meta.requireAuth)) {
    const token = store.state.token;
    if (token !== null) {
      axios.defaults.auth = {
        username: token,
        password: ""
      };
      next();
    } else {
      next("/login");
    }
  } else {
    next();
  }
});

export default router;
