from threading import Thread
import os 
import math
import time

def calc():
	for i in range(0,40):
		math.sqtr(i)
		
threads=[]
cpus = os.cpu_count()
print("Nucleos en tu cpu", cpus)
for i in range (cpus):
	print("Registrando el hilo %d" %i)
	threads.append(Thread(target=calc))
	
start =time.time()

for thread in threads:
	thread.star()
for thread in threads:
	thread.join()
end =time.time()
print ("Se tardo :", end - star)
