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

def prom():
    n1=int(input("ingrese su nota "))
    n2=int(input("ingrese su nota "))
    n3=int(input("ingrese su nota "))
    suma=(n1+n2+n3)/3
    print(f"su promedio es {suma}")
def calculadora