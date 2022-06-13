from aplicacion.modelos.usuario import Usuario
from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios

#=========================================0
#CLase storemanager
# NO TIENE VARIABLES!!!
#========================================

class ManejoDeInscripciones:
    #==========================================
    #Decorador static method 
    #El objerto solo tie3ne la función de inscribirUsuario
    #ENVUELVE LA FUNCIÓN SIN LLAMAR VARIABLES LOCALES
    #EL OBJETO ManejoDeInscripciones es la interface intercambiable 
    #==========================================================

    @staticmethod
def inscribirUsuario (usuario:Usuario,repositorioDeUsuarios:RepositorioDeUsuarios)-> None:
    print("----------> Guardando Usuario ...\n")
            repositorioDeUsuarios.abrir()
            repositorioDeUsuarios.guardar(usuario)
            repositorioDeUsuarios.cerrar()
