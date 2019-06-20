<template>
  <div>
    <showEdits></showEdits>
  </div>
</template>

<script>
import editor from "./components/editor.vue";
import showEdits from "./components/showEdits.vue";
export default {
  name: "app",
  components: {
    editor: editor,
    showEdits: showEdits
  },
  data() {
    return {};
  }
};
</script>

<style>
</style>
