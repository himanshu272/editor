<template>
  <div class="jumbotron">
    <h2>
      <b>Add your Text:</b>
    </h2>
    <div>
      <label>FileName:</label>
      <input v-model="filename" required />
    </div>
    <div>
      <label>Text:</label>
      <textarea v-model="info.text" rows="40" cols="70"></textarea>
    </div>
    <div>
      <label>Language</label>
      <select v-model="type">
        <option v-for="(option,index) in languages" v-bind:key="index">{{ option }}</option>
      </select>
    </div>
    <button class="btn btn-primary" v-on:click="download">Download</button>
    <button class="btn btn-success" v-on:click="push" v-show="!see">Add to Database</button>
  </div>
</template>

<script>
export default {
  name: "app",
  props: {},
  components: {},
  data() {
    return {
      info: {
        username: null,
        text: null
      },
      languages: ["Python", "C++", "Java", "JavaScript", "Text"],
      filename: "",
      type: "",
      see: true
    };
  },
  methods: {
    download: function() {
      var extension = "";
      if (this.type === "Python") extention = ".py";
      else if (this.type === "C++") extension = ".cpp";
      else if (this.type === "JavaScript") extension = ".js";
      else if (this.type === "Java") extension = ".java";
      else extension = ".txt";
      var element = document.createElement("a");
      element.setAttribute(
        "href",
        "data:text/plain;charset=utf-8," + encodeURIComponent(this.info.text)
      );
      element.setAttribute("download", this.filename + extension);

      element.style.display = "none";
      document.body.appendChild(element);

      element.click();
      document.body.removeChild(element);
      window.location.href = "http://localhost:8080/";
    },
    push: function() {
      var vm = this;
      const params = new URLSearchParams();
      params.append("username", localStorage.getItem("Username"));
      params.append("notes", vm.info.text);
      params.append("language", vm.type);
      params.append("filename", vm.filename);
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
