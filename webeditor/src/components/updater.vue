<template>
  <div class="jumbotron">
    <uploadbtn @file-update="update"></uploadbtn>
    <label for="exampleInputEmail1">Your Text:</label>
    <textarea v-model="text" rows="30" cols="50"></textarea>
    <button class="btn btn-success" v-on:click="download">Download</button>
  </div>
</template>

<script>
const axios = require("axios");
import UploadButton from "vuetify-upload-button";

export default {
  name: "app",
  components: {
    uploadbtn: UploadButton
  },
  data() {
    return {
      text: "",
      type: "",
      name: ""
    };
  },
  methods: {
    post: function() {
      var self = this;
      var url = "http://localhost:8000/notes/" + self.Index + "/";
      const requestBody = {
        username: self.info.username,
        language: self.info.language,
        notes: self.info.text
      };

      const config = {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded"
        }
      };
      axios
        .put(url, requestBody, {
          headers: { "Content-Type": "application/json" }
        })
        .then(result => {
          window.location.href = "http://localhost:8080/";
        })
        .catch(err => {});
    },
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
    }
  }
};
</script>
<style>
</style>
