print("Bienvenido al programa")
day=int(input("Ingrese el numero de dia que desea:"))
month=int(input("Ingrese el numero de mes que desea:"))
year=int(input("Ingrese el año que sea hasta de 4 digitos:"))

dias=["Sabado","Domingo", "Lunes", "Martes", "Miercoles", "Jueves","Viernes"]

if 0<day<=31 and 0<month<=12 and 0<year<=9999:
    print("Fecha valida")
    j=year//100
    k=year%100

    h=int((day+(2.6*(month+1))+k+(k/4)+(j/4)-2*j)%7)
    print("El dia que seleccionaste fue", dias[h])

else:
    print("Fecha invalida intentelo de nuevo.")

