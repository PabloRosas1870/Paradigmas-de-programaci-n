#======================================
#Input permite obtener datos del usuario en prompter 
#=================================================

nombre = input("Dame tu nombre:")
print ("Hola como estas ", nombre)

#=====================================
#Los enteros son de precision ilimitada 
#======================================

y=50000000000000000000
print (y)

#============================
#Sepuede delimitar los numeros con guion 
#=======================================

y = 5_000_000
print (y)

#=======================================
#La funcion int cambia strings  y float en enteros  
#==================================================

numero= int (input("Dame tu edad:"))
type (numero)

#============================
#La notacion cientifica de flotantes utiliza e o E 
#===================================================

#1.2 x10 ala -9
#============================
y=1.2E-09
print (y)

#=================================
#La funcion float convierte enteros y strings en flotantes
#==========================================================

y=float("14.13")
print (y)

#=======================================
#Los complejos se escriben con la raíz de menos uno
#j siempre con un numero prefijo 
#No se acepta la j suelta 
#==================================================
z = 1+1j

#============================
#Strings en varias lineas 
#============================

parrafo =""" En el bosque de la china
la chinita se perdió"""
print (parrafo)

#=========================================
#La funcion len obtiene el tamaño del string 
#"""""""""""-----------------------------------------

n= len (parrafo)
print (n)
 
#============================
#Las letras en un string ocupan lugares como en un arreglo 
#tambiende atras hacia adelante comenzando en -1 el ultimo
#=============================================================

palabra= ("hola")
print (palabra[0])
print (palabra[-4])

