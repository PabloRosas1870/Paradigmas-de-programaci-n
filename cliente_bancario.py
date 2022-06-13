#========================================
#Clase Clientebancario
#=================================
class ClienteBancario:
    __nombres: str = None 
    __apellidos: str =None 
    __ edad: int =0
    __balanceDeCuenta: float =0.0

    def __init__ (self, nombres:str,apellidos:str,edad:int=0,balanceDeCuenta: float=0.0):
        self.__validarEdad(edad)
        self.__validarCantidad (balanceDeCuenta)
        self.nombres= nombres
        self.apellidos=apellidos 
        self.__edad=edad
        self.balanceDeCuenta=balanceDeCuenta

    def getNombreCompleto (self)-> str:
        return self.nombres + ""+ self.apellidos
    def __mandarEmail (self,titulo:str,texto:str)-> None:
        print("mandar email:"+titulo+"con texto:" +texto )

    def __enviarBalanceAlBanco (self,cantidad:float) ->None:
        print("ENviando cantidad:" + str (cantidad)+"al banco...")

#=======================================================================
#Método privado con dos guines bajos 
# Si la edad es menor que 18 gerenar mensaje 
#===========================================

def __validarEdad (self,edad:int)-> None:
    if edad <18:
        raise Exception ("todavia ta chavo")

def inprimirInfo (self)-> str:
    return "NOmbre:"+ self.getNombreCompleto()+ ",Edad:" +str(self.__edad)+ ",Balance:" +str (self.__balanceDeCuenta)

#==============================================
#Método privado  que checa si el balance es negativo
# y genra un error 
#======================================0

def __validarCantidad (self,balanceDeCuenta:float)-> None:
     if balanceDeCuenta < 0:
         raise Exception ("El balance de cuenta no puede ser negativo (also, échenle un taco)")
     
def guardarDinero (self,cantidad:float)->None:
    self.__balanceDeCuenta =self.__balanceDeCuenta + cantidad
    self.mandarEmail("_ _ _ guardando depósito_ _ _ ","Se recibieron"+str (cantidad))
    self:__enviarBalanceAlBanco(cantidad)

def retirarDinero (self,cantidad:float)-> None:
    cantidadFInal = self.__balanceDeCuenta-cantidad
    self.__ validarCantidad(cantidadFinal)
    self.__balanceDeCuenta= cantidadFInal
    self.__mandarEmail("----retirando dinero---","seretiró"+str (cantidad))

    self.__enviarBalanceAlBanco(cantidad)



