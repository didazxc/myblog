import axios from "axios";

export default {
  login(username: string, password: string) {
    axios.defaults.auth = {
      username: username,
      password: password
    };
    return axios.post(process.env.VUE_APP_API_URL + "/auth/login");
  }
};
