/**
 * First we will load all of this project's JavaScript dependencies which
 * includes Vue and other libraries. It is a great starting point when
 * building robust, powerful web applications using Vue and Masonite.
 */


// require('./bootstrap');
// window.Vue = require('vue');

/**
 * The following block of code may be used to automatically register your
 * Vue components. It will recursively scan this directory for the Vue
 * components and automatically register them with their "basename".
 *
 * Eg. ./components/ExampleComponent.vue -> <example-component></example-component>
 */

// const files = require.context('./', true, /\.vue$/i)
// files.keys().map(key => Vue.component(key.split('/').pop().split('.')[0], files(key).default))

// Vue.component('example-component', require('./components/ExampleComponent.vue').default);

/**
 * Next, we will create a fresh Vue application instance and attach it to
 * the page. Then, you may begin adding components to this application
 * or customize the JavaScript scaffolding to fit your unique needs.
 */

// const app = new Vue({
//     el: '#app',
// });

// import { createApp } from 'vue';

// import App from './App.vue';

// createApp(App).mount('#app')

// import Vue from 'vue';

// import Notification from './components/Notification.vue'

// new Vue({
//     el:  '#app',

//     components: { Notification }
// })

import Vue from 'vue';

import DatePicker from 'vue2-datepicker';
import Delete from './components/Delete.vue'
import Dropdown from './components/DropDown.vue'
import Dropdownlist from './components/DropDownList.vue'
import DeletePopup from './components/DeletePopup.vue'
import CheckAll from './components/CheckAll.vue'
import Cancel from './components/Cancel.vue'
import Carousel from './components/Carousel.vue'
import CarouselButton from './components/CarouselButton.vue'
import CarouselIndicator from './components/CarouselIndicator.vue'
import Popup from './components/Popup.vue'
import Update from './components/Update.vue'

// import {DropDownButtonPlugin} from "@syncfusion/ej2-vue-splitbuttons";

import 'vue2-datepicker/index.css';
import moment from 'moment';
import { EventBus } from './bus.js';

import {store} from './store'
import { mapGetters } from 'vuex';

// Vue.use(DropDownButtonPlugin);

new Vue({
    el:  '#app',

    store,

    components: { Dropdown, DatePicker, Update, Delete, Cancel},

    delimiters: ['[[',']]'], 

    // code for the dropdown component
    data() {
        return {
            ServiceType: '',
            // service_scheduled: '',
            // service: 'Pool Cleaning', 
            month: 'January',
            day: '1', 
            time: '8:00', 
            daytime: 'AM',
        
            options: {
                services: ['Pool Cleaning', 'Pool Repair', 'Pool Installation Estimate'],
                account: ['Cancel Accout', 'Schedule A Service', 'Update Account Information', 'Update Password',
                                'Update/Set Up Billing Information', 'Pool Service Appointment', 'Pool Service History'],



                // months: ['January', 'February', 'March', 'April', 'May', 'June',
                //         'July', 'August', 'September', 'October', 'November', 'December'],

                // days: ['1', '2', '3', '4', '5', '6' , '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', 
                //     '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
                
                // times: ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30',
                //         '1:00', '1:30', '2:00', '2:30', '3:00', '3:30', '4:00', '4:30', '6:00', '6:30'], 

                // daytime: ['AM', 'PM'],

                // id: ['service_type', 'service_month', "service_day", "service_time", "day_time"],

                height: '28.5vh',

                overflow: 'scroll',
            },

            date: ' ',
            time: ' ',
            
            momentFormat: {
                //[optional] Date to String
                stringify: (date) => {
                    return date ? moment(date).format('LL') : ''
                },
            }
        }    
    }, 

    methods:{
        updateService(value){
            this.ServiceType= value
            this.service = value
        }, 

        notAfterToday(date) {
            const today = new Date();
            return (date.getTime() + 86400000) <= today.getTime();
            },

        notDuringThisTime(date) {
            const pickedDate = this.date  // returns day picked
            const pickedTime = this.time  // returns the time picked
            

            const timeAM = new Date(pickedDate.getFullYear(), pickedDate.getMonth(), pickedDate.getDate(), 9)  // establishes the AM time to compare picked time with.
            const timePM = new Date(pickedDate.getFullYear(), pickedDate.getMonth(), pickedDate.getDate(), 18) // establishes the PM time to compare picked time with.

            const testDate = new Date(pickedDate.getFullYear(), pickedDate.getMonth(), pickedDate.getDate(), pickedTime.getHours(), pickedTime.getMinutes()).getTime()
            
            if (testDate < timeAM.getTime()) {
                this.time = ' '
                EventBus.$emit('error-message-am', true)
            }

            if (testDate > timePM.getTime()) {
                this.time = ' '
                EventBus.$emit('error-message-pm', true)
            }  
        },

        updateSchedule(){
            if (this.time === ' ' && this.date === ' '){
                EventBus.$emit('update-schedule', false)
            }
            else {
                EventBus.$emit('update-schedule', true)
            }
        }, 

        valueUpdate(service){
            this.$store.commit('setServiceType', service) }
        },

        startLoader(){
           
        },

    computed: {
        ...mapGetters([
            'getServiceType'
        ]), 

        service: {
            get() {
                return this.$store.state.service;
            },
            set(service) {
                this.$store.commit('setServiceType', service);
            }
        },
    }
})
    
new Vue ({
    el: '#carousel',

    components: {
        Carousel,
        CarouselButton,
        CarouselIndicator
    },

    delimiters: ['[[',']]'], 

    data(){
        return{
            i: 0,
            
            images: ["/static/img/pool1.jpg",
                    "/static/img/pool2.jpg",
                    "/static/img/pool3.jpg",
                    "/static/img/pool4.jpg"],     

            active: true, 
            selected: 0
        }
    }, 

    methods:{
        next(){
            if (this.i == 0 || this.i <= this.images.length){
                this.i = this.i + 1    
                this.selected = this.i
                
            }

            if (this.i == this.images.length){
                this.i = 0
                this.selected = this.i
                
            }
        },

        prev(){
            if(this.i == 0) {
                this.i = this.images.length - 1
                this.selected = this.i
            }
                else if(this.i > 0){
                this.i = this.i - 1
                this.selected = this.i
            }
        },

        change(n){
            this.i = n
            this.selected = n
            
        }
    } 
})

new Vue({
    el: '#popup',

    components: {
        Popup
    }, 

    data() {
        return {
            
           
        }
    }
})

new Vue({
    el: '#warning',

    components: {
        DeletePopup
    }, 

    data() {
        return {
            
           
        }
    }
})

new Vue({
    el: '#checkbox',

    components: {
        CheckAll
    }, 

    data() {
        return {
            
           
        }
    }
})
 

new Vue({
    el: '#list',

    components: {
        Dropdownlist
    }, 

    data() {
        return {
            
           
        }
    }
})




