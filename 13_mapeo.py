from mpi4py import MPI 
import math

comm= MPI.WORLD
size=comm.Get_size()
rank =comm.Get_rank()

n=40 
x= range (n)
m= int (math.ceil(float(len(x))/size))
x_chunk = list(x [rank*m:(rank+1)*m])
r_chunk= list (map (math.sqtr,x_chunk))

#=============================0
#UNa sola lista de todos los datos 
#===============================

r= comm.allreduce(r_chunk)

#===========================================
#Una sola matriz con todos los datos 
#===========================================
rr= comm.allgather(r_chunk)

#======================================0
#UNa matriz con todos los datos 
#========================================
rrr =com.gather(r_chunk,root=1)

if rank ==0:
    print (r)
    print(rr)
    print(rrr)
if rank ==1:

