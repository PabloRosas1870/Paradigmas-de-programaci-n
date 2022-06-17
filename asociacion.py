#===================================================
#La clase A tiene tres numeros reales 
#============================================
class A:
	__a:float=0.0
	__b:float =0.0
	__c:float =0.0
	
	def __init__ (self,a:float,b:float,c:float):
		self.a=a
		self.b=b
		self.c = c
#=========================================
#La clase B tiene dos numeros reales 
#================================================
class B:
	__d:float=0.0
	__e:float= 0.0 
	
	def __init__ (self,d :float, e:float):
		self.d =d
		self.e = e
#==============================================
#Metodo para sumar todo (internos mas externos 
#===============================================

def sumar_todo( self, aa:float,bb:float):
	x:float = self.d+self.e+aa+bb
	return x

#========================
#Asociacion 
#===================
 #Usando objetos independientes 
objetoA=A(1.0,2.0,3.0)
objetoB = (4.0, 5.0)
print (objetoB.sumar_todo(objetoA.a,objetoA.b))

#===============================
#El objeto c tiene dos reales y un objeto A
#El objeto A se instancia dentro del objeto c 
#===================================================

class C:
	__d:float=0.0
	__e:float=0.0
	__Aa:A=None
	
	def __init__(self,d:float,e:float):
		self.d =d
		self.e=e
		#A está instanciado en c 
		self.Aa=A(1.0,2.0,3.0)
	
	def sumar_todo(self):
		x:float = self.d + self.e+self.Aa.a.b
		return x

#========================================================
#Composición 
#Contiene otro objeto adentro 
#================================
objetoC =C (4.0,5.0)
print (objetoC.sumar_todo())

#=====================================
#Objeto D tiene dos reales y un objeto adentro 
#definido por fuera 
#===============================================
class D:
	__d:float=0.0
	__e:float= 0.0
	__Aa:A=None
	
	def __init__ (self,d:float,e:float,Aa:A):
		self.d=d 
		self.e=e
		self.Aa=Aa
		
	def sumar_todo(self):
		x:float=self.d+self.e+self.Aa.a+Self.Aa.b
		return x
		
#=========================================
#Agregación 
#Construye el objeto agragado por fuera
#===========================================
objetoD=D(4.0,5.0, oobjetoA)
print (objetoD.sumar_todo())

 
 
