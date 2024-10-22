<template>

<div class ="form_list" @click.right="context_menu">
    <div class = 'header'>
        <table>
  <caption>
Статистика подразделения
  </caption>
  <thead>
    <tr>
      <th scope="col">Количество пользователей:</th>
      <th scope="col">{{this.$store.state.consumer.consumers.length}}</th>
    </tr>
  </thead>
    <tbody>
      <tr>
        <th scope="row">Средний возраст:</th>
        <th  scope="col">{{ get_average_consumer($store.state.consumer.consumers) }}</th>
      </tr>
      <tr>
        <th scope="row">Средний стаж работы:</th>
        <th scope="row">{{get_averworkday_consumer($store.state.consumer.consumers)}}</th>
     </tr>
  </tbody>
</table>
</div>  
<h1>Список пользователей</h1>
    <div class ='menu_consumer' v-if = "consumers.length > 0 ">
 <consumer-item 
 v-for = "consumer in $store.state.consumer.consumers"
  :consumer="consumer"
  :key="consumer.id"/>
    </div>
    <h2 v-else style="color:red">
    Список пользователей пуст
</h2>

</div>


</template>

<script >
import ConsumerItem from "@/components/ConsumerItem"
import { get_birthday,get_workday} from "@/dll/statistic"
import { CM_CALL } from "@/dll/scripts";
import { mapGetters, mapState } from "vuex";


export default {
 components:{ConsumerItem},    

props:{
    consumers:{
  type: Array,
  required:true,
 },unit_stats:{type: Array,required:true,},
  
},
methods:{
  context_menu(){CM_CALL();
  },

get_average_consumer(json_data){
 
return get_birthday(json_data);
}, 

get_averworkday_consumer(json_data){

return get_workday(json_data);
}, 

},
createConsumer(){this.$emit('create',this.consumer)}, 
mounted(){
  this.$emit('create',this.consumers)
  this.consumer = {id:'',name : '',data_birthday : '',data_workday:''}},
  computed:{
    ...mapGetters(["CONSUMERS"]),
    ...mapState(['consumers']),
  }
}
</script>

<style scoped> 
.form_list{
    padding: 5vh 50px;

	position: fixed;
	transition: 0.4s ease;
	right: 0px;
  font-size:14px;
  overflow:scroll;
  background: linear-gradient(132deg,rgba(255,255,255,0.05),rgba(255,255,255,0));
    -webkit-backdrop-filter: blur(1px);
    backdrop-filter: blur(1px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.05);

}
.form_list::-webkit-scrollbar{
    background: none;
    width: 0;
    height: 0;
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