# explicasion y uso de match

def suma():
    n1=int(input("ingrese un numero: "))
    n2=int(input("ingrese otro numero: "))
    print("el resultado de la suma es", n1+n2)
def resta():
    n1=int(input("ingrese un numero: "))
    n2=int(input("ingrese otro numero: "))
    print("el resultado de la resta es", n1-n2)
def mul():
    n1=int(input("ingrese un numero: "))
    n2=int(input("ingrese otro numero: "))
    print("el resultado de la multiplicar es", n1*n2)
def division():
    n1=int(input("ingrese un numero: "))
    n2=int(input("ingrese otro numero: "))
    print("el resultado de la divicion es", n1/n2)
def calcu():
    while True:
        op=int(input('''seleccione su opcio
                    1.-suma
                    2.-resta
                    3.-multiplicar
                    4.-divicion
                    0.-salir
                    '''))

        match op:
            case 1:
                print("suma")
                suma()
            case 2:
                print("resta")
                resta()
            case 3:
                print("multiplicar")
                mul()
            case 4:
                print("division")
                division()
            case 0:
                print("salir")
                break
            case _:
                print("opcion invalida")
calcu()