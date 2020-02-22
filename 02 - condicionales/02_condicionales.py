'''
Ejemplos para las tutorias de los cursos de:
Introduccion a la programacion     CE1101
Taller de programacion             CE1102
Introduccion a la programacion     IC1802
Taller de programacion             IC1803
Elementos de la computacion        CA2125
Taller I                           CO4108

Erick Andres Obregon Fonseca
Ing. en Computadores
erickobregonf@gmail.com

Ejemplos de uso de condicionales, operadores logicos y aritmeticos

Conocimientos previos
-Booleanos (True, False)
-Entrada y salida de datos (input, print)
-Operadores relacionales (<, >, ==, <=, >=, !=)
-Operadores logicos (and, or, not)
-Operadores aritmeticos (+, -, *, /, //, **, %)

###############################
Estructura de los condicionales
if condicion1:
    # Bloque de codigo si se cumple la condicion1
elif condicion2:
    # Bloque de codigo si se cumple la condicion2
.
.
.
else:
    # Bloque de codigo si no se cumple alguna de las condiciones anteriores
'''


print('Ejemplo1')
# El if se ejecuta si la condicion es verdadera, como True siempre es
# verdadero el if siempre se ejecuta
if True:
    print('La condicion es verdadera')


print('\nEjemplo2') # Verificar si dos numeros son iguales
# Pedir dos numeros al usuario
num1 = int(input('Ingrese un numero: '))
num2 = int(input('Ingrese otro numero: '))
# Validar si los numeros son iguales
if num1 == num2:
    print(num1, 'es igual a', num2)
# Si los numeros son diferentes el else se ejecuta
else:
    print(num1, 'es diferente de', num2)


print('\nEjemplo3') # Mostrar el mayor de dos numeros
# Pedir dos numeros al usuario
num1 = int(input('Ingrese un numero: '))
num2 = int(input('Ingrese otro numero: '))
# Validar si el primer numero es mayor que el segundo
if num1 > num2:
    print(num1, '>', num2)
# Validar si el segundo numero es mayor que el primero
elif (num1 < num2):
    print(num2, '>', num1)
# Si ninguna de las anteriores se cumple
# Significa que los numeros son iguales
else:
    print(num1, 'no es mayor ni menor que', num2, 'es igual')


print('\nEjemplo4')
'''
Verificar si, dados tres numeros,
se cumple alguna de las siguientes condiciones:
1. Si el tercer numero es el resultado de la suma de los cuadrados de
los primeros dos numeros
2. Si el tercer numero es el resultado de la diferencia de los
cuadrados de los primeros dos numeros
3. Si el tercer numero es el resultado de la multiplicacion de los
primeros dos numeros
4. Si el tercer numero es el resultado de la division de los primeros
dos numeros
5. Si el tercer numero es el residuo de la division de los primeros
dos numeros
6. Si el tercer numero es resultado de la division entera de los
primeros dos numeros
7. Si no cumple ninguna
'''
# Pedir los tres numeros al usuario
num1 = int(input('Ingrese el primer numero: '))
num2 = int(input('Ingrese el segundo numero: '))
num3 = int(input('Ingrese el resultado: '))
# Validar la primer condicion
if num1 ** 2 + num2 ** 2 == num3:
    print(num1, '** 2', '+', num2, '** 2 =', num3)
# Validar la segunda condicion
elif num1 ** 2 - num2 ** 2 == num3:
    print(num1, '** 2', '-', num2, '** 2 =', num3)
# Validar la tercer condicion
elif num1 * num2 == num3:
    print(num1, '*', num2, '=', num3)
# Validar la cuarta condicion
elif num1 / num2 == num3:
    print(num1, '/', num2, '=', num3)
# Validar la quinta condicion
elif num1 % num2 == num3:
    print(num1, '%', num2, '=', num3)
# Validar la sexta condicion
elif num1 // num2 == num3:
    print(num1, '//', num2, '=', num3)
# Si no se cumplio ninguna de las condiciones anteriores se ejecuta el else
else:
    print('No cumple ninguna condicion')


print('\nEjemplo5') # Condicionales anidados
# Pedir un numero entre 1 y 10
num = int(input('Ingrese un numero entre 1 y 10: '))
# Verificar si el numero es par
if num % 2 == 0:
    # Verificar si el numero es primo
    if num == 2:
        print('El numero es par y primo')
    else:
        print('El numero es par y no primo')
# El numero es impar
else:
    # Verificar si el numero es primo
    if num == 3:
        print('El numero es impar y primo')
    elif num == 5:
        print('El numero es impar y primo')
    elif num == 7:
        print('El numero es impar y primo')
    # El numero no es primo
    else:
        print('El numero no es par ni primo')
'''
NOTA:
a. Note que, entre 1 y 10, y en general, el unico numero primo y par es 2,
por eso solo ese se valida si es primo
b. Note que entre 1 y 10 los numeros 3, 5 y 7 son primos e impares
Recuerde que 1 no es primo, por definicion:
'Un numero primo es aquel que es divisible entre 1 y el mismo excluyendo al 1'
'''

print('\nEjemplo6') # Operador or
# Pedir un numero
num = int(input('Ingrese un numero entre 1 y 10: '))
# Verificar si el numero es primo
if (num == 2) or (num == 3) or (num == 5) or (num == 7):
    print(num, 'es primo')
# Si no es primo se ejecuta el else
else:
    print(num, 'no es primo')


print('\nEjemplo7') # Operador and
# Pedir un numero
num1 = int(input('Ingrese un numero: '))
num2 = int(input('Ingrese otro numero: '))
# Verificar si el primer numero es mayor que el segundo
# y si ademas el primer numero es par
if (num1 > num2) and (num1 % 2 == 0):
    print(num1, '>', num2, '\nY', num1, 'es par')
# Verificar si el primer numero es menor que el segundo
# y si ademas el primer numero es par
elif (num1 < num2) and (num1 % 2 == 0):
    print(num1, '<', num2, '\nY', num1, 'es par')
# Verificar si el primer numero es mayor que el segundo
# y si ademas el primer numero es impar
elif (num1 > num2) and (num1 % 2 != 0):
    print(num1, '>', num2, '\nY', num1, 'es impar')
# Verificar si el primer numero es menor que el segundo
# y si ademas es impar
elif (num1 < num2) and (num1 % 2 != 0):
    print(num1, '<', num2, '\nY', num1, 'es impar')
# Si no se cumple ninguna condicion
else:
    print('No se evaluan mas condiciones')


print('\nEjemplo8') # Pedir valor bool
# Pedir valor
cierto = bool(int(input('Ingrese 1 para True y 0 para False: ')))
# Validar si el valor es True
if cierto:
    print('Verdadero')
# Si no es True, es False
else:
    print('Falso')

print('\nEjemplo9') # Operador not
# Pedir valor
cierto = bool(int(input('Ingrese 1 para True y 0 para False: ')))
# Si el valor es False se niega y cambia su valor a True
if not cierto:
    print('False ahora es True')
# Si el valor es True se niega y cambia su valor a False
else:
    print('True ahora es False')

# Fin de los ejemplos
# Modifique los ejemplos anteriores para probar nuevas cosas
