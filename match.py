# explicasion y uso de match

# def suma():
#     n1=int(input("ingrese un numero: "))
#     n2=int(input("ingrese otro numero: "))
#     print("el resultado de la suma es", n1+n2)
# def resta():
#     n1=int(input("ingrese un numero: "))
#     n2=int(input("ingrese otro numero: "))
#     print("el resultado de la resta es", n1-n2)
# def mul():
#     n1=int(input("ingrese un numero: "))
#     n2=int(input("ingrese otro numero: "))
#     print("el resultado de la multiplicar es", n1*n2)
# def division():
#     try:
#         n1=int(input("ingrese un numero: "))
#         n2=int(input("ingrese otro numero: "))
#         print("el resultado de la divicion es", n1/n2)
#     except ZeroDivisionError as nombre_de_excepcion:
#         print(f"se produjo una excepcion {nombre_de_excepcion}: ")
# def calcu():
#     while True:
#         op=int(input('''seleccione su opcio
#                     1.-suma
#                     2.-resta
#                     3.-multiplicar
#                     4.-divicion
#                     0.-salir
#                     '''))

#         match op:
#             case 1:
#                 print("suma")
#                 suma()
#             case 2:
#                 print("resta")
#                 resta()
#             case 3:
#                 print("multiplicar")
#                 mul()
#             case 4:
#                 print("division")
#                 division()
#             case 0:
#                 print("salir")
#                 break
#             case _:
#                 print("opcion invalida")
# calcu()

# # Código que podría generar una excepción
# # Dentro de este bloque de código, debes colocar
# # lo que quieres validar por medio de una
# # excepción, ejemplo, operaciones matemáticas,
# # Set de variables, etc....
 
# resultado = 10/ 0
# Try:
# except ZeroDivisionError as nombre_de_excepcion:
# # Código para manejar la excepción
# print(f"Se produjo una excepción: {nombre_de_excepcion}")
# else:
# # Código a ejecutar si no se produjo ninguna excepción
# print("No se produjo ninguna excepción")
# finally:
# # Código a ejecutar siempre, independientemente de si se produjo
# una excepción o no
# print("Este bloque se ejecuta siempre")

# def prom():
#     n1=int(input("ingrese su nota "))
#     n2=int(input("ingrese su nota "))
#     n3=int(input("ingrese su nota "))
#     suma=(n1+n2+n3)/3
#     print(f"su promedio es {suma}")
# def calculadora

# total=0
# to=0
# cantidad=0

# def user():
#     global nom
#     nom=input("ingrese su nombre: ")
# def pro():
#     global cantidad,total,to

    
#     produc=int(input('''selecsione un producto
#                      1.-confor 1500
#                      2.-sepillo de dientes 1000
#                      3.-pasta de diente 2000
#                      '''))
#     match produc:
#         case 1:
#             total+=1500
#             to+=(1500*1.19)
#             cantidad+=1     
#         case 2:
#             total+=1000
#             to+=(1500*1.19)
#             cantidad+=1  
#         case 3:
#             total+=2000
#             to+=(1500*1.19)
#             cantidad+=1  
# def bol():
#     print(f"usuario {nom}")
#     print("productos totales", cantidad)
#     print(f"presio sin iva {total} con iva {round(to)}")
# def cat()        
#     while True:
#         op=int(input('''escoja una opcion
#                     1.-ingrese su nombre
#                     2.-selecsionar productos
#                     3.-imprimir boletas
#                     4.-salir
#                     '''))
#         match op:
#             case 1:
#                 user()
#             case 2:
#                 pro()
#             case 3:
#                 bol()
#             case 4:
#                 print("saliendo")
#                 break
# # cat()

# alumnos=int(input("ingrese la cantidad de alumnos: "))
# mientras=0
# for i in range(alumnos):
#     i+=1
#     mientras=0
#     suma=0
#     nota=int(input("ingrese la cantidad de notas: ")) 
#     for e in range(nota):
#         e+=1
#         notas=int(input(f"ingrese la nota {e} alumno {i}: "))
#         mientras+=notas
#         promedio=mientras/nota

#     if promedio>=4.0:
#         print(f"aprobaste tu nota es {promedio}")
#     else:
#         print(f"reprobaste {promedio}")

import random
import time
# while True:
#     try:
#         perros=int(input("cuantos perros envias:"))
#     except Exception:
#         print("solo numeros ")
#     else:
#         break
# cuotas=random.randint(1,5)
# n=0
# e=0
# print(f"la cuota minima es {cuotas}")
# time.sleep(1)
# for i in range(perros):
#     time.sleep(1)
#     conejos=random.randint(1,7)
#     i+=1
#     print(f"el perro {i} trajos {conejos} conejos")
#     if conejos>=cuotas:
#         print(f"el perro {i} resivio premio ")
#         n+=1
#     elif conejos<cuotas:
#         print(f"el perro {i} no resivio premio ")
#         e+=1
# print(f"perros que cumplieros {n}")
# print(f"perros que no cumplieron {e}")

# rojos=int(input("cuantos rojos tienes"))

# for i in range(rojos):
#     taller=random.randint(1,4)
#     decimas=0.3*taller
#     if decimas>=1:
#         vives=True
#     else:
#         f=False
#     nota=int(input("ingrese sus notas"))
#     fin=nota+decimas
#     print(f"la nota final es {fin}")

#     if fin>=3.5 and vives:
#         fin=4.0
#     if fin>=4:
#         print("el estudiante pasa")
#     else:
#         print("el estudainte repite") 

# total=0
# a=0
# e=0
# r=0
# t=0
# def pago():
#     global total,a,e,r,t
#     try:
#         lavado=int(input('''el lavado tiene 3 nivels diferentes
#                         1.-full $15.000
#                         2.-standar $10.000
#                         3.-basico $7.000
#                         '''))
#         if lavado==1:
#             total+=15000
#             a+=1
#             t+=1
#         elif lavado==2:
#             total+=10000
#             a+=1
#             r+=1
#         elif lavado==3:
#             total+=7000
#             a+=1
#             e+=1
#     except Exception:
#         print("solo numeros")
# def venta():

#     print(f"el total de venta es {total}")
#     print(f"cuantos autos an ingresado {a}")
#     if t>=1:
#         print("el monto mas alto es $15.000")
#     elif r>=1:
#         print("el monto mas alto es $10.000")
#     elif e>=1:
#         print("el monto mas alto es $7.000")
# def ventas(): 
#     while True:
#         try:
#             op=int(input('''lavados de autos
#                         1.-cursa pagos del autos
#                         2.-ver ventas diarias 
#                         3.- salir 
#                         '''))
            
#             match op:
#                 case 1:
#                     pago()
#                 case 2:
#                     venta()
#                 case 3:
#                     break
#                 case _:
#                     print("ingrese un numero")
#         except Exception:
#             print("solo numeros")
# ventas()

# para cerrar un programa de sub menu ahi que usar importar sys y luegos escribir  sys.exit()


