import {HTTP} from "@/axios/common"
export const consumerList = {
    state:() =>({
        customs:[],
    }),
    getters:{
      CUSTOMS: state => {return state.customs} 
    },
    mutations:{
  
    setCustoms(state,input_param){
        const params = {'search': input_param};
        HTTP.get('consumer/', {params}).then(response=>state.customs = response.data);
    },

    },
    actions:{
        //getConsumerUnit(context,param){ context.commit('setCustoms',param)}
        getConsumerUnit(context,param){
                context.commit('setCustom',{input_param:param});

        }

    },
    namespaced:true
}