#Crear un programa teniendo en cuenta que la edad de la persona es 60 y colocar un print en el caso que tenga 65 y en el caso de que tenga 55

edad=60

if edad>=65:
  print("usted tiene 65")
  elif edad<=55:
    print("usted tiene 65")
   else:
    print("usted tiene 60")
    
#definir genero de un indivudo y una edad usando las condicionales y las sentencias 
#en el caso de que el genero y la edad no coincidan que usarias?

#recordando que if es si
#elif es entonces si
#else es entonces

sexo="Masculino"
edad=60

    
if sexo == "Femenino":
    if edad >= 60:
        print("Estás en edad de jubilarte")
    else:
        print("Todavía no estás en edad de jubilarte")
elif sexo == "Masculino":
    if edad >= 65:    
        print("Estás en edad de jubilarte")
    else:
       print("Todavía no estás en edad de jubilarte") 
