import Vue from "vue";
import App from "./App.vue";
import VueResource from "vue-resource";
import VueRouter from "vue-router";
import UploadButton from "vuetify-upload-button";
import editor from "./components/editor.vue";
import showEdits from "./components/showEdits.vue";
import updater from "./components/updater.vue";
Vue.use(VueResource);
Vue.use(UploadButton);
Vue.use(VueRouter);

const routes = [
  { path: "/", component: showEdits },
  { path: "/add/", component: editor },
  { path: "/upload/", component: updater }
];
const router = new VueRouter({ routes, mode: "history" });
new Vue({
  el: "#app",
  router: router,
  render: h => h(App)
});
