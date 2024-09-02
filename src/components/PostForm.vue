<template>
    <div class = 'add_form' >
    <form @submit.prevent>
        <h4>Добавить подразделение</h4>
        <my-input v-model="post.name" placeholder="Название"/>
          <my-input  v-model = "post.type"  placeholder="Тип"/>
          <my-input  v-model = "post.parent"  placeholder="Подчиняется"/>
          
 
        <my-button  style ='align-self: flex-end' @click='createPost' >Создать</my-button>
        </form>
    </div>
</template>

<style scoped>
</style >

<script>

export default {
    data(){
       return{
        post:{
            id:'',
           name:'',
           parent:'',
           type:''
        }
    }
},
    methods:{
createPost(){
this.post.id= Date.now();
this.$emit('create',this.post);



        }
    }
}
    
</script>