#====================================
#Primera funcion
#===================================
def saludo():
    #===============================
    #Documentacion rapida
    ##=============================
    """Esta fucnión saluda"""
    print("sups my bruddas")

#===============================
#llamando a la función 
#=================================
saludo()
#=====================================================
#Se ejecuta pero no se asigna 
#================================================
salida = saludo()
#================================
#ESTO NO FUNCIONA
#===================================
print(salida)
#==============================
#Moostrar documentacion
#================================
#help(saludo)
#=====================================
#Función con argumento
#=====================================
def salu2(nombre):
    print("sups" ,nombre,"!")
salu2("Doge")
salu2("Cheems")
#=================================================
#Ahorrar trabajo al robotito (intérprete)
#nombre:str (la variable es un str)
#=================================================
def saludos (nombre:str):
    """Esta fiuncción te saluda por tu nombre estrictametn
    print()"""
    print("ey yoo, it's ma wiqqa",nombre,"!")
saludos("doge")
a=123
print(type(a))
saludos(a)
#==============================================
#FUnción con argumentos
#==============================================
def saludos_multiples(nombre1,nombre2,nombre3):
    #Esta función saluda a tres panas a la vez
    print("hey!", nombre1,"sups,",nombre2,"and u ",nombre3)
saludos_multiples("DOge","DOguette", "Uncle Tedd")
#===========================================================
#FUNCIÓN DE N ARGUMENTOS
#=========================================================
def muchos_saludos(*nombres):
    """Esta función saluda a todos los panas que quieras"""
    i=0
    #===========================================================
    #end= es jpara ponerlo de corrido 
    #============================================================
    print("Sups",end="")
    while len(nombres )>i:
        #Último nombre
        if(i==len(nombres )-1):
            print(nombres[i])
        else:
            #CUalquier otro nombre
            print(nombres[i],end=",")
        i+=1
muchos_saludos("cheems","doge","Nate","Abril","Higgers")
#=)====================================================================
#Lllamar al a fucncion con argumetnos en desorden 
#)))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
def greet (firstname, lastname):
    print("Heck you ",  firstname, lastname,"!")#Los cuales pueden ser llamados en desorden
greet(lastname="Cheemsmith",firstname="Doge")
#===================================================================
#Funciones con argumentos escondidos**
#========================================================================
def greet2(**person):
    #==========================================================
    #Persona tiene caracteristicas first name and lastname
    #=========================================================
    print('Hello', person['firstname'],person['lastname'])
greet2(firstname='DOge',lastname='Cheemsmith')
greet2 (lastname='Higgers',firstname='Nathaniel')
#=========================================================================
#Funciones con valores por default
#=========================================================================
def greet3(name='Buddy'):
    print('Hello', name)
greet3()#utiliza el valor default
greet3("doge")
#===================================================================
#Función con resultado
#============================================================
def suma(a,b):
    return a+b
#==================================================
#PROGRAMACION FUNCIONAL
#Se pueden llamar finciones enj nfinciones
#=================================================
total=suma(5,suma(10,20))
print (total)
#=========================================================
#Calculo lamda
#nombre d ela función= lamda variable: función
#=================================================
x_cuadrada=lambda x:x*x
a1=x_cuadrada(5)
print(a1)
#==================================================
#Lambdade varias variables
#===================================================
suma= lambda x1,x2,x3:x1+x2+x3
print(suma(1,2,3))
sumas=lambda *x:x[0]+x[1]+x[2]+x[3]
print(sumas(100,200,300,400))
#=======================================================================
#USO DE UNA FUNCIÓN ANONIMA
#EL ARGUMENTO FUERA DEL PARENTR3ESIS
#======================================================================

