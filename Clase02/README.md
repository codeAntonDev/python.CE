# <b>Curso de Python - Canal Ejecutivo</b>

## 2. Estructuras de Control de Flujo y Funciones

### ¿Qué es una Estructura de Control de Flujo?

Una estructura de control de flujo en programación es un mecanismo que permite alterar el flujo de ejecución de un programa, es decir, el orden en que se ejecutan las instrucciones.

En lugar de ejecutar todo secuencialmente, las estructuras de control permiten hacer decisiones, repeticiones y saltos condicionales a diferencia de los elementos que vimos hasta ahora en Python, tales como Variables, Tipos de Datos, Operadores.

### Sentencia **IF** (_if_)

<div style="margin-top: -5px"><hr></div>

<br>

- Sintaxis

  ```python
  if expresion:
     sentencia(s)
  ```

  Expresión: Evalua a _True_ o _False_.  
  Sentencia: Mostrará o se ejecutará si la expresión es _True_.

### Sentencia **ELSE** (_else_)

<div style="margin-top: -5px"><hr></div>

<br>

- Sintaxis

  ```python
  if expresion:
     sentencia(s)
  else:
     sentencia(s)
  ```

### Sentencia **ELIF** (_elif_)

<div style="margin-top: -5px"><hr></div>

<br>

- Sintaxis

  ```python
  if expresion:
     sentencia(s)
  elif expresion:
     sentencia(s)
  elif expresion:
     sentencia(s)
  .
  .
  .
  else:
     sentencia(s)
  ```

### Bucles

<div style="margin-top: -5px"><hr></div>

<br>

- For

  El **Bucle** ( _for_ ) en Python, nos permite implementar sentencias que se repitan un número finito de veces, principalmente para **_iterar_** una lista de elementos.

  ```python
  for variable in iterable:
      sentencia(s)
  ```

- While

  El **Bucle** ( _while_ ) en Python, nos permite implementar sentencias que se repitan un número finito de veces, si nos dá **_True_**.

  ```python
  while expresion:
      sentencia(s)
  ```

### Declaraciones o Sentencias: **Break** **Pass** **Continue**

<div style="margin-top: -5px"><hr></div>

<br>

- _Break_

  Esta sentencia la podemos utilizar para **_terminar_** de manera inmediata una estructura de control de flujo de **while** o **for**.

<br>

- _Continue_

  Esta sentencia no termina la ejecución completa de los **_bucles_** **while** o **for**, si no que termina la ejecución de la iteración actual.

<br>

- _Pass_

  Esta sentencia la podemos usar cuando no tenemos ninguna **_sentencia_** determinada en los bucles **while** o **for**.

### Funciones en Python

<div style="margin-top: -5px"><hr></div>

<br>

- Sintaxis

  ```python
  def nom_funcion():
      sentencia(s)

  def nom_funcion(args):
      sentencia(s)
  ```

### Modulos en Python

<div style="margin-top: -5px"><hr></div>

<br>

- Modulo **Random**

  ```python
  import random
  ```

- Modulo **Math**

  ```python
  import math
  ```

- Modulo **Os**

  ```python
  import os
  ```

- Modulo **Sys**

  ```python
  import sys
  ```

- Modulo **Numpy**

  ```python
  import numpy
  ```

- Modulo **Pandas**

  ```python
  import pandas
  ```
