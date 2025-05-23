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
    try:
        op=int(input('''En un delivery de Sushi vende 4 tipos de Sushi:
                1.-comprar sushi
                2.-boleta
                0.-salir
                '''))
        match op:
            case 1:
                sushi()
            case 2:
                bolet()
            case 0:
                print("saliendo")
                break
            case _:
                print("solo escoja un numero valido")
    except Exception:
        print("solo numeros")

deuda=100000
def tar():
  global deuda
  while True:
    while True:
      try:
        monto=int(input("Cuánto desea pagar?"))
      except Exception:
        print("Ingrese sólo números enteros")
      else:
        break
    if monto>=0 and monto<=deuda:
      deuda=deuda-monto
    else:
      print("Monto inválido")
    print(f"Deuda actualizada, su deuda actual es de {deuda}")
    choice=input("Para salir pulse x")
    if choice=="x":
      break