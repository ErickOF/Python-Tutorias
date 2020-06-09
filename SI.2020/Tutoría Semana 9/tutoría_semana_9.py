# -*- coding: utf-8 -*-
"""Tutoría Semana 9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FVLHsCVcJHYXo1PO5OzCoadWViB-Oaab

# Cadenas
"""

cadena = 'AbcdkdkjsidusfoijsSDFHISDFJ143827!'

cadena[0]

cadena[len(cadena) - 1]

cadena[-1]

cadena[2:5]

cadena[:5]

cadena[10:]

cadena[:]

cadena[2:10:2]

cadena[::-1]

def esPalindromo(cadena):
    #if cadena == cadena[::-1]:
    #    return True
    #else:
    #    return False
    return cadena == cadena[::-1]

esPalindromo('Hola')

esPalindromo('ana')

esPalindromo('Ana')

'Ana'.lower()

nombre = 'Ana'
nombre = nombre.lower()
nombre

nombre = 'Ana'
nombre = nombre.upper()
nombre

nombre = 'Ana'
print(nombre.islower())

nombre = 'ANA'
print(nombre.isupper())

cadena = 'Hola 123'
print(cadena, cadena.isalpha())
print(cadena[:4], cadena[:4].isalpha())

cadena = 'Hola 123'
print(cadena, cadena.isnumeric())
print(cadena[5:], cadena[5:].isnumeric())

cadena = 'Hola 123'
print(cadena, cadena.isdigit())
print(cadena[5:], cadena[5:].isdigit())
cadena.isdigit()

cadena = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'
cadena.split('.')

cadena = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'
cadena.replace(' ', '-')

cadena = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'
cadena.replace(' ', '').replace('d', 't')

cadena = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'
letras = [c for c in cadena]
letras

cadena = 'Erick'
cadena += '!'
print(cadena)

cadena = 'Erick'
cadena[0] = 'e'

cadena = 'Erick'
cadena = 'e' + cadena[1:]
print(cadena)

cadena = 'ERick'
letra = 'r'

if letra not in cadena:
    print('La letra no existe')
else:
    cadena = cadena.replace('r', 'R')

print(cadena)

def obtenerPosicion(cadena, caracter):
    cadena = cadena.lower()
    caracter = caracter.lower()

    if caracter not in cadena:
        return []
    else:
        posiciones = []

        for i in range(len(cadena)):
            if cadena[i] == caracter:
                posiciones.append(i)
        
        return posiciones

obtenerPosicion('skdfjghslSSSdfkksdkfhgs', 's')

def obtenerPosicionPila(cadena, caracter):
    if caracter not in cadena:
        return []
    else:
        return obtenerPosicionPilaAux(cadena.lower(), caracter.lower(), 0)

def obtenerPosicionPilaAux(cadena, caracter, i):
    if i == len(cadena):
        return []
    else:
        if cadena[i] == caracter:
            return [i] + obtenerPosicionPilaAux(cadena, caracter, i + 1)
        else:
            return obtenerPosicionPilaAux(cadena, caracter, i + 1)

obtenerPosicionPila('skdfjghslSSSdfkksdkfhgs', 's')

def obtenerPosicionCola(cadena, caracter):
    if caracter not in cadena:
        return []
    else:
        return obtenerPosicionColaAux(cadena.lower(), caracter.lower(), 0, [])

def obtenerPosicionColaAux(cadena, caracter, i, posiciones):
    if i == len(cadena):
        return posiciones
    else:
        if cadena[i] == caracter:
            return obtenerPosicionColaAux(cadena, caracter, i + 1, posiciones + [i])
        else:
            return obtenerPosicionColaAux(cadena, caracter, i + 1, posiciones)

print(obtenerPosicionCola('skdfjghslSSSdfkksdkfhgs', 's'))

def eliminarCaracter(cadena, caracter, n):
    if caracter not in cadena:
        return cadena
    else:
        return eliminarCaracterAux(cadena, caracter, n, '')

def eliminarCaracterAux(cadena, caracter, n, resultado):
    if cadena == '' or n == 0:
        return resultado + cadena
    else:
        if cadena[0].lower() == caracter.lower():
            return eliminarCaracterAux(cadena[1:], caracter, n - 1, resultado)
        else:
            return eliminarCaracterAux(cadena[1:], caracter, n, resultado + cadena[0])

print(eliminarCaracter('skdfjghslSSSdfkksdkfhgs', 's', 10))

"""# Archivos
```python
archivo = open(nombre_archivo, modo)
```

## Modo:
* r (read)   - Leer
* w (write)  - Sobre escribir
* a (append) - Leer y escribir agregando nuevo texto
* b (bytes)  - Hacer una operación en bytes

### Ejemplos
* rb - Leer en bytes
* wb - Escribir en bytes
* ab - Agregar en bytes
"""

archivo = open('notas.txt', 'r')
# Contenido del archivo como un texto
contenido = archivo.read()
archivo.close()

print(contenido)

archivo = open('ej.txt', 'r')
# Contenido del archivo como un texto
contenido = archivo.readlines()
archivo.close()

print(contenido)

archivo = open('ej.txt', 'r')
# Contenido del archivo como un texto
contenido = archivo.read()
archivo.close()

lineas = contenido.split('\n')
print(lineas)

archivo = open('sample_data/README.txt', 'w')
archivo.write('Hoy por la mañana...\n')
archivo.close()

archivo = open('sample_data/README.txt', 'a')
archivo.write('Me levanté muy cansado...')
archivo.close()

contenido = ['Hola\n', 'Adios\n', 'Saludos']

archivo = open('ej.txt', 'w')
archivo.writelines(contenido)
archivo.close()

palabras = []

cantidad = int(input('Digite la cantidad de palabras a ingresar: '))

for i in range(cantidad):
    palabra = input('Ingrese una palabra: ')
    palabras.append(palabra + '\n')

nombre = input('Ingrese el nombre del archivo donde guardar las palabras: ')

archivo = open(nombre, 'w')
archivo.writelines(palabras)
archivo.close()

palabras = []

cantidad = int(input('Digite la cantidad de palabras a ingresar: '))

for i in range(cantidad):
    palabra = input('Ingrese una palabra: ')
    palabras.append(palabra)

nombre = input('Ingrese el nombre del archivo donde guardar las palabras: ')

contenido = '\n'.join(palabras)
print(contenido)

archivo = open(nombre, 'w')
archivo.write(contenido)
archivo.close()

def leerArchivo(nombre):
    archivo = open(nombre, 'r')
    contenido = archivo.read()
    archivo.close()
    
    return contenido

def limpiarContenido(contenido):
    notas = []
    
    for nota in contenido.split('\n'):
        nota = nota.split(',')
        diccionario = {'Nombre': nota[0], 'Materia': nota[1], 'Nota': float(nota[2])}
        notas.append(diccionario)

    return notas

def promedioGeneral(notas):
    suma = 0

    for nota in notas:
        suma += nota['Nota']
    
    return suma / len(notas)

def promedioPorEstudiante(notas):
    promedio = {}

    for nota in notas:
        nombre = nota['Nombre']

        if nombre not in promedio:
            promedio[nombre] = {'suma': nota['Nota'], 'cantidad': 1}
        else:
            promedio[nombre]['suma'] += nota['Nota']
            promedio[nombre]['cantidad'] += 1
    
    return promedio

def promedioPorMateria(notas):
    promedio = {}

    for nota in notas:
        materia = nota['Materia']

        if materia not in promedio:
            promedio[materia] = {'suma': nota['Nota'], 'cantidad': 1}
        else:
            promedio[materia]['suma'] += nota['Nota']
            promedio[materia]['cantidad'] += 1
    
    return promedio

nombre = input('Ingrese el nombre del archivo con las notas: ')

contenido = leerArchivo(nombre)

notas = limpiarContenido(contenido)

promedio = promedioGeneral(notas)
promedioEstudiantes = promedioPorEstudiante(notas)
promedioMaterias = promedioPorMateria(notas)

print(notas)
print(f'Promedio General: {promedio}\n')

for estudiante in promedioEstudiantes:
    nota = promedioEstudiantes[estudiante]
    print(f'Promedio de {estudiante} es: {nota["suma"] / nota["cantidad"]}')

print()

for materia in promedioMaterias:
    nota = promedioMaterias[materia]
    print(f'Promedio de {materia} es: {nota["suma"] / nota["cantidad"]}')