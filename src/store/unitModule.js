import {HTTP} from "@/axios/common"
export const unitModule = {
    state:() =>({
        units:[],

    }),
    getters:{
      UNITS: state => {return state.units} 
    },
    mutations:{
    setUnits: (state)=>{
        HTTP.get('unit_type',).then(response=>state.units = response.data);
    }
    },
    actions:{
        GetUnit(context){context.commit('setUnits');}},
    namespaced:true
}