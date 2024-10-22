
<template>
<div class = 'list_menu'>
<div class ='menu' 
  @click.right="context_menu" 
  v-if = "units.length > 0">

 <h3>Список подразделений</h3>
 
<unit-item v-for = "unit in units" 
:unit="unit" 
:key="unit.id"
@remove = "$emit('remove',unit)"/>
</div>

<h2 v-else style="color:red">Список подразделений пуст</h2>
</div>
<!--my-button  style ='align-self: flex-end' @click='put_post' >обновить</my-button-->
</template>

<script>
import UnitItem from '@/components/UnitItem';
import { HTTP } from '@/axios/common';
import { CM_CALL } from '@/dll/scripts';
export default{
    components:{UnitItem},

props:{
 units:{
  type: Array,
  required:true,
 }
},
methods:{
context_menu(){
CM_CALL();
},


ShowDialog(){
  this.$emit('dialogVisible',true)
},
put_unit(){
    HTTP.put('unit/1/',{name:'NIKITA'},{headers: {xsrfHeaderName: "X-CSRFToken"}})
}
}
}

</script>

<style scoped>

.menu{
    display: block;
	padding:  4px;
	/* height: 80vh; */
    overflow:scroll;
	position: fixed;

	transition: 0.4s ease;
    list-style: none;
text-decoration: none;
}
.menu::-webkit-scrollbar{
    background: none;
    width: 0;
    height: 0;
   
}
.menu{
    background: linear-gradient(132deg,rgba(255,255,255,0.05),rgba(255,255,255,0));
    -webkit-backdrop-filter: blur(1px);
    backdrop-filter: blur(1px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.05);
}
</style>