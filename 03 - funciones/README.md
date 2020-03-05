# Funciones

Ejemplos creación de funciones

## Conocimientos previos
- Los temas evaluados en los ejemplos anteriores
- Funcionamiento del return en una función
- Qué es un parámetro
- Diferencias entre variables locales y globales


## Estructura de una función que

### No recibe parámetros y no retorna valores
```python
def funcion():
    # Bloque de codigo
```


### No recibe parámetros pero retorna un dato
```python
def funcion():
    # Bloque de codigo
    return dato
```


### No recibe parámetros pero retorna más de un dato
```python
def funcion():
    # Bloque de codigo
    return dato, dato2, dato3, ..., dato_n
```


### Recibe un parámetro pero no retorna valores
```python
def funcion(parametro):
    # Bloque de codigo
```


### Recibe más de un parámetro pero no retorna valores
```python
def funcion(parametro, parametro2, ..., parametro_n):
    # Bloque de codigo
```


### Recibe mas de un parámetro y retorna un dato
```python
def funcion(parametro, parametro2, ..., parametro_n):
    # Bloque de codigo
    return dato
```


### Recibe más de un parámetro y retorna más de un dato

```python
def funcion(parametro, parametro2, ..., parametro_n):
    # Bloque de codigo
    return dato, dato2, dato3, ..., dato_m
```


## Profundizando en los parámetros de las funciones
Los parámetros de las funciones siempre son obligatorios, por lo que si no incluímos uno, Python nos dará un error indicándonos cuál nos hace falta. Por ejemplo:

```python
def sumar(a, b):
    return a + b

>>> print(sumar(2, 3))
5
```

Nosotros estamos obligados a enviar dos valores como parámetros.

Tenemos otro tipo de parámetro llamado **args** (de **arguments**), el cual nos permite pasar de 0 a muchos parámetros y estos son almacenados como una tupla dentro de una variable. Este parámetro se representa colocando un * antes del nombre del parámetro. Por ejemplo

```python
def funcion(*valores):
    return valores

>>> print(funcion())
()
>>> print(funcion(1))
(1,)
>>> print(funcion(2, 4, 6))
(2, 4, 6)
>>> print(funcion(0, 2, 5, 7, 'a', 'b'))
(0, 2, 5, 7, 'a', 'b')
```

Finalmente, tenemos un último parámetro llamado **kargs** (de **key arguments**), el cual se representa con ** antes del nombre del parámetro. Este parámetro almacena los valores pasados en la función como un diccionario (el cual se verá más adelante). Cada valor debe tener una llave para que sea tomado en cuenta. Por ejemplo:

```python
def funcion(**valores):
    return valores

>>> print(funcion())
{}
>>> print(funcion(x=2))
{'x': 2}

>>> print(funcion(x=2, y=3, z=4))
{'x': 2, 'y': 3, 'z': 4}
```

También se puede realizar combinaciones entre los distintos tipos de parámetros que vimos anteriormente
```python
def funcion(num1, letra, *valores, **llaves):
    print(num1)
    print(letra)
    print(valores)
    print(llaves)

>>> funcion(2, 'a', 3, 5, 6, 8, x=5, y=3)
2
'a'
(3, 5, 6, 8)
{'x': 5, 'y': 3)
```
