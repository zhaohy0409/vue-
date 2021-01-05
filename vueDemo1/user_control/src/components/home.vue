<template>
    <div id="home">
        <h4>用户首页</h4>
        <table border="2">
            <tr>
                <td>ID</td>
                <td>姓名</td>
                <td>年龄</td>
                <td>信息</td>
                <td>操作</td>
            </tr>
            <tr v-for="(user,index) in user_list" :key="index">
                <td>{{user.id}}</td>
                <td>{{user.naem}}</td>
                <td>{{user.age}}</td>
                <td>{{user.msg}}</td>
                <td>
                    <button @click="user_mgs(user.id)">详细信息</button>
                    |
                    <button @click="del_user_mgs(user.id)">删除</button>
                </td>
            </tr>
        </table>
    </div>
</template>

<script>
export default {
    name: "home",
    data() {
        return {
            user_list: [
                {id: 1, naem: '发一', age: 24, msg: '弱鸡'},
                {id: 2, naem: '赵二', age: 17, msg: '菜鸡'},
                {id: 3, naem: '张三', age: 45, msg: '大婶'},
                {id: 4, naem: '李四', age: 33, msg: '大神'},
                {id: 5, naem: '王五', age: 21, msg: '耗子尾之'},
            ]
        }
    },
    methods:{
        user_mgs(s){
            this.$router.push("/user/"+s+"/")
        },
        del_user_mgs(s){
            this.user_list.splice(s-1,1);
        }
    }
}
</script>

<style scoped>
table{
    text-align: center;
}
</style>
