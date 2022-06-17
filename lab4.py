#====================================
#Programacion orientada a objetos
#=====================================

#=======================================
#Una case para un objeto vacio
#Que no es tan vacio , necesita 
#la palabra pass 
#===========================

class ObjetoVacio:
    pass
#===================================
# nada es un objetoVacio
#=================================
nada= ObjetoVacio()
print(type(nada))
#====================================
#La clase llanta
#===========================
class Llanta:
    #=====================================
    #Variable cuenta es de toda la clase
    #=====================================
    cuenta = 0 
    #==========================================
    #Funcion constructora de identidad
    #__init__  es una funciuón reservada 
    #comienza con uno mismo : self 
    #pero puede ser otro nombre
    #parametros de entrada = default 
    #================================
    def __init__(mi,radio=50,ancho=30,presion=1.5):
        #variable de la estructura completa Llanta 
        Llanta.cuenta +=1
        #variables exclusivas de cada objeto
        mi.radio=radio
        mi.ancho=ancho
        mi.presion= presion

#=============================================
#Objetois instanciados
#============================================
llanta1= Llanta (50,30,1.5)
llanta2 = Llanta (presion =1.2)
llanta3 = Llanta ()
llanta = Llanta (40,30,1.6)
#==================================================
#Objeto que contiene otros objetos
#==================================================
class Coche:
    def __init__ (mi,ll1,ll2,ll3,ll4):
        mi.llanta1=ll1
        mi.llanta2 =ll2
        mi.llanta3 = ll3
        mi.llanta4= ll4
micoche= COche(llanta1,llanta2,llanta3,llanta4)
print("TOtal de llantas:",Llanta.cuenta)#Variable global de la clase 
print("Presion de la llanta4=",llanta4.presion)#Presion de la llanta 4
print("Radio de la llanta cuatro",llanta4.radio)
print("Radio de la llanta 3",llanta3.radio)
print ("Presion de la llannta 1 de mi cohce",micohce.llanta1.presion)
#=============================================================
#Encapsulamiento
#====================================

#========================================================
#Uso de la funcion proiperty para poner y obtener atributos 
#=========================================================
class Estudiante:
    def __init__(mi):
        mi.__nombre =''
    def ponerme_nombre(mi,nombre):
        print('Se lamó a la función ponerme_nombre')
        mi.__nombre=nombre
    def onbtener_nombre(mi):
        print('se llamo a obtener_nombre')
        return mi.__nombre
    nombre=property(obtener_nombre,ponerme_nombre)
    #=================================================
    #Crear Objeto estudiante sin nombre 
    #==========================================
    estudiante= Estudiante()

    #===================================================
    #Ponerle nombre usando la propiedad nombre y la función ponerle_nombre 
    #(SIn tener que llamar explicitamente  ala función)
    #=================================================================
    estudiante.nombre="Diego"
    #=====================================================================
    #Obtener el nombre con la funciíon obtrener_nombre
    #__nombre es una variable encapsulada (no visible desde afuera)
    #(sin tener que llamar explicitamente a la función obtener_nombre)
    print (estudiante.nombre)
    #Esto no funciona 
    #print (esstudiante.nombre)

    #===================================
    #Herencia de clases
    #=======================================
    class Cuadrilatero:
        def __init__ (mi,a ,b,c,d):
            mi.lado1=a
            mi.lado2=b
            mi.lado3=c
            mi.lado4=d
        def perimetro(mi):
            p=mi.lado1+mi.lado2+mi.lado3+mi.lado4
            print("perimetro=",p)
            return p
#=========================================        
#Su hijo rectangulo 
#rectangulo es hijo de cuadrilatero
#Rectangulo (cuadrilatero)
#=====================================
class Rectangulo (CUadrilatero):
    def __init__ (self,a,b):
        #============================
        #COnstructor de su madre XD
        #============================
        super().__init__(a,b,a,b)
#===========================================
#Su nieto cuadrado 
#Hijo de rectangulo
#COmo en el señor de los anillos 
#=========================
class Cuadrado(Rectangulo):
    def __init__(self, a):
        super().__init__(a,a)
    def area(self):
        area=self.lado1**2
        return area
#def perimetro (self) :
# p =4.0 * self.lado1
#print ("perimetro=",p)
#return p

#======================
#Crear un cuadrado 
#=======================
cuadrado1 = Cuadrado(5)

#===============================================
#Lllamar al metodo perimetro de su abuelo cuadrilatero 
#=========================================================
perimetro1 = cuadrado1.perimetro()

#========================================
#Llamar a su propio metodo area
#========================================

area1 = cuadrado1.area()
print("Perimetro =",perimetro1)
print ("Area=",area1)

#==============================================================
