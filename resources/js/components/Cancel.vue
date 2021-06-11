<template>
    <span>
        <button v-if= 'cancel == false' @click.prevent="cancelAppt" type="button" class='button3 text-black' style="outline:none"><i class="cancel far fa-window-close"></i></button>
        <button v-else @click.prevent="unCancelAppt" type="button" class='button3 text-black' style="outline:none"><i class="cancel far fa-window-close"></i></button>

    </span>
</template>
<script>
    import axios from "axios"
    export default{
        data () {
            return {
                cancel: false
            }
        },

        methods: {
            cancelAppt(event){
                var token = document.head.querySelector('meta').getAttribute('content')
    
                const d = new Date()
                const date = d.toDateString()
               
                var element = event.target.getAttribute('id')
                 var trLen = document.getElementById('app').getElementsByTagName('tr').length
                for (var i=0; i < trLen; i++){
                    var trId = document.getElementById('app').getElementsByTagName('tr')[i].getAttribute('id')
                    if (element === trId){
                        var buttonTr = document.getElementById('app').getElementsByTagName('tr')[i]
                        buttonTr.getElementsByTagName('td')[4].innerHTML = "Cancelled"
                    }
                 }
                 var service_id = buttonTr.getElementsByTagName('td')[0].innerHTML
                 this.cancel = true
            
                 axios.post('/api/schedules',{id: service_id, cancelled_on: date, state: 'Cancelled'}, 
                     {headers: {"X-CSRF-Token": token}
                }).then(function (response){
                    // buttonTr.getElementsByTagName('td')[4].innerHTML = response.data
                    console.log(response.data)

                }).catch(function (error){
                    console.log(error)
                })
            },

            unCancelAppt(event){
                var token = document.head.querySelector('meta').getAttribute('content')
    
                const d = new Date()
                const date = d.toDateString()
               
                var element = event.target.getAttribute('id')
                 var trLen = document.getElementById('app').getElementsByTagName('tr').length
                for (var i=0; i < trLen; i++){
                    var trId = document.getElementById('app').getElementsByTagName('tr')[i].getAttribute('id')
                    if (element === trId){
                        var buttonTr = document.getElementById('app').getElementsByTagName('tr')[i]
                        buttonTr.getElementsByTagName('td')[4].innerHTML = "Active"
                    }
                 }
                 var service_id = buttonTr.getElementsByTagName('td')[0].innerHTML
                 this.cancel = false
            
                 axios.post('/api/schedules',{id: service_id, cancelled_on: 'NULL', state: 'Active'}, 
                     {headers: {"X-CSRF-Token": token}
                }).then(function (response){
                    // buttonTr.getElementsByTagName('td')[4].innerHTML = response.data
                    console.log(response.data)

                }).catch(function (error){
                    console.log(error)
                })
            }
        }, 

        // This adds id attributes to html elements
        mounted () {
                var rowLen = document.getElementById('app').getElementsByTagName('tr').length

                var i = 0
                    while (i < rowLen){
                        var deleteButton = document.getElementById('app').getElementsByClassName('button3')[i]
                        deleteButton.setAttribute('id', i+1)
                        i++;
                }
                var m = 0
                    while (m < rowLen){
                        var i = document.getElementById('app').getElementsByClassName('cancel')[m]
                        i.setAttribute('id', m+1)
                        m++;
            }
        }
    }

</script>
    