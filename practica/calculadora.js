
function sumar(){

    const valor1 = parseFloat(document.getElementById('valor1').value)
    const valor2 = parseFloat(document.getElementById('valor2').value)

    const resultado = valor1 + valor2

    document.getElementById('resultado').textContent = `El resultado es ${resultado}`
}