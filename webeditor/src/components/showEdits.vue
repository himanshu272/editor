<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="collapse navbar-collapse">
        <ul class="navbar-nav">
          <li class="nav-item active">
            <router-link to="/add/">New</router-link>
          </li>
          <li class="nav-item active">
            <router-link to="/upload/">Upload</router-link>
          </li>
        </ul>
      </div>
    </nav>
    <div class="jumbotron">
      <h1>Hello there!</h1>
      <p class="lead">This is a simple web editor! Login to save the files to your own database!</p>
      <hr class="my-4">
      <p>It works on Vue-js as a frontend JavaScript framework and django-rest-framework as a frontend.</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "app",
  components: {},
  data() {
    return {
      edits: [],
      show: true,
      see: false,
      pass: {},
      passIndex: undefined
    };
  },
  /*created() {
    this.$http.get("http://127.0.0.1:8000/notes/").then(function(data) {
      this.edits = data.body;
    });
  },*/
  methods: {
    transfer: function(obj, index) {
      this.pass = obj;
      this.passIndex = index;
      this.see = true;
    }
  }
};
</script>

<style scoped>
.navbar-nav > li {
  padding-left: 15px;
  padding-right: 15px;
}
</style>
