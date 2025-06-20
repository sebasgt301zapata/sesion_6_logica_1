num_1= float(input("primer numero a consultar"))
num_2= float(input("segundo numero a consultar"))
operador=input("que tipo de operacion quieres hacer? +,-,*,/): ")

match operador:
    case"+":
        print("resultado", num_1 + num_2)
    case"-":
        print("resultado",num_1 - num_2)
    case"*":
        print("resultado",num_1 * num_2)
    case"/":
        if num_2 != 0:
            print("resultado",num_1 / num_2)
        else:
            print("resultado no valido")
    case _:
        print("resultado no valido")

    