import {HTTP} from "@/axios/common"
export const postModule = {
    state:() =>({
        posts:[],
        customs:[],
        limit:5,
    }),
    getters:{
      POSTS: state => {return state.posts} 
    },
    mutations:{
    setPosts: (state,posts)=>{
        state.posts = posts;
    },
    setCustoms(state,customs){
        state.customs = customs;
    },
    },
    actions:{
        getConsumerUnit(){
        
            const params = {'search': 1};
            HTTP.get('consumer/', {params})
            this.dialogVisible = false;
            },
            setPosts : async(context,posts)=>{
                let {data} = await HTTP.get('unit');
            if (data.status == 200) {
                context.commit('setPosts', posts);
              }
            },

    },
}