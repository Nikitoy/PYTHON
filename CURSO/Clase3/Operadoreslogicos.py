#Operadores Lógicos

#Los operadores lógicos (and, or y not) nos van a permitir operar con los valores booleanos True y False, 
#obteniendo un nuevo valor de verdad, a partir de trabajar con estos operadores lógicos. 

#Operador not (Negación)

#not True # False
#not False # True

#Esto lo podemos desarrollar también con operaciones que retornen un valor de verdad. Por ejemplo:

x = 2
y = 5

x > y # False

not x > y # True


#Operador and (y)

#también conocido en otros lenguajes se suelen usar los símbolos &&, es un operador que nos permite evaluar dos valores de verdad, 
#los cuales para obtener un valor de verdad True, 
#ambos operadores deben ser True, si uno de ellos es False el resultado obtenido será False. Veamos un ejemplo:

True and True # True
True and False # False
False and True # False
False and False # False


#Esto mismo lo podemos ver aplicado con operadores condicionales.

5 > 3 and 5 == 3 + 2 # True

5 < 3 and 5 == 5 # False

5 == 5 and 5 != 5 # False

5 < 3 and 5 != 5 # False


#Operador or (o)

#es un operador que del mismo modo que el operador and nos permite operador con valores de verdad,
#pero en esta ocasión basta con qué uno de valores booleanos sea True para que el resultado final sea True. Veamos un ejemplo:

True or True # True
True or False # True 
False or True # True 
False or False # True 

#Esto mismo también lo podemos ver en conjunto con los operadores condicionales.

5 > 3 or 5 == 3 + 2 # True

5 < 3 or 5 == 5 # True

5 == 5 or 5 != 5 # True

5 < 3 or 5 != 5 # False
