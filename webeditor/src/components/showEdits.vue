<template>
  <div v-on:update="show=!show">
    <div v-show="!see">
      <div v-show="show">
        <button v-on:click="show=!show">Add a new text:</button>
        <h2>These are the texts:</h2>
        <ul>
          <li v-for="(edit, id) in edits" v-bind:key="id">
            <label>{{ edit.username }}</label>
            <p>{{ edit.notes }}</p>
            <span>{{ edit.language }}</span>
            <button v-on:click.prevent="transfer(edit,id)">Edit</button>
          </li>
        </ul>
      </div>
      <editor v-bind:show="show"></editor>
    </div>
    <updater v-bind:see="see" v-bind:index="this.passIndex" v-bind:item="this.pass"></updater>
  </div>
</template>

<script>
import updater from "./updater.vue";
import editor from "./editor.vue";
export default {
  name: "app",
  components: {
    editor: editor,
    updater: updater
  },
  data() {
    return {
      edits: [],
      show: true,
      see: false,
      pass: {},
      passIndex: undefined
    };
  },
  created() {
    this.$http.get("http://127.0.0.1:8000/notes/").then(function(data) {
      this.edits = data.body;
    });
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

<style>
</style>
