<template>
    <span class="mr-2">
        <button @click.prevent='updateValues' type="button" class='button1 text-blue-600 border-none' style="outline:none"><i class="update fas fa-edit"></i></button>
    </span>

</template>

<script>
 export default{   
        
    data (){
        return {
            elementId: '',
            serviceId: '',
            serviceType: '',
            serviceDate: '',
            serviceTime: '',
        }
    }, 

    methods: {
        updateValues(event){
            var element = event.target.getAttribute('id')
            var trLen = document.getElementById('app').getElementsByTagName('tr').length
    
            for (var i=0; i < trLen; i++){
                var trId = document.getElementById('app').getElementsByTagName('tr')[i].getAttribute('id')
                if (element === trId){
                    var buttonTr = document.getElementById('app').getElementsByTagName('tr')[i]
                }
            }
            var service_id = buttonTr.getElementsByTagName('td')[0].innerHTML
            var service = buttonTr.getElementsByTagName('td')[1].innerHTML
            // var service_date = buttonTr.getElementsByTagName('td')[2].innerHTML
            // var service_time = buttonTr.getElementsByTagName('td')[3].innerHTML
             
            this.$emit('update-value', service)

            const url = '/schedule/'+ service_id.trim()
            window.location.href = url
        } 
    },

    // This add id attributes to html elements
    mounted(){
        const monthNames = ["January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"];
        const d = new Date();
        const month = monthNames[d.getMonth()];
        const day = d.getDate()
        const year = d.getFullYear()
        const currentDate = month + ' ' + day + ',' + ' ' + year 
        
        var len = document.getElementById('app').getElementsByTagName('td').length
        var rowLen = document.getElementById('app').getElementsByTagName('tr').length
       
        var i = 0
            while (i < len){
                var td = document.getElementById('app').getElementsByTagName('td')[i]
                td.setAttribute('id', i+1)
                i++;
            }
        var j = 0
            while (j < rowLen){
                var td = document.getElementById('app').getElementsByClassName('button1')[j]
                td.setAttribute('id', j+1)
                j++;
            }
        var k = 0
            while (k < rowLen) {
                var tr = document.getElementById('app').getElementsByTagName('tr')[k]
                var date = tr.getElementsByTagName('td')[2].innerHTML 
                
                if (new Date(date).getTime() <= new Date(currentDate).getTime()){
                    tr.style.background = 'rgba(255, 0, 0, 0.4)'
                    tr.getElementsByTagName('td')[4].innerHTML  = "Past Due"
                    tr.getElementsByTagName('td')[4].style.color='black'
    
                }
                tr.setAttribute('id', k+1)
                k++;
            }
        var m = 0
            while (m < rowLen){
                var i = document.getElementById('app').getElementsByClassName('update')[m]
                i.setAttribute('id', m+1)
                m++;
            }
    },
}
</script>