#===============================================
#Uso de filtros 
#========================================


#===============================
#Hacer una lista de los numeros por arriba del promedio 
#=======================================================

#Modulo de estasdistica 

import statistics 

bigdata=[ 1.3,3.4,-200,1.5,6,]
promedio= statistics.mean(bigdata)
print(promedio)

#====================================================
#Hazme una lista de lemetos que cumplan la condición x > promedio 
#filter (condición, datos )
#===========================================
print (list(filter( lambda x:x >promedio,bigdata)))

#=====================================
#Limpiar los datos 
#===================================

paises = ["","Argentina" , "", "Brasil", "Chile", "", "Mexico", "", "Colombia","", "", "Cuba" "Venezuela"]
#======================================
#FIltra lo que  no contiene nada 
#=====================================

print (list (filter(None ,paises)))

