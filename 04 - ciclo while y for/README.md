# Ciclos while y for

Ejemplos de uso de ciclos

## Conocimientos previos
- Los temas evaluados en los ejemplos anteriores
- Qué es un ciclo y cómo funcina un while y for
- El break y pass


## Estructura general del while
```python
while condicion:
    # Codigo a ejecutar
```

Un ciclo while se repite mientras la condicion que se coloco, se cumpla.


## Estructura de un ciclo for con in range()
```python
for variable in range(fin):
    # Codigo
```
- variable empieza en 0 y termina en 'fin - 1'
- variable aumenta de 1 en 1

```python
for variable in range(inicio, fin):
    # Codigo
```
- variable empieza en inicio y termina en 'fin - 1'
- variable aumenta de 1 en 1

```python
for variable in range(inicio, fin, salto):
    # Codigo
```
- variable empieza en inicio y termina en 'fin - 1'
- variable aumenta de salto en salto

## Estructura de un ciclo for con in elementos
```python
for elemento in elementos:
    # Codigo
```

En este caso, la variable *elementos* tiene que ser un iterable (lista, tupla, array, etc), así la variable *elemento* toma el valor de cada uno de los valores en un ciclo diferente. Es decir, si *elementos = [1, 2, 3]*, en el primer ciclo *elemento = 1*, en el segundo ciclo *elemento = 2* y en el tercer ciclo *elemento = 3* y finaliza el ciclo.
