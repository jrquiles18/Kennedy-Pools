<template>
    <!-- <div v-if="accountCancelled" class="absolute bg-gray-800 text-white rounded py-2 px-2 focus:outline-none focus:shadow-outline"> -->
    <div v-if="accountCancelled" class="absolute bg-gray-800 text-white rounded py-2 px-2 focus:outline-none focus:shadow-outline">

        <h1 class="text-center">This account has been cancelled.  Use your previous account information to reactivate account?</h1>
        <div class='flex mt-4 justify-between'>
            <button @click.prevent="accountCancelled=false" class='absolute top-0 right-0 py-2 px-3 text-base' style="outline:none"><i class="fas fa-window-close"></i></button>
            <button  @click="oldAccount" class="bg-blue-500 hover:bg-blue-700 text-white  py-2 px-2 ml-2 rounded focus:outline-none focus:shadow-outline">Yes, Use previous account information.</button>
            <button  @click="newAccount" class="bg-blue-500 hover:bg-blue-700 text-white  py-2 px-2 ml-2 rounded focus:outline-none focus:shadow-outline">Yes, But start a new account.</button>
            <button  @click="oneTimeService" class="bg-red-500 hover:bg-red-700 text-white  py-2 px-2 ml-2 rounded focus:outline-none focus:shadow-outline">No, Just need a one time service.</button>
        </div>
    </div>
</template>
<script>
    import axios from "axios"
    export default{
        props: {
            open: Boolean
        },
        data(){
            return {
                accountCancelled: false,
                clicked: false
            }
        },

        methods: {
            oldAccount(){
                const path = window.location.pathname.split('/');
                const id = path[2];
                axios.get('/api/users/' + id).then((response) => {
                    const firstname = response.data['firstname']
                    document.getElementById('firstname').value = firstname

                    const lastname = response.data['lastname']
                    document.getElementById('lastname').value = lastname

                    const address = response.data['address']
                    document.getElementById('address').value = address

                    const cellPhone = response.data['cell_phone']
                    document.getElementById('cell_phone').value = cellPhone

                    const email = response.data['email']
                    document.getElementById('email').value = email

                    const userName = response.data['username']
                    document.getElementById('username').value = userName

                }).catch((error) => {
                    console.log(error)
                })
                this.accountCancelled = false
            },

            newAccount(){
                this.accountCancelled = false   
            },
            oneTimeService(){
                window.location.href='/schedule/one-time-schedule/'
                this.accountCancelled = false
            }
        },

        mounted(){
            this.accountCancelled = true
            // axios.get('/api/users/6').then((response) => {
            //         console.log(response.data)
            //         this.accountCancelled = true
            // }).catch(function (error){
            //     console.log(error)
            //     })
            // if (this.clicked === true){
            //     axios.get('/api/users').then((response) => {
            //         console.log(response.data)
            //         this.accountCancelled = response.data
            // }).catch(function (error){
            //     console.log(error)
            //     })
            // }
        }, 
    }
</script>