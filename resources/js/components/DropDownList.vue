<template>
    <div class="relative mr-8 bg-blue-500 hover:bg-blue-700 text-white font-bold rounded py-2 px-2 rounded focus:outline-none focus:shadow-outline">
        <button @click="optionsAreVisible = !optionsAreVisible" class="relative z-10 focus:outline-none focus:shadow-outline" style="outline: none">
            My Account<i class="far fa-user ml-3"></i>
        </button>
        <button v-if="optionsAreVisible" @click="optionsAreVisible=false" tabindex="-1" class="fixed h-full w-full inset-0 cursor-default"></button>
        <div class="flex justify-center" v-if="optionsAreVisible"> 
            <ul class="absolute z-auto max-h-20 w-full mt-2 shadow appearance-none border rounded bg-white text-xs
            font-bold text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline overflow-auto">
                <li class="text-center pr-2 pl-2">
                    <a href="/schedule"><li class="mt-2 mb-2 font-bold text-gray-800 hover:bg-blue-700 hover:text-white">Schedule A Service</li></a>
                    <a href="/account/update"><li class='mb-2 font-bold text-gray-800 hover:bg-blue-700 hover:text-white'>Update Account Information</li></a>
                    <a href="/account/password"><li class="mb-2 font-bold text-gray-800 hover:bg-blue-700 hover:text-white">Update Password</li></a>
                    <a href="/account/billing"><li class="mb-2 font-bold text-gray-800 hover:bg-blue-700 hover:text-white">Update/Set Up Billing Information</li></a>
                    <a href="/account/appointments"><li class="mb-2 font-bold text-gray-800 hover:bg-blue-700 hover:text-white">Pool Service Appointments</li></a>
                    <a href="/account/cleaning"><li class="mb-2 font-bold text-gray-800 hover:bg-blue-700 hover:text-white">Pool Service History</li></a>
                    <a href="/account/cancel"><li class="mb-2 font-bold text-gray-800 hover:bg-blue-700 hover:text-white">Cancel Account</li></a>
                </li>
            </ul>
        </div>
    </div>
</template>
<script>    
    export default{
        props: {
            list: Array
        },

        data() {
            return {
                optionsAreVisible: false, 
            }
        },

    // closes dropdown from the keyboard by hitting the escape key
        created(){
            const handleEscape = (e) => {
                if (e.key === 'Esc' || e.key === 'Escape') {
                    this.optionsAreVisible = false
                }
            }

            document.addEventListener('keydown', handleEscape)
            this.$once('hook.beforeDestroy', () => {
                document.removeEventListener('keydown', handleEscape)
            })
        },
    }

</script>