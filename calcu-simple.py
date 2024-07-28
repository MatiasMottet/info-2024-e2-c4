#Esta función realiza operaciones simples de un calculadora
def calculadora():

    numero1 = float(input("Ingrese un numero: "))
    numero2 = float(input("Ingrese otro numero: "))

    operacion = input("Ingrese la operación que quiere realizar: +, -, *, /: ")

    if operacion == "+":
        resultado = numero1 + numero2
    elif operacion == "-":
        resultado = numero1 - numero2
    elif operacion == "*":
        resultado = numero1 * numero2
    elif operacion == "/":
        if numero2 == 0:
            print("No se puede dividir entre 0")
            return
        else:
            resultado = numero1 / numero2
    else:
        print("La operación es inválida")
        return

    print("El resultado es: ", resultado)

calculadora()