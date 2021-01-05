import Vue from 'vue'
import Router from 'vue-router'
import home from "../components/home";
import user from "../components/user";
import message from "../components/message";


Vue.use(Router)

export default new Router({
    routes: [
        {path: "/home", component: home},
        {path: "/user/:id", component: user},
        {path: "/message", component: message},
        {path: "/", redirect: "/home"},
        {path: "/*", redirect: "/home"},
    ]
})
