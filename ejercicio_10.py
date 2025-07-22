print("Bienvenido al programa")
print("Primer Fecha")
d1=int(input("Ingrese el numero de día:"))
m1=int(input("Ingrese el numero de mes:"))
a1=int(input("Ingrese el numero de año:"))
print("Segunda Fecha")
d2=int(input("Ingrese otro numero de día:"))
m2=int(input("Ingrese otro numero de mes:"))
a2=int(input("Ingrese otro numero de año:"))

date1=(d1, m1, a1)
date2=(d2, m2, a2)
if date1>date2:
    print("La primer fecha es mayor")
    if m1 == m2 and a1 == a2:
        print("Las fechas están en el mismo mes y año.")
        print(f"Han pasado:{d1 - d2} días,{m1 - m2} meses ,{a1 - a3} años")
    else:
        print("Las fechas NO están en el mismo mes y año.")
        print(f"Han pasado:{d1 - d2} días,{m1 - m2} meses ,{a1 - a3} años")

elif date1<date2:
    print("La segunda fecha es mayor.")
    if m1 == m2 and a1 == a2:
        print("Las fechas están en el mismo mes y año.")
        print(f"Han pasado:{d1 - d2} días,{m1 - m2} meses ,{a1 - a3} años")
    else:
        print("Las fechas NO están en el mismo mes y año.")
        print(f"Han pasado:{abs(d1 - d2)} días,{(m1 - m2)} meses ,{(a1 - a2)} años")

else:
    print("Ambas fechas son iguales.")
    print("No ha pasado ningun día")

