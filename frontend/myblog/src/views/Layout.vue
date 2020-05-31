<template>
  <el-container direction="vertical">
    <el-container>
      <Aside
        :collapse.sync="isAsideCollapse"
        :menus="menus"
        :default-active="menuKey"
      />
      <el-container id="content" direction="vertical">
        <Header :isAsideCollapse.sync="isAsideCollapse" :title="title">
          <el-dropdown :hide-on-click="false" @command="handleCommand">
            <el-avatar> {{ userName }}</el-avatar>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item icon="el-icon-switch-button" command="logout"
                >登出</el-dropdown-item
              >
            </el-dropdown-menu>
          </el-dropdown>
        </Header>
        <div id="main"><router-view /></div>
        <div class="footer">
          <span
            >copyright &copy; didazxc. All Rights
            Reserved</span
          >
        </div>
      </el-container>
    </el-container>
  </el-container>
</template>

<script>
  import Aside from "../components/layout/Aside";
  import Header from "../components/layout/Header";

  export default {
  name: "Layout",
  components: {
    Aside,
    Header
  },
  data() {
    return {
      menuKey: "/home",
      title: "",
      isAsideCollapse: false
    };
  },
  computed: {
    menus() {
      function flatRoutes(routes,fa=''){
        return routes.flatMap(r=>{
          if(r.children){
            const path = r.path.slice(0,1)==='/'?r.path:fa+'/'+r.path;
            return flatRoutes(r.children,path);
          }else{
            if(r.meta){
              const path = r.path.slice(0,1)==='/'?r.path:fa+'/'+r.path;
              r.meta.index = path;
              return [r.meta];
            }else{
              return [];
            }
          }
        })
      }
      const dic = {};
      flatRoutes(this.$router.options.routes).forEach(v=>{
        dic[v.index]=v;
      });
      return dic;
    },
    userName() {
      const user = this.$store.state.user;
      if (user !== null) return user.name;
      else return "noLogin";
    }
  },
  methods: {
    handleCommand(cmd) {
      switch (cmd) {
        case "logout":
          this.$store.dispatch("logout");
          break;
      }
    },
    setMenuKey(value) {
      this.menuKey = value;
      this.title = this.menus[value].title;
    }
  },
  watch: {
    "$route.path": function(newVal) {
      this.setMenuKey(newVal);
    }
  },
  mounted() {
    this.setMenuKey(this.$route.path);
  }
};
</script>

<style>
body {
  margin: 0;
}
#content {
  height: 100vh;
  overflow: hidden;
}
#main {
  height: 100%;
  overflow: scroll;
  padding: 20px;
}
#main::-webkit-scrollbar {
  display: none;
}
.footer {
  padding: 0 10px;
  text-align: right;
  font-size: 12px;
  background-color: #333;
  color: white;
}
</style>
