from mpi4py import MPI 
import numpy 

comm = MPI.COMM_WORLD 
rank =comm.Get_rank()

#=====================================
#Se indica el tipo de datos explicitamente 
#=========================================

#===========================================
#Ejemplo 1 usando enteros 
#=========================================

if rank ==0:

    #==============================================
    #   Arreglo de enteros del 1 al 9  
    #===================================

    data = numpy.arange(10,dtype ='i')
    #===========================================
    #ENvio bloquenate esqpecificando el tipo de datos
    #===============================================

    comm.Send ([data,MPI.INT],dest=1 ,tag =77)

elif rank==1:
    data = numpy.empty(10,dtype='i')
    comm.Recv ([data,MPI,INT],source= 0, tag=77)
    print (data)

#=================================================
#Tambien se pued esin decidir el tipo de dato pero deben 
#coincidir el tipo de arreglo a los extremos del mensaje 
#==========================================================

#===================================
#Ejempĺo 2 usando flotantes 
#===========================================

if ranki== 0:
    data = numpy.arange (10,dtype=numpy.float64)
    comm.Send(data,dest=1,tag=13)

elif rank ==1:
    data = numpy.empty (10, dtype= numpy.float64)
    comm.Recv(data,source=0,tag=13)
    print (data)

