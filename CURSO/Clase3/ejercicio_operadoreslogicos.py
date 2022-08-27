#mplementando los Operadores Lógicos


#ahora, con los conocimientos de Operadores Lógicos incorporados,
#vamos a continuar con el ejemplo de la jubilación planteado previamente. Repasamos el código previamente desarrollado:

sexo = "Masculino"
edad = 64

if sexo == "Femenino" and edad >= 60:
    print("Estás en edad de jubilarte")
elif sexo == "Masculino" and edad >= 65:
    print("Estás en edad de jubilarte")
else:
   print("Todavía no estás en edad de jubilarte") 
   
#utilizamos el operador and


sexo = "Masculino"
edad = 65

if sexo == "Femenino" and edad >= 60 or sexo == "Masculino" and edad >= 65:
    print("Estás en edad de jubilarte")
else :
   print("Todavía no estás en edad de jubilarte") 
   
#utilizamos el operador or
