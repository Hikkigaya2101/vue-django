<template>
    <div class = 'add_form' >
        {{ $store.state.post.posts}}
        {{parser_type_unit}}
    <form @submit.prevent>
        <h4>Добавить подразделение</h4>    
         <!--my-select   :options = "$store.state.post.posts" placeholder="Тип"/-->
         <my-input v-model="post.type" placeholder="Тип"/> 
        <my-input v-model="post.name" placeholder="Название"/>
          <my-input  v-model = "post.parent"  placeholder="Подчиняется"/>
        <my-button  style ='align-self: flex-end' @click='emitPost' >Создать</my-button>
        </form>
    </div>
</template>

<style scoped>
</style >

<script>
import {  mapState } from "vuex";
import { HTTP } from '@/axios/common';
//import MySelect from './UI/MySelect.vue';
export default {
    //components:{MySelect},
    data(){
       return{
        post:{id:'',
        type:'',
           name:'',
           parent:''},
           parser_type_unit:{},
    }
},
    methods:{
emitPost(){this.post.id= Date.now();
this.$emit('create',this.post);
HTTP.post('unit/',this.post,{headers: { xsrfHeaderName: "X-CSRFToken"}})
this.dialogVisible = false;
console.log(this.post)}},
mounted(){
HTTP.get('unit_type').then(response=>this.parser_type_unit = response.data);
},
    computed:{
        ...mapState(['POSTS']),
    }
}
    
</script>