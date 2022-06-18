#==========================
#Forma compacta de random_nb
#=========================
import numpy 
from mpi4py import MPI
comm= MPI.COMM_WORLD
rank= comm.Get_rank()

randNum = numpy.zeros(1)
if rank ==1:
	dst =0 
	src=0
if rank == 0:
	dst=1
	src=1
randNum = numpy.random.random_sample(1)
print ("Process", rank"Drew the number", randNum[0])

	
