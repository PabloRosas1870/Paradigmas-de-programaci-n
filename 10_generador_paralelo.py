from multiprocessing import Process
import random
import os 
N: int =10

def generador (N:float)-> None :
    semilla: float =random.uniform(-1,1)
    print ("la semilla es:" ,semilla)
    random.seed(semilla)
    for i in (N):
        x:float =random.uniform(-1,1)
        y:float = random.uniform(-1,1)
        print ("x=",x,"\t y =",y)

procesos =[]
cpus =os.cpu_count()
print ("Procesadores=",cpus)
for i in range (cpus):
    procesos.append(Process(target=generador,args=(N,)))

#COmienza los procesos en paralelo
for i in procesos:
    proceso.start()

#Espera q que todos los procesos terminen 
for proceso in procesos:
    proceso.join()

