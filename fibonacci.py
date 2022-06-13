#===========================
#Recursividad y memoización
#==========================



#====================================
#Herramientas para memoización
#===================================
from functools import lru_cache

def fibonacci_lento(n):
     if n==1 :
         return 1
     if n==2:
         return 1
     if n>2:
         return fibonacci_lento(n-1)+ fibonacci_lento(n-2)

for i in range (1,10):
    print(str(i)+":",fibonacci_lento(i))

#====================================================
# Optimización 2 , uso de conjujntos para guardar valores 
#=========================================================


#=====================================
#Conjuntoi de fibonaccis 
#===============================
fibonaccis ={}

def fibonacci(n):
    #=======================================
    #Revisa si ya existe y regresa el valor 
    #=======================================
    if n in fibonacci:
        return fibonaccis[n]
    if n==1:
        valor=1
    elif n==2:
        valor =1
    elif n>2:
        valor= fibonacci(n-1)+ fibonacci(n-2)
    #===========================================
    #Guardalo 
    #==========================================
    fibonaccis [n]=valor 
    return valor
print ("Este es el segundo algoritmo para los fibonacci")

for i in range (1, 100):
    print(str(i)+":",fibonacci(i))

#==========================
#Uso de decoradores para memoización 
#maxsize: es cuantos anteriores guarde 
#=====================================

@lru_cache (maxsize =3)
def nfibonacci (n):
    if type (n)!= int:
        raise TypeError ("wigga, please, u know n has to be a positive  integer")
    if n<1:
        raise TypeError ("Niqqa, please!")
    if n==1:
        return 1
    elif n==2:
        return 1 
    elif n>2:
        return nfibonacci(n-1)+ nfibonacci(n-2)
for i in range (1,100):
    print(str(i)+":",nfibonacci(i))

