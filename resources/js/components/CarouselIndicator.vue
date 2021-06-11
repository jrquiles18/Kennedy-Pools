<template>
<div class='flex justify-center mt-3'>
    <button @click="currentSlide(0)" :class="{'bg-red-700': num === 0, 'bg-gray-800': num !== 0}" 
        class="rounded-full h-3 w-3 flex items-center justify-center bg-gray-800 inline-block mr-2 cursor-pointer hover:bg-gray-200 border-none focus:outline-none"></button>
    <button @click="currentSlide(1)" :class="{'bg-red-700': num === 1, 'bg-gray-800': num !== 1}" 
        class="rounded-full h-3 w-3 flex items-center justify-center bg-gray-800 inline-block mr-2 cursor-pointer hover:bg-gray-200 border-none focus:outline-none"></button>
    <button @click="currentSlide(2)" :class="{'bg-red-700': num === 2, 'bg-gray-800': num !== 2}" 
        class="rounded-full h-3 w-3 flex items-center justify-center bg-gray-800 inline-block mr-2 cursor-pointer hover:bg-gray-200 border-none focus:outline-none"></button>
    <button @click="currentSlide(3)" :class="{'bg-red-700': num === 3, 'bg-gray-800': num !== 3}" 
        class="rounded-full h-3 w-3 flex items-center justify-center bg-gray-800 inline-block mr-2 cursor-pointer hover:bg-gray-200 border-none focus:outline-none"></button>
    <slot></slot>
</div>
</template>

<script>
   
    // import { EventBus } from '../bus'
    export default{
        props: {
            slideImg: Array,
            isActive: Boolean,
            num: Number
        },

        data(){
             
            return {
              
            }
        }, 

        methods:{
            currentSlide(index){
                this.$emit('change', index)
            },
        },
    }
</script>

