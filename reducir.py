#=============================================
#Uso de construcciones (colapsar resultados)
#==========================================

#=========================================
#Multiplicacion de todos los numeros en la lista 
#===============================================

from functools import reduce 

bigdata =[2,3,5,7,13,17,23,29]

#==============================
#Función x*y
#===========================

multiplicar = lambda x,y: x*y

print(reduce(multiplicar,bigdata))

