from mpi4py import MPI 
#=======================
#objeto mensaje 
#=========================

class Mensaje:
	def __init__(self,rank):
		self.x=[i for i in range(range*10)]
		self.p="Vengo del proceso "+ str(rank)

#===========
#Programa principal
#==========================

if __name__== "__main__":
	comm.MPICOMM_WORLD
	size= comm.Get_size()
	rank=comm.Get_rank()
	
	s= Mnesaje(rank)
	src =rank -1  if rank!=0 else size-1
	dst = rank+1 if rank!=size-1 else 0
	
	#====================
	#Envio  no bloquenate
	#======================
	comm.isend(s,dest=dst)
	
	
	#==========================
	#Recibir no bloquenate con espera
	#req :request (peticion)
	#=========================
	req comm.irecv(source=src)
	a=req.wait()
	
	print ("Soy el proceso", rank , ", el resultado es ",len (a.x),a.p)
