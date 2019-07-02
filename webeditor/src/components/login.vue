<template>
  <div>
    <div class="form-group">
      <label>Username:</label>
      <input v-model="username" class="form-control" placeholder="Enter Username">
      <small id="emailHelp" class="form-text text-muted">This is case sensitive.</small>
    </div>
    <div class="form-group">
      <label>Password:</label>
      <input v-model="password" type="password" class="form-control" placeholder="Password">
    </div>
    <button type="submit" class="btn btn-primary" v-on:click="login">Submit</button>
    <div class="form-group">{{ error }}</div>
  </div>
</template>

<script>
import bus from "../bus";
export default {
  name: "app",
  components: {},
  data() {
    return {
      username: "",
      password: "",
      error: ""
    };
  },
  methods: {
    login: function() {
      var vm = this;
      var body = {
        username: vm.username,
        password: vm.password
      };
      const axios = require("axios");
      axios
        .post("http://127.0.0.1:8000/api/login", body)
        .then(function(response) {
          localStorage.setItem("Token", response.data.token);
          localStorage.setItem("Username", vm.username);
          bus.$emit("logged", false);
          vm.$router.push("/");
        })
        .catch(function(error) {
          vm.error = error;
        });
    }
  }
};
</script>

<style>
</style>
