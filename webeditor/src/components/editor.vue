<template>
  <div class="jumbotron">
    <h2>
      <b>Add your Text:</b>
    </h2>
    <div>
      <label>FileName:</label>
      <input v-model="filename" required>
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
    <button class="btn btn-primary" v-on:click="download">Add Text</button>
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
      type: ""
    };
  },
  methods: {
    post: function() {
      var self = this;
      console.log(this.info.text);
      this.$http
        .post("http://localhost:8000/notes/", {
          notes: self.info.text,
          username: self.info.username,
          language: self.info.language
        })
        .then(function(data) {
          console.log(data);
        });
      this.$emit("update");
    },
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
    }
  }
};
</script>

<style>
</style>
