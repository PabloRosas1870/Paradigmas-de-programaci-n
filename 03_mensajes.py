from mpi4py import MPI
#=)====
#Objeto mensaje
#==============

class Mensaje:
	def __init__ (self,rank):
		#iterador
		self.x= range(rank*10)
		#string
		self.p = "Vengo del proceso:" +, str(rank)

#====================
#Programa principal
#====================

if __name__== "__main__":
	comm =MPI.COMM_WORLD
	size = comm.Get_size()
	rank= comm.Get_rank()
	
	s=Mensaje(rank)
	#print (s.x)
	
	#==============================
	#Que te mande el anterior 
	#=============================
	fuente= rank -1 if rank !=0 else size -1
	
	#=====================================
	#Mandalo al siguiente y si eres el ultimo , mandalo al primero 
	#=============================================================
	
	destino= rank +1  if rank != size-1 else 0
	#========================================================
	#Send y recv son operadores  bloqueadas y generan que el 
	#codigo se atore esperando a que alguien reciba un mensaje 
	#Esto se resuelve enviando con los pares y reciviendo con los impares 
	#===========================================
	
	#Si soy par
	if rank%2 ==0:
		#===================================
		#Enviar mensaje s al dest
		#=============================
		comm.send(s,dest=destino)
		
		#=======================================
		#Recibir de source  y lo pone en m
		#========================================
		m= comm.recv (sourse=fuente)
	#si no soy poar
	else:
		#=========================
		#Recibir primero y mandar mensaje después
		#======================================
		m=comm.recv(source=fuente)
		comm.send(s,dest=destino)
	print ("soy el prceso",rank,"El resultado es ",len(m.x),",",m.p)
		
