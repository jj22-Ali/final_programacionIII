// const {createApp} = Vue;
// createApp({
//     data(){
//         return{
//             frutas : [
//                 {nombre : 'naranja', cantidad: 10},
//                 {nombre : 'banana', cantidad: 0},
//                 {nombre : 'durano', cantidad: 3}
//             ],
//             nuevaFruta : ''
//         }
//     },
//     methods: {
//         agregarFruta(){
//             this.frutas.push({
//                 nombre: this.nuevaFruta, cantidad: 0})
//         }
//     }
// }).mount('#app');

//? Creación de componentes

// const componente1 = {
//     template :'<h4> Hola {{usuario}} </h4>',
//     data(){
//         return{
//             usuario : 'tercero'
//         }
//     }
// }

// const componente2= {
//     template: `
//         <div             
//             v-on:mouseover = "cambiarNombre()"
//             v-on:mouseout = "restablecerNombre()">
//             <h4><span id= nombre>{{titulo}}</span></h4>
//         </div>    
//     `,
//     data(){
//         return{
//             titulo: 'Componente en Vue'
//         }
//     },
//     methods:{
//         cambiarNombre(){
//             this.titulo = 'TIENE EL MOUSE SOBRE EL DIV'
//         },

//         restablecerNombre(){
//             this.titulo = 'Componente en Vue'
//         }
//     }
// }

// const {createApp} = Vue
// createApp({
//     components:{
//         saludo : componente1,
//         titulo : componente2
//     }
// }).mount('#app')

//? Watcher

// const {createApp} = Vue
// createApp({
//     data(){
//         return{
//             kilometro : 0,
//             metro: 0
//         }
//     },

//     watch:{
//         kilometro(valor){
//             this.kilometro = valor;
//             this.metro = valor*1000;
//         },

//         metro(valor){
//             this.metro = valor;
//             this.kilometro = valor /1000;
//         }
//     }
// }).mount('#app')


//? $refs

// const {createApp} = Vue
// createApp({
//     methods:{
//         guardar(){
//             const texto = this.$refs.texto.value
//             const textArea = this.$refs.textArea
//             textArea.innerHTML = textArea.innerHTML + '<br>' + texto;
//         },

//         borrar(){
//             const textArea = this.$refs.textArea
//             textArea.innerHTML = '';
//         }
//     }
// }).mount('#app')