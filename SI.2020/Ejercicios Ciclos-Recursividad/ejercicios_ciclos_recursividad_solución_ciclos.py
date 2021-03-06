# -*- coding: utf-8 -*-
"""Ejercicios ciclos/recursividad - Solución ciclos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/144yL3mSjr3nlwDSMmWWvZReec0E3XFYK

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
    # Variable donde se guarda el nuevo numero con unicamente numeros pares
    nuevo = 0
    # Factor el cual nos ayuda a aplicar la idea de notacion desarrollada
    # Ver explicacion de notacion desarrollada
    # https://es.khanacademy.org/math/pre-algebra/pre-algebra-arith-prop/pre-algebra-place-value/a/whole-numbers-in-expanded-form-review
    factor = 1

    if num2 != 0:
        # Ejecutar hasta que el numero se haga cero
        while num2 != 0:
            # Se agrega el digito de mas a la derecha al nuevo numero
            nuevo += (num2 % 10) * factor
            # Aumentar factor diez veces
            factor *= 10
            # Cortar el digito de mas a la derecha
            num2 //= 10
    # Si no
    else:
        # El factor se pone en diez, ya que el digito de mas a la derecha del
        # nuevo numero sera un cero
        factor = 10
    
    # Ejecutar hasta que el numero se haga cero
    while num1 != 0:
        # Se agrega el digito de mas a la derecha al nuevo numero
        nuevo += (num1 % 10) * factor
        # Aumentar factor diez veces
        factor *= 10
        # Cortar el digito de mas a la derecha
        num1 //= 10
    
    return nuevo

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

testConcatenarNumeros()

"""# **Ejercicio 2**

Escribir una función que construya un nuevo número con los dígitos pares de
*num1*.
"""

def construirPares(num):
    # Si el numero es cero, se devuelve cero
    if num == 0:
        return 0

    # Variable donde se guarda el nuevo numero con unicamente numeros pares
    nuevo = 0
    # Factor el cual nos ayuda a aplicar la idea de notacion desarrollada
    factor = 1
    # Variable que guarda la cantidad de pares agregados
    pares = 0

    # Ejecutar hasta que el numero se haga cero
    while num != 0:
        # Tomar el digito de mas a la derecha
        dig = num % 10

        # Si el numero es par
        if dig % 2 == 0:
            # Se agrega al nuevo numero
            nuevo += dig * factor
            # Aumentar factor diez veces
            factor *= 10
            # Aumentar la cantidad de pares
            pares += 1
        
        # Cortar el digito de mas a la derecha
        num //= 10

    # Si se agregaron pares
    if pares > 0:
        # Se devuelve el numero
        return nuevo
    # Si no
    else:
        # Se devuelve menos uno
        return -1

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

testConstruirPares()

"""# **Ejercicio 3**

Escribir una función que cuente la cantidad de apariciones de un dígito en un
número.
"""

def contarApariciones(digito, num):
    # Si el numero y el digito son iguales se devuelve uno, ya que solo hay un
    # digito en el numero y, por lo tanto, solo una aparicion
    if num == digito:
        return 1
    
    # Variable donde se guarda el numero de apariciones
    apariciones = 0

    # Ejecutar hasta que el numero se haga cero
    while num != 0:
        # Si el digito de mas a la derecha es igual al digito que se busca
        if num % 10 == digito:
            # Se suma uno a la cantidad de apariciones
            apariciones += 1

        # Cortar el digito de mas a la derecha
        num //= 10

    return apariciones

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

testContarApariciones()

"""# **Ejercicio 4**

Escriba una función que calcule el factorial de un número

$0! = 1$

$1! = 1$

$2! = 2 * 1 = 2$

$3! = 3 * 2 * 1 = 6$

$4! = 4 * 3 * 2 * 1 = 24$

$n! = n * (n - 1) * (n - 2) * ... * 2 * 1$
"""

# Version while
"""
def factorial(num):
    # Variable donde se guardara el resultado del factorial
    # Se inicia en uno ya que se haran multiplicaciones
    fact = 1

    # Ejecutar hasta que el numero se haga cero
    while num != 0:
        # Multiplicar el factorial actual por el numero actual
        fact *= num
        # Se disminuye numero
        num -= 1

    return fact
"""

# Version for
def factorial(num):
    # Variable donde se guardara el resultado del factorial
    # Se inicia en uno ya que se haran multiplicaciones
    fact = 1

    # Ejecutar hasta que i llegue al valor de num
    for i in range(2, num + 1):
        # Multiplicar el factorial actual por el numero actual
        fact *= i

    return fact

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

testFactorial()

"""# **Ejercicio 5**

Escribir una función que calcule el fibonacci de un número.
El fibonacci de un número es la suma del fibonacci del anterior y el
trasanterior.

$fibonacci(0) = 0$

$fibonacci(1) = 1$

$fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)$
"""

# Version while
"""
def fibonacci(num):
    # Si num es cero, se devuelve cero
    if num == 0:
        return 0
    # Si num es uno, se devuelve uno
    elif num == 1:
        return 1

    # Variable donde se guarda el valor del trasanterior
    trasanterior = 0
    # Variable donde se guarda el valor del anterior
    anterior = 1
    # Fibonacci actual
    actual = 2

    # Ejecutar hasta llegar al fibonacci deseado
    while actual < num:
        # Calcular el nuevo trasanterior y el anterior
        trasanterior, anterior = anterior, trasanterior + anterior
        # Aumentar el fibonacci actual
        actual += 1

    # Definicion de fibonacci
    resultado = anterior + trasanterior
    return resultado
"""

# Version for
def fibonacci(num):
    # Si num es cero, se devuelve cero
    if num == 0:
        return 0
    # Si num es uno, se devuelve uno
    elif num == 1:
        return 1

    # Variable donde se guarda el valor del trasanterior
    trasanterior = 0
    # Variable donde se guarda el valor del anterior
    anterior = 1
    
    # Ejecutar hasta llegar al fibonacci deseado
    for actual in range(2, num):
        # Calcular el nuevo trasanterior y el anterior
        trasanterior, anterior = anterior, trasanterior + anterior

    # Definicion de fibonacci
    resultado = anterior + trasanterior
    return resultado

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

testFibonacci()

"""# **Ejercicio 6**

Escriba una función que valida si un número es un palíndromo.
Un número es un palíndromo si es igual al darle la vuelta.
"""

def darVuelta(num):
    # Variable donde se almacena el numero al reves
    numAlReves = 0

    # Ejecutar hasta que el numero se haga cero
    while num != 0:
        # Agregar el nuevo digito mas a la derecha
        numAlReves = numAlReves * 10 + (num % 10)
        # Cortar el digito de mas a la derecha
        num //= 10
    
    return numAlReves

def esPalindromo(num):
    # Se le da vuelta al numero
    numAlReves = darVuelta(num)

    # Devuelve True o False dependiendo de si los valores son iguales o no
    return num == numAlReves

    # Opcionalmente, con solo esta linea basta
    #return num == darVuelta(num)

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

testEsPalindromo()

"""# **Ejercicio 7**

Escriba una función  que reciba dos números enteros y obtenga como resultado
dos números, el primero compuesto por los dígitos del primer número que no
pertenecen al segundo número y el segundo formado por los elementos del segundo
número que no pertenecen al primer número.
"""

def estaEnNumero(num, dig):
    while num != 0:
        if num % 10 == dig:
            return True
        
        num //= 10

    return False

def diferenciar(num1, num2):
    diferencia = 0
    factor = 1

    while num1 != 0:
        digito = num1 % 10
        
        if not estaEnNumero(num2, digito):
            diferencia += digito * factor
            factor *= 10
        print(factor, num1, num2, diferencia)
        num1 //= 10
    
    return diferencia

def calcularDiferencia(num1, num2):
    # Se obtiene la diferencia de ambos numeros
    diferencia1 = diferenciar(num1, num2)
    diferencia2 = diferenciar(num2, num1)

    # Se devuelven las diferencias
    return diferencia1, diferencia2

diferenciar(1234567890, 56237)

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

testCalcularDiferencia()

"""# **Ejercicio 8**

Si de 5 parejas de hormigas cada una engendra 3 hormiguitas, luego mueren,
dejando que las 15 hormiguitas nacidas, engendren también 3 hormiguitas por
pareja, luego mueren y se sigue repitiendo el proceso.
Escriba una función que recibe como argumento un entero positivo y que
determine el número de hormiguitas qué existirán al cabo de n períodos.
Considere que siempre se pueden formar las parejas.
"""

# Version while
"""
def calcularHormigas(n):
    # Poblacion inicial de hormigas
    # Como son cinco parejas, son diez hormigas inicialmente
    hormigas = 10

    # Ejercutar hasta que n sea cero
    while n != 0:
        # Calcular la nueva cantidad de hormigas
        hormigas = hormigas // 2 * 3
        # Se le resta uno a la cantidad de periodos
        n -= 1

    return hormigas
"""

# Version for
def calcularHormigas(n):
    # Poblacion inicial de hormigas
    # Como son cinco parejas, son diez hormigas inicialmente
    hormigas = 10

    # Ejercutar hasta que n sea cero
    for _ in range(n):
        # Calcular la nueva cantidad de hormigas
        hormigas = hormigas // 2 * 3

    return hormigas

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

testCalcularHormigas()

"""# **Ejercicio 9**
Escriba una función que valide si un par de número son amigos. En matemáticas un par de números m y n es llamado par amigable (o números amigos), si la suma
de todos los divisores de m (excluyendo a m) es igual al número n, y la suma de
todos los divisores del número n (excluyendo a n) es igual a m (donde m != n).

Ejemplo: los números 220 y 284 son un par amigable. La explicación es la
siguiente:

Los únicos números que dividen de forma exacta a 220 son 1, 2, 4, 5, 10, 11, 20,
22, 44, 55 y 110, y la suma de ellos es: 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 = 284

Los únicos números que dividen de forma exacta a 284 son 1, 2, 4, 71 y 142 , y
la suma de ellos es: 1 + 2 + 4 + 71 + 142 = 220

*Ejercicio tomado de William Mata*
"""

# Version while
"""
def sumarDivisores(num):
    # Variable donde se guarda la suma de los divisores
    suma = 0
    # Variable donde se va guardando cada divisor
    div = 1

    # Ejercutar hasta que divisor llegue al valor de num
    while div < num:
        # Si div es un divisor de numero
        if num % div == 0:
            # Se suma a los divisores
            suma += div
        
        # Se aumenta en uno el divisor
        div += 1
    
    return suma
"""

# Version For
def sumarDivisores(num):
    # Variable donde se guarda la suma de los divisores
    suma = 0

    # Ejercutar hasta que divisor llegue al valor de num
    for div in range(1,  num):
        # Si div es un divisor de numero
        if num % div == 0:
            # Se suma a los divisores
            suma += div
    
    return suma

def esParAmigable(num1, num2):
    # Si los numeros son iguales no son amigos
    if num1 == num2:
        return False
    
    # Obtener la suma de los dvisores
    div1 = sumarDivisores(num1)
    div2 = sumarDivisores(num2)

    # Devuelve True si la suma de los divisores del primer numero es igual al
    # segundo numero y, a la vez, la suma de los divisores del segundo numero
    # es igual al primer numeros
    return div1 == num2 and div2 == num1

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

testEsParAmigable()

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

# Version while
"""
def formarRango(inicio, fin):
    # Variable donde se guarda el resultado
    rango = 0

    # Ejecutar ientras fin no llegue a inicio
    while fin >= inicio:
        # Se cuenta la cantidad de digitos que tiene el numero a agregar
        cantidadDigitos = contarDigitos(fin)
        # Se corre el rango a al izquierda la cantidad de digitos que tiene el
        # numero a agregar y se suma el numero
        rango = rango * 10**(cantidadDigitos) + fin
        # Se disminuye fin en uno
        fin -= 1

    return rango
"""

# Version for
def formarRango(inicio, fin):
    # Variable donde se guarda el resultado
    rango = 0

    # Ejecutar ientras fin no llegue a inicio
    for num in range(fin, inicio - 1, -1):
        # Se cuenta la cantidad de digitos que tiene el numero a agregar
        cantidadDigitos = contarDigitos(num)
        # Se corre el rango a al izquierda la cantidad de digitos que tiene el
        # numero a agregar y se suma el numero
        rango = rango * 10**(cantidadDigitos) + num

    return rango

def testFormarRango():
    assert formarRango(0, 2) == 210
    assert formarRango(0, 9) == 9876543210
    assert formarRango(5, 10) == 1098765
    assert formarRango(98, 101) == 1011009998
    assert formarRango(997, 1005) == 100510041003100210011000999998997
    print('Formar rango funciona.')

testFormarRango()

"""# **Ejercicio Bonus**

Escriba una función que reciba dos números y los concatene ordenando de mayor a
menor los digitos de los números.
"""

def insertarDigEnOrden(num, digitoAInsertar):
    # Variable donde se guarda el nuevo numero con el digito insertado
    nuevo = 0
    # Factor el cual nos ayuda a aplicar la idea de notacion desarrollada
    factor = 1
    # Variable que indica si el digito se inserto
    insertado = False

    while num != 0 and not insertado:
        # Guardar el digito de mas a la derecha
        dig = num % 10

        # Si el digito a insertar es menor o igual al digito actual
        if dig >= digitoAInsertar:
            # Se inserta ese digito junto a lo que queda del numero
            nuevo += digitoAInsertar * factor + num * factor * 10
            # Se indica que ya se inserto el numero
            insertado = True
        # Si no
        else:
            # Se agrega el digito de nuevo al numero
            nuevo += dig * factor
        
        # Se corta el digito de mas a la derecha
        num //= 10
        # Se multiplica factor por diez
        factor *= 10
    
    # Si el valor no se inserto
    if not insertado:
        # Se agrega como digito de mas a la izquierda
        nuevo += digitoAInsertar * factor

    return nuevo

def insertarEnOrden(nuevo, num, cantidadCeros):
    # Recorrer hasta que el numero se haga cero
    while num != 0:
        # Se toma el digito de mas a la derecha
        dig = num % 10

        # Si el digito es un valor diferente de cero
        if dig != 0:
            # Se inserta en orden en el nuevo numero
            nuevo = insertarDigEnOrden(nuevo, dig)
        # De lo contrario
        else:
            # Se aumenta en uno la cantidad de ceros
            cantidadCeros += 1
        num //= 10
    
    return nuevo, cantidadCeros

def concatenarYOrdenar(num1, num2):
    # Almacena la cantidad de ceros a agregar
    cantidadCeros = 0

    # Si ambos numeros son ceros
    if num1 == 0 and num2 == 0:
        # Se devuelve cero
        return 0
    # Si alguno de los numeros es cero
    elif num1 == 0 or num2 == 0:
        # Se agrega un cero
        cantidadCeros += 1

    # Se llama la funcion que inserta los digitos en orden
    nuevo, cantidadCeros = insertarEnOrden(0, num1, cantidadCeros)
    nuevo, cantidadCeros = insertarEnOrden(nuevo, num2, cantidadCeros)

    # Devuelve el numero agregando la cantidad de ceros correspondiente
    return nuevo * 10**cantidadCeros

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

testConcatenarYOrdenar()