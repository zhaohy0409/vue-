<template>
    <div id="user">
        <h4>用户管理</h4>
        <ul>
            <li>编号:{{ $route.params.id }}</li>
            <li>姓名:{{user_list[$route.params.id-1].naem}}</li>
            <li>年龄:{{user_list[$route.params.id-1].age}}</li>
            <li>信息:{{user_list[$route.params.id-1].msg}}</li>
            <li>工资:{{user_list[$route.params.id-1].salay}}</li>
            <li>评价:{{user_list[$route.params.id-1].evaluate}}</li>
        </ul>

    </div>
</template>

<script>
// let id1=document.getElementById("a")
// let id=id1.innerHTML
// console.log(id)
export default {
    name: "user",
    data() {
        return {
            user_list: [
                {id: 1, naem: '发一', age: 24, msg: '弱鸡',salay:'1500元',evaluate:'他的学历很低只有幼儿园'},
                {id: 2, naem: '赵二', age: 17, msg: '菜鸡',salay:'5000元',evaluate:'他的学历较低只有高中'},
                {id: 3, naem: '张三', age: 45, msg: '大婶',salay:'3000元',evaluate:'他的学历低只有初中'},
                {id: 4, naem: '李四', age: 33, msg: '大神',salay:'18000元',evaluate:'他的学历还特别高有硕士学位了'},
                {id: 5, naem: '王五', age: 21, msg: '耗子尾之',salay:'10000元',evaluate:'他的学历还可以有出大专了'},
            ],
            // id: {{$route.params.id}}

        }
    },
}
</script>

<style scoped>

</style>
