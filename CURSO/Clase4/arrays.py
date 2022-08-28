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


#Para acceder a la cantidad de elementos que posee el array debemos llamar a una función interna de Python llamada len() que significa lenght (longitud).

len(autos)

esto se hace para saber cuantos elementos hay en esta lista


Para agregar un elemento vamos a usar la función append(). La sintaxis es la siguiente:
  
  autos.append("Dodge") # ['Chevrolet', 'Volvo', 'BMW', 'Dodge']
  
  asi apareceria en la lista
  
Para remover elementos lo podemos hacer de 2 maneras, una es usando la función pop()

  autos.pop(1)
  autos # ['Chevrolet', 'BMW']
  
  y se borro el elemento con indice 1
  
Otra forma de remover elementos del array es usando la función remove() 

  autos.remove("BMW")
  autos # ['Chevrolet']
