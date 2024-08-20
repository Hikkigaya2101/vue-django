<template>
    <div class="custom_card">  
        <div><strong>id пользователя:</strong>{{ custom.id }}</div>
    <div><strong>ФИО:</strong>{{ custom.name }}</div>
    <div><strong>Дата рождения:</strong>{{ custom.data_birthday }}</div>     
        </div>
    </template>
    
    <script>
    export default{
    props:{
     custom:{
      type: Object,
      required:true,
     }
    }
    }
    </script>
    
    <style scoped>
    
    .custom_item{
    padding:15px;
    border: 2px solid teal;
    margin-top: 15px;
    box-sizing: border-box;
  font-size:30px;
  justify-content: center;
  text-align: center;

    }
    </style>