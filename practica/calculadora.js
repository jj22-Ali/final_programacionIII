
function sumar(){
    const numero1 = parseFloat(document.getElementById('valor1').value);
    const numero2 = parseFloat(document.getElementById('valor2').value);

    let resultado = numero1 + numero2;

    document.getElementById('resultado').texContent = `El resultado es ${resultado}`
}