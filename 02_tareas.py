#========================================
#mpirun -4 python3 tareas_mpi.py
#=====================================

from mpi4py import MPI

#========================
#Objeto de comunicadores 
#==========================

comm= MPI.COMM_WORLD

#===========================
#Cuantos somos en total
#===========================

size = comm.Get_size()

#======================
#Quien soy
#===================

rank = comm.Get_rank()
#===========================
#Si yo soy el cero , haf¿go esto
#===================================
if rank ==0 :
	print ("Yo soy el proceso 0 ")
	
#==========================================
#Si yo soy el uno hago esto otro 
#=========================================

elif rank ==1 :
	print ("Yo soy el proceso 1")
	
#============================================
#Si yo no soy el uno ni el dos , entonces hago esto otro 
#========================================================
else:
	print ("Yo no soy ni el uno ni el dos")
print ("Reportandome, soy el proceso ", str(rank),"de" ,str(size))
