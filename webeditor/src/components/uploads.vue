<template>
  <div>
    <div class="jumbotron" v-show="fail">
      <p>
        You have no pastes.
        <router-link to="/add/">
          <i>Click here</i>
        </router-link>to add a new file.
      </p>
    </div>
    <div class="card" v-for="(note,index) in pastes" v-bind:key="index">
      <div class="card-body" style="width:35rem;">
        <h4 class="card-head text-left w-100 p-3">
          <p>{{ note.filename }}</p>
        </h4>
        <hr class="my 4" />
        <div class="card-body text-left w-100" style="padding-top: 0cm;">
          <p>{{ note.notes }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import bus from "../bus";
export default {
  name: "app",
  components: {},
  data() {
    return {
      pastes: [],
      fail: false
    };
  },
  methods: {},
  mounted() {
    const config = {
      headers: {
        Authorization: "Token " + localStorage.getItem("Token")
      }
    };
    const axios = require("axios");
    var vm = this;
    axios
      .get("http://127.0.0.1:8000/text/notes/", config)
      .then(function(response) {
        vm.pastes = response.data.filter(function(obj) {
          return obj.username == localStorage.getItem("Username");
        });
        if (vm.pastes.length == 0) vm.fail = true;
      });
  }
};
</script>
<style>
</style>
