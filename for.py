#  explicasion de uso de for

# for i in range(3):
#     print("hola")
# num=int(input("ingrese un numero "))

# for i in range(num):
#     print("repeticione", i+1)

# nombre=input("ingrese su nombre ")
# edad=input("ingrese su edad ")
# print(f"su nombre es {nombre} \nsu edad {edad}")

#  escribit =print
# leer = input
# si,=if
# para = for  
# tabla de multplicar
# num=in(input("ingrese un numero "))
# for i in range(1.11):
#     print()

# for i in range(1,11):
#     print("tabla del", i)
#     for j in range(1.11):
#         print(f"{i} x {j} = {i*j}")

# pedir al usuario la cantidad de notas y promediarla
# can=int(input("ingrese la cantidad de notas "))
# total=0
# notasazul=0
# for i in range(can):
#     print("ingrese la nota", i+1)
#     nota=float(input())
#     total=total+nota
#     prom=total/can
#     if nota>=4:
#         notasazul+=1
# print(f"su promedio es {round(prom,1)}")
# print(f"la cantidad de notas sobre 4 fue {notasazul}")

# if prom>=4:
#     print("aprobo")
# else:
#     print("reprobo")

# for i in range(3):
#     clave=2123
#     pas=int(input("ingrese la clave"))
#     if pas==clave:
#         print("vien venido")
#         break
#     else:
#         print("erro de clave")

# num=int(input("ingrese numero \n"))
# kaiser=0
# nose=0
# for i in range(num):
#     voto=int(input("ingrese su voto: \n1.-kaiser \n2.-nose \n"))
#     if voto==1:
#         kaiser +=1
#     elif voto==2:
#         nose +=1
#     else:
#         print("erro selecsione un voto ")
# print(f"los votos de keiser son {kaiser}")
# print(f"los votos de nose son {nose}")
# if kaiser>nose:
#     print("gano kaiser")
# else:
#     print("gano nose")

# palabra=str(input("ingrese un palabra "))
# caracter=0
# for i in palabra:
#     print(i)
#     caracter+=1
#     print(f"cantidad de caracter {caracter}")
# nume=0
# while nume<=5:
#     nume +=1
#     print(nume)

# import time 
# num=10
# while num>=0:
#     print(num)
#     time.sleep(1)
#     num -=1
# resp="no"
# while resp!="si":
#     repr=input("deseas salir del sistema")

# clave=2123
# inte=3
# ingre=int(input("ingrese su clave "))
# while clave!=ingre :
#     print("error de clave ")
#     if inte==0:
#         break
#     inte -=1
#     print(f"leque dan {inte} intentos")
# if clave==ingre:
#     print("clave aceptado ")
# else:
#     print("sistema bloqueado")

# op=int(input("1.-pan 250 \n2.-donas 500 \n3.-confor 550 \n0.- salir \n"))
# total=0
# while op != 0:
#     op=int(input("1.-pan 250 \n2.-donas 500 \n3.-confor 550 \n0.- salir \n"))
#     if op==1:
#         print("pan")
#         total +=250
#     elif op==2:
#         print("donas")
#         total +=500
#     elif op==3:
#         print("confor")
#         total +=550
#     else:
#         print("escojer un numero ")
# print(f"el total es {total}")
# print(f"total con iva {round(total*1.19)}")

# num=5
# while num!=0:
#     if num% 2==0:
#         print(f"el numero {num} es par")
#     else:
#         print(f"el numero {num} es impar")

# print("/"*100)
# import random
# randy=random.randint(1.10)
# print(randy)
'''
% = espara para ser ver si es un numero de otro 
'''
# edad=-1
# while edad <0 or edad>100:
#     edad=int(input("ingrese edad "))
#     if (edad <0 or edad> 100):
#         print(f"edad fuera de rango de 0.100")
# print("as ingreaso exsitosa mente")

# num=int(input("ingrese un numero"))
# e=0
# c=0
# while num!=0:
#     num-=1
#     if num% 2==0:
#         print(f"el numero {num} es par")
#         e+=1
#     else:
#         print(f"el numero {num} es impar")
#         c+=1
# print(f"numero par {e}")
# print(f"numero par {c}")

# import random

# numAzar=random.randint(1,30)

# if numAzar>=20:
#     print("puedes pasar")
# else:
#     print("le falta numero")

# import random
# numAsar=random.randint(1,50)
# num=int(input("ingrese un numero"))
# while num!= numAsar: 
#     if num > numAsar:
#         print("el numero es meno ")
#         num=int(input("in tentalo de nuevo"))
#     else:
#         print("el numero es mallor ")
#         num=int(input("in tentalo de nuevo"))
# print("ganaste ")

# import random
# meta=30
# turno=random.randint(1,2)
# j1=0
# j2=0

# import time
# while j1<meta and j2<meta :
#     turno +=1
#     if turno % 2==0:
#         print("jugador 1")
#         time.sleep(1)
#         dado=random.randint(1,6)
#         j1 += dado
#         print(f"el jugador saco {dado} \navanza hasta la casilla {j1}")
#     else:
#         print("jugador 2")
#         time.sleep(1)
#         dado=random.randint(1,6)
#         j2 += dado
#         print(f"el jugador saco {dado} \navanza hasta la casilla {j2}")

# if j1>=meta :
#     print("gana j1")
# elif j2>=meta:
#     print("gana j2")

# arancel=200000
# descuento=0
# comuna=int(input("1-la florida \n2-la pintana \n3-puente alto \nsan joaquin \nselecciona una comuna \n"))
# if comuna==1:
#     descuento +=20
# elif comuna==2:
#     descuento +=30
# elif comuna==3:
#     descuento +=25
# elif comuna==4:
#     descuento +=15
# else:
#     print(" escojer un valor valor valido")

# grupo=int(input("cuantas perosna vive "))
# if grupo==1:
#     descuento +=2
# elif grupo>1 and grupo<5:
#      descuento +=3
# elif grupo>=5:
#     descuento+=4
# else:
#     print(" seleccion incorrecto")

# print(f"el descuento es {descuento}")
# desc=arancel*descuento/100
# total=arancel-desc
# print(f"el total a pagar es ${total}")
         