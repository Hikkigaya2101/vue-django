<template>
    <div class = 'add_consumer_form' >
    <form @submit.prevent>
        <h4>Добавить сотрудника</h4>

        <my-input v-model="consumer.name" placeholder="ФИО"/>
          <my-input  v-model = "consumer.data_birthday"  placeholder="Дата рождения"/>
          <my-input  v-model = "consumer.data_workday"  placeholder="Дата назначения на должность"/>
          <my-input v-model="consumer.unit" placeholder="Подразделение"/>
        <my-button  style ='align-self: flex-end' @click='emitConsumer' >Создать</my-button>
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
        consumer:{
name:'',
data_birthday:'',
data_workday:'',
unit:''
}
    }
},
    methods:{
emitConsumer(){
// this.$emit('create',this.consumer)
HTTP.post('consumer/',this.consumer, {headers: {xsrfHeaderName: "X-CSRFToken"}})
console.log(this.consumer)
this.$emit('**dialogConsumerVisible',false)
        }
    }
}
    
</script>
<style>

</style>