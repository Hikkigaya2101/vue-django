import { createStore } from "vuex";
import { postModule } from "./postModule";
import { consumerList } from "./consumerList";
export default createStore({
    
    modules:{
post:postModule,
custom:consumerList
    }
}

)