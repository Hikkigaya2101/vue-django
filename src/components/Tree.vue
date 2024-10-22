<template>
    <div class =" tree">
      <ul>
        <li v-for="i of posts" :key="i.id">
        
          <Tree :posts="i.parent" v-if="i.parent"/>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    // eslint-disable-next-line vue/multi-word-component-names
    name: 'Tree',
    props: {posts:[{id:'',type:'',name:'',parent:''}],
      items: Array,
    
  }}
  </script>
  <style >
  .tree{
color: aqua;
  }
  </style>