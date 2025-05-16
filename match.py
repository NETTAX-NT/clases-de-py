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

alumnos=int(input("ingrese la cantidad de alumnos: "))
mientras=0
for i in range(alumnos):
    i+=1
    mientras=0
    nota=int(input("ingrese la cantidad de notas: ")) 
    for e in range(nota):
        e+=1
        notas=int(input(f"ingrese la nota {e} alumno {i}: "))
        mientras+=notas
        promedio=mientras/nota
    if promedio>=4.0:
        print(f"aprobaste tu nota es {promedio}")
    else:
        print(f"reprobaste {promedio}")

