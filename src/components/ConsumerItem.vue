<template>
    <div class="consumer_card">  

        <div><strong>id пользователя:</strong>{{ consumer.id }}</div>
    <div><strong>ФИО:</strong>{{ consumer.name }}</div>
    <div><strong>Дата рождения:</strong>{{ consumer.data_birthday }}</div>
    <div><strong>Дата выхода на работу:</strong>{{ consumer.data_workday }}</div>   
    <div><strong>Подразделение:</strong>{{ consumer.unit }}</div>
  
        </div>
    </template>
    
    <script>
import { mapMutations } from 'vuex';

    export default{
    props:{
     consumer:{
      type: Object,
      required:true,
     }
    },mounted(){
    // Выделение подразделение
document.querySelector(' .consumer_card').onclick = function() {
    document.querySelector(".consumer_card").style.border = "2px solid white";
    document.querySelector(".consumer_card").style.color = "white";
}
},
methods:{
    ...mapMutations({
        setUnits:'unit/setUnits'
    })
}
    }
    </script>
    
    <style scoped>
    .consumer_card{
    padding:10px;
    border: 2px solid teal;
    margin-top: 10px;
    box-sizing: border-box;
  font-size:14px;
  justify-content: center;
  text-align: center;
    }
    .consumer_card:hover{
    border: 2px solid rgba(221, 223, 232, 0.5);
    background: linear-gradient(135deg,
    (rgba(255,255,255,0.05))
    (rgba(255,255,255,0.05)));
-webkit-backdrop-filter: blur(1px);
backdrop-filter: blur(1px);
box-shadow: 0 8px 24px rgba(11, 183, 189, 0.5);      
}

    </style>