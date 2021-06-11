<template>
<transition name="fade">
    <div v-if="popUpOpen" class="absolute flex justify-center content-center">
        <div  class="relative top-0 right-0 m-3">
            <div class="bg-red-500 rounded-lg shadow-md p-6 pr-10"  style="min-width: 340px">
                <button @click.prevent="popUpOpen=false" class='absolute top-0 right-0 py-2 px-3 text-base' style="outline:none"><i class="fas fa-window-close"></i></button>
                <div v-if="timeUnavailable" class="flex items-center">{{message.am}}</div>
                <div v-if="pmTimeUnavailable" class="flex items-center">{{message.pm}}</div>
                <div v-if='scheduleUpdated' class="flex items-center">{{message.updated}}</div>
            </div>
        </div>
    </div>
</transition>
</template>

<script>
import { EventBus } from '../bus.js'
export default{
    
    data(){
        return {
            timeUnavailable: false,
            pmTimeUnavailable: false, 
            scheduleUpdated: false,
            popUpOpen: false,
            message: {
                am:  "Whoa, I'm still sleeping at that time. Please pick a time after 9:00 am.",
                pm: "No, No, I have to get to bed some time. Please pick a time before 6:00 pm.",
                updated:  "Your pool appointment has been updated."
            }, 
        }
    },
    mounted(){
        EventBus.$on('error-message-am', timeUnavailable => {
            this.timeUnavailable = timeUnavailable
            this.popUpOpen = true
            
        }),

        EventBus.$on('error-message-pm', pmTimeUnavailable => {
            this.pmTimeUnavailable = pmTimeUnavailable
            this.timeUnavailable = false
            this.popUpOpen = true
        }),

        EventBus.$on('update-schedule', scheduleUpdated => {
            if (scheduleUpdated === false){
                this.popUpOpen = false
            }
            else {
                this.scheduleUpdated = scheduleUpdated
                this.popUpOpen = true
            }
        })
    }
}
</script>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>