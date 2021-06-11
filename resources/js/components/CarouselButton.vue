<template>
<div class='flex justify-center'>
    <div class='flex justify-between relative items-center'>
         <button @click="$emit('previous')" class="absolute hover:text-white h-10 w-10 font-bold text-3xl border-none focus:outline-none mt-20"><i class="fas fa-caret-left"></i>

</button>           
    </div>
    <slot></slot>  
    <div class='flex justify-between relative items-center'>
         <button @click="$emit('next')" class="absolute  hover:text-white h-10 w-10 font-bold text-3xl -ml-10 border-none focus:outline-none mt-20"><i class="fas fa-caret-right"></i></button>         
    </div>    
</div>
</template>

<script>
    
    // import { EventBus } from '../bus'
    export default{
        props: {
            img: String
        },

        data(){
            return{
                numIndicator: 0
            }
        },

        // methods: {
        //    indicatorChange () {
        //        EventBus.$emit('indicator-change', this.numIndicator)
        //    }
        // }

    }

</script>