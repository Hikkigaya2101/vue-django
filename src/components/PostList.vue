
<template>
  
        <div class ='menu' @click.right="context_menu" v-if = "posts.length > 0">
            <h3>Список подразделений</h3>
 
<post-item v-for = "post in posts" 
:post="post" 
:key="post.id"
@remove = "$emit('remove',post)"/>
  <my-button  style ='align-self: flex-end' @click='createCustom' >Создать</my-button>
</div>
<h2 v-else style="color:red">
    Список подразделений пуст
</h2>
<div class="but">

</div>



</template>

<script>
import PostItem from '@/components/PostItem';

export default{
    components:{PostItem},

props:{
 posts:{
  type: Array,
  required:true,
 }

},
methods:{
    context_menu(){
        console.log(123);
    },
ShowDialog(){
  this.$emit('dialogVisible',true)
  console.log('HZ')
}
}

}

</script>

<style>

.menu{
    display: block;
	padding: 5vh 40px;
	height: 80vh;
    overflow:scroll;

	position: fixed;
	opacity: 0.7;
	transition: 0.4s ease;
    list-style: none;
text-decoration: none;
}
.menu::-webkit-scrollbar{
    background: none;
}
.but{

    z-index: 0;
    
}

</style>