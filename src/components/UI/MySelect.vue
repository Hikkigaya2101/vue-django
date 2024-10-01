<template>
    <select v-model = "post"  @change="changeOption">
       <options disabled value = ''>Выберите из списка</options>
<option v-for = "post in $store.state.post.posts" :key = "post.id" :value = "post.name"></option>
    </select>
    </template>
  
  <script>
  import { mapState } from 'vuex';
  export default {
    name: 'my-select',
    props: {
      modelValue: {name:''},
      options:{type:Array}
    },
    methods: {
      changeOption(event) {
        this.$emit('update:posts', event)
      }
    },
    computed:{
      ...mapState(['post'])  
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