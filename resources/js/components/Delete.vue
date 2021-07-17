<template>
    <span class='mr-2'>
        <!-- <button @click.prevent="deleteRow" type="button" class='button2 text-red-600' style="outline:none"><i class="delete fas fa-trash-alt"></i></button> -->
        <button @click.prevent="openPopUp" type="button" class='button2 text-red-600' style="outline:none"><i class="delete fas fa-trash-alt"></i></button>

    </span>
</template>

<script>
    import { EventBus } from '../bus.js'
    import axios from "axios"
    export default{
        data (){
            return {
                data: []
            }
        }, 

        methods: {
            openPopUp(event){
                
                var element = event.target.getAttribute('id')
                var trLen = document.getElementById('app').getElementsByTagName('tr').length
                // console.log(trLen)
                for (var i=0; i < trLen; i++){
                    var trId = document.getElementById('app').getElementsByTagName('tr')[i].getAttribute('id')
                    if (element === trId){
                        var buttonTr = document.getElementById('app').getElementsByTagName('tr')[i]
                        var index = i
                        
                    }
                 }
                var service_id = buttonTr.getElementsByTagName('td')[0].innerHTML
                // console.log(service_id)
                EventBus.$emit('open-pop-up', true)
                EventBus.$emit('delete-row', {id: service_id, element: element, index: index})
                
            },
        },
        
        // This adds id attributes to html elements
        mounted () {
                var rowLen = document.getElementById('app').getElementsByTagName('tr').length

                var i = 0
                    while (i < rowLen){
                        var deleteButton = document.getElementById('app').getElementsByClassName('button2')[i]
                        deleteButton.setAttribute('id', i+1)
                        i++;
                }
                var m = 0
                    while (m < rowLen){
                        var i = document.getElementById('app').getElementsByClassName('delete')[m]
                        i.setAttribute('id', m+1)
                        m++;
            }
        }
    }
</script>