import Vue from 'vue';
import Vuex from 'vuex';
import createPersistedState from "vuex-persistedstate";



Vue.use(Vuex);

// opens up the "store"
export const store =  new Vuex.Store({
    // state is date
    state: {
        service: '',
        service_scheduled: '',
        serviceDate: 'date', 
    }, 

    plugins: [createPersistedState()],

    getters: {
        getServiceType:  state => {
            return state.service_scheduled
        }, 
    }, 

    mutations: {
        setServiceType: (state, newServiceType) => {
            state.service = newServiceType
            console.log(state.service)
        },
    }, 
});

