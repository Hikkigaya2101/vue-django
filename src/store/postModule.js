import {HTTP} from "@/axios/common"
export const postModule = {
    state:() =>({
        posts:[],
        customs:[],
        limit:5,
    }),
    getters:{
      POSTS: state => {return state.limit} 
    },
    mutations:{
    setPosts: (state,posts)=>{
        state.posts = posts;
    },
    setCustoms(state,customs){
        state.customs = customs;
    },
    setLikes(state){
         state.limit+=2;
    },
    },
    actions:{
        getConsumerUnit(){
            const params = {'search': 27};
            HTTP.get('consumer/', {params})
            },
            setPosts : async(context,posts)=>{
                let {data} = await HTTP.get('unit');
            if (data.status == 200) {
                context.commit('setPosts', posts);
              }
            },
            message(){
                console.log('gavno');
            }

    },
    namespaced:true
}