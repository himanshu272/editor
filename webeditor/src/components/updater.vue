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
export default {
  name: "app",
  props: ["index", "item", "see"],
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
      var url = "http://127.0.0.1:8000/notes/" + this.Index + "/";
      this.$http
        .put(url, {
          username: this.username,
          language: this.language,
          notes: this.text
        })
        .then(function(data) {
          console.log(data);
        });
    }
  }
};
</script>
<style>
</style>
