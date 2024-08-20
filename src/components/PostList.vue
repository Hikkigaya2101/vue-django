
<template>
  
        <div class ='menu' @click.right="context_menu" v-if = "posts.length > 0">
            <h3>Список подразделений</h3>
 
<post-item v-for = "post in posts" 
:post="post" 
:key="post.id"
@remove = "$emit('remove',post)"/>
<my-button 
  @click = "ShowDialog">Создать пользователя
</my-button>
</div>
<h2 v-else style="color:red">
    Список пользователей пуст
</h2>

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
	padding: 5vh 20px;
	height: 30vh;

	position: fixed;
	opacity: 0.7;
	transition: 0.4s ease;
}


</style>