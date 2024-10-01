import {HTTP} from "@/axios/common"
export const consumerList = {
    state:() =>({
        customs:[],
    }),
    getters:{
      CUSTOMS: state => {return state.customs} 
    },
    mutations:{
  
    setCustoms(state,id){
        const params = {'search': id};
        HTTP.get('consumer/', {params}).then(response=>state.customs = response.data);
    },

    },
    actions:{
        //getConsumerUnit(context,param){ context.commit('setCustoms',param)}
        getConsumerUnit(context,id){context.commit('setCustoms',id); }

    },
    namespaced:true
}