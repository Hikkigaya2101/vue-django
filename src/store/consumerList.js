import {HTTP} from "@/axios/common"
export const consumerList = {
    state:() =>({
        consumers:[],
    }),
    getters:{
      CONSUMERS: state => {return state.consumers} 
    },
    mutations:{
  
    setConsumers(state,id){
        const params = {'search': id};
        HTTP.get('consumer/', {params}).then(response=>state.consumers = response.data);
    },

    },
    actions:{
        //getConsumerUnit(context,param){ context.commit('setCustoms',param)}
        getConsumerUnit(context,id){context.commit('setConsumers',id); }

    },
    namespaced:true
}