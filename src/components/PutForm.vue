<template>
    <div class = 'add_form' >
    <form @submit.prevent>
        <h4>Изменить данные подразделения</h4>    
         <my-input  v-model = "unit.type"  placeholder="Тип"/>
        <my-input v-model="unit.name" placeholder="Название"/>
          <my-input  v-model = "unit.parent"  placeholder="Подчиняется"/>
        <my-button  style ='align-self: flex-end' @click='emitUnit' >Создать</my-button>
        </form>
    </div>
</template>

<style scoped>
</style >

<script>
import { HTTP } from '@/axios/common';
export default {
    data(){
       return{
        unit:{id:'',
        type:'',
           name:'',
           parent:''

        }
    }
},
    methods:{
emitUnit(){
HTTP.put('unit/',this.unit,{headers: { xsrfHeaderName: "X-CSRFToken"}})
this.dialogVisible = false;
        }
    }
}
    
</script>