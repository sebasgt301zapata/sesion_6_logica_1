num_1= float(input("primer numero a consultar"))
num_2= float(input("segundo numero a consultar"))
operador=input("que tipo de operacion quieres hacer? +,-,*,/): ")

if operador == "+":
    print("resultado",num_1 + num_2)
elif operador =="-":
    print("resultado",num_1-num_2)
elif operador == "*":
    print("resultado",num_1*num_2)
elif operador == "/":
    if num_2 !=0:
        print("resultado",num_1/num_2)
    else:
        print("error dividiendo por cero")
else:
    print("operador no valido")