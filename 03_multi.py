from multiprocessing import Process
import os 
import math
import time 

def calc():
	for i in range (0,40):
		math.sqtr(i)
		
procesos=[]
cpus = os.cpu_count()
print("Nucleos en tu cpu", cpus)
for i in range (cpus):
	print("Registrando el proceso  %d" %i)
	procesos.append(Thread(target=calc)
atart= time.time()
for proceso in procesos:
	proceso.start()
for proceso in procesos:
	proceso.join()
end time =time.time()
print("Se tardó:" , end-start)
