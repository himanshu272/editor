<template>
  <div class="editor" v-show="!show">
    <h2>Edit your Text:</h2>
    <form>
      <label>Username1:</label>
      <input v-model="info.username" required>
      <label>Text:</label>
      <textarea v-model="info.text"></textarea>
      <label>Language</label>
      <select v-model="info.language">
        <option v-for="(option,index) in languages" v-bind:key="index">{{ option }}</option>
      </select>
      <button v-on:click="post">Add Text</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "app",
  props: {
    show: {
      type: Boolean
    }
  },
  components: {},
  data() {
    return {
      info: {
        username: null,
        text: null,
        language: null
      },
      languages: ["python", "c++", "java", "javascript", "text"]
    };
  },
  methods: {
    post: function() {
      var self = this
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
      this.show = !this.show;
      this.$emit("update");
    }
  }
};
</script>

<style>
#editor {
  box-sizing: border-box;
}
#editor {
  margin: 20px auto;
  max-width: 500px;
}
label {
  display: block;
  margin: 20px 0.1px;
}
input,
textarea {
  display: block;
  width: 100%;
  padding: 8px;
}
</style>
