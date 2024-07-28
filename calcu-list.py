#Test de lista
lista = []
condicion = "si"
continuo = "si"
while condicion == "si":
    lista.append(int(input("Ingrese el valor que desea agragar a la lista: ")))
    condicion = input("¿Desea seguir agregando valores?")
print(lista)

print(f'''
      1 - Sumar todos los elementos de la lista
      2 - Encontrar el maximo
      3 - Encontrar el mínimo
      4 - Filtrar por elementos pares
      5 - Filtrar por elementos impares''')

while continuo == "si":
    opcion = (int(input("Ingrese una opción: ")))
    if opcion == 1:
        suma = sum(lista)
        print("La suma de los elementos es: ", suma)
    elif opcion == 2:
        maximo = max(lista)
        print("El máximo es: ", maximo)
    elif opcion == 3:
        minimo = min(lista)
        print("El mínimo es: ", minimo)
    elif opcion == 4:
        losPares = list(filter(lambda x: x % 2 == 0, lista))
        print("Los pares son: ", losPares)
    elif opcion == 5:
        losImpares = list(filter(lambda x: x % 2 == 1, lista))
        print("Los impares son: ", losImpares)
    continuo = input("¿Desea continuar?")