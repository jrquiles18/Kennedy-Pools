
// import Vue from 'vue';

// import Notification from './components/Notification.vue'

// new Vue({
//     el:  '#app',

//     components: { Notification }
// })

// function used to make flash session message disappear
$("document").ready(function(){
    setTimeout(function(){
       $("#flash").remove();
    }, 5000 ); 
});

// $("#loader").on('click', function () {
//     $("#spinner").show()
// })