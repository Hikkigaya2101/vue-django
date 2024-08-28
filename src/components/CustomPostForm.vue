<template>
    <div class = 'add_custom_form' >
    <form @submit.prevent>
        <h4>Добавить сотрудника</h4>
        <my-input v-model="custom.id" placeholder="id"/>
        <my-input v-model="custom.name" placeholder="ФИО"/>
          <my-input  v-model = "custom.data_birthday"  placeholder="Дата рождения"/>
          <my-input  v-model = "custom.data_workday"  placeholder="Дата назначения на должность"/>
        <my-button  style ='align-self: flex-end' @click='createCustom' >Создать</my-button>
        </form>
    </div>
</template>

<style scoped>
</style >

<script>

import { HTTP } from '@/axios/common'
export default {
    data(){
       return{
        custom:{
id:'',
name:'',
data_birthday:'',
data_workday:''
}
    }
},
    methods:{
createCustom(){

this.$emit('create',this.custom)
this.custom = {id:'',name : '',data_birthday : '',data_workday:''}

HTTP.post('consumer',{
    name: 'Fred',
    type: 'Flintstone'}, {headers: {
            xsrfHeaderName: "X-CSRFToken"
        }})
        }
    }
}
    
</script>
<style>
.add_custom_form{
    
}
</style>