# -*- coding: utf-8 -*-
"""03 - Entrada y Salida de Datos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17UW8vmtuLF0sy0Vx9YLYhM7Y9JthFG7_

# **Entrada**

Para la entrada de datos vía consola usamos la función pre construida de Python
```python
input()
```
la cual siempre nos devolverá un string sin importar el dato que ingresemos.
"""

input('Ingrese una cadena: ')

input('Ingrese un número entero: ')

input('Ingrese un número decimal: ')

input('Ingrese un número complejo: ')

"""Note que los valores anteriores están encerrados entre comillas, lo cual nos
indica que es valor de tipo string.

Para recibir un tipo de dato no string, convertimos lo que nos devuelve la
función
```python
input()
```
al tipo de datos que queremos.
"""

int(input('Ingrese un número entero: '))

float(input('Ingrese un número decimal: '))

complex(input('Ingrese un número complejo: '))

"""Opcionalmente, podemos usar la función pre construida de Python
```python
eval(x)
```
la cual se encarga de convertir al tipo de datos correspondiente.
"""

eval(input('Valor: '))

eval(input('Valor: '))

eval(input('Valor: '))

"""También, podemos saber el tipo de dato que estamos trabajando usando la función
pre construida de Python
```python
type(obj)
```
"""

type(23)

type(43.12)

type('Hola')

type(1+3j)

type([1, 2, 3])

type((1, 2, 3))

type({1, 2, 3})

type({'hola': 1, 'adios': 2, 'pato': 3})

valor = eval(input('Valor: '))
type(valor)

"""# **Salida**

Para la salida de datos vía consola, usamos la función preconstruida de Python
```python
print(...)
```
"""

print('Hola')

print(2)

print(43.5)

print([1, 2, 3])

print((1, 2, 3))

print({1, 2, 3})

print({'hola': 1, 'adios': 2, 'pato': 3})

print(1+3j)

"""## **Darle estilo a la salida**

Tenemos diferentes formas de darle un formato fancy a la salida:

### 1. print(f" ")

Antes de imprimir nuestros datos podemos colocar *f* o *F* antes de abrir
comillas, lo cual nos permite colocar expresiones de Python entre { y } que
pueden referirse a variables o valores.
"""

num1 = 10
num2 = 20
suma = num1 + num2
print(f'{num1} + {num2} = {suma}')

num1 = 10
num2 = 20
print(f'{num1} + {num2} = {num1 + num2}')

print(f'{10} + {20} = {30}')

print(f'{10} + {20} = {10 + 20}')

"""### 2. str.format()

Este método lleva un poco más de trabajo que el anterior. Se usan *{}*, las cuales serán sustituidas en orden por cada una de los valores datos en el
*format*.
"""

num1 = 42
num2 = 13
div = num1 / num2
print('{} / {} = {}'.format(num1, num2, div))

"""Observe el resultado enterior, tiene muchos decimales, podríamos indicar la
cantidad de decimales que queremos de la siguiente manera:
"""

num1 = 42
num2 = 13
div = num1 / num2
print('{} / {} = {:.3}'.format(num1, num2, div))

"""También podemos indicar porcentajes"""

print('{:.1%}'.format(0.1))

"""### 3. Separación por comas

Podemos separar cada valor que queremos imprimir por una coma.
"""

print('Hola', 23, 43.12)

"""#### 4. Concatenación

Podemos imprimir realizando una concatención de valores. Hay que tener cuidado
de que todos los datos deben ser de tipo string para que no dé error. Esto debido a que solo se puede concatener string con string.
"""

num1 = 10
num2 = 20
suma = num1 + num2
print(str(num1) + ' + ' + str(num2) + ' = ' + str(suma))

"""## **Cambiar el final de línea**

Observe el siguiente código:
"""

print('Hola')
print(23)
print(43.12)

"""Note que cada *print* escribe en una nueva línea. Esto se debe a un parámetro
llamado *end*, el cual podemos cambiar por lo que queramos.
"""

print('Hola', end='\n')
print(23, end='\n')
print(43.12, end='\n')

print('Hola', end='\t')
print(23, end='\t')
print(43.12, end='\t')

print('Hola', end='---')
print(23, end='---')
print(43.12, end='---')

"""**Nota:** ¿No entiende para qué sirve *\n* y *\t*? [Esto podría ayudarle](https://docs.python.org/2.0/ref/strings.html).

## **Cambiar la separación de los valores**

Observe el siguiente código:
"""

print('Hola', 23, 43.12)

"""Cuando hacemos un *print* en Python, separando los valores por coma, por
defecto, cada valor es separado mediante un espacio. Esto se debe a un
parámetro en Python llamado *sep*, el cual podemos cambiar por lo que nosotros
queramos.
"""

print('Hola', 23, 43.12, sep=' ')

print('Hola', 23, 43.12, sep='')

print('Hola', 23, 43.12, sep='---')

print('Hola', 23, 43.12, sep='\t')

print('Hola', 23, 43.12, sep='***')

"""# **Sep y end juntos**"""

print('Hola', 23, 43.12, sep='***', end='-')
print('Hola', 23, 43.12, sep='**', end='--')
print('Hola', 23, 43.12, sep='*', end='---')