<template>
  <div class="jumbotron">
    <uploadbtn @file-update="update"></uploadbtn>
    <label for="exampleInputEmail1">Your Text:</label>
    <textarea v-model="text" rows="30" cols="50"></textarea>
    <button class="btn btn-success" v-on:click="download">Download</button>
    <button class="btn btn-primary" v-on:click="push" v-show="!see">Push to Database</button>
  </div>
</template>

<script>
const axios = require("axios");
import UploadButton from "vuetify-upload-button";
import bus from "../bus";
export default {
  name: "app",
  components: {
    uploadbtn: UploadButton
  },
  data() {
    return {
      text: "",
      type: "",
      name: "",
      see: true
    };
  },
  methods: {
    update: function(file) {
      const reader = new FileReader();
      this.name = file.name;
      this.type = file.type;
      var vm = this;
      reader.onload = function() {
        vm.text = reader.result;
      };
      reader.readAsText(file);
    },
    download: function() {
      var extension = "";
      if (this.type === "text/x-c++src") extension = ".cpp";
      else if (this.type === "text/x-python") extension = ".py";
      else if (this.type === "application/x-javascript") extension = ".js";
      else if (this.type === "text/x-java") extension = ".java";
      else extension = ".txt";
      var element = document.createElement("a");
      element.setAttribute(
        "href",
        "data:text/plain;charset=utf-8," + encodeURIComponent(this.text)
      );
      element.setAttribute("download", this.name + extension);

      element.style.display = "none";
      document.body.appendChild(element);

      element.click();
      document.body.removeChild(element);
      window.location.href = "http://localhost:8080/";
    },
    push: function() {
      var vm = this;
      var language = "";
      if (vm.type === "text/x-c++src") language = "C++";
      else if (vm.type === "text/x-python") language = "Python";
      else if (vm.type === "application/x-javascript") language = "JavaScript";
      else if (vm.type === "text/x-java") language = "Java";
      else language = "Text";
      const params = new URLSearchParams();
      params.append("username", localStorage.getItem("Username"));
      params.append("notes", vm.text);
      params.append("language", language);
      params.append("filename",vm.name);
      const config = {
        headers: {
          Authorization: "Token " + localStorage.getItem("Token"),
          "Content-Type": "application/x-www-form-urlencoded"
        }
      };
      const axios = require("axios");
      axios
        .post("http://127.0.0.1:8000/text/notes/", params, config)
        .then(function(response) {
          alert("Saved to the database!");
          vm.$router.push("/");
        })
        .catch(function(error) {
          console.log(error);
        });
    }
  },
  mounted() {
    if (localStorage.getItem("Token") != null) this.see = false;
  }
};
</script>
<style>
</style>
