#Actividad de clase lunes 29/07: Pasar tupla a lista

#tupla = (2,4,6)

#def to_list(tupla):
#    miLista = [elemento * 2 for elemento in tupla]
#    return miLista
#--------------------------------------------------------
# Ordenamiento por selección
def seleccion(lista):
    n = len(lista)
    for i in range(n):
        minIndex = i
        for x in range(i+1, n):
            if lista[x] < lista[minIndex]:
                minIndex = x
        lista [i], lista[minIndex] = lista[minIndex], lista[i]
    return lista

lista = [22, 35, 76, 19, 50]
print("Antes de ordenar: ")
print(lista)
print("Después de ordenar: ")
print(seleccion(lista))

#Ordenamiento por Inserción
def insercion(lista):
    for j in range(1, len(lista)):
        varActual = lista[j]

        i = j-1
        while i >= 0 and lista[i]> varActual:
            lista[i+1] = lista[1]
            i -= 1
        lista[i+1] = varActual
    return lista

lista = [29, 17, 30, 47, 6]
print("Antes de ordenar: ")
print(lista)
print("Después de ordenar: ")
print(insercion(lista))

#Ordenamiento por burbuja
def burbuja(lista):
    for i in range(len(lista)):
        for x in range(len(lista)-i-1):
            if lista[x] > lista[x+1]:
                val = lista[x]
                lista[x] = lista[x+1]
                lista[x+1] = val
    return lista

lista=[25, 15, 50, 10, 30]
print("Antes de ordenar: ")
print(lista)
print("Después de ordenar: ")
print(burbuja(lista))