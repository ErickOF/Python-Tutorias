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

Ejemplos de uso de ciclos

Conocimientos previos
-Los temas evaluados en los ejemplos anteriores
-Que es un ciclo y como funcina un while y for
-El break, pass

###############################
Estructura general del while
while condicion:
    # Codigo a ejecutar

Un ciclo while se repite mientras la condicion que se coloco, se cumpla.


Estructura de un ciclo for con in range()
for variable in range(fin):
    # Codigo
-variable empieza en 0 y termina en 'fin - 1'
-variable aumenta de 1 en 1

for variable in range(inicio, fin):
    # Codigo
-variable empieza en inicio y termina en 'fin - 1'
-variable aumenta de 1 en 1

for variable in range(inicio, fin, salto):
    # Codigo
-variable empieza en inicio y termina en 'fin - 1'
-variable aumenta de salto en salto
'''

print('Ejemplo1') # Creacion de una funcion que cuenta hasta un numero indicado por el usuario
def contarWhile():
    # Se pide el numero hasta el que se desea contar
    num = int(input('Ingrese el numero hasta el que desea contar: '))
    # Numero desde el que inicia la cuenta
    cont = 1
    while cont <= num: # Se repite el ciclo hasta que cont sea mayor que num
        print(cont)
        # Se le aumenta 1 a cont en cada ciclo
        cont += 1

contarWhile()


print('\nEjemplo2') # Mostrar pares
def mostrarParesWhile():
    # Pedir el rango
    inicio = int(input('Ingrese el numero desde el que desea empezar a buscar los pares: '))
    fin = int(input('Ingrese el numero hasta el que desea buscar los pares: '))
    # Se repite el ciclo hasta que inicio sea mayor que fin
    while inicio <= fin:
        # Nota: Note que inicio es la variable que tomara todos los valores numericos
        # hasta llegar a el valor de fin
        # Se verifica si inicio es par
        if inicio % 2 == 0:
            # Se muestra el numero par que se encontro
            print(inicio)
        # Aumentar 1 a inicio en cada ciclo
        inicio += 1

mostrarParesWhile()


print('\nEjemplo3') # Mostrar primos de 2 a 100
# Esta funcion verifica si el numero es primo
def esPrimoWhile(num):
    # Variable que toma el valor de los numeros que estan entre 2 y el num
    divisor = 2
    # Se repite hasta que divisor tenga el valor de num
    while divisor < num:
        # Si el residuo de num entre divisor da 0
        if num % divisor == 0:
            # Significa que el numero no es primo y se indica con un False
            return False
        # Se continua con el siguiente divisor
        divisor += 1
    # Si se sale del ciclo significa que no hay divisores por lo que num es primo
    return True
    
def mostrarPrimosWhile():
    # Variable que guarda el numero desde la cual se desea buscar los numeros primos
    num = 2
    # Se repite hasta que num sea mayor que 100
    while num <= 100:
        # Se llama la funcion que verifica si un numero es primo
        if esPrimoWhile(num):
            # Si entra al condicional significa que la funcion retorno True
            # Por lo que se imprime el numero
            print(num)
        # Se continua con el siguiente numero
        num += 1

mostrarPrimosWhile()


print('\nEjemplo4') # Creacion de una funcion que cuenta hasta un numero indicado por el usuario
def contarFor():
    # Se pide el numero hasta el que se desea contar
    num = int(input('Ingrese el numero hasta el que desea contar: '))
    # Se inicia cont en 1 y se cuenta hasta num
    # Recuerde que se cuenta hasta el numero - 1, por eso se agrega el 1
    for cont in range(1, num + 1):
        print(cont)
        # Se le aumenta 1 a cont en cada ciclo automaticamente

contarFor()


print('\nEjemplo5') # Mostrar pares
def mostrarParesFor():
    # Pedir el rango
    inicio = int(input('Ingrese el numero desde el que desea empezar a buscar los pares: '))
    fin = int(input('Ingrese el numero hasta el que desea buscar los pares: '))
    # Se repite el ciclo hasta que inicio sea igual que fin + 1
    for num in (inicio, fin + 1):
        # Se verifica si num es par
        if num % 2 == 0:
            # Si lo es se muestra en pantalla
            print(num)

mostrarParesFor()


print('\nEjemplo6') # Mostrar primos de 2 a 100
# Esta funcion verifica si el numero es primo
def esPrimoFor(num):
    # Se repite hasta que divisor tenga el valor de num
    for divisor in range(2, num):
        # Si el residuo de num entre divisor da 0
        if num % divisor == 0:
            # Significa que el numero no es primo, se indica con un False
            return False
        # Se pasa al siguiente divisor automaticamente
    # Si se sale del ciclo significa que no hay divisores por lo que num es primo
    return True
    
def mostrarPrimosFor():
    # Variable que guarda el numero desde la cual se desea buscar los numeros primos
    num = 2
    # Se repite hasta que num sea igual que 101
    # Note que el ciclo se repite hasta 100 porque se llega hasta fin - 1
    for num in range(2, 101):
        # Se llama la funcion que verifica si un numero es primo
        if esPrimoWhile(num):
            # Si entra al condicional significa que la funcion retorno True
            print(num)

mostrarPrimosFor()


print('\nEjemplo7') # Contar de 5 en 5
def contarConSaltos():
    # Se repite hasta que num sea igual que 101
    for num in range(0, 101, 5):
        # Mostrar el numero
        print(num)

contarConSaltos()

# Fin