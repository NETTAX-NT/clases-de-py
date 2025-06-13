# # es con juntos de pares de datos

# dic={
#     "nombre":"mel broks",
#     "numeroa": 943231,
#     "casado": True
# }
# # print(dic)

# for key,value in dic.items():
#     print(key,value)

# dic["ciudad"]="talca"
# for key,value in dic.items():
#     print(key,value)

# dic["casado"]=False
# for key,value in dic.items():
#     print(key,value)

# frutas={
#     "sandia":3000,
#     "manzanas":1500,
#     "naranja":1000
# }
# print(frutas)
# fruta=input("ingrese una fruta: ")
# pre=int(input("ingrese precio: "))
# frutas[fruta]=pre
# print(frutas)

frutas={
    "naranja":1000,
    "manzana":1500
}
while True:
    op=int(input('''seleccione una opcion
                 1.- ingresar fruta y precio
                 2.- actualizar precio
                 3.-borrar fruta y precio
                 4.-mostrat todas las frutas y precio
                 5.-comprar
                 6.-salir
                 '''))
    match op:
        case 1:
            frut=input("ingrese una fruta")
            pre=int(input("ingrese su precio"))
            frutas[frut]=pre
        case 2:
            print("ACTUALIZAR PRECIO")
            for lol,dad in frutas.items():
                print(lol,dad)
            actu=input("ingrese el nombre de la fruta")
            nue=int(input("ingresar precio nuevo"))
            frutas[actu]=nue
        case 3:
            for lol,dad in frutas.items():
                print(lol,".-",dad)
            dell=input("seleccione la fruta a borra")
            del frutas[dell]
        case 4:
            for lol,dad in frutas.items():
                print(lol,".-",dad)
        case 5:
            print()
        case 6:
            break