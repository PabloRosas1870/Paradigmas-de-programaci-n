''' ESTE ES UN SUPERCOMENTARIO 
DE INICIO A NUESTRO RESUMEN 
'''
#=================================
#Operaciones básicas 
#================================
print (2+3)
print(2*3)
print (2/3)
print (2**10)
print (2**0.5) #raiz cuadrada 
print (10%2) 
print (10%0.1) #Exclusivo de python 


#=============================================
#Para saber el tipo de objeto se usa type
#=============================================

t=0
print(type (t)) # entero 

t= 3.6 
print (type(t)) #real flotante
t=True 
print (type(t)) #booleano, bool 

#===============================
#Mensajes a pantalla 
#===============================
print ("Este es un comando de python ", "Este es otro enunciado", t)

print ('id:',1)
print ('First name:', 'Steve')
print('Last Name' , 'Jobs')
print ("Vamos a sumar esto" + "Con esto otro ")

#=====================================================
#Continuar juna instruccion en varios renglones 
#==================================================
if 100 > 99 and \
200<= 300 and\
True!= False:
	print ('Hello World')
	
#====================================
#Comandos diferentes en la misma linea
#=====================================
print ("Hola"); print ("tu") #Se considera un mal estilo

#===============================================
#Usando parentesis redondos , cuadrados  o llaves
#Se puede escribir en varios renglones 
#========================================== 

list =[1,2,3,4,
5,6,7,8,
9,19,11,12]

matriz=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print (list)
print (matriz)
#=======================================
#Identacion estricta para procesos dependientes de : (dos puntos)
#==================================================================

if 10>5:
	print (" diez es mayor que cinco")
	print ("otra identacion ")

for i in list:
	print (i)
	print ("oki")
	
if 10>5 :
	print ("verdadero")
	if 10<20:
		print ("verdadero")
elif 5>3: #comienza segunda condicion 
	print("Esto no se imprimira ")
else:
	print :("aqui unca llega ")

#=============
#Funciones
#==============
def say_hello(name):
	print ("Hello ", name)
	print ("Welcome to python tutorials")

say_hello("julian")
