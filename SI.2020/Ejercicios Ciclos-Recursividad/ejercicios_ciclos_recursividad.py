# -*- coding: utf-8 -*-
"""Ejercicios ciclos/recursividad.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18mqGHheqMBAt2Eb2D-u-_O2qIw-RjTjv

# **Instrucciones**
1. Utilice el siguiente archivo ya sea solo para recursividad (pila o cola) o
solo para ciclos (while o for). Puede crear dos archivos para trabajar cada tema
por separado.
2. Si usa ciclos, queda a su criterio escoger cuál ciclo (while o for)
soluciona mejor el problema (ambos podrían solucionar el mismo). Lo mismo
aplica con recursividad.
3. Se le provee un esqueleto de la función con los parámetros que debe recibir.
Su trabajo es rellenar la función para que cumpla con la especificación del
ejercicio.
4. Se provee una función la cuál realiza las pruebas necesarias. Si su función
pasa todas las pruebas, significa que está correcta. De lo contrario, debe
cambiar el ejercicio.
5. Estos ejercicios son únicamente de práctica, por lo que si lo desea puede
enviarlos al tutor para recibir feedback. No es obligatorio hacerlos.
6. Debe de quitar el comentario a la función de prueba que desear probar.
7. Puede implementar cualquier función extra que necesite, así como reutilizar
función ya hechas en este código.

## **Ejemplo**

Realice una función que cuente la cantidad de dígitos de un número

```python
>>> contarDigitos(23)
2
>>> contarDigitos(23456)
5
>>> contarDigitos(123)
3
>>> contarDigitos(-12123)
5
```
"""

def contarDigitos(num):
    if num == 0:
        return 1
    elif num < 0:
        num = abs(num)

    cantidad = 0

    while num != 0:
        cantidad += 1
        num //= 10
    
    return cantidad

def testContarDigitos():
    assert contarDigitos(0) == 1
    assert contarDigitos(23) == 2
    assert contarDigitos(-1) == 1
    assert contarDigitos(3483578) == 7
    assert contarDigitos(-98748578995) == 11
    assert contarDigitos(-15) == 2
    print('Contar digitos funciona.')

testContarDigitos()

"""## **Ejercicio 1**

Escribir una función que encadene los dígitos del segundo número con el primer número, de acuerdo al comportamiento siguiente:
"""

def concatenarNumeros(num1, num2):
    return 0

def testConcatenarNumeros():
    assert concatenarNumeros(0, 0) == 0
    assert concatenarNumeros(0, 1) == 1
    assert concatenarNumeros(0, 12) == 12
    assert concatenarNumeros(0, 100) == 100
    assert concatenarNumeros(0, 123455678) == 123455678
    assert concatenarNumeros(1, 0) == 10
    assert concatenarNumeros(12, 0) == 120
    assert concatenarNumeros(450, 0) == 4500
    assert concatenarNumeros(123456, 10) == 12345610
    assert concatenarNumeros(39835938, 39458349) == 3983593839458349
    assert concatenarNumeros(2346, 28743) == 234628743
    print('Concatenar numeros funciona.')

#testConcatenarNumeros()

"""# **Ejercicio 2**

Escribir una función que construya un nuevo número con los dígitos pares de
*num1*.
"""

def construirPares(num):
    return 0

def testConstruirPares():
    assert construirPares(0) == 0
    assert construirPares(1) == -1
    assert construirPares(2) == 2
    assert construirPares(3) == -1
    assert construirPares(4) == 4
    assert construirPares(5) == -1
    assert construirPares(6) == 6
    assert construirPares(7) == -1
    assert construirPares(8) == 8
    assert construirPares(9) == -1
    assert construirPares(22) == 22
    assert construirPares(324) == 24
    assert construirPares(357385) == 8
    assert construirPares(350085) == 8
    assert construirPares(357305) == 0
    assert construirPares(19385938359) == 88
    assert construirPares(135797531) == -1
    assert construirPares(1847387) == 848
    print('Construir pares funciona.')

#testConstruirPares()

"""# **Ejercicio 3**

Escribir una función que cuente la cantidad de apariciones de un dígito en un
número.
"""

def contarApariciones(digito, num):
    return 0

def testContarApariciones():
    assert contarApariciones(0, 0) == 1
    assert contarApariciones(1, 0) == 0
    assert contarApariciones(2, 0) == 0
    assert contarApariciones(7, 0) == 0
    assert contarApariciones(8, 0) == 0
    assert contarApariciones(1, 10) == 1
    assert contarApariciones(2, 129) == 1
    assert contarApariciones(8, 43658379) == 1
    assert contarApariciones(6, 86482765785) == 2
    assert contarApariciones(3, 33333) == 5
    assert contarApariciones(2, 3828722982223059) == 6
    assert contarApariciones(1, 9849580258290) == 0
    print('Contar apariciones funciona.')

#testContarApariciones()

"""# **Ejercicio 4**

Escriba una función que calcule el factorial de un número

$0! = 1$

$1! = 1$

$2! = 2 * 1 = 2$

$3! = 3 * 2 * 1 = 6$

$4! = 4 * 3 * 2 * 1 = 24$

$n! = n * (n - 1) * (n - 2) * ... * 2 * 1$
"""

def factorial(num):
    return 0

def testFactorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120
    assert factorial(6) == 720
    assert factorial(7) == 5040
    assert factorial(8) == 40320
    assert factorial(9) == 362880
    assert factorial(10) == 3628800
    assert factorial(11) == 39916800
    assert factorial(12) == 479001600
    assert factorial(13) == 6227020800
    assert factorial(14) == 87178291200
    assert factorial(15) == 1307674368000
    print('Factorial funciona.')

#testFactorial()

"""# **Ejercicio 5**

Escribir una función que calcule el fibonacci de un número.
El fibonacci de un número es la suma del fibonacci del anterior y el
trasanterior.

$fibonacci(0) = 0$

$fibonacci(1) = 1$

$fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)$
"""

def fibonacci(num):
    return 0

def testFibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert fibonacci(8) == 21
    assert fibonacci(9) == 34
    assert fibonacci(10) == 55
    assert fibonacci(11) == 89
    assert fibonacci(12) == 144
    assert fibonacci(13) == 233
    assert fibonacci(14) == 377
    assert fibonacci(15) == 610
    print('Fibonacci funciona.')

#testFibonacci()

"""# **Ejercicio 6**

Escriba una función que valida si un número es un palíndromo.
Un número es un palíndromo si es igual al darle la vuelta.
"""

def esPalindromo(num):
    return False

def testEsPalindromo():
    assert esPalindromo(0) == True
    assert esPalindromo(1) == True
    assert esPalindromo(22) == True
    assert esPalindromo(23) == False
    assert esPalindromo(123) == False
    assert esPalindromo(151) == True
    assert esPalindromo(2657) == False
    assert esPalindromo(2222) == True
    assert esPalindromo(1234321) == True
    assert esPalindromo(1231234) == False
    assert esPalindromo(23145654132) == True
    assert esPalindromo(123214) == False
    assert esPalindromo(1234567890987654321) == True
    print('Es palindromo funciona.')

#testEsPalindromo()

"""# **Ejercicio 7**

Escriba una función  que reciba dos números enteros y obtenga como resultado
dos números, el primero compuesto por los dígitos del primer número que no
pertenecen al segundo número y el segundo formado por los elementos del segundo
número que no pertenecen al primer número.
"""

def calcularDiferencia(num1, num2):
    return 0, 0

def testCalcularDiferencia():
    assert calcularDiferencia(0, 0) == (0, 0)
    assert calcularDiferencia(1234, 254) == (13, 5)
    assert calcularDiferencia(1468, 866124) == (0, 2)
    assert calcularDiferencia(2935, 623587) == (9, 687)
    assert calcularDiferencia(8527938, 8452739) == (0, 4)
    assert calcularDiferencia(893475, 389457) == (0, 0)
    assert calcularDiferencia(73528, 283049) == (75, 49)
    assert calcularDiferencia(35897, 8387) == (59, 0)
    assert calcularDiferencia(29370, 1487) == (2930, 148)
    print('Calcular diferencia funciona.')

#testCalcularDiferencia()

"""# **Ejercicio 8**

Si de 5 parejas de hormigas cada una engendra 3 hormiguitas, luego mueren,
dejando que las 15 hormiguitas nacidas, engendren también 3 hormiguitas por
pareja, luego mueren y se sigue repitiendo el proceso.
Escriba una función que recibe como argumento un entero positivo y que
determine el número de hormiguitas qué existirán al cabo de n períodos.
Considere que siempre se pueden formar las parejas.
"""

def calcularHormigas(n):
    return 0

def testCalcularHormigas():
    assert calcularHormigas(0) == 10
    assert calcularHormigas(1) == 15
    assert calcularHormigas(2) == 21
    assert calcularHormigas(3) == 30
    assert calcularHormigas(4) == 45
    assert calcularHormigas(5) == 66
    assert calcularHormigas(6) == 99
    assert calcularHormigas(7) == 147
    assert calcularHormigas(8) == 219
    assert calcularHormigas(9) == 327
    assert calcularHormigas(10) == 489
    assert calcularHormigas(11) == 732
    assert calcularHormigas(12) == 1098
    assert calcularHormigas(13) == 1647
    assert calcularHormigas(14) == 2469
    assert calcularHormigas(15) == 3702
    assert calcularHormigas(16) == 5553
    assert calcularHormigas(17) == 8328
    assert calcularHormigas(18) == 12492
    assert calcularHormigas(19) == 18738
    print('Calcular hormigas funciona.')

#testCalcularHormigas()

"""# **Ejercicio 9**
Escriba una función que valide si un par de número son amigos. En matemáticas un par de números m y n es llamado par amigable (o números amigos), si la suma
de todos los divisores de m (excluyendo a m) es igual al número n, y la suma de
todos los divisores del número n (excluyendo a n) es igual a m (donde m != n).

Ejemplo: los números 220 y 284 son un par amigable. La explicación es la
siguiente:

Los únicos números que dividen de forma exacta a 220 son 1, 2, 4, 5, 10, 11, 20,
22, 44, 55 y 110, y la suma de ellos es: 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44
+ 55 + 110 = 284

Los únicos números que dividen de forma exacta a 284 son 1, 2, 4, 71 y 142 , y
la suma de ellos es: 1 + 2 + 4 + 71 + 142 = 220

*Ejercicio tomado de William Mata*
"""

def esParAmigable(num1, num2):
    return False

def testEsParAmigable():
    assert esParAmigable(220, 284) == True
    assert esParAmigable(15, 18) == False
    assert esParAmigable(1210, 1184) == True
    assert esParAmigable(30, 42) == False
    assert esParAmigable(2620, 2924) == True
    assert esParAmigable(1510, 900) == False
    assert esParAmigable(5020, 5564) == True
    assert esParAmigable(1234, 789) == False
    print('Es par amigable funciona.')

#testEsParAmigable()

"""# **Ejercicio 10**

Escriba una función para obtener un solo número que contenga todos los números
enteros sucesivos (de 1 en 1) que se encuentren en un rango. El programa recibe
2 entradas enteras positivas: el inicio del rango y el fin del rango.
Retorna un número conteniendo todos los números enteros en el rango indicado.

Los números deben ponerse en el resultado secuencialmente de derecha a
izquierda.

Proceso:
Debe generar la serie de números enteros sucesivos (de 1 en 1) en el rango
indicado y formar un solo número con esa serie. El primer número de la serie
será el número de más a la derecha en el número resultante, luego se le pega a
la izquierda el segundo número de la serie y así sucesivamente hasta el último
número en el rango.

*Ejercicio tomado de William Mata*
"""

def formarRango(inicio, fin):
    return 0

def testFormarRango():
    assert formarRango(0, 2) == 210
    assert formarRango(0, 9) == 9876543210
    assert formarRango(5, 10) == 1098765
    assert formarRango(98, 101) == 1011009998
    assert formarRango(997, 1005) == 100510041003100210011000999998997
    print('Formar rango funciona.')

#testFormarRango()

"""# **Ejercicio Bonus**

Escriba una función que reciba dos números y los concatene ordenando de mayor a
menor los digitos de los números.
"""

def concatenarYOrdenar(num1, num2):
    return 0

def testConcatenarYOrdenar():
    assert concatenarYOrdenar(0, 0) == 0
    assert concatenarYOrdenar(0, 1) == 10
    assert concatenarYOrdenar(1, 0) == 10
    assert concatenarYOrdenar(12, 0) == 210
    assert concatenarYOrdenar(12, 10) == 2110
    assert concatenarYOrdenar(123, 135) == 533211
    assert concatenarYOrdenar(100, 901) == 911000
    assert concatenarYOrdenar(123478, 18247) == 88774432211
    assert concatenarYOrdenar(97624, 8462) == 987664422
    print('Concatener y ordenar funciona')

#testConcatenarYOrdenar()