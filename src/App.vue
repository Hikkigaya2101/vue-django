<template>
<div  class = 'app' >
  <div id="app">
    <Tree :units="units"/>
  </div>
  <!-- Список подразделений -->

<unit-list 
:units="units"  
@remove ="removePost"/>

<!-- Добавить подразделение -->

  <my-dialog v-model:show="dialogVisible">
      <post-form   @create="createUnit"/> 
  </my-dialog>

  <my-dialog v-model:show="putch_dialogVisible">
      <put-form   @create="createPut"/>
  </my-dialog>


  <!-- Список сотрудников -->
<consumer-list :consumers="consumers" ></consumer-list>

<!-- Модальное окно добавление пользователя -->

<my-dialog v-model:show="dialogConsumerVisible">
      <consumer-post-form   @create = "createConsumer()"/>
  </my-dialog>

  <my-button class = 'btn_consumer' @click = "ShowConsumerDialog">Создать пользователя</my-button>

  <!-- контексное меню подразделений-->
  <nav id="context-menu" class="context-menu">
    <ul class="context-menu__items">
      <li class="context-menu__item">
        <a href="#" class="context-menu__link" data-action="View" @click="ShowDialog"><i class="fa fa-eye"></i> Добавить подразделение</a>
      </li>
      <li class="context-menu__item">
        <a href="#" class="context-menu__link" data-action="Edit" @click="ShowPutDialog"><i class="fa fa-edit"></i> Изменить подразделение</a>
      </li>
      <li class="context-menu__item">
        <a class="context-menu__link" data-action="Delete" @click="removePost"><i class="fa fa-times"></i> Удалить подразделение</a>
      </li>
    </ul>
  </nav>

  <!-- <nav id="context-menu" class="context-menu">
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
  </nav> -->




</div>
</template>
<script>

import PostForm from '@/components/PostForm';
import PutForm from '@/components/PutForm';
import UnitList from "@/components/UnitList";
import ConsumerList from "@/components/ConsumerList";
import ConsumerPostForm from "@/components/ConsumerPostForm"
// eslint-disable-next-line
import { CM_CALL } from '@/dll/scripts'
import Tree from "@/components/Tree";

import { HTTP } from '@/axios/common';
import { mapActions, mapGetters } from 'vuex';

export default{
  components:{PostForm,UnitList,ConsumerList,ConsumerPostForm,PutForm,Tree},

  data(){
return{items: [
        {
          name: "foo",
          children: [{ name: "bar", children: [{ name: "baz" }, { name: "qux" }] }
]
        },
        {
          name: "lorem",
          children: [{ name: "ipsum" }]
        },
        {
          name: "dolor"
        }
      ],
units:[{id:'',type:'',name:'',parent:''}],
consumers:[{name:'',data_birthday:'',data_workday:'',unit:''}],
  dialogVisible: false,
  dialogConsumerVisible:false,
  putch_dialogVisible:false,}
},

   mounted(){
HTTP.get('unit').then(response=>this.units = response.data);
//HTTP.get('unit').then(response=>(this.setPosts(response.data)));
HTTP.get('consumer/').then(response=>this.consumers = response.data);

//контексное меню

},
computed:{
...mapActions({GetUnit:'post/GetUnit'}),
...mapGetters(['POSTS']),

},   

methods:
{createUnit(unit){
   this.units.push(unit);  
   this.dialogVisible = false;
},

createPut(unit){
   this.units.push(unit);  
   this.putch_dialogVisible = false;

},
createConsumer(consumer){
  this.consumer.push(consumer);  
//HTTP.post('consumer/',this.custom, {headers: {xsrfHeaderName: "X-CSRFToken"}})
        this.dialogConsumerVisible = false},

ShowConsumerDialog(){
this.dialogConsumerVisible = true;
  },
removePost(unit){
this.units = this.units.filter(p =>p.id !== unit.id);
//HTTP.delete('unit/',this.posts.filter(p =>p.id !== post.id),{headers: {xsrfHeaderName: "X-CSRFToken"}})
},
ShowDialog(){
  this.dialogVisible = true;
},
ShowPutDialog(){
  this.putch_dialogVisible = true;
},
// async getUnit(){
//   const units=(await HTTP.get('unit/')).data;
//   console.log(units);
//   return units;},
},

}
</script>

<style >
h1{
  display: flex;
  position: relative;
  margin: 0 auto;
}
.btn_consumer{
  right: 0;
  display: flex;
  position: fixed;
}
body{
      background: linear-gradient(to bottom right, rgb(124, 124, 152), rgb(52, 50, 51));
      color:aqua; 
      font-size: 15px;}

.new_custom{
  position:static;
  height: auto;
}
.app{
  display: flex;
  position: fixed;
  
}
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
