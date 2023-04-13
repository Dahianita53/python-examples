# Introducción a la programación con python

Dentro de la comunidad de python hay algunos estandares bastante reglamentados a los que se espera que se adhiera a los programadores de python, porque este lenguaje y comunidad en particular a tratado de codificar algunas de sus preferencias sobre como su codigo, deberia tener la forma de algo llamado PEP8.

## PEP8

Es una propuesta que trata de estandarizar el aspecto que deberia tener nuestro codigo; es decir, que es muy posible escribir codigo que no solo sea correcto, sino que incluso podria estar bien diseñado,pero es un desastre y simplemente no se ve muy bien, por lo tanto es mas dificil de leer y cada vez que se hace que algo sea mas dificil de leer o menos mantenible, solo esta aumentando la probabilidad de introducir errores por lo tanto, es bueno que su codigo tenga el formato adecuado.

Suele ser una buena practica usar mayuscula en ciertas palabras, al menos en ingles, usar una buena puntuacion, usar saltos de parrafo y cosas por el estilo.

¿que significa verse bien en el mundo del codigo de programacion?
si observas PEP8 resulta que intenta estandarizar una serie de detalles que se manifestarian en tu propio codigo. Una vez que hayaas escrito un numero de lineas y la premisa general del PEP8 y realmente la nocion de estilo en la comunidad de python especialmente, es que "la legibilidad cuenta" por lo general los lenguajes, python entre ellos vienen con lo que generalmente se conoce como una guia de estilo, no muy diferente a PEP8.

En el contexto de python estas son algunas pautas que deberia guiar el diseño de su propio  codigo:

* indentation: se refiere a los espacios al comienzo de una línea de código

* tabs or spaces?: Aunque las tabulaciones y los espacios son intercambiables, la guía de estilo de Python (PEP 8) recomienda usar espacios en lugar de tabulaciones

* maximun line length: longitud maxima de la linea simplemente no debe pasarse una cierta cantidad de caracteres a la derecha de su pantalla

* blank lines: pueden hacer que sea un poco mas facil comprender lo que esta sucediendo

* imports: organizar códigos grandes en pequeñas porciones reutilizables; compartir tu código con otras personas e, inversamente, usar el código de otras personas

## Pylint

Es un programa que se conoce como linter, este programa analiza bastante estaticamente es decir, lee su codigo de arriba a abajo, de izquierda a derecha, y trata de averiguar si hay posibles errores en el, o al menos inconsistencias con algo asi como una guia de estilo prescrita.

para instalarla "pip install pylint"

## Programas que formatean el codigo por ti

* Pycodestyle
*  black: para instalarlo "pip install black"