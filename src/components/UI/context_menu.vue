<template>
  <nav id="context-menu" class="context-menu">
    <ul class="context-menu__items">
      <li class="context-menu__item">
        <a href="#" class="context-menu__link" data-action="View" @click="ShowDialog"><i class="fa fa-eye"></i> Добавить пользователя</a>
      </li>
      <li class="context-menu__item">
        <a href="#" class="context-menu__link" data-action="Edit" @click="ShowPutDialog"><i class="fa fa-edit"></i> Изменить пользователя</a>
      </li>
      <li class="context-menu__item">
        <a class="context-menu__link" data-action="Delete" @click="removePost"><i class="fa fa-times"></i> Удалить пользователя</a>
      </li>
    </ul>
  </nav>
  </template>
  
  <script>
  export default {
    name: 'my-button'
  }
  </script>
  
  <style scoped>
.context-menu {
  display: none;
  position: absolute;
  z-index: 10;
  padding: 12px 0;
  width: 240px;
  background-color: #fff;
  border: solid 1px #dfdfdf;
  box-shadow: 1px 1px 2px #cfcfcf;
}
.context-menu--active {
  display: block;
}

.context-menu__items {
  list-style: none;
  margin: 0;
  padding: 0;
}

.context-menu__item {
  display: block;
  margin-bottom: 4px;
}

.context-menu__item:last-child {
  margin-bottom: 0;
}

.context-menu__link {
  display: block;
  padding: 4px 12px;
  color: #0066aa;
  text-decoration: none;
}

.context-menu__link:hover {
  color: #fff;
  background-color: #0066aa;
}
  </style>