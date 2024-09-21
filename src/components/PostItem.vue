<template>
<div class="post" @click="getConsumerUnit()">  

    <div>
        <div><strong>Название:</strong>{{ post.name }}</div>
    <div><strong>Тип:</strong>{{ post.type }}</div>
   
    </div>
    <div class="post__btns">
        <!--my-button @click="$emit('remove',post)">Удалить</my-button-->
    </div>
    </div>
    
</template>

<script>
import { HTTP } from '@/axios/common';
export default{

props:{
 post:{
  type: Array,
  required:true,
 }
},
mounted(){
document.querySelector('.post').onclick = function() {
document.querySelector(".post").style.border = "2px solid white";
document.querySelector(".post").style.color = "white";

}
},
methods:{
    getConsumerUnit(){
        
const params = {'search': 1};
HTTP.get('consumer/', {params})
this.dialogVisible = false;

    },
}
}
</script>

<style scoped>

.post{
padding:10px;
border: 2px solid teal;
margin-top: 15px;
}
.post:hover{
    border: 2px solid rgba(221, 223, 232, 0.5);
    background: linear-gradient(135deg,
    (rgba(255,255,255,0.05))
    (rgba(255,255,255,0.05)));
-webkit-backdrop-filter: blur(1px);
backdrop-filter: blur(1px);
box-shadow: 0 8px 24px rgba(11, 183, 189, 0.5);    
}


</style>