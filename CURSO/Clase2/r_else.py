#else

#Especificando un bloque else posterior al bloque if o elif, lo que hacemos es establecer que acción vamos a tomar cuando la condición previa es False.

a = 200
b = 33
if b > a: #false
  print("b es mayor que a")
elif a == b: #false
  print("a y b son iguales")
else:
  print("a es mayor que b")
