<template>
    <div class='flex items-center justify-center'>
        <input id='chk' @click='selectAll' type="checkbox" name="checkbox">
        <span class='ml-2'>Select All</span>
    </div>
</template>

<script>
    import { EventBus } from '../bus.js'
    export default{
        data(){
            return{
                isSelect: true,
                check: true,
                rowsToDelete:[]
            }
        },
        methods: {
            selectAll(){
                // this.isSelect = ! this.isSelect
                console.log(this.isSelect)
                var rows = document.getElementById('app').querySelectorAll('tr')
                if (this.isSelect === true && typeof rows !== 'undefined'){
                    for (var i = 0; i < rows.length; i++) {
                        rows[i].style.background = 'rgba(255, 0, 0, 0.4)';
                        var rowToDelete = rows[i].getElementsByTagName('td')[0].innerHTML
                        console.log(rowToDelete)
                        this.rowsToDelete.push(rowToDelete)
                    }
                    EventBus.$emit('open-pop-up2', {warning1: true, warning2: false})
                }
                else{
                    for (var i=0; i < rows.length; i++){
                        rows[i].style.background = 'rgba(250, 251, 252)'
                    }
                }
            }  
        },
    }
</script>

