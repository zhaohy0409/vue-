<template>
    <div id="a">
        <el-container>
            <el-header>Header</el-header>
            <el-table
                :data="user_list.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase()))"
                style="width: 100%">

                <el-table-column
                    label="ID"
                    prop="id">
                </el-table-column>

                <el-table-column
                    label="Name"
                    prop="username">
                </el-table-column>

                <el-table-column
                    label="Age"
                    prop="age">
                </el-table-column>

                <el-table-column
                    label="Salay"
                    prop="salay">
                </el-table-column>

                <el-table-column
                    label="Date"
                    prop="date">
                </el-table-column>

                <el-table-column
                    align="right">
                    <template slot="header" slot-scope="scope">
                        <el-button type="primary" icon="el-icon-edit" size="mini"@click="adduser()">添加</el-button>
                    </template>
                    <template slot-scope="scope">
                        <el-button
                            size="mini"
                            @click="handleEdit(scope.$index, scope.row)">Edit
                        </el-button>
                        <el-button
                            size="mini"
                            type="danger"
                            @click="handleDelete(scope.$index, scope.row)">Delete
                        </el-button>
                    </template>
                </el-table-column>
            </el-table>
            <el-footer>Footer</el-footer>
        </el-container>

    </div>
</template>

<script>
export default {
    name: "index",
    data() {
        return {
            user_list: [],
            search: ''
        }
    },
    created() {
        this.$axios({
            url: "http://127.0.0.1:8000/empapp/index/",
            method: "get",
            // params:"",
        }).then(response => {
            // console.log(response.data.results)
            this.user_list = response.data.results
        }).catch(error => {
            // console.log(error, "11111111")
        })
    },
    methods: {
        handleEdit(index, row) {
            console.log(index, row);
            this.$router.push("/unplist/" + row.id + "/")
        },
        handleDelete(index, row) {
            console.log(index, row.id);
            this.$axios({
                url: "http://127.0.0.1:8000/empapp/index/"+row.id,
                method: "delete",
                // params: {id:row.id,}
            }).then(response => {
                alert(response.data.message)
            }).catch(error => {
                // alert(error.data.message)
            })
        },
        adduser(){
            this.$router.push("addlist")
        }
    },


}
</script>

<style scoped>
.el-header, .el-footer {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 60px;
}

.el-aside {
    background-color: #D3DCE6;
    color: #333;
    text-align: center;
    line-height: 200px;
}

.el-main {
    background-color: #E9EEF3;
    color: #333;
    text-align: center;
    line-height: 160px;
}

body > .el-container {
    margin-bottom: 40px;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
    line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
    line-height: 320px;
}
</style>
