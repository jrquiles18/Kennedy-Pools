<template>
    <div v-if='open' class='z-20 bg-black bg-opacity-25 h-full w-full fixed'>
        <div class='flex justify-center relative h-full'>
            <div class='ring'>
            <div class='flex justify-center inline top-3'>
                <div class='' >
                    <div class="lds-ring"><div></div><div></div><div></div><div></div></div> 
                </div>
            </div>
            <div v-if='sched' class='flex justify-center'>{{message[0]}}</div>
            <div v-if='register' class='flex justify-center'>{{message[1]}}</div>
        </div>
        </div>
    </div>
</template>

<script>
    import { EventBus } from '../bus.js'
    export default{
        data(){
            return {
                message: ['Scheduling Now!', 'Registering Your Account Now!'],
                open: false,
                sched: false,
                register: false

            }
        },
        mounted (){
            EventBus.$on('open-spinner', (payload) => {
                this.open = true
                this.sched = payload
            }),

            EventBus.$on('open-spinner-register', (payload) => {
                // console.log(payload)
                this.open = true
                this.register = payload
            })
        }
    }
</script>

<style>
    /* .message{
        padding-top: 25px;
        margin-left: 10px;
    } */
    /* .spin{
        z-index: 10;
        width: 100%;
        height: 100%;
        background-color:  rgba(0,0,0,0.2);
        position: fixed;
    }  */
    .ring{
        position: absolute;
        top: 25%;
        margin: 0 auto;
        height: 100%;
        display:  inline;
    } 
    .lds-ring {
  display: inline-block;
  position: relative;
  width: 80px;
  height: 80px;
}
.lds-ring div {
  box-sizing: border-box;
  display: block;
  position: absolute;
  width: 64px;
  height: 64px;
  margin: 8px;
  border: 8px solid black;
  border-radius: 50%;
  animation: lds-ring 1.2s cubic-bezier(0.5, 0, 0.5, 1) infinite;
  border-color: black transparent transparent transparent;
}
.lds-ring div:nth-child(1) {
  animation-delay: -0.45s;
}
.lds-ring div:nth-child(2) {
  animation-delay: -0.3s;
}
.lds-ring div:nth-child(3) {
  animation-delay: -0.15s;
}
@keyframes lds-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>