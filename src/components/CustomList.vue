<template>
<div class ="form_list">
    <div class = 'header'>
        <table>
  <caption>
Статистика подразделения
  </caption>
  <thead>
    <tr>
      <th scope="col">Количество пользователей:</th>
      
    </tr>
    
  </thead>
  <tbody>
    <tr>
      <th scope="row">Средний возраст:</th>
      <th v scope="col"></th>
    </tr>
    <tr>
      <th scope="row">Средний стаж работы:</th>
      <!--div >{{getAge(customs[2].data_birthday)}}</div-->
      <button @click="get_data_birthday">12</button>
    </tr>

    
  </tbody>

</table>


</div>  
<h1>Список пользователей</h1>
  {{dialogCustomVisible}}
    <div class ='menu_custom' v-if = "customs.length > 0 ">
 
 <custom-item v-for = "custom in customs" 
:custom="custom" 
:key="custom.id"/>
    </div>
    <h2 v-else style="color:red">
    Список пользователей пуст
</h2>
<my-button @click = "ShowCustomDialog">Создать пользователя</my-button>
</div>
<my-dialog v-model:show="dialogCustomVisible">
      <custom-post-form   @create="createCustom"/>

  </my-dialog>
</template>

<script >
import CustomItem from "@/components/CustomItem"
import CustomPostForm from "@/components/CustomPostForm.vue"

export default {
 components:{CustomItem,CustomPostForm},    

props:{
    customs:{
  type: Array,
  required:true,
 },unit_stats:{type: Array,
  required:true,}
},


data(){
  return{
    dialogCustomVisible:false,
  }
},
methods:{
  ShowCustomDialog(){
this.dialogCustomVisible = true;
  },
getAge(dateString) {
    var today = new Date();
    var birthDate = new Date(dateString);
    var age = today.getFullYear() - birthDate.getFullYear();
    var m = today.getMonth() - birthDate.getMonth();
    if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
        age--;
    }
    return age;
},
get_data_birthday(){
var json_data = this.customs;

var result = [];
for(var i in json_data)
     console.log(json_data[i])
    result.push([i, json_data[i]]);
    //console.log(result)
      }




   
},
mounted(){
  this.$emit('create',this.customs)
  this.custom = {id:'',name : '',data_birthday : '',data_workday:''}

}
}
</script>

<style> 
.form_list{
    padding: 5vh 50px;
	background-color: none;
	height: 100vh;
	position: fixed;
	transition: 0.4s ease;
	right: 0px;
  font-size:14px;

}
th{
    padding:15px;
    border: 2px solid teal;
    margin-top: 15px;
    box-sizing: border-box;
  font-size:12px;
  justify-content: center;
  text-align: center;

}
</style>