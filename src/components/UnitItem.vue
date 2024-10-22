<template>
    <div class="unit" @click="getUnit(unit.id)">  
    <div>
        <div><strong>Название:</strong>{{ unit.name }}</div>
    <div><strong>Тип:</strong>{{ unit.type }}</div>
   
    </div>
    <div class="unit__btns">
        <!--my-button @click="$emit('remove',post)">Удалить</my-button-->
    </div>
    </div>
    
</template>

<script>
import { mapActions } from 'vuex';

export default{

props:{
 unit:{
  type: Array,
  required:true,
 }
},
mounted(){
// // document.querySelector('.unit').onclick = function() {
// // this.style.border = "2px solid white";
// // this.style.color = "white";
// }
},
computed:{...mapActions({getConsumerUnit:'consumer/getConsumerUnit'})
},
methods:{
    getUnit(id_unit){
        this.$store.dispatch("consumer/getConsumerUnit",id_unit);
    }
}
}
</script>

<style scoped>

.unit{
padding:10px;
border: 2px solid rgba(21, 112, 113, 0.533);
margin-top: 15px;
}
.unit:hover{
    border: 2px solid rgba(221, 223, 232, 0.5);
    background: linear-gradient(135deg,
    (rgba(255,255,255,0.05))
    (rgba(255,255,255,0.05)));
-webkit-backdrop-filter: blur(1px);
backdrop-filter: blur(1px);
box-shadow: 0 8px 24px rgba(11, 183, 189, 0.5);    
}
.unit:focus{
border: 2px solid white;
color: aliceblue;
}

</style>