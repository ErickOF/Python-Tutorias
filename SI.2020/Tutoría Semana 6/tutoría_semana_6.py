# -*- coding: utf-8 -*-
"""Tutoría Semana 6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1I0efwOM3UQC_iuFHpGcrlzb_r_9QEUPS

# Ejercicios

## Ejercicio 1

* append(elemento)
"""

def append(lista, elemento):
    """Inserta elemento al final de la lista
    """
    lista = lista + [elemento]
    return lista

lista = [1, 2, 3]
append(lista, 10)

def insert(lista, pos, elemento):
    """Insertar en la posicion pos el elemento
    """
    if pos >= len(lista):
        return lista + [elemento]

    listaNueva = []

    for i in range(len(lista)):
        if i == pos:
            listaNueva.append(elemento)
        
        listaNueva.append(lista[i])

    return listaNueva

lista = [1, 2, 3]
insert(lista, 30, 10)

lista = [1, 2, 3]
lista.insert(100, 0)
lista

def remove(lista, elemento, primeraAparicion=False):
    listaNueva = []
    apariciones = 0

    for num in lista:
        if num != elemento or (apariciones >= 1 and primeraAparicion):
            listaNueva.append(num)
        else:
            apariciones += 1

    return listaNueva

lista = [1, 2, 3, 4, 3, 5, 6, 3, 3, 30]
remove(lista, 3, True)

def esPrimo(num):
    if num < 2:
        return False

    for div in range(2, num):
        if num % div == 0:
            return False

    return True

def obtenerListaPrimos():
    inicio = 1
    fin = 100
    listaPrimos = []

    for num in range(inicio, fin + 1):
        if esPrimo(num):
            listaPrimos.append(num)
    
    return listaPrimos

obtenerListaPrimos()

def sumarVector(lista1, lista2):
    if len(lista1) == len(lista2):
        suma = []

        #for i in range(len(lista1)):
        #    suma.append(lista1[i] + lista2[i])

        # zip([1, 2, 3], [4, 5, 6])
        # ((1, 4), (2, 5), (3, 6))
        for num1, num2 in zip(lista1, lista2):
            suma.append(num1 + num2)
        
        return suma
    else:
        raise ValueError('Las listas deben ser del mismo largo')

try:
    suma = sumarVector([1, 2, 3], [4, 5, 6])
    suma.append(1)
    print(suma)
except ValueError:
    print('No se pueden sumar')

"""# Multiplicacion de vectores (producto punto)
$u = (1, 2, 3)$
$v = (0, 1, 1)$

$v \cdot u = 1 \cdot 0 + 2 \cdot 1 + 3 \cdot 1$
$v \cdot u = 5$
"""

def multVector(lista1, lista2):
    if len(lista1) == len(lista2):
        mult = 0

        for i in range(len(lista1)):
            mult += lista1[i] * lista2[i]
        
        return mult
    else:
        raise ValueError('Las listas deben ser del mismo largo')

multVector([1, 2, 3], [0, 1, 1])

def eliminarRepetidas(lista, elemento):
    listaNueva = []

    for num in lista:
        if num != elemento:
            listaNueva.append(num)

    return listaNueva

def contarNotas(notas):
    resultado = notas
    cuenta = []

    # Solo una aparicion
    for nota in notas:
        notas = eliminarRepetidas(notas, nota)
        notas.append(nota)

    # Contar
    for nota in notas:
        cuenta.append((nota, resultado.count(nota)))

    return cuenta

contarNotas([100, 875, 480, 560, 480, 875, 100, 100, 575, 480, 480])

def listarIndices(num, lista):
    indices = []

    """
    for i in range(len(lista)):
        if num == lista[i]:
            indices.append(i)
    """

    for i, valor in enumerate(lista):
        if num == valor:
            indices.append(i)
    
    return indices

listarIndices("uno", ["dos", "uno", "dos", "tres", "uno", "uno"])

def obtenerPositivosNegativos(lista):
    positivos = []
    negativos = []

    for num in lista:
        if num < 0:
            negativos.append(num)
        else:
            positivos.append(num)
    
    return [positivos, negativos]

obtenerPositivosNegativos([4, 2, 0, -15, -17, -1, 2, 8, -4, -2])

"""# Matrices"""

A = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12]]

A.append([12, 13, 14, 15])

A

A[0]

A[0][2]

for fila in A:
    for columna in fila:
        print(columna, end='\t')
    print()

for i in range(len(A)):
    for j in range(len(A[0])):
        print(f'A[{i}][{j}] = {A[i][j]}')

import random


def crearMatriz(filas, cols):
    A = []

    for i in range(filas):
        fila = []

        for j in range(cols):
            fila.append(random.randint(0, 9))
        
        A.append(fila)
    
    return A

def sumarMatrices(A, B):
    suma = []

    for i in range(len(A)):
        fila = []

        for j in range(len(B[i])):
            fila.append(A[i][j] + B[i][j])
        
        suma.append(fila)
    
    return suma

A = crearMatriz(2, 3)
B = crearMatriz(2, 3)
print(A)
print(B)
suma = sumarMatrices(A, B)
print(suma)

"""# Diccionarios"""

diccionario = {}
diccionario

diccionario['llave'] = 'valor'
diccionario

diccionario['salut'] = 'hola'
diccionario

diccionario['salut']

diccionario['manzana']

diccionario['salut'] = 23
diccionario

del diccionario['salut']

del diccionario

diccionario

diccionario = {'salut': 'hola', 'apple': 'manzana', 'hunger': 'hambre'}
diccionario

diccionario.values()

diccionario.keys()

diccionario.items()

for key in diccionario:
    print(key, diccionario[key])

for key in diccionario.keys():
    print(key, diccionario[key])

for key, value in diccionario.items():
    print(key, value)

diccionario2 = {2: 'dos', 3: 'tres', 4: 'cuatro'}
diccionario2

diccionario['dict'] = diccionario2

diccionario

elementos = (('one', 1), ('two', 2), ('three', 3))
dict(elementos)

del diccionario['dict']

diccionario

diccionario['apple'] = 'pommes'

diccionario

diccionario['apple'] = []
diccionario['apple'].append('manzana')
diccionario['apple'].append('pommes')

diccionario

diccionario.copy()

diccionario.clear()

diccionario

ciudades = {'Cartago': }