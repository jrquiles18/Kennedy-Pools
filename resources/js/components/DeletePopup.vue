<template> 
    <div v-if="popUpOpen" class="bg-blue-200 rounded-lg border-2 border-black shadow-md p-6 pr-10"  style="min-width: 340px">
        <!-- <button class='absolute top-0 right-0 py-2 px-3 text-base' style="outline:none"><i class="fas fa-window-close"></i></button> -->
        <div v-if="popUpWarning" class="flex items-center">{{warning1}}</div>
        <div v-else class="flex items-center">{{warning2}}</div>
        <div class="mt-4 flex justify-around">
            <button  @click="deleteRow" type="button" class="rounded-md border-2 border-black p-2 bg-red-500 hover:bg-red-700" style="outline:none">Delete</button>
            <button @click.prevent="closePopUp(); closePopUp2()"  class="rounded-md border-2 border-black p-2 bg-green-500 hover:bg-green-700" style="outline:none">Cancel</button>
        </div>
    </div>
</template>

<script>
    import { EventBus } from '../bus.js'
    import axios from "axios"
    export default{
        data() {
            return {
                popUpOpen: false,
                popUpWarning: false,
                warning1:  'Are you sure you would like to delete this appointment?',
                warning2: "Are you sure you would like to delete all the appointments?",
                service_id: ' ',
                element: ' ',
                index: ' '
            }
        },

        methods: {
            closePopUp(){
                this.popUpOpen = false
            },

            closePopUp2(){
                this.popUpOpen = false
                var rows = document.getElementById('app').querySelectorAll('tr')
                for (var i=0; i < rows.length; i++){
                        rows[i].style.background = 'rgba(250, 251, 252)'
                    }
                document.getElementById('chk').checked = false
            },

            deleteRow(){
               axios.delete('/api/schedules/' + this.service_id.trim(), {
                    data: {id: this.service_id.id}
                }).then(function (response){
                    console.log(response.data)

                }).catch(function (error){
                    console.log(error)
                })
                document.getElementById('app').deleteRow(this.index)
                this.popUpOpen = false
            }
        },

        mounted (){
            EventBus.$on('open-pop-up', popUpOpen => {
                this.popUpOpen = popUpOpen
                this.popUpWarning = popUpOpen
            }),
            EventBus.$on('open-pop-up2', data =>{
                this.popUpOpen = data.warning1
                this.popUpWarning = data.warning2
            }),
            EventBus.$on('delete-row', data => {
                this.service_id = data.id 
                this.element = data.element
                this.index = data.index
            })
        }, 
    }   
</script>