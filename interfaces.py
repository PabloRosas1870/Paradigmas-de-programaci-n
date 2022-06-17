#================================
#Del direcrorio aplicacion , el subdirectorio repositorio 
#el archivo base de datos.py : trae el objeto base de datos 
#============================================

from aplicacion.repositorio.basededatos import BaseDeDatos

#======================================================
#Del directorio aplicacion , el subdirectorio repositorio ,
#El archivo s3.py : trae el objeto s3
#====================================================

from aplicación.repositorio.s3 import S3

#=====================================================
#Del directorio aplicacion , subdirectorio  repositorio, traer
#el archivo sistema de archivos.py, trae el objeto sistema de archivos 
#===============================================================

from aplicacion.repositorio.sistemadearchivos import SistemaDeArchivos

#======================================================
#Del directorio Aplicacion , subdirectorio modelos, 
#El archivo usuarios.py traer el objeto Usuario
#===================================================

from aplicacion.modelos.usuario import Usuario

#==========================================
# Del directorio aplicacion  y agun subdirectorio
#traer ----
# el archivo manejo de inscripciones .py  : trae el objeto ManejoDeInscripciones 
#============================================================

from aplicacion.negocios.manejodeinscripciones import ManejoDeInscripciones

#=============================================
#Crear el objero usuario 
#=============================

usuario= Usuario("Roberto", "Jimenez",18)

#==========================
#Crear el objeto s3
#=========================

repositorioS3= S3 ("321321321","sdf324223", "MiCubeta")

#=====================================================
#Interface  inscribir usuario de Manejo de inscripciones 
#=======================================================
repositorioSistemaDeArchivos = SistemaDeArchivos("/home/users")

#=================================================
#Interface inscribir usuario del objeto manejo de inscripcipones 
#=================================-=============================

ManejoDeInscripciones.inscribirUsuario(usuario,repositorioSistemaDeArchivos)
print ("\n")
#===============================================
#Crear el objeto base de datos 
#====================================

repositorioBaseDeDatos = BaseDeDatos("localhost","admin","admin123")
#===================================
#Interface inscribir usuario del on¿bjeto maneji¿o de inscripciones 
#================================================
ManejoDeInscripciones.inscribirUsuario(usuario,repositorioBaseDeDatos)
print ("\n")

