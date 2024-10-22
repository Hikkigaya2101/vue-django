<template>
    <div class = 'add_form' >
    

    <form @submit.prevent>
        <h4>Добавить подразделение</h4>    
         <!-- <my-select  v-model="unit.type" :options = "parser_type_unit" placeholder="Тип"></my-select> -->
         <my-input v-model="unit.type" placeholder="Тип"/> 
        <my-input v-model="unit.name" placeholder="Название"/>
          <my-input  v-model = "unit.parent"  placeholder="Подчиняется"/>
        <my-button  style ='align-self: flex-end' @click='emitUnit' >Создать</my-button>
        </form>
    </div>
</template>

<style scoped>
.add_form{
    color: aqua;
}
</style >

<script>
import {  mapState } from "vuex";
import { HTTP } from '@/axios/common';
// import MySelect from './UI/MySelect.vue';
export default {
    // components:{MySelect},
    data(){
       return{
        unit:{id:'',
        type:'',
           name:'',
           parent:''},
           parser_type_unit:{},
    }
},
    methods:{
emitUnit(){this.unit.id= Date.now();
this.$emit('create',this.unit);
HTTP.post('unit/',this.unit,{headers: { xsrfHeaderName: "X-CSRFToken"}})
this.dialogVisible = false;}},
mounted(){
HTTP.get('unit_type').then(response=>this.parser_type_unit = response.data);
console.log(this.parser_type_unit);

},
    computed:{
        ...mapState(['UNITS']),
    }
}
    
</script>