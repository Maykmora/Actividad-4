print("Bienvenido al programa")

salary=int(input("Ingrese su salario anual:"))
dependents=int(input("Ingrese el numero de dependientes:"))

if salary<40000 and dependents>2:
    print("Usted no paga impuestos")
elif 0<salary<=30000:
    print(f"El impuesto que debe pagar es {salary*0.05+dependents*1000}")
elif 30001<salary<=60000:
    print(f"El impuesto que debe pagar es {salary*0.1+dependents*1000}")
elif 60001<salary<=100000:
    print(f"El impuesto que debe pagar es {salary*0.15+dependents*1000}")
elif salary>100000:
    print(f"El impuesto que debe pagar es {salary*0.2+dependents*1000}")
else:
    print("Error, intente de nuevo")