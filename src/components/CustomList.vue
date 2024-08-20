<template>
<div class ="form_list">
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

<script>
import CustomItem from "@/components/CustomItem";
export default {
 components:{CustomItem},    
props:{
 customs:{
  type: Array,
  required:true,
 }
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

}
</style>