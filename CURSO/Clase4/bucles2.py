El bucle for nos permite recorrer una estructura como un array de una manera diferente de lo realizado con el bucle while.

autos = ["Ford", "Volvo", "BMW"]

for x in autos:
  print(x)

# Ford
# Volvo
# BMW

#el for La diferencia con respecto a este último bucle es que no necesitamos especificar el valor inicial y el valor final del array utilizado

#La primer línea de código del bucle for, indica que vamos a recorrer los elementos del array autos y 
#vamos a guardar cada uno de estos valores en la variable x.

#Luego mostramos el valor de x. 


#Del mismo modo que usamos un condicional dentro del bucle while, vamos a poder usar el condicional if dentro del bucle for.

autos = ["Ford", "Volvo", "BMW"]

for x in autos:
    if(x != "Volvo"):
        print(x)

# Ford
# BMW
