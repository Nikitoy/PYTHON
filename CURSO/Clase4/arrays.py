#Arrays

#Podemos usar arrays para almacenar múltiples datos en una sola variable. Veamos su sintaxis

autos = ["Ford", "Volvo", "BMW"] 

autos[0] # Ford
autos[1] # Volvo
autos[2] # BMW

#Para acceder a cada uno de los elementos que se encuentran en el array, podemos hacerlo a partir de su índice, es decir, 
#sobre la posición en la que se encuentra cada auto.
#Cada elemento dentro de un array posee un índice, comenzando desde la posición 0 (cero).

#si desde chico te decian que el primer numero era 1 bueno en programacion se cuenta desde el 0

x = autos
x = autos[0]

print(autos)
print(x)

#las lista las podemos almacenar en variables, pero si queremos imprimir un unico elemento de esa lista, buscamos el indice del elemento en la lista
#y en la variable ponemos el nombre de la lista y entre [] el numero de indice
