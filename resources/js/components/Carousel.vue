<template>
    <div class=" mt-5">
        <div class='shadow-md'>
            <img :src="img">
        </div>
    </div>
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