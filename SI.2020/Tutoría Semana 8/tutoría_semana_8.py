# -*- coding: utf-8 -*-
"""Tutoría Semana 8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VsA4xVigUR8tcEGbIDlMOv6kjsAoKT4K

# Separar cadenas con
```python
str.split()
```
"""

cadena = "Hola soy Erick"

cadena.split()

cadena.split(' ')

cadena.split('a')

cadena = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

cadena.split()

cadena.split(',')

cadena.splitlines()

cadena2 = 'Hola soy Erick\nAdios Juana\nComer dulces\nManzanas rojas\n'

cadena2.splitlines()

cadena2.split('\n')

cadena.split('m')

"""# Listas"""

lista = []

lista = [1, 2, 3, 4, 5, ...]

lista = ['hola', 'adios', 'salud', ...]

lista = [1, 2, 'hola', [1, 2, 3], {'hola': 23}, {1, 2, 3}]

lista[0]

lista[1]

lista[3]

len(lista)

for i in range(len(lista)):
    print(i, lista[i])

i = 0
for elemento in lista:
    print(i, elemento)
    i += 1

for i, elemento in enumerate(lista):
    print(i, elemento)

impares = [1, 3, 5, 7,  9, 11, 13, 15]
pares   = [2, 4, 6, 8, 10, 12, 14, 16, 18]

for i in range(len(impares)):
    print(i, pares[i], impares[i])

for par, impar in zip(pares, impares):
    print(par, impar)

vector1 = [0, 6, 3]
vector2 = [2, -1, 5]
suma = []

for i in range(len(vector1)):
    suma.append(vector1[i] + vector2[i])

print(suma)

lista = []
lista.insert(0, 'hola')
print(lista)

lista.insert(1000, 'adios')

print(lista)

lista.pop()

lista = [1, 2, 3, 4, 5]
eliminado = lista.pop()

print(eliminado, lista)

lista = [1, 2, 3, 4, 5]
eliminado = lista.pop(0)

print(eliminado, lista)

lista = [1, 2, 3, 4, 5]
lista.pop()

print(lista)

lista = [1, 0, 2, 6, 3, 4, 5]
lista.remove(6)

print(lista)

lista = [1, 0, 2, 6, 3, 4, 5]
lista[0:3]

lista = [1, 0, 2, 6, 3, 4, 5]
lista[:3]

lista = [1, 0, 2, 6, 3, 4, 5]
lista[2:]

lista[:]

lista[:100000]

lista[-1]

lista[-2]

lista = [1, 0, 2, 6, 3, 4, 5]

for i in range(-1, -len(lista) - 1, -1):
    print(i, lista[i])

lista = [1, 0, 2, 6, 3, 4, 5]
lista[::-1]

lista = [1, 0, 2, 6, 3, 4, 5]
lista[::2]

lista[inicial:final:paso]

lista[1::2]

print(lista)
lista = lista + [2]
print(lista)

lista += [3]

print(lista)

lista = [0, 1, 2, 3, 4, 5, 6, 7]
i = 6

lista = lista[:i] + lista[i+1:]
print(lista)

lista = [0, 1, 2, 3, 4, 5, 6, 7]
i = 100000000
num = 1000

lista = lista[:i] + [num] + lista[i:]
print(lista)

def insertar(indice, num, lista):
    if indice < 0:
        return [num] + lista
    elif indice >= len(lista):
        return lista + [num]

    nuevaLista = []

    for i in range(len(lista)):
        if i == indice:
            nuevaLista += [num]
        nuevaLista += [lista[i]]
    
    return nuevaLista

lista = [0, 1, 2, 3, 4, 5, 6, 7]
i = 1000
num = 1000

print(insertar(i, num, lista))

impares = [1, 3, 5, 7,  9, 11, 13, 15]
pares   = [2, 4, 6, 8, 10, 12, 14, 16, 18]

lista = impares + pares
print(lista)

def insertarEnOrden(num, lista):
    if lista == []:
        return [num]
    elif lista[0] > num: # Opcional
        return [num] + lista
    elif lista[-1] < num:
        return lista + [num]
    
    for i in range(len(lista)):
        if lista[i] > num:
            lista = lista[:i] + [num] + lista[i:]
            break

    return lista

import random

numeros = [random.randint(-20, 20) for _ in range(10)]
listaNueva = []

for num in numeros:
    listaNueva = insertarEnOrden(num, listaNueva)

print(listaNueva)

import datetime

print(datetime.datetime.now())

frase = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
frase = frase.replace(',', '')
frase = frase.replace('.', '')
frase = frase.lower()
palabras = frase.split()

palabrasSinRepetir = list(set(palabras))

for palabra in palabrasSinRepetir:
    cantidad = palabras.count(palabra)
    print(f'{palabra}: {cantidad}')

def sumar(num):
    suma = 0

    for i in range(1, num + 1):
        suma += i
    
    return suma

sumar(10)

