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

Ejemplos de entradas y salidas de datos
'''


print('Ejemplo1:')
# Mostrar una cadena de texto
print('Hola Mundo!')


print('\nEjemplo2:')
# Mostrar un numero entero
print(23)
# Mostrar un numero de punto flotante o decimal
print(45.89)


print('\nEjemplo3:')
# Mostrar la salida de una cadena + numero
# Manera incorrecta. Quitar el comentario para ver el error
#print('Numero ' + 23)
# NOTA: format(*args, **kwargs) llena el {} con el parametro indicado
print('Numero ' + str(23))
print('Numero', 23)
print('Numero {}'.format(23))


print('\nEjemplo4:')
# Pedir un dato de tipo cadena al usuario
cadena = str(input('Ingrese una letra, palabra o frase: '))
print(cadena)

# Aqui tambien se pide una cadena
cadena2 = input('Ingrese una letra, palabra o frase: ')
print(cadena2)


print('\nEjemplo5:')
# Pedir dato de tipo entero al usuario
entero = int(input('Ingrese un numero entero: '))
print(entero)


print('\nEjemplo6:')
# Pedir dato de tipo flotante al usuario
# Nota: si digita un numero n sin decimales se muestra como n.0
flotante = float(input('Ingrese un numero con decimales: '))
print(flotante)


print('\nEjemplo7:')
# Mostrar la salida de distintos datos en un solo print
# NOTA: '\n' agrega un salto de linea, es decir, escribe en el siguiente reglon
# NOTA2: '\t' agrega una tabulacion
# NOTA3: Se pueden usar las comillas triples para escribir en multiples lines
print('Primera forma:\nLa primer cadena que se ingreso fue ' + cadena +
      '\nLa segunda cadena que se ingreso fue ' + cadena2 +
      '\nEl numero entero que se ingreso fue ' + str(entero) +
      '\nEl numero con decimales que se ingreso fue ' + str(flotante))

print('\nLa segunda forma:\nLa primer cadena que se ingreso fue', cadena,
      '\nLa segunda cadena que se ingreso fue', cadena2,
      '\nEl numero entero que se ingreso fue', entero,
      '\nEl numero con decimales que se ingreso fue', flotante)

print('''\nLa tercer forma:
La primer cadena que se ingreso fue {}
La segunda cadena que se ingreso fue {}
El numero entero que se ingreso fue {}
El numero con decimales que se ingreso fue {}'''.format(cadena, cadena2, entero, flotante))

    
print('\nEjemplo8:')
# Cambiar el separado del print
# Ejemplo sin especificar el caracter de separado
print('Ejemplo8.1:', cadena, cadena2, entero, flotante)
# Caracter de separado es un espacio en blanco
print('Ejemplo8.2:', cadena, cadena2, entero, flotante, sep=' ')
# Caracter de separado es un -
print('Ejemplo8.3:', cadena, cadena2, entero, flotante, sep='-')
# Caracter de separado es *
print('Ejemplo8.4:', cadena, cadena2, entero, flotante, sep='*')
# Caracter de separado es _
print('Ejemplo8.5:', cadena, cadena2, entero, flotante, sep='_')


print('\nEjemplo9:')
# Cambiar el final de linea del print
# Sin cambiar el final de linea
print('Ejemplo9.1')
print(cadena)
print(cadena2)
print(entero)
print(flotante)

# Si el final de linea es \n
print('Ejemplo9.2', end='\n')
print(cadena, end='\n')
print(cadena2, end='\n')
print(entero, end='\n')
print(flotante, end='\n')

# Si el final de linea es un espacio vacio
print('Ejemplo9.3', end=' ')
print(cadena, end=' ')
print(cadena2, end=' ')
print(entero, end=' ')
print(flotante)

# Si el final de linea es -
print('Ejemplo9.4', end='-')
print(cadena, end='-')
print(cadena2, end='-')
print(entero, end='-')
print(flotante)

# Si el final de linea es *
print('Ejemplo9.5', end='*')
print(cadena, end='*')
print(cadena2, end='*')
print(entero, end='*')
print(flotante)

# Si el final de linea es _
print('Ejemplo9.6', end='_')
print(cadena, end='_')
print(cadena2, end='_')
print(entero, end='_')
print(flotante)

# Fin de los ejemplos
# Experimente con los ejemplos
# Cambie cosas
# Haga programas usando lo aprendido
