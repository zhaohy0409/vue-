<template>
    <div id="app">
        <h3>-----------用户管理系统----------</h3>
        <router-link to="/home">用户首页</router-link>
        <router-link to="/user">用户管理</router-link>
        <router-link to="/message">留言板</router-link>
        <hr>
        <router-view></router-view>
    </div>
</template>

<script>
export default {
    name: 'App'
}
</script>

<style>

</style>
