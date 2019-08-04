<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="collapse navbar-collapse" v-on:logged="show=!show">
        <ul class="navbar-nav">
          <li class="nav-item active">
            <router-link to="/add/">New</router-link>
          </li>
          <li class="nav-item active">
            <router-link to="/upload/">Upload</router-link>
          </li>
          <li class="nav-item active" v-show="!show">
            <router-link to="/previous/">Your Files</router-link>
          </li>
        </ul>
        <ul class="navbar-nav ml-auto">
          <li class="nav-item" v-show="show">
            <router-link to="/login/">Login</router-link>
          </li>
          <li class="nav-item" v-on:registered="show=!show" v-show="show">
            <router-link to="/register/">Register</router-link>
          </li>
          <li class="nav-item">
            <button class="btn btn-danger" v-on:click="logout" v-show="!show">Log Out</button>
          </li>
          <li class="nav-item">
            <button
              v-google-signin-button="clientId"
              class="google-signin-button"
            >Continue with Google</button>
          </li>
        </ul>
      </div>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script>
import bus from "./bus";
import GoogleSignInButton from "vue-google-signin-button-directive";
export default {
  name: "app",
  directives: {
    GoogleSignInButton
  },
  components: {},
  data() {
    return {
      show: true,
      clientId:
        "806142332461-jmaj11anan2s2p7asmjj73e0hl0duda8.apps.googleusercontent.com"
    };
  },
  methods: {
    logout: function() {
      localStorage.removeItem("Token");
      localStorage.removeItem("Username");
      this.show = true;
      this.$router.push("/");
    },
    OnGoogleAuthSuccess(idToken) {
      const axios = require("axios");
      const params = new URLSearchParams();
      params.append("access_token", idToken);
      axios
        .post("http://127.0.0.1:8000/social/google-oauth2/", params)
        .then(function(response) {
          console.log(response);
        });
    },
    OnGoogleAuthFail(error) {
      console.log(error);
    }
  },
  mounted() {
    bus.$on("logged", data => {
      this.show = data;
    });
    bus.$on("registered", data => {
      this.show = data;
    });
  }
};
</script>

<style>
.navbar-nav > li {
  padding-left: 15px;
  padding-right: 15px;
}
</style>
