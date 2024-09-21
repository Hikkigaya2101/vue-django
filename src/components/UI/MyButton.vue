<template>
    <button class="btn">
      <slot></slot>
    </button>
  </template>
  
  <script>
  export default {
    name: 'my-button'
  }
  </script>
  
  <style scoped>
  .btn {
    z-index: 1;
    padding: 10px 25px;
    background: none;
color: aqua;
    border: 1px solid rgb(18, 122, 122);
  }
  .btn:focus{
    box-shadow: 0 8px 24px rgba(11, 183, 189, 0.5);    
  }
  </style>