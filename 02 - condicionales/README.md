# Condicionales

Ejemplos de uso de condicionales, operadores logicos y aritmeticos


## Conocimientos previos

* Booleanos (True, False)
* Entrada y salida de datos (input, print)
* Operadores relacionales (<, >, ==, <=, >=, !=)
* Operadores logicos (and, or, not)
* Operadores aritmeticos (+, -, *, /, //, **, %)


## Estructura de los condicionales

```python
if condicion1:
    # Bloque de codigo si se cumple la condicion1
elif condicion2:
    # Bloque de codigo si se cumple la condicion2
.
.
.
else:
    # Bloque de codigo si no se cumple alguna de las condiciones anteriores
```


## Tablas de verdad

### AND

|  A    |   B   | A ⋅ B |
|:-----:|:-----:|:-----:|
|   0   |   0   |   0   |
|   0   |   1   |   0   |
|   1   |   0   |   0   |
|   1   |   1   |   1   |

### OR

|  A    |   B   | A + B |
|:-----:|:-----:|:-----:|
|   0   |   0   |   0   |
|   0   |   1   |   1   |
|   1   |   0   |   1   |
|   1   |   1   |   1   |

### NOT

|  A    |  ¬A   |
|:-----:|:-----:|
|   0   |   1   |
|   1   |   0   |
