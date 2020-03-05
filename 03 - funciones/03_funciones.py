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

Ejemplos creacion de funciones

Conocimientos previos
-Los temas evaluados en los ejemplos anteriores
-Funcionamiento del return en una funcion
-Que es un parametro
-Diferencias entre variables locales y globales

#################################################
Estructura de una funcion que no recibe parametro
y no retorna valores
def funcion():
    # Bloque de codigo

Estructura de una funcion que no recibe parametros
pero retorna un dato
def funcion():
    # Bloque de codigo
    return dato

Estructura de una funcion que no recibe parametros
pero retorna mas de un dato
def funcion():
    # Bloque de codigo
    return dato, dato2, dato3, ..., dato_n

Estructura de una funcion que recibe un parametro
pero no retorna valores
def funcion(parametro):
    # Bloque de codigo

Estructura de una funcion que recibe mas de un parametro
pero no retorna valores
def funcion(parametro, parametro2, ..., parametro_n):
    # Bloque de codigo

Estructura de una funcion que recibe mas de un parametro
y retorna un dato
def funcion(parametro, parametro2, ..., parametro_n):
    # Bloque de codigo
    return dato

Estructura de una funcion que recibe mas de un parametro
y retorna mas de un dato
def funcion(parametro, parametro2, ..., parametro_n):
    #Bloque de codigo
    return dato, dato2, dato3, ..., dato_m
'''


# Creacion de una funcion que no retorna
print('Ejemplo1')
def saludar():
    print('Hola')

# Llamar la funcion
saludar()


# Creacion de una funcion que retorna un valor
print('\nEjemplo2')
def saludar2():
    return 'Hola'

# Llamar la funcion
print(saludar2())
# Llamar funcion y almacenar el valor en una variable
saludo = saludar2()
print(saludo)


# Creacion de una funcion que suma dos numeros
print('\nEjemplo3')
def sumar(num1, num2):
    print('La suma de', num1, '+', num2, 'es', num1 + num2)

# Pedir los datos
num1 = int(input('Digite el primer numero: '))
num2 = int(input('Digite el segundo numero: '))
# Llamar la funcion
sumar(num1, num2)


# Funcion que retorna la resta de dos numeros
print('\nEjemplo4')
def restar(num1, num2):
    return num1 - num2

# Pedir los datos
num1 = int(input('Digite el primer numero: '))
num2 = int(input('Digite el segundo numero: '))
# Llamar la funcion y almacenar el valor en una variable
resultado = restar(num1, num2)
print('La resta de', num1, '-', num2, 'es', resultado)


# Creacion de una funcion que multiplica dos numeros
print('\nEjemplo5')
def multiplicar():
    # Pedir los numeros
    num1 = int(input('Digite el primer numero: '))
    num2 = int(input('Digite el segundo numero: '))
    print('La multiplicacion de', num1, '*', num2, 'es', num1 * num2)

# Llamar la funcion
multiplicar()


# Funcion que retorna la division de dos numeros
print('\nEjemplo6')
def dividir():
    num1 = int(input('Digite el primer numero: '))
    num2 = int(input('Digite el segundo numero: '))
    return num1 / num2

# Llamar la funcion y almacenar el resultado
resultado = dividir()
print('La resta de', num1, '/', num2, 'es', resultado)


# Creacion de una funcion que pide datos y los retorna
print('\nEjemplo7')
def pedir_datos():
    # Pedir los datos
    nombre = input('Ingrese su nombre: ')
    apellido = input('Ingrese su apellido: ')
    edad = int(input('Ingrese su edad: '))
    # Retornar multiples datos
    return nombre, apellido, edad

# Llamar la funcion y guardar los valores
nombre, apellido, edad = pedir_datos()
# Recuerde el format del archivo 01_entrada_y_salida_de_datos
print('Su nombre es {} {} y su edad {}'.format(nombre, apellido, edad))
print('Su nombre es', nombre, apellido, 'y su edad', edad)


# Llamar funciones dentro de otras
print('\nEjemplo8')
# Version con condicionales 1
def verificar_par1(num):
    # Se verifica si el residuo de dividir el numero entre 2 es 0
    if num % 2 == 0:
        # Si lo es, el numero es par
        return True
    # Si no, es impar
    else:
        return False

# Version con condicionales 2
def verificar_par2(num):
    # Se verifica si el residuo de dividir el numero entre 2 es 0
    if num % 2 == 0:
        # Si lo es, el numero es par
        return True
    # Si no, es impar
    return False

# Version Chuck Norris
def verificar_par3(num):
    # Retorna un booleano si se cumple
    # Pruebe quitando el comentario o en consola la siguiente linea
    #print(num % 2 == 0)
    return num % 2 == 0

# Funcion que pide tres numeros y verifica si son pares
def pedir_numeros():
    num1 = int(input('Digite el primer numero: '))
    num2 = int(input('Digite el segundo numero: '))
    num3 = int(input('Digite el tercer numero: '))
    # Usar la primer funcion para verificar el primer numero es par
    if verificar_par1(num1):
        print(num1, 'es par')
    else:
        print(num1, 'no es par')
    # Usar la segunda funcion para verificar el segundo numero es par
    if verificar_par2(num2):
        print(num2, 'es par')
    else:
        print(num2, 'no es par')
    # Usar la tercera funcion para verificar el tercer numero es par
    if verificar_par3(num3):
        print(num3, 'es par')
    else:
        print(num3, 'no es par')

# Llamar la funcion
pedir_numeros()

'''
NOTA:
Note que las funciones retornan un valor booleano y, ademas, recuerde
que los condicionales funcionan con un valor de True o False, por lo
que no se necesita comparar su valor de retorno con estos ultimos.

Ejemplo:
Suponga que la funcion verificar_primo(num) retorna True o False.
Si nosotros queremos verificar si un numero es primo lo correcto seria:

if verificar_primo(num):
    # Bloque de codigo

y estaria incorrecto hacer:

if verificar_primo(num) == True:
    # Bloque de codigo

debido a que es redundante.
'''


# Llamar funciones dentro de otras
print('\nEjemplo9')
# Se quiere verificar si la resta de dos numeros a y b, es igual a la
# division de dos numeros c y d
# Para este ejemplo se reutilizaran algunas funciones creadas previamente
def verificar_igualdades():
    # Pedir valores para la resta
    num1 = int(input('Digite el primer numero: '))
    num2 = int(input('Digite el segundo numero: '))
    # Pasar por parametro los valores para que se resten. Ver linea 90
    resta = restar(num1, num2)
    # Llamar funcion que divide dos numeros. Ver linea 111
    division = dividir()
    # Verificar la condicion
    if resta == division:
        print('Se cumple la condicion')
    else:
        print('No se cumple la condicion')

verificar_igualdades() # Llamar funcion

# Fin de los ejemplos