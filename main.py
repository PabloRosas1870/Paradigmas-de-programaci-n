from aplicacion.banco.cliente_bancario import ClienteBancario
#============================================
#try : intenta (correr las instrucciones)
#excep: atrapar el error de una variable e 
#e se pouede convertir  a string 
#====================================================

#=============================================
#Error por sacar mas dinero del que tiene 
#=============================================

try:
	cliente=ClienteBancario("Jaime Rodriguez","Hernadez Sanches ", 28,0.0)
	cliente.guardarDinero (300)
	print(cliente.imprimirInfo())
	cliente.retirarDinero(400)
	print(clilente.imprimirInfo())

#==============================================
#Excepcion es el objeto mas general de error 
#=============================================

except Exception as e:
	print("Error :"+str (e))
#=====================================
#Error por usar un atributo privado
#======================================

try:
	print (cliente.__nombres)
except Exception as ex:
	print ("Error:" + str (ex))
	
#=======================================
# Forma correcta 
#========================================

print (cliente.nombres)

