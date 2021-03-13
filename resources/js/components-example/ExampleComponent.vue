<template>
<div>
    {{message}}
</div>
    <!-- <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="card">
                    <div class="card-header">Example Component</div>

                    <div class="card-body">
                        I'm an example component.
                        <example-component></example-component>
                    </div>
                </div>
            </div>
        </div>
    </div> -->
</template>

<script>
    export default{
        data(){
            return{
                message: 'Hello World!'
            }
        }
    }

    // export default {
    //     mounted() {
    //         console.log('Component mounted.')
    //     }
    // }
</script>