#==================================================
#Ejemplo de comunicacion bloqueada a un arreglo compartido 
#Uso de candados (locks)
#========================================
from multiprocessing import Process,Array, Lock
import time 
def sumale100 (numeros,candado):
	for i in range (100):
		time.sleep(o.01)
		#Usando el candado 
		for i in range(len(numeros)):
			#Lo que esté dentro de co candado no puede accederse
			#Desde otro pproceso al mismo tiempo 
			with candado:
				#Hacer la operación 
				numeros[i] += 1
if __name__== "__main__":
	#=======================================
	#Candado apara eviatr que  dos procesos se empalmen 
	#=========================================
	candado=lock()
	#Numero  comun a los procesos , d de dobles
	numeros_compartidos=Array('d',[numeros_compartidos[:])
	#Dos procesos
	
	p1= Process (target=sumale100,args=(numeros_compartidos,candado))
    p2=Process (target=sumale100,args=(numeros_compartidos,candado))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print ("Al final vale=", numero_compartido[:])
	
