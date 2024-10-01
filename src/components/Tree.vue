<template>
    <div>
      <ul>
        <li v-for="i of items" :key="i.name">
        
          <Tree :items="i.children" v-if="i.children"/>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    // eslint-disable-next-line vue/multi-word-component-names
    name: 'Tree',
    props: {
      items: Array
    }
  };
  </script>