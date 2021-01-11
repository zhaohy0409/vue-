<template>
    <div>
        <el-row :gutter="20">
            <el-col :span="8">
                <div class="grid-content bg-purple">&nbsp;</div>
            </el-col>
            <el-col :span="8">
                <div class="grid-content bg-purple">
                    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
                        <el-form-item label="姓名" prop="name">
                            <el-input v-model="ruleForm.name"></el-input>
                        </el-form-item>
                        <el-form-item label="密码" prop="password">
                            <el-input v-model="ruleForm.password"></el-input>
                        </el-form-item>
                        <el-form-item label="年龄" prop="age">
                            <el-input v-model.number="ruleForm.age"></el-input>
                        </el-form-item>
                        <el-form-item label="工资" prop="salay">
                            <el-input v-model.number="ruleForm.salay"></el-input>
                        </el-form-item>
                        <el-form-item label="出生日期" required>
                            <el-col :span="11">
                                <el-form-item prop="date1">
                                    <el-date-picker type="datetime" placeholder="选择日期" v-model="ruleForm.date1"
                                                    style="width: 240%;"></el-date-picker>
                                </el-form-item>
                            </el-col>
                        </el-form-item>
                        <el-form-item>
                            <el-button type="primary" @click="submitForm('ruleForm')">立即创建</el-button>
                            <el-button @click="resetForm('ruleForm')">重置</el-button>
                        </el-form-item>
                    </el-form>
                </div>
            </el-col>
            <el-col :span="8">
                <div class="grid-content bg-purple">&nbsp;</div>
            </el-col>
        </el-row>
    </div>
</template>

<script>
export default {
    name: "add_list",
    data() {
        return {
            ruleForm: {
                name: '',
                password: '',
                age: '',
                salay: '',
                date1: '',
            },
            rules: {
                name: [
                    {required: true, message: '请输入姓名', trigger: 'blur'},
                    {min: 2, max: 10, message: '长度在 2 到 10 个字符', trigger: 'blur'}
                ],
                password: [
                    {required: true, message: '请输入密码', trigger: 'blur'},
                    {min: 6, max: 20, message: '长度在 6 到 20 个字符', trigger: 'blur'}
                ],
                age: [
                    {required: true, message: '年龄不能为空'},
                    {type: 'number', message: '年龄必须为数字值'}
                ],
                salay: [
                    {required: true, message: '工资不能为空'},
                    {type: 'number', message: '年龄必须为数字值'}
                ],

                date1: [
                    {type: 'date', required: true, message: '请选择日期', trigger: 'change'}
                ],
            }
        };
    },
    methods: {

        submitForm(formName) {
            this.$refs[formName].validate((valid) => {
                if (valid) {
                    this.$axios({
                        url: "http://127.0.0.1:8000/empapp/index/",
                        method: "post",
                        data: {
                            username:this.ruleForm.name,
                            userpassword:this.ruleForm.password,
                            age:this.ruleForm.age,
                            salay: this.ruleForm.salay,
                            date:this.ruleForm.date1,}
                    }).then(response => {
                        alert(response.data.message);
                    }).catch(error => {
                        alert(error.data.message);
                    })
                } else {
                    console.log('error submit!!');
                    return false;
                }
            });
        },
        resetForm(formName) {
            this.$refs[formName].resetFields();
        }
    },
}
</script>

<style scoped>

</style>
