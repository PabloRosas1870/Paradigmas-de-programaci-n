#======================================
#LABORATORIO TRES 
#CONDICIONALES
#======================================
 precio=50
 #======================
 #Si esto
 #====================
if precio<50:
     print("EL precio es mayor a cincuenta")
#==============================================
#SI no, esto otro
#==========================================
elif precio>50:
    print("El precio es mayor de 50")
#======================================
#SI nada de lo anterior...
#======================================
else:
    print("el precio es 50")
#==============================================
#Condicionales Anidados
#=============================================
if total >100:
    if total>500:
        print("Total es matyorque 500")
    else:
        if total<500 and total > 400:
            print("total es maoyor5 que 500 pero mayor que cuatrocientos")
        elif total<500 and total >300:
            print("total entre 300 y500 ")
        else:
            print("total entre 100 y 300")
#================================================
#Condicional de igualdad son con ==
#===============================================
elif total == 100:
    print ("totales cien")
else:
    print("total es menor que cien")
#=========================================================
   # contador mientras la condicion sea verdadera 
#=========================================================
num=0
while num<5:
    num= num+1
    print('num=',num)
    if num==3:
        break
num=0
while num<5:
    nums=[10,20,30,40,50]
    for i in nums:
        print (i)
#==================================================
#Bucle sobre una lista 
#===================================================
nums=[10,20,30,40,50]
for i in nums:
    print(i)
#===================================================
#Bucle sobre un string
#===================================================
for char in 'Hello':
    print(char)
#====================================================
#Items es igaula a elementos
#Bucle sobre un diccionario
#=====================================================
numNames={1:'One' ,2 :'Two', 3:'Three'}
for pair in numNames.items():
    print (pair)
#========================================
#Bucle sobre diccionario
#Key=llave
#value=valor
#========================================
for k,v in numNames,items():
    print ("key=",k,",value=",v)

