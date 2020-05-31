<template>
  <el-row
    :gutter="10"
    style="display: flex;align-items: center;justify-content: center;min-height:80vh;overflow: hidden;"
  >
    <el-col
      :xs="{ span: 20 }"
      :sm="{ span: 12 }"
      :md="{ span: 8 }"
      :lg="{ span: 8 }"
      :xl="{ span: 6 }"
    >
      <el-card>
        <el-form :model="form">
          <el-form-item label="用户" prop="name">
            <el-input v-model.number="form.username" />
          </el-form-item>
          <el-form-item label="密码" prop="pass">
            <el-input
              type="password"
              v-model="form.password"
              autocomplete="off"
            />
          </el-form-item>
          <el-form-item>
            <el-button
              v-loading.fullscreen.lock="loading"
              type="primary"
              @click="submitForm"
              >提交</el-button
            >
          </el-form-item>
        </el-form>
      </el-card>
    </el-col>
  </el-row>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      loading: false,
      form: {
        username: null,
        password: null
      }
    };
  },
  computed: {
    token() {
      return this.$store.state.token;
    }
  },
  methods: {
    submitForm() {
      this.loading = true;
      this.$store
        .dispatch("login", this.form)
        .then(res => {
          this.loading = false;
          this.$router.push("/");
        })
        .catch(res => {
          this.loading = false;
          this.$message({ type: "error", message: "登陆失败，请重试" });
        });
    }
  },
  mounted() {
    if (this.$store.state.token) {
      this.$router.push("/");
    }
  }
};
</script>

<style scoped></style>
