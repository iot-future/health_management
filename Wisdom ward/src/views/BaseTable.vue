<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item>
                    <i class="el-icon-lx-cascades"></i> 病人信息管理
                </el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="container">
            <div class="handle-box">
                <el-button type="primary" icon="el-icon-s-custom" @click="all()" class="mr10">获取病人的全部数据</el-button>
                 <el-button type="primary" icon="el-icon-circle-plus" @click="handleadd()" class="mr100">添加</el-button>
                <el-input v-model="id" placeholder="病人ID" class="handle-input mr10" maxlength="18" autocomplete="off" @input="v => id = v.replace(/[^\d]/g,'')"></el-input>
                <el-button type="primary" icon="el-icon-search" style="margin-top: 10px" @click="get(id)">查询</el-button>
                <el-button type="danger" icon="el-icon-delete-solid" @click="del(id);all()">删除</el-button>
            </div>
            <el-table :data="patient"  border class="table" ref="multipleTable" header-cell-class-name="table-header">
                <el-table-column prop="id" label="身份证" width="220px" align="center"/>
                <el-table-column prop="name_p" label="姓名" width="220px" align="center"/>
                <el-table-column prop="room" label="病房号" width="220px" align="center"/>
                <el-table-column prop="phone" label="电话" width="220px" align="center"/>
                <el-table-column prop="address" label="地址" width="250px" align="center"/>
                <el-table-column label="状态" width="250px" align="center">
                     <template #default="scope">
                        <el-tag type="success" v-if="scope.row.state_p=='1'">临时住院</el-tag>
                        <el-tag type="danger" v-else-if="scope.row.state_p=='0'">隔离住院</el-tag>
                        <el-tag type="primary" v-else>长期住院</el-tag>
                    </template>
                </el-table-column>

                <el-table-column label="操作"  align="center">
                    <template #default="scope">
                        <el-button type="text" icon="el-icon-edit" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
                    </template>
                </el-table-column>
            </el-table>
           
        </div>

        <!-- 添加弹出框 -->
        <el-dialog title="添加" v-model="addVisible" width="30%">
            <el-form label-width="70px">
                <el-form-item label="身份证">
                    <el-input v-model.number="id" maxlength="18" autocomplete="off" @input="v => id = v.replace(/[^\d]/g,'')"></el-input>
                </el-form-item>
                <el-form-item label="姓名">
                    <el-input v-model="name_p"></el-input>
                </el-form-item>
                <el-form-item label="房间号">
                    <el-input v-model="room" maxlength="5" autocomplete="off" @input="v => room = v.replace(/[^\d]/g,'')"></el-input>
                </el-form-item>
                <el-form-item label="电话">
                    <el-input v-model="phone" maxlength="11" autocomplete="off" @input="v => phone = v.replace(/[^\d]/g,'')"></el-input>
                </el-form-item>
                <el-form-item label="地址">
                    <el-input v-model="address"></el-input>
                </el-form-item>
                <el-form-item label="状态">
                    <el-input v-model="state_p"></el-input>
                </el-form-item>
            </el-form>
            <template #footer>
                <span class="dialog-footer">
                    <el-button @click="empty_all()">清 空</el-button>
                    <el-button @click="addVisible = false">取 消</el-button>
                    <el-button type="primary" @click="add(id,name_p,room,phone,address,state_p);all();addVisible = false">添 加</el-button>
                </span>
            </template>
        </el-dialog>

        <!-- 编辑弹出框 -->
        <el-dialog title="编辑" v-model="editVisible" width="30%">
            <el-form label-width="70px">
                <el-form-item label="身份证">
                    <el-input v-model="id" maxlength="18" autocomplete="off" @input="v => id = v.replace(/[^\d]/g,'')"></el-input>
                </el-form-item>
                <el-form-item label="姓名">
                    <el-input v-model="name_p"></el-input>
                </el-form-item>
                <el-form-item label="房间号">
                    <el-input v-model="room" maxlength="5" autocomplete="off" @input="v => room = v.replace(/[^\d]/g,'')"></el-input>
                </el-form-item>
                <el-form-item label="电话">
                    <el-input v-model="phone" maxlength="11" autocomplete="off" @input="v => phone = v.replace(/[^\d]/g,'')"></el-input>
                </el-form-item>
                <el-form-item label="地址">
                    <el-input v-model="address"></el-input>
                </el-form-item>
                <el-form-item label="状态">
                    <el-input v-model="state_p"></el-input>
                </el-form-item>
            </el-form>
            <template #footer>
                <span class="dialog-footer">
                    <el-button @click="empty()">清 空</el-button>
                    <el-button @click="editVisible = false">取 消</el-button>
                    <el-button type="primary" @click="updata_p(id,name_p,room,phone,address,state_p);get(id);editVisible = false">修 改</el-button>
                </span>
            </template>
        </el-dialog>
    </div>
</template>

<script>
import { ref, reactive } from "vue";
import axios from "axios"
import { ElMessage, ElMessageBox } from "element-plus";
export default {

    
    setup(){

        const editVisible = ref(false);
        let form = reactive({
            id:"",
            name_p: "",
            room:"",
            phone:"",          
            address: "",
        });
        let idx = -1;
        const handleEdit = (index, row) => {
            idx = index;
            Object.keys(form).forEach((item) => {
                form[item] = row[item];
            });
            editVisible.value = true;
        };

        const addVisible = ref(false);
        const handleadd = () => {
            addVisible.value = true;
        };

        return{
            handleEdit,
            editVisible,
            addVisible,
            handleadd,
        }

    },

    data() {
        return {
            id: ref(''),
            name_p: ref(''),
            room: ref(''),
            phone: ref(''),
            address: ref(''),
            state_p:ref(''),
            patient:[],
            
        };
    },
    mounted() {
        this.all();
    },

    methods: {
       
        empty() {
            this.id=ref('');
            this.name_p = ref('');
            this.room = ref('');
            this.phone = ref('');
            this.address = ref('');
            this.state_p = ref('')
        },

        empty_all() {
            this.id = ref('');
            this.name_p = ref('');
            this.room = ref('');
            this.phone = ref('');
            this.address = ref('');
            this.state_p = ref('')
        },

        all() {    //查找patient表全部数据
            axios.get('http://119.3.16.162:8085/patient').then(res => {
                this.patient = res.data
            }).catch(err => {
                console.log("获取数据失败" + err);
            })
        },


        //查询单独
        get(id) {
            var num = id;
            var addr = "http://119.3.16.162:8085/getp/" + num;
            console.log(addr);
            axios.get(addr).then(response => {
                this.patient = response.data
            })
                .catch(function (error) {
                    console.log(error);
                });
        },

        //增
        add(id, name_p, room, phone, address,state_p) {
            var num = id;
            var Name = name_p;
            var Room = room;
            var Phone = phone;
            var Address = address;
            var State = state_p;
            ElMessage.success(`添加成功，请重新获取`);
            var addr = "http://119.3.16.162:8085/addpatients?" + "id=" + num + "&name_p=" + Name + "&room=" + Room + "&phone=" + Phone + "&address=" + Address + "&state_p=" +State;
            console.log(addr);
            axios.get(addr).then(function (response) {
            })
                .catch(function (error) {
                    console.log(error);
                });
        },

        //删
        del(id) {
            var num = id;
            ElMessage.success("删除成功，请重新获取");
            var addr = "http://119.3.16.162:8085/deletep/" + num;
            console.log(addr);
            axios.get(addr).then(function (response) {
                console.log(response);
            })
                .catch(function (error) {
                    console.log(error);
                });
        },

        //改
        updata_p(id, name_p, room, phone, address,state_p) {
            var num = id;
            var Name = name_p;
            var Room = room;
            var Phone = phone;
            var Address = address;
            var State = state_p;
            ElMessage.success(`修改成功，请重新查询`);
            var addr = "http://119.3.16.162:8085/updatep/" + num + "/" + Name + "/" + Room + "/" + Phone + "/" + Address + "/" + State;
            console.log(addr);
            axios.get(addr).then(res => {
            })
                .catch(error => {
                    console.log(error);
                });
        }

    },
}
</script>

<style scoped>
.handle-box {
    margin-bottom: 20px;
}

.handle-select {
    width: 120px;
}

.handle-input {
    width: 300px;
    display: inline-block;
}
.table {
    width: 100%;
    font-size: 14px;
}
.red {
    color: #ff0000;
}
.mr10 {
    margin-right: 10px;
}
.mr100{
    margin-right: 750px;
}
.table-td-thumb {
    display: block;
    margin: auto;
    width: 40px;
    height: 40px;
}
</style>
