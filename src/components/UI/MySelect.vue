<template>
    <select v-model = "SelectedType"  
    @change="changeOption">
       <options disabled value = ''>Выберите из списка</options>
<option
 v-for = "type in options" 
  :key = "type.id" 
  :value = "type.name">
</option>
    </select>
    </template>
  
  <script >
  import { mapState } from 'vuex';
  export default {
    name: 'my-select',
    props: {
      
      options:{type:Array}
    },
    SelectedType:'',
    methods: {
      changeOption(event) {
        this.$emit('update:units', event)
      }
    },
    computed:{
      ...mapState(['unit'])  
    }
  }
  </script>
  
  <style scoped>
  select {
    width: 80%;
    border: 1px solid teal;
    padding: 10px 15px;
    margin-top: 15px;
    color:aqua
  }
  
  </style>