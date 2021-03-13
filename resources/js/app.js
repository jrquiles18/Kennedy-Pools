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
// document.getElementById('schedule').style.backgroundColor = "blue";
import Vue from 'vue';

import Dropdown from './components/DropDown.vue'
import Carousel from './components/Carousel.vue'
import CarouselButton from './components/CarouselButton.vue'
import CarouselIndicator from './components/CarouselIndicator.vue'

new Vue({
        el:  '#app',
    
        components: { Dropdown, 
        
        },

        delimiters: ['[[',']]'], 

        data() {
            return {
                // value: 'hello', 
                service: 'Pool Cleaning', 
                month: 'January',
                day: '1', 
                time: '8:00', 
                daytime: 'AM',
                // message:  'Hello!!!!',
    
                options: {
                    services: ['Pool Cleaning', 'Pool Repair', 'Pool Installation Estimate'],

                    months: ['January', 'February', 'March', 'April', 'May', 'June',
                            'July', 'August', 'September', 'October', 'November', 'December'],

                    days: ['1', '2', '3', '4', '5', '6' , '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', 
                        '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
                    
                    times: ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30',
                            '1:00', '1:30', '2:00', '2:30', '3:00', '3:30', '4:00', '4:30', '6:00', '6:30'], 

                    daytime: ['AM', 'PM'],

                    id: ['service_type', 'service_month', "service_day", "service_time", "day_time"],

                    height: '28.5vh',

                    overflow: 'scroll',
                }
            }     
        }, 

        methods:{
            updateService(value){
                this.service = value
            }, 

            updateMonth(value){
                this.month = value
            },

            updateDay(value){
                this.day = value 
            }, 

            updateTime(value){
                this.time = value
            }, 

            updateDaytime(value){
                this.daytime = value
                const timesAM = ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30']
                const timesPM = ['12:00', '12:30', '1:00', '1:30', '2:00', '2:30', '3:00', '3:30', '4:00', '4:30', '6:00', '6:30']
                if (timesAM.includes(this.time) && this.daytime === 'PM'){
                    alert('No evening appointments available for this time.')
                    this.daytime = 'AM'
                    
                } else if (timesPM.includes(this.time) && this.daytime === 'AM') {
                    alert('No morning appointment available for this time')
                    this.daytime = 'PM'
                }
            }
            
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
            }

            if (this.i == this.images.length){
                this.i = 0
            }
        },

        prev(){
            if(this.i == 0) {
                this.i = this.images.length - 1
            }
                else if(this.i > 0){
                this.i = this.i - 1
            }
        },

        change(n){
            this.i = n
            this.selected = n
            
        }
    } 
})


        




