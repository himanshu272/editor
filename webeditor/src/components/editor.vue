<template>
  <div class="editor" v-show="!show">
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
        username: "",
        text: "",
        language: ""
      },
      languages: ["python", "c++", "java", "javascript", "text"]
    };
  },
  methods: {
    post: function() {
      this.$http
        .post("http://127.0.0.1:8000/notes/", {
          notes: this.info.text,
          username: this.info.username,
          language: this.info.language
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
