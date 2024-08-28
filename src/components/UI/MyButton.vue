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
    color: rgb(205, 235, 235);
    border: 1px solid rgb(223, 232, 232);
  }
  </style>