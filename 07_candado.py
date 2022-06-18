#================================================0
#Ejemplo de la comunicación bloqueada al mismo valor compartido
#=============================================================

from multiprocessing import Process, Value , Lock
import time 

def sumale100(numero,candado):
    for i in range(100):
        time.sleep(0.1)
        #POner el candado
        candado.acquire()
        #Hacer la operacion
        numero.value += 1 
        #quitar la operación 
        numero.value += 1 
        #quitar el candado 
        candado.release()

if __name__ "__main__":

    #candado para evitar que dos procesos se empalmen
   candado =Lock()

   #===========================================================
   #Néro común a los procesos , i de enteros , comienza siendo 0
   #Value es un objeto de numero compartido 
   #==============================================================

   numero_compartido= Value ('i',0)
   print ("Al principio vale =", numero_compartido.value)
   p1= Process (target=sumale100,args=(numeros_compartidos,candado))
   p2=Process (target=sumale100,args=(numeros_compartidos,candado))

   p1.start()
   p2.start()

   p1.join()
   p2.join()

   print ("Al final vale=", numero_compartido.value)

