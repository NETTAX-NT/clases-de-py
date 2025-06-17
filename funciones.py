# def suma_ret():
#     n1=int(input("ingrese un numero"))
#     n2=int(input("ingrese un numero"))
#     return n1+n2
# def suma():
#     n1=int(input("ingrese un numero"))
#     n2=int(input("ingrese un numero"))
#     print(n1+n2)
# def suma_arg(n1,n2):
#     print(n1+n2)
# def suma_arg_ret(n1,n2):
#     return n1+n2
# n1=int(input("ingrese un numero"))
# n2=int(input("ingrese un numero"))
# suma_arg(n1,n2)
# print(suma_arg_ret(n1,n2)*2)
# #suma()
# num=suma_ret*5
# print(num)

# def iva(nu):
#     nu=int(input("ingrese un numero para pasarlo a iva: "))
#     numero=(nu*19)/100
#     print(f"el valor del iva es {numero}")
#     print(f"mas en el precio {nu+numero}")

# def des():
#     t=int(input("ingrese el precio: "))
#     d=int(input("ingrese el descuento: "))
#     descuento=(t*d)/100
#     print(f"su de cuento es {descuento}")
#     print(f"el precio con su descuento {t-descuento}")
# iva()
# des()

'''
create=
read=
update=
delete=
'''
# productos=[
#     {"nombre":"lapiz","precio":400},
#     {"nombre":"goma","precio":300},
#     {"nombre":"estuche","precio":1600}
# ]
# for item in productos:
#     print(f"el articulo {item["nombre"]} tiene un precio de {item["precio"]}")
pro=[
    {"nombre":"papas", "precio":1000}
]
def mostrat()

while True:
    op=int(input('''seleccione una opcion
                 1.-agregar un articulo
                 2.-borra articulo
                 3.-actualisar articulo
                 4.-mostrar articulo
                 5.-salir
                 '''))
    match op:
        case 1:
            nu=input("ingrese in nuevo producto: ")
            n=int(input("ingrese precio: "))
            pro.append({"nombre":nu,"precio":n})
        case 2:
            for i in range(len(pro)):
                print(f"{i+1}.-{pro[i]["nombre"]}----{pro[i]["precio"]}")
            quitar=int(input("selccione una opcion: "))
            pro.pop(quitar-1)
        case 3:
            for i in range(len(pro)):
                print(f"{i+1}.-{pro[i]["nombre"]}----{pro[i]["precio"]}")
            elmis=int(input("ingrese el producto que quires cambiar el precio: "))
            nuevo1=int(input("ingrese el nuevo nombre: "))
            nuevo=int(input("ingrese el nuevo precio: "))
            pro[elmis-1]["nombre"]=nuevo1
            pro[elmis-1]["precio"]=nuevo
        case 4:
            for i in range(len(pro)):
                print(f"{i+1}.-{pro[i]["nombre"]}----{pro[i]["precio"]}")
        case 5:
            break