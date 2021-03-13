<template>
<div class="">
    <div class='relative'>
        <button v-if="optionsAreVisible" @click="optionsAreVisible = false" class="fixed inset-0 h-full w-full cursor-default"></button>
        <input @click="optionsAreVisible = !optionsAreVisible"  v-model="scheduled" :id="unique"  :name="unique"  class="shadow appearance-none border rounded w-full py-1 px-3 text-gray-700 text-center mb-3 leading-tight focus:outline-none focus:shadow-outline">
        <slot></slot>
        <div class="flex justify-center">
            <ul :style="{height: height, overflow: overflow}" v-if="optionsAreVisible" class="absolute z-auto max-h-20 w-full shadow appearance-none border rounded bg-white text-sm 
                font-bold text-gray-700 text-center mb-3 leading-tight focus:outline-none focus:shadow-outline overflow-auto">
                <li v-for="item in list" :key="item" @click="selectOption(item)" class="hover:bg-blue-700 hover:text-white m-2 p-2">{{item}}</li>
            </ul>
        </div>
    </div>
</div>
</template>

<script>
    export default{
        props: {
            label: String,
            scheduled: String, 
            unique: String,
            // name: String, 
            list: Array,
            height: String,
            overflow: String,
            value: String
        },
        data(){
            return {
                optionsAreVisible: false, 
            }
        },

        methods: {
            selectOption(item){
                // this.value = item
                const pickedValue = item
                this.$emit('picked-value', pickedValue)
                this.optionsAreVisible = false
            }
        }, 
}
</script> 

