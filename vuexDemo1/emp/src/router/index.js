import Vue from 'vue'
import Router from 'vue-router'
import unp_list from "../components/unp_list";
import Index from "../components";
import add_list from "../components/add_list";

Vue.use(Router)

export default new Router({
  routes: [
    {path: "/index", component: Index},
    {path: "/unplist/:id", component: unp_list},
    {path: "/addlist", component: add_list},
    {path: "/", redirect: "/index"},
    {path: "/*", redirect: "/index"},


  ]
})
