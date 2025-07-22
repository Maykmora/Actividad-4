print("Bienvenido al programa")
age=int(input("Ingrese su edad:"))
day=input("Ingrese el dia de la semana que desea:")
student=input("¡Es estudiante?:")

if age<13:
    print("No puedes ver peliculas para mayores de 15 ")
    if day=="miercoles":
        print("El día miercoles hay 2x1")
        if student=="si":
            print("Por ser estudiante paga Q.35")
        else:
            print("Por no ser estudiante paga Q.50")
    else:
        if student=="si":
            print("Por ser estudiante paga Q.35")
        else:
            print("Por no ser estudiante paga Q.50")


else:
    if day=="miercoles":
        print("El día miercoles hay 2x1")
        if student=="si":
            print("Por ser estudiante paga Q.35")
        else:
            print("Por no ser estudiante paga Q.50")
    else:
        if student=="si":
            print("Por ser estudiante paga Q.35")
        else:
            print("Por no ser estudiante paga Q.50")