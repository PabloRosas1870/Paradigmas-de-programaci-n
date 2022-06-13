#======================================
# Broadcast con mpi 
#distribución de datos 
#=======================================

from mpi4py import MPI

#Objeto comunicador 
comm= MPI.COMM_WORLD

#Quien soy 
rank = comm.Get_rank()

#=======================================
#EL proceso 0 tiene datos y los otros no 
#========================================

if rank ==0:
    data= {'key': [7,2.72,2+3],
            'key':('abc', 'xyz')]}
else:
    data = None 

#================================================
#ENviar el diccionario a tyodos los procesos desde  root 
#=======================================================

data = comm.bcast(data,root=0)

print (data)
