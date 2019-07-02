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
        </ul>
      </div>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script>
import bus from "./bus";
export default {
  name: "app",
  components: {},
  data() {
    return {
      show: true
    };
  },
  methods: {
    logout: function() {
      localStorage.removeItem("Token");
      localStorage.removeItem("Username");
      this.show = true;
      this.$router.push("/");
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
