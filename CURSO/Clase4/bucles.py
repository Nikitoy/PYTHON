#Bucles

#Los bucles nos permiten repetir un bloque de código, una cantidad de veces determinada.
#En Python existen dos tipos de estructuras de control repetitivas, los bucles while y for.

#Bucle While

#Utilizando el bucle while vamos a poder ejecutar un cierto bloque de código mientras una condición sea igual a True. Veamos un ejemplo:
  
  i = 1
while i < 6:
  print(i)
  i = i + 1

# 1
# 2
# 3
# 4
# 5

#definimos una variable y un bucle que mientras i sea menor a 6 que imprima el valor de i y le sume 1
#cuando i deje de ser menor a 6 se detendra el bucle

#crear una lista 
#definir una variable y sumarle 1 hasta que el valor deje de ser menor
#al numero de elementos de la lista

autos = ["Ford", "Volvo", "BMW"]

i = 0
while i < len(autos):
  print(autos[i])
  i = i + 1

# Ford
# Volvo
# BMW


#Podemos ingresar un condicional dentro un bucle, es decir, tendríamos una estructura condicional dentro otra.

autos = ["Ford", "Volvo", "BMW"]

i = 0
while i < len(autos):
  if(autos[i] != "Volvo"):
  	print(autos[i])
  i = i + 1

# Ford
# BMW

#En el ejemplo anterior, usamos el Operador Condicional != (distinto) para mostrar los autos del array,
#siempre y cuando el elemento evaluado sea distinto de la cadena de caracteres “Volvo”.
