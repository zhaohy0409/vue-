<template>
    <div>
        <form action="">
            <el-form :model="ruleForm" status-icon ref="ruleForm" label-width="100px"
                     class="demo-ruleForm">
                <el-form-item label="用户名" prop="user">
                    <el-input type="text" v-model="ruleForm.user" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="密码" prop="Pass">
                    <el-input type="password" v-model="ruleForm.pass" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="submitForm('ruleForm')">登录</el-button>
                    <el-button @click="resetForm('ruleForm')">重置</el-button>
                </el-form-item>
            </el-form>
        </form>
    </div>
</template>

<script>
export default {
    name: "longin",
    data() {
        return {
            ruleForm: {
                user: '',
                pass: '',
            },
        };
    },
    methods: {
        submitForm(formName) {
            this.$refs[formName].validate((valid) => {
                if (valid) {
                    this.$axios({
                        url:"http://127.0.0.1:8000/empapp/login/",
                        method:"post",
                        data:{
                            user:this.ruleForm.user,
                            pwd:this.ruleForm.pass,
                        }
                    }).then(response => {
                        alert(response.data.data_message);
                    }).catch(error => {
                        alert(error.data.data_message);
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
    }

}
</script>

<style scoped>

</style>
