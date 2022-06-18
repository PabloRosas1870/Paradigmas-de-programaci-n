#========================================
#Uso de MPI optimizado para calculos numericos 
#=================================================

from mpi4py import MPI

import numpy as np
class Mensaje:
	def __init__ (self,rank):
		#==========================================
		#Arreglo de numpy (optimizado)
		#)===================================
		self.x = np.array([float(x+rank)
		self.p = "Vego del proceso " + str (rank)
		
#================
#programa
#================
if __name__ == "__main__":
	comm=MPI.COMM_WORLD
	size= comm.Get_size()
	rank=comm.Get_rank()
	
	s=Mensaje(rank)
	src=rank-1 if rank != 0 else size -1 
	dts = rank+1 if rank!= size-1 else 0
	
	#===================
	#Arreglo para enviar 
	#=====================
	
	m=s.x
	
	#print(m)
	
	#==================
	#Isend Irecv son para comunicacion 
	#no bloqueante se arreglos de numpy 
	#==================================
	comm.Isend (m,dest=dst)
	
	#=============================
	#Arreglo para recibir 
	#con dimension 10 y tipo de datos 
	#float64  (doble presicicion 
	#===============================
	a= np.zeros(10,dtype=np.float64)
	req=comm.Irecv(a,source=srrc)
	req.Wait()
	
	print ("Soy el proceso ", rank ,",El resultado es",a)
