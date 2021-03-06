# -*- coding: utf-8 -*-
"""Tutoría Semana 11

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BWn6JintMgSHA7fIpFJ7zeDgMME0zwHh

# **Tuplas**
"""

tupla = ()
print(tupla)

tupla = (1,)
print(tupla)

tupla = (1, 2, 3, 4, 5, 6)
print(tupla)

tupla[0] = 10

tupla = (10,) + tupla[1:]
print(tupla)

i = 3
elemento = 5

tupla = tupla[:i] + (elemento,) + tupla[i+1:]
print(tupla)

def modificarEnTupla(tupla, i, elemento):
    tupla = tupla[:i] + (elemento,) + tupla[i+1:]
    return tupla

print(modificarEnTupla((1, 2, 3, 4, 5, 6), 2, 5))

def insertarEnTupla(tupla, i, elemento):
    return tupla[:i] + (elemento,) + tupla[i:]

print(insertarEnTupla((1, 2, 3, 4, 5, 6), 3, 5))

def eliminarEnTuplaPorPosicion(tupla, i):
    return tupla[:i] + tupla[i+1:]

print(eliminarEnTuplaPorPosicion((1, 2, 3, 4, 5, 6), 3))

def eliminarEnTuplaPorElemento(tupla, elemento):
    for i in range(len(tupla)):
        if tupla[i] == elemento:
            return tupla[:i] + tupla[i+1:]

    return tupla

print(eliminarEnTuplaPorElemento((1, 2, 3, 4, 5, 6), 3))

def popTupla(tupla, pos=len(tupla)-1):
    elemento = tupla[pos]
    tupla = tupla[:pos] + tupla[pos+1:]

    return tupla, elemento

nuevaTupla, eliminado = popTupla((1, 2, 3, 4, 5, 6), 3)
print(nuevaTupla, eliminado)

nuevaTupla, eliminado = popTupla((1, 2, 3, 4, 5, 6))
print(nuevaTupla, eliminado)

"""# **Programación Orientada a Objetos (POO)**

```python
class NombreClase:
    def __init__(self):
        # Inicializo los atributos
    
    # Metodo -> Son acciones que pueden realizar los objetos
    def hacerAlgo(self):
        pass
```
"""

class Persona:
    def __init__(self, pnombre, papellidos, pedad, lugar='Cartago'):
        self.nombre = pnombre
        self.apellidos = papellidos
        self.edad = pedad
        self.lugar = lugar
        self.hijos = []
    
    def __str__(self):
        # Siempre debe devolver un string
        return f'Mi nombre es {self.nombre} {self.apellidos}\n' +\
               f'Tengo {self.edad} años\nY vivo en {self.lugar}'
    
    def presentarse(self):
        print(f'Mi nombre es {self.nombre} {self.apellidos}')
        print(f'Tengo {self.edad} años')
        print(f'Y vivo en {self.lugar}')
    
    def agregarHijos(self, hijo):
        self.hijos.append(hijo)
    
    def verHijos(self):
        for hijo in self.hijos:
            print(hijo, '\n')

pErick = Persona('Erick Andres', 'Obregon Fonseca', 22, 'San Jose')
pMaria = Persona('Maria', 'Ortiz', 19, 'Guanacaste')

pErick.presentarse()
pMaria.presentarse()

pErick.lugar = 'Cartago'
pErick.edad += 1

pErick.presentarse()
pMaria.presentarse()

pErick.agregarHijos(pMaria)
pErick.agregarHijos(pMaria)
pErick.agregarHijos(pMaria)
print(pErick)
print(pMaria)

pErick.verHijos()

class Estudiante:
    def __init__(self, nombre, apellidos, carnet):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__carnet = carnet
    
    def getNombre(self):
        return self.__nombre

    def getApellidos(self):
        return self.__apellidos

    def getCarnet(self):
        return self.__carnet

    def setNombre(self, nuevoNombre):
        self.__nombre = nuevoNombre

    def setApellidos(self, nuevoApellidos):
        self.__apellidos = nuevoApellidos

    def setCarnet(self, nuevoCarnet):
        self.__carnet = nuevoCarnet

eErick = Estudiante('Erick', 'Obregon', 2016123157)
eErick.setNombre('Erick Andres')
eErick.setApellidos('Obregon Fonseca')
print(eErick.getNombre())
print(eErick.getApellidos())
print(eErick.getCarnet())

"""## **Sobre carga de operadores**

Algunas funcionalidades genéricas que pueden ser sobre cargadas

| Sr.No. | Method, Description & Sample Call |
|--------|-----------------------------------|
|   1    | \_\_init\_\_(self [,args...]) <br> Constructor (with any optional arguments <br> Sample Call : obj = className(args) |
|   2    | \_\_del\_\_(self) <br> Destructor, deletes an object <br> Sample Call : del obj |
|   3    | \_\_repr\_\_(self) <br> Evaluatable string representation <br> Sample Call : repr(obj) |
|   4    | \_\_str\_\_(self) <br> Printable string representation <br> Sample Call : str(obj) |
|   5    | \_\_cmp\_\_(self, x) <br> Object comparison <br> Sample Call : cmp(obj, x)

### **Operadores**
| **Operator** | **Method** |
| ------------ | ---------- |
|     a + b    | \_\_add\_\_(self, other) |
|     a - b    | \_\_sub\_\_(self, other) |
|     a * b    | \_\_mul\_\_(self, other) |
|     a @ b    | \_\_matmul\_\_(self, other) |
|     a \   b  | \_\_truediv\_\_(self, other) |
|     a _\_\ b   |   \_\_floordiv\_\_(self, other)    |
|     a % b    |      \_\_mod\_\_(self, other)      |
| divmod(a, b) |    \_\_divmod\_\_(self, other)     |
|     a ** b   | \_\_pow\_\_(self, other[, modulo]) |
|     a << b   | \_\_lshift\_\_(self, other) |
|     a >> b   |  \_\_rshift\_\_(self, other) |
|     a & b    |  \_\_and\_\_(self, other) |
|     a ^ b    |  \_\_xor\_\_(self, other) |
|     a \| b    |  \_\_or\_\_(self, other) |
|     a ~ b    |  \_\_not\_\_(self, other) |
"""

class Cuadrado:
    def __init__(self, lado):
        self.__lado = lado
    
    def __str__(self):
        return f'<Lado: {self.__lado}cm>'
    
    def __add__(self, cuadrado):
        nuevoLado = self.__lado + cuadrado.getLado()
        return Cuadrado(nuevoLado)
    
    def __sub__(self, cuadrado):
        nuevoLado = abs(self.__lado - cuadrado.getLado())
        return Cuadrado(nuevoLado)
    
    def __mul__(self, elemento):
        nuevoLado = 0
        
        if isinstance(elemento, Cuadrado):
            nuevoLado = self.__lado * elemento.getLado()
        elif isinstance(elemento, (int, float)):
            nuevoLado = self.__lado * elemento
        else:
            raise TypeError(f'Unsupported operand type(s) for *: {type(self)} and {type(elemento)}')

        return Cuadrado(nuevoLado)

    def getLado(self):
        return self.__lado

    def setLado(self, lado):
        self.__lado = lado
    
    def calcularArea(self):
        return self.__lado * self.__lado # lado**2

cuadrado1 = Cuadrado(10)
print(cuadrado1)
print(cuadrado1.calcularArea())

cuadrado2 = Cuadrado(15)
print(cuadrado2)
print(cuadrado2.calcularArea())

cuadradoSuma = cuadrado1 + cuadrado2
print(cuadradoSuma)
print(cuadradoSuma.calcularArea())

cuadradoResta = cuadrado1 - cuadrado2
print(cuadradoResta)
print(cuadradoResta.calcularArea())

cuadradoMult = cuadrado1 * cuadrado2
print(cuadradoMult)
print(cuadradoMult.calcularArea())

cuadradoMult2 = cuadrado1 * 2
print(cuadradoMult2)
print(cuadradoMult2.calcularArea())

cuadradoMult2 = cuadrado1 * []
print(cuadradoMult2)
print(cuadradoMult2.calcularArea())

cuadradoSuma = cuadrado1 + 2

from random import randint


class Matriz:
    def __init__(self, filas, columnas, menor=0, mayor=9):
        self.__filas = filas
        self.__columnas = columnas
        self.__matriz = [[randint(menor, mayor) for _ in range(columnas)] for _ in range(filas)]

    def mostrarMatriz(self):
        # Recorremos filas
        for i in range(self.__filas):
            # Recorremos columnas
            for j in range(self.__columnas):
                print(self.__matriz[i][j], end='\t')
            print()

    def getFilas(self):
        return self.__filas

    def getColumnas(self):
        return self.__columnas
    
    def setValor(self, i, j, elemento):
        self.__matriz[i][j] = elemento
    
    def getValor(self, i, j):
        return self.__matriz[i][j]

    def __add__(self, matriz):
        # Validar que la matriz tenga las mismas dimensiones
        if self.__filas != matriz.getFilas() or self.__columnas != matriz.getColumnas():
            raise ValueError('No se pueden sumar matrices de diferente tamaño.')

        # Resultado de la suma de las matrices
        suma = Matriz(self.__filas, self.__columnas)

        # Recorremos filas
        for i in range(self.__filas):
            # Recorremos columnas
            for j in range(self.__columnas):
                # Sumamos
                suma.setValor(i, j, self.__matriz[i][j] + matriz.getValor(i, j))
        
        return suma

A = Matriz(5, 5, menor=5)
B = Matriz(5, 5, mayor=100)
C = A + B

A.mostrarMatriz()
print()
B.mostrarMatriz()
print()
C.mostrarMatriz()