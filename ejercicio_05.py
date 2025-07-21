print("Bienvenido al programa")
day=int(input("Ingrese el numero de dia que desea:"))
month=int(input("Ingrese el numero de mes que desea:"))
year=int(input("Ingrese el año que sea hasta de 4 digitos"))

if 0<day<=31 and 0<month<=12 and 0<year>9999:
    print("Fecha valida")
    k=year%10
    print(k)