
reiniciar = True

while reiniciar:

   try:
    num1 = int(input("Introduce un numero para multiplicar: "))
    num2 = int(input("Introduce otro numero para multiplicar: "))
    
   except ValueError:
    print("Hay algun error :,( ), introduce un numero de nuevo. ")
    
   else:
        print("El resultado es: ", num1 * num2)
    
   finally:
     pregunta = input("Quieres seguir multiplicanding? introduce s/N:\n ")
   if pregunta == "N":
     reinicio= False
     
   else:
     print("En-ten-didoo, vamos a multiplicar de nuevo:")