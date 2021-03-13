<template>
<div class='flex justify-center'>
    <!-- <div class="absolute bg-gray-800 hover:text-white h-10 w-10 font-bold text-sm outline-none">
         <button >Prev</button>           
    </div> -->
    <div class='flex justify-between relative items-center'>
         <button @click="$emit('previous')" class="absolute bg-gray-800 hover:text-white h-10 w-10 font-bold text-sm border-none focus:outline-none mt-20">Prev</button>           
    </div>
    <slot></slot>  
    <div class='flex justify-between relative items-center'>
         <button @click="$emit('next')" class="absolute bg-gray-800 hover:text-white h-10 w-10 font-bold text-sm -ml-10 border-none focus:outline-none mt-20">Next</button>         
    </div>    
</div>
</template>

<script>
    export default{
        props: {
            img: String
        },

        data(){
            return{

            }
        },
    }

</script>