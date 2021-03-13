<template>
    <!-- <div class="flex justify-center">
        <div class="flex justify-between relative items-center bg-red-500">
            <button class="absolute bg-gray-800 hover:text-white h-10 w-10 font-bold text-sm">Prev</button>           
        </div> -->
        <div class=" mt-10">
            <div class='shadow-md'>
                <img :src="img">
            </div>
        </div>
        
        <!-- <div class="flex justify-between relative items-center bg-red-500">
            <button class="absolute bg-gray-800 hover:text-white h-10 w-10 font-bold text-sm -ml-10">Next</button>           
        </div>

    </div> -->
</template>
<script>
    export default{
        props: {
            img: String
        },

        data(){
            return {
               
            }
        },
    }
</script>