#=======================================
#Conjunto en python
#======================================
even_nums={2,4,6,8,10}# Conjunto de números pares
print(even_nums)
#EL bool no es parte del conjunto 
emp={1,'esteve',10.5.True}#COnjunto de diferentes objetos 
print(nums)

#==========================================
#COnvertir secuencia a conjunto
#No lo genera en orden
#===============================================
s= set ('Hello}')
print(s)
#===========================================
#De dicccionario a conjunto:conjunto de llaves 
#===============================================
d={1:'one', 2:'Two'}
s= set (d)#Casteo sobre d
print(s)
s.add(100)
print(s)

s.update(nums)
print(s)

s.remove(100)
print(s)

s1= {1,2,3,4,5}
s2={4,5,6,7,8}
su=s1|s2 #union de conjkuntos
print (su)
si=s1&s2 #interseccion 
print (si)

sd= s1_s2 #DIferencia de conjuntos 
print (sd)
sd1=s2-s1
print(sd1)
#ss= Omitimos esa línea a falta del caracter correspondiente, pero la idea es que la diferencia simetrica está expresada por un conjunto "elevado al otro"

#============================================================================
#Uso de diccionarios
#============================================================================
capitals={"USA": "Washington DC" , "France": "Paris" , "India" :"New Delhi"}
print(capitals)
#========================================================================
#llave:valor
#========================================================================
#diccionario vacío 
d={}
#LLave entera , valor string
numNames={1:"One",2:"Two",3:"Three"}
#Llave real, valor string
decManes={1.5:"ONe and a half" ,2.5:"Two and a Half", 3.5:"Three and a half"}
#Llave tupla, valor string
items={("Parker","Reynolds","Camlin"):"pen",("LG","Whirlpool","Samsung"):"Refrigeradores"}
#Llave string , valor int
romanNums={'I':1,'II':2,'III':3, 'IV':4, 'V':5}
print(RomanNums)
print(RomanNums["I"])
print (capitals.get("India"))
print(capitals.get("india"))
#Reportar llave y valor 
for k in capitals:
       print("Key="+k", Value"+capitals[k])
#Nuevo dato para el diccionario
del capitals["Mexico"]
print(capitals)

#Borrar el diccionario
del capitals

#Reportar llaves 
print(romanNums.Keys())
#Reprotar valores
print(romanNums.values())
#Juicio de llave (está o no está la llave en el diccionario)
print("I" in romanNums )
print("X"in romanNums)
print("XX"not in romanNums)

#======================================================================
#listas
#Las listas pueden ser de objetos difernetes 
#======================================================
miprimeralista=[]#Lista vcía
print(miprimeralista)
#===========================================
#Llenado de lista
#==============================================
miprimeralista=[1,"Javie",1.34,"Bosco","Angel","Abigail",True]
print(miprimeralista)
#==================================================
#list: hacer una lista
#range(i,j):seceuncia de i hasta j-1
#===================================================
nums=list(range(1,61))
for i in nums:
    print(i)
#============================================
#INcluir nuevos elementos a la lista
#===========================================
nums.append(61)
nums.append(62)
nums.append(61)
print(nums)
#=============================================
#Quitar elementos de la lista 
#=============================================
nums.remove(61)
print(nums)
#===============================================
#QUitar elemto con indice i
#==============================================
i=61
del nums[i]
print(nums)
#============================================
#Borrar la lista
#=================================================
del (nums)
#==========================================
#SUmar LISTAS
#========================================
L1=[1,2,3]
L2=[4,5,6]
print(L1+L2)
#=========================================
#Llenado a mano 
#=========================================
potencial=[]
for i in range(0,10000):
    potencial.append(float(i))
print(potencial[100])
#==========================================================
#Generar una tupla con llista
#===========================================================
potencial=tuple(potencial)
print(potencial[100])



    
