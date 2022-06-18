import numpy as np 
from mpi4py import MPI
comm= MPI.COMM_WORLD
rank = comm.Get_rank()

#==================
#Arreglo cob  un solo elemto 
#=============================
randNum =np.zeros(1)
if rank == 1 :
	randNum = np.random.random_sample(19
	print("Proceso", rank, "generó", randNum[0])
	comm.Isend(randNum,dest=0)
	req=comm.Irecv(randNum,source=0)
	req.Wait()
	print ("Proceso", rank "Recibió el numero", randNum[o])
	
if rank == 0 :
	randNum = np.random.random_sample(19
	print("Proceso", rank, "generó", randNum[0])
	comm.Isend(randNum,dest=0)
	req=comm.Irecv(randNum,source=0)
	req.Wait()
	print ("Proceso", rank "Recibió el numero", randNum[o])
	
	
