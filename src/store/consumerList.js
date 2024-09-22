import {HTTP} from "@/axios/common"
export const consumerList = {
    state:() =>({
        customs:[],
    }),
    getters:{
      POSTS: state => {return state.customs} 
    },
    mutations:{
  
    setCustoms(state,customs){
        state.customs = customs;
    },

    },
    actions:{
        getConsumerUnit(){
            const params = {'search': 27};
            HTTP.get('consumer/', {params}).then(response=>this.customs = response.data)

            },
         
          

    },
    namespaced:true
}