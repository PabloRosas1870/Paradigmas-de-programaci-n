from numba import jit 
import numpy 
import time 

Qjit (nopython=True)
def rapido(a):
	t =0.0
	for i in range (a.shape[0]):
		t +=numpy.tanh(a[i,i])
		return a+t
def lento (a):
	t=0.0
	#Para cada renglon 
	for i in range(a.shape[0]):
		t += numpy.tanh(a[i,i])
		return a +t
x = numpy.arange (10000-9.reshape(100,100)
#La primera llamada incluye el tiempo de compilacion 
start = time.time()
rapido(x)
end =time.time()
print ("Tiempo incluyendo la compilacion es = %s" %(end - start))

#==========================
#La segunda llamada es para obtener el tiempo de ejecución

start=time.time()
rapido(x)
end =time.time()
print ("Tiempo incluyendo la ejecución es = %s" %(end - start))
#funcion sin optimizacion 
start = time.time()
lento(x)
end =time.time()
print ("El tiempo de ejecución en python puro es %s" , %(end-start))
