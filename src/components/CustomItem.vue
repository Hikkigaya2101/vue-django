<template>
    <div class="custom_card">  

        <div><strong>id пользователя:</strong>{{ custom.id }}</div>
    <div><strong>ФИО:</strong>{{ custom.name }}</div>
    <div><strong>Дата рождения:</strong>{{ custom.data_birthday }}</div>
    <div><strong>Дата выхода на работу:</strong>{{ custom.data_workday }}</div>   
       
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
    
    .custom_card{
    padding:10px;
    border: 2px solid teal;
    margin-top: 10px;
    box-sizing: border-box;
  font-size:14px;
  justify-content: center;
  text-align: center;
    }
    </style>