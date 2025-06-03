# tota=0
# pro=0
# a=0
# s=0
# d=0
# f=0
# def sushi():
#     global tota,pro,a,s,d,f
#     while True:
#         op=int(input('''En un delivery de Sushi vende 4 tipos de Sushi:
#                 1.-pikachu $4500
#                 2.-otaku roll $5000
#                 3.-pulpo venenoso roll 5200
#                 4.-anguila electrica roll 4800
#                 0.-volver
#                 '''))
#         if op==1:
#             tota+=4500
#             pro+=1
#             a+=1
#         elif op==2:
#             tota+=5000
#             pro+=1
#             s+=1
#         elif op==3:
#             tota+=5200
#             pro+=1
#             d+=1
#         elif op==4:
#             tota+=4800
#             pro+=1
#             f+=1
#         elif op==0:
#             print("volviedo a la pagina principal")
#             break
# def bolet():
#     while True:
#         descuento=input("tiene descuento (si/no) ")
#         if descuento=="si":
#             gregar=input("ingrese descuento: ")
#             if gregar=="soyotaku":
#                 desfinal=tota*10/100
#                 break
#             else:
#                 print("volver a intentarlo")
#         elif descuento=="no":
#             break
    
#     print(f"totalde productos {pro}")
#     if a>=1:
#         print(f"pikachu {a}")
#     elif s>=1:
#         print(f"otaku roll {s}")
#     elif d>=1:
#         print(f"pulpo venenoso roll {d}")
#     elif f>=1:
#         print(f"anguila electrica roll {f}")
#     print(f"total a pagar {tota}")
#     if desfinal>=1:
#         print(f"pagar con de cuento {tota-desfinal}")
# while True:
    # try:
    #     op=int(input('''En un delivery de Sushi vende 4 tipos de Sushi:
    #             1.-comprar sushi
    #             2.-boleta
    #             0.-salir
    #             '''))
    #     match op:
    #         case 1:
    #             sushi()
    #         case 2:
    #             bolet()
    #         case 0:
    #             print("saliendo")
    #             break
    #         case _:
    #             print("solo escoja un numero valido")
    # except Exception:
    #     print("solo numeros")

# user1=None
# user2=None
# user3=None
# contra1=None
# contra2=None
# contra3=None

# def inicio():
#   while True:
#     while True:
#       try:
#         user=input("ingrese su usuario: ")
#       except Exception:
#         print("ingrese solo letras")
#       try:
#         contra=int(input("ingrese su contraseña: "))
#         break
#       except Exception:
#         print("ingrese solo numeros")
#     if (user==user1 and contra==contra1) or (user==user2 and contra==contra2) or (user==user3 and contra==contra3):
#       op=int(input('''seleccione una opcion
#              1) Realizar llamada
#              2) Enviar correo electrónico
#              3) Cerrar sesión
#              '''))
#       match op:
#         case 1:
#           tele()
#         case 2:
#           men()
#         case 3:
#           break
#         case _:
#           print("ingrese un numero valido")
# def regis():
#   global user1,user2,user3,contra1,contra2,contra2,user,contra
#   user=input("creun usuario: ")
#   if user1==None and user1==None:
#     user1=user
#     contra=int(input("ingrese su contraseña: "))
#     contra1=contra
#   elif user2==None and user3==None:
#     user2=user
#     contra=int(input("ingrese su contraseña: "))
#     contra2=contra
#   elif user3==None and user3==None:
#     user3=user
#     contra=int(input("ingrese su contraseña: "))
#     contra3=contra
# def tele():
#   while True:
#     while True:
#       try:
#         llama=input("ingrese el numero: ")
#         break
#       except Exception:
#         print("solo numeros")
#     if llama.startswith("9") and len(llama)==9:
#       print("llamando")
#       break
#     else:
#       print("numero invalido vuelva a intertarlo")
# def men():
#   mensaje=input("ingrese el gmail: ")
#   if "@" in mensaje:
#     print(f"sele esta enviando un correo a {mensaje}")
# while True:
  # while True:
  #   try:
  #     op=int(input('''selecciona una opcion
  #                 1.- iniciar sesion
  #                 2.- registrar usuario 
  #                 3.- salir
  #                 '''))
  #     break  
  #   except Exception:
  #     print("selec ciona numeros")
  # match op:
  #   case 1:
  #     inicio()
  #   case 2:
  #     regis()
  #   case 3:
  #     break
  #   case _:
  #     print("ingrese un numero valido")

