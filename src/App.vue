<template>
<h1 style="color:aqua">{{$store.state}}</h1>
<my-button class="button" @click="POSTS">vuex</my-button>
<div  class = 'app' >
  <!--div id="app">
    <Tree :items="items"/>
  </div-->
<post-list :posts="posts"  
@remove ="removePost"/>
  <my-dialog v-model:show="dialogVisible">
      <post-form   @create="createPost"/>
  </my-dialog>

  <my-dialog v-model:show="putch_dialogVisible">
      <put-form   @create="createPut"/>
  </my-dialog>
  
  <!--my-button @click = "CM_CALL()">ВКЛ контексное меню</my-button-->

<custom-list :customs="customs" />

</div>
<my-dialog v-model:show="dialogCustomVisible">
      <custom-post-form   @create = "createCustom()"/>

  </my-dialog>
  <my-button class = 'btn_consumer' @click = "ShowCustomDialog">Создать пользователя</my-button>

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

import PostForm from '@/components/PostForm';
import PutForm from '@/components/PutForm';
import PostList from "@/components/PostList";
import CustomList from "@/components/CustomList";
import CustomPostForm from "@/components/CustomPostForm"
// eslint-disable-next-line
import { CM_CALL } from '@/dll/scripts'
//import Tree from "@/components/Tree";

import { HTTP } from '@/axios/common';
import { mapActions, mapGetters } from 'vuex';



export default{
  components:{PostForm,PostList,CustomList,CustomPostForm,PutForm},

  data(){
return{items: [
        {
          name: "foo",
          children: [
            { name: "bar", children: [{ name: "baz" }, { name: "qux" }] }
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
posts:[{id:'',
type:'',
name:'',
parent:''
}
],
customs:[{
name:'',
data_birthday:'',
data_workday:'',
unit:''}],
  dialogVisible: false,
  dialogCustomVisible:false,
  putch_dialogVisible:false,
  }},
   mounted(){
HTTP.get('unit').then(response=>this.posts = response.data);
//HTTP.get('unit').then(response=>(this.setPosts(response.data)));
HTTP.get('consumer/').then(response=>this.customs = response.data);



//контексное меню
(function() {
  
  "use strict";
  /**
   * Function to check if we clicked inside an element with a particular class
   * name.
   * 
   * @param {Object} e The event
   * @param {String} className The class name to check against
   * @return {Boolean}
   */
  function clickInsideElement( e, className ) {
    var el = e.srcElement || e.target;
    
    if ( el.classList.contains(className) ) {
      return el;
    } else {
      // eslint-disable-next-line no-cond-assign
      while ( el = el.parentNode ) {
        if ( el.classList && el.classList.contains(className) ) {
          return el;
        }
      }
    }

    return false;
  }

  /**
   * Get's exact position of event.
   * 
   * @param {Object} e The event passed in
   * @return {Object} Returns the x and y position
   */
  function getPosition(e) {
    var posx = 0;
    var posy = 0;

    // eslint-disable-next-line no-redeclare
    if (!e) var e = window.event;
    
    if (e.pageX || e.pageY) {
      posx = e.pageX;
      posy = e.pageY;
    } else if (e.clientX || e.clientY) {
      posx = e.clientX + document.body.scrollLeft + document.documentElement.scrollLeft;
      posy = e.clientY + document.body.scrollTop + document.documentElement.scrollTop;
    }

    return {
      x: posx,
      y: posy
    }
  }
  var contextMenuLinkClassName = "context-menu__link";
  var contextMenuActive = "context-menu--active";
  var taskItemClassName = "list_menu";
  var taskItemInContext;
  var clickCoords;
  var clickCoordsX;
  var clickCoordsY;
  var menu = document.querySelector("#context-menu");
  var menuState = 0;
  var menuWidth;
  var menuHeight;
  var windowWidth;
  var windowHeight;
  function init() {
    contextListener();
    clickListener();
    keyupListener();
    resizeListener();
  }

  function contextListener() {
    document.addEventListener( "contextmenu", function(e) {
      taskItemInContext = clickInsideElement( e, taskItemClassName );

      if ( taskItemInContext ) {
        e.preventDefault();
        toggleMenuOn();
        positionMenu(e);
      } else {
        taskItemInContext = null;
        toggleMenuOff();
      }
    });
  }
  function clickListener() {
    document.addEventListener( "click", function(e) {
      var clickeElIsLink = clickInsideElement( e, contextMenuLinkClassName );

      if ( clickeElIsLink ) {
        e.preventDefault();
        menuItemListener( clickeElIsLink );
      } else {
        var button = e.which || e.button;
        if ( button === 1 ) {
          toggleMenuOff();
        }
      }
    });
  }
  function keyupListener() {
    window.onkeyup = function(e) {
      if ( e.keyCode === 27 ) {
        toggleMenuOff();
      }
    }
  }
  function resizeListener() {
    // eslint-disable-next-line no-unused-vars
    window.onresize = function(e) {
      toggleMenuOff();
    };
  }
  function toggleMenuOn() {
    if ( menuState !== 1 ) {
      menuState = 1;
      menu.classList.add( contextMenuActive );
    }
  }
  function toggleMenuOff() {
    if ( menuState !== 0 ) {
      menuState = 0;
      menu.classList.remove( contextMenuActive );
    }
  }

  /**
   * Positions the menu properly.
   * 
   * @param {Object} e The event
   */
  function positionMenu(e) {
    clickCoords = getPosition(e);
    clickCoordsX = clickCoords.x;
    clickCoordsY = clickCoords.y;

    menuWidth = menu.offsetWidth + 4;
    menuHeight = menu.offsetHeight + 4;

    windowWidth = window.innerWidth;
    windowHeight = window.innerHeight;

    if ( (windowWidth - clickCoordsX) < menuWidth ) {
      menu.style.left = windowWidth - menuWidth + "px";
    } else {
      menu.style.left = clickCoordsX + "px";
    }

    if ( (windowHeight - clickCoordsY) < menuHeight ) {
      menu.style.top = windowHeight - menuHeight + "px";
    } else {
      menu.style.top = clickCoordsY + "px";
    }
  }

  /**
   * Dummy action function that logs an action when a menu item link is clicked
   * 
   * @param {HTMLElement} link The link that was clicked
   */
  function menuItemListener( link ) {
    console.log( "Task ID - " + taskItemInContext.getAttribute("data-id") + ", Task action - " + link.getAttribute("data-action"));
    toggleMenuOff();
  }
  init();
})();
},
computed:{
...mapActions(['setPosts']),
...mapGetters(['POSTS'])
},   

methods:
{createPost(post){
   this.posts.push(post);  
    
   //HTTP.post('unit/',this.post,{headers: { xsrfHeaderName: "X-CSRFToken"}})
   this.dialogVisible = false;

},
createPut(post){
   this.posts.push(post);  
    
   //HTTP.post('unit/',this.post,{headers: { xsrfHeaderName: "X-CSRFToken"}})
   this.putch_dialogVisible = false;

},
createCustom(custom){
  this.customs.push(custom);  
//HTTP.post('consumer/',this.custom, {headers: {xsrfHeaderName: "X-CSRFToken"}})
        this.dialogCustomVisible = false},

ShowCustomDialog(){
this.dialogCustomVisible = true;
  },
onClick (text) {
  alert(`You clicked ${text}!`)},

removePost(post){
this.posts = this.posts.filter(p =>p.id !== post.id);
console.log('FINISH')
//HTTP.delete('unit/',this.posts.filter(p =>p.id !== post.id),{headers: {xsrfHeaderName: "X-CSRFToken"}})
},
ShowDialog(){
  this.dialogVisible = true;
},
ShowPutDialog(){
  this.putch_dialogVisible = true;
},
async getUnit(){
  const units=(await HTTP.get('unit/')).data;
  console.log(units);
  return units;},
},

}
</script>

<style>
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
/*градиент
body{ margin:auto;
  padding:0;
position:fixed;
  box-sizing: border-box;
  color:  #fcfffc;
  font-family: Arial, "Helvetica Neue", Helvetica, sans-serif;
	font-size: 17px;
  font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    overflow: auto;
    background: linear-gradient(315deg, rgba(101,0,94,1) 3%, rgba(60,132,206,1) 38%, rgba(48,238,226,1) 68%, rgba(255,25,25,1) 98%);
    animation: gradient 15s ease infinite;
    background-size: 400% 400%;
    background-attachment: fixed;}*/
   
    body{

      background-color: black;
      color:rgb(32, 218, 211); 
    }
@keyframes gradient {
    0% {
        background-position: 0% 0%;
    }
    50% {
        background-position: 100% 100%;
    }
    100% {
        background-position: 0% 0%;
    }
}
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
