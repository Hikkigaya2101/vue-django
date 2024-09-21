<template>
    <div class = 'add_form' >
    <form @submit.prevent>
        <h4>Изменить данные подразделения</h4>    
         <my-input  v-model = "post.type"  placeholder="Тип"/>
        <my-input v-model="post.name" placeholder="Название"/>
          <my-input  v-model = "post.parent"  placeholder="Подчиняется"/>
        <my-button  style ='align-self: flex-end' @click='emitPost' >Создать</my-button>
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
        post:{id:'',
        type:'',
           name:'',
           parent:''

        }
    }
},
    methods:{
emitPost(){
HTTP.put('unit/',this.post,{headers: { xsrfHeaderName: "X-CSRFToken"}})
this.dialogVisible = false;
console.log(this.post)
        }
    }
}
    
</script>