<template>
    <div id="message">
        <h3><---------------留言板---------------></h3>
        <input type="text" v-model="text">
        <input type="button" value="发表" @click="add_text">
        <ul>
            <li v-for="(val,inx) in all_text">
                <span>{{val}}</span> <a href="javascript:;" @click="deltext(inx,val)">删除</a>
            </li>
        </ul>

        <span>总数量：{{all_text.length}}条</span>
        <input type="button" value="清空" @click="delAll" v-show="all_text.length!=0">
    </div>
</template>

<script>
export default {
    name: "message",
    data() {
        return {
            text: "",
            all_text: localStorage.all_text ? JSON.parse(localStorage.all_text) : [],
        }
    },
    methods: {
        add_text() {
            let text = this.text;
            if (text) {
                this.all_text.push(this.text);
                localStorage.all_text = JSON.stringify(this.all_text);
                this.text = "";
            }
        },
        deltext(inx,val){
            this.all_text.splice(inx,1);
            localStorage.removeItem(val);
        },
        delAll() {
            this.all_text = [];
            localStorage.clear();
        },
    }

}
</script>

<style scoped>

</style>
