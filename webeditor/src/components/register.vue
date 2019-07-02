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
    <button type="submit" class="btn btn-primary" v-on:click="push">Register</button>
    <div class="form-group">{{ error }}</div>
  </div>
</template>

<script>
import bus from "../bus.js";
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
    push: function() {
      var vm = this;
      const params = new URLSearchParams();
      params.append("username", vm.username);
      params.append("password", vm.password);
      const axios = require("axios");
      const config = {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded"
        }
      };
      axios
        .post("http://127.0.0.1:8000/api/register", params, config)
        .then(function(response) {
          localStorage.setItem("Token", response.data.token);
          localStorage.setItem("Username", vm.username);
          bus.$emit("registered", false);
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