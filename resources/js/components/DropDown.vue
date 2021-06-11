<template>
<div class="" >
    <div class='relative' @mouseleave="optionsAreVisible=false" >
        <!-- <button v-if="optionsAreVisible" @click="optionsAreVisible = false" class="fixed inset-0 h-full w-full cursor-default"></button> -->
        <div>
            <input @click.stop='open' v-model="service" :id="unique"  :name="unique" placeholder="Select A Service Type"
            class="shadow appearance-none border rounded w-full py-1 px-3 text-gray-700 text-center mb-1  leading-tight focus:outline-none focus:shadow-outline cursor-pointer">
            <div class="flex justify-center" v-if="optionsAreVisible"   > 
                <ul  :style="{height: height, overflow: overflow}" class="absolute z-auto max-h-20 w-full shadow appearance-none border rounded bg-white text-sm 
                font-bold text-gray-700 text-center mb-3 leading-tight focus:outline-none focus:shadow-outline overflow-auto">
                <li  v-for="item in list" :key="item" @click="selectOption(item)" class="hover:bg-blue-700 hover:text-white m-2 p-2">{{item}}</li>
                </ul>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import { EventBus } from '../bus.js'

    export default{
        props: {
            label: String,
            service: String, 
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
            },
            open(){
                this.optionsAreVisible = !this.optionsAreVisible
            },
        }
}
</script> 

