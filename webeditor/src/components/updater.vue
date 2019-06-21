<template>
  <div v-show="see">
    <h2>Edit your Text:</h2>
    <form>
      <label>Username:</label>
      <input v-model="info.username" required>
      <label>Text:</label>
      <textarea v-model="info.text"></textarea>
      <label>Language</label>
      <select v-model="info.language">
        <option v-for="(option,index) in languages" v-bind:key="index">{{ option }}</option>
      </select>
      <button v-on:click="post">Save Text</button>
    </form>
  </div>
</template>

<script>
const axios = require("axios");

export default {
  name: "app",
  props: ["index", "item", "see"],
  watch: {
    // This would be called anytime the value of title changes
    item(newValue, oldValue) {
      // you can do anything here with the new value or old/previous value
      this.info.username = newValue.username;
      this.info.text = newValue.notes;
      this.info.language = newValue.language;
    },
    index(newValue, oldValue) {
      this.Index = newValue;
    }
  },
  components: {},
  data() {
    return {
      info: {
        username: this.item.username,
        text: this.item.notes,
        language: this.item.language
      },
      languages: ["python", "c++", "java", "javascript", "text"],
      Index: this.index
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
      // this.$http
      //   .put(url, {
      //     username: self.username,
      //     language: self.language,
      //     notes: self.text
      //   })
      //   .then(function(data) {
      //     console.log(data);
      //   });

      console.log(requestBody);
      axios
        .put(url, requestBody,  { headers: { 'Content-Type': 'application/json' } })
        .then(result => {
          // Do somthing
        })
        .catch(err => {
          // Do somthing
        });
    }
  }
};
</script>
<style>
</style>
