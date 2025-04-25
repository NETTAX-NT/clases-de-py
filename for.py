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

print("/"*100)
import random
randy=random.