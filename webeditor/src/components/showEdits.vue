<template>
  <div>
    <div class="jumbotron">
      <h1>Hello there!</h1>
      <p class="lead">This is a simple web editor! Login to save the files to your own database!</p>
      <hr class="my-4">
      <p>It works on Vue-js as a frontend JavaScript framework and django-rest-framework as a backend which provides a RESTful API.</p>
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
