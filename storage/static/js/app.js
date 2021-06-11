
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

// $("#body").on('click', '.delete', function () {
//     $(this).closest('tr').remove()
// })
$("#loader").on('click', function () {
    $("#spinner").show()
})