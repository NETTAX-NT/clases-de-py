
'''
listas diccionario set tuplas son las tipos de colecsion
crud= create ,read ,update ,and ,delate

lista=[1,2,3,4,5]
print(2)
########################
lista=[1,2,3,4,5]
lista.append(6)
for i in lista:
  print(i)
###########################
lista=[1,2,3,4,5]
lista.insert(3,"nata")
for i in lista:
  print(i)
###########################
lista=[1,2,3,"nata",4,5]
lista.remove("nata")
for i in lista:
  print(i)
###########################
lista=[5,4,3,2,1]
lista.reverse() # desordena
lista.sort() # ordena
for i in lista:
  print(i)
'''
# listas=[]
# def agre():
#     global listas
#     inser=input("ingrese un producto: ")
#     listas.append(inser)
# def elim():
#     global listas
#     listas.sort()
#     print(listas)
#     while True:
#         try:
#             inser=input("que poducto quieres eliminar: ")
#             listas.remove(inser)
#             break
#         except Exception:
#             print("producto no existente")
#             break
# def mos():
#     global listas
#     listas.sort()
#     print(listas)    
# while True:
    # op=int(input('''seleccione una opcion
    #              1.- agregar un producto
    #              2.- eliminar un producto
    #              3.- mostrar todos los productos
    #              4.- salir 
    #              '''))
    
    # match op:
    #     case 1:
    #         agre()
    #     case 2:
    #         elim()
    #     case 3:
    #         mos()
    #     case 4:
    #         break
    #     case _:
    #         print("numero in valido")


