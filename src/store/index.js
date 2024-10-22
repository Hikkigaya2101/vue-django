import { createStore } from "vuex";
import { unitModule } from "./unitModule";
import { consumerList } from "./consumerList";
export default createStore({
    
    modules:{
unit:unitModule,
consumer:consumerList
    }
}

)