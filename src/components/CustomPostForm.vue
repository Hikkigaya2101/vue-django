<template>
    <div class = 'add_custom_form' >
    <form @submit.prevent>
        <h4>Добавить сотрудника</h4>

        <my-input v-model="custom.name" placeholder="ФИО"/>
          <my-input  v-model = "custom.data_birthday"  placeholder="Дата рождения"/>
          <my-input  v-model = "custom.data_workday"  placeholder="Дата назначения на должность"/>
          <my-input v-model="custom.unit" placeholder="Подразделение"/>
        <my-button  style ='align-self: flex-end' @click='emitCustom' >Создать</my-button>
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
        custom:{
name:'',
data_birthday:'',
data_workday:'',
unit:''
}
    }
},
    methods:{
emitCustom(){
this.$emit('create',this.custom)
HTTP.post('consumer/',this.custom, {headers: {xsrfHeaderName: "X-CSRFToken"}})
console.log(this.custom)
        }
    }
}
    
</script>
<style>

</style>