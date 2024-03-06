print( "Saludos jugador, Que objeto quisiera comprar?\n\n"  +
      "Items disponibles:\n\n" + 
      "1.-Espadas:\n\n" + 
      "2.-Lanza Misiles Sovietico:\n\n" + 
      "3.-Incendia bosques +:\n\n" + 
      "4.-Navaja con tetanos de alto nivel:\n\n" + 
      "5.-Matralleta con balas expansivas:\n\n ")

comprar = [4]
dinero = 2500

Espada = 350
Misiles = 1800
LanzaLLamas = 970
Navaja = 175
ArmaLarga = 1099

if 0 in comprar or comprar == []:
    print("Seleccione del 1-5 el arma que prefiera para jugar:")
    
    if 1 in comprar:
        dinero= dinero - Espada
        
    if 2 in comprar:
        dinero= dinero - Misiles
        
    if 3 in comprar:
        dinero= dinero - LanzaLLamas
        
    if 4 in comprar:
        dinero= dinero - Navaja
        
    if 5 in comprar:
        dinero= dinero - ArmaLarga
        
    if dinero <0:
        print("Eres pobre, consigue pasta tio.")
        
    if comprar == [1] or comprar == [2] or comprar == [3] or comprar == [4] or comprar == [5]:
     print("Te resta: " + str(dinero) + "Peje coins")
     print("Se ha comprado el equipamiento belico")








