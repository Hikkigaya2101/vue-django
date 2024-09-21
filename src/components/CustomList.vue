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
      <th scope="col">{{this.customs.length}}</th>
    </tr>
    
  </thead>
  <tbody>
    <tr>
      <th scope="row">Средний возраст:</th>
    <th  scope="col">{{ get_average_consumer(this.customs) }}</th>
    </tr>
    <tr>
      <th scope="row">Средний стаж работы:</th>
      <th scope="row">{{get_averworkday_consumer(this.customs)}}</th>

      <!--button @click="get_average_consumer">12</button-->
    </tr>
  </tbody>
</table>
</div>  
<h1>Список пользователей</h1>

    <div class ='menu_custom' v-if = "customs.length > 0 ">
 <custom-item v-for = "custom in customs"
  :custom="custom"
  :key="custom.id"/>

    </div>
    <h2 v-else style="color:red">
    Список пользователей пуст
</h2>

</div>

</template>

<script >
import CustomItem from "@/components/CustomItem"
import { get_birthday,get_workday} from "@/dll/statistic"


export default {
 components:{CustomItem},    

props:{
    customs:{
  type: Array,
  required:true,
 },unit_stats:{type: Array,required:true,},
  
},
methods:{
get_average_consumer(json_data){
 
return get_birthday(json_data);
}, 

get_averworkday_consumer(json_data){

return get_workday(json_data);
}, 

},
createCustom(){this.$emit('create',this.custom)}, 
mounted(){
  this.$emit('create',this.customs)
  this.custom = {id:'',name : '',data_birthday : '',data_workday:''}}
}
</script>

<style> 
.form_list{
    padding: 5vh 50px;
	background-color: none;
	height: 80vh;
	position: fixed;
	transition: 0.4s ease;
	right: 0px;
  font-size:14px;
  overflow:scroll;

}
.form_list::-webkit-scrollbar{
    background: none;
}
th{
    padding:15px;
    border: 2px solid teal;
    margin-top: 15px;
    box-sizing: border-box;
  font-size:15px;
  justify-content: center;
  text-align: center;

}
caption{
  font-size: 20px;
}
</style>