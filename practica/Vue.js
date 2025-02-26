const {createApp} = Vue
createApp({
    data(){
        return{
            contador: 0
        }
    },
    methods: {
        incrementar(){
            this.contador += 1
        },

        decrementar(){
            this.contador -= 1
        }
    }
}).mount('#app')