import {HTTP} from "@/axios/common"
export const postModule = {
    state:() =>({
        posts:[],

    }),
    getters:{
      POSTS: state => {return state.posts} 
    },
    mutations:{
    setPosts: (state)=>{
        HTTP.get('unit_type',).then(response=>state.posts = response.data);
    }
    },
    actions:{
        GetUnit(context){context.commit('setPosts');}},
    namespaced:true
}