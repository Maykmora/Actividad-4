print("Bienvenido al programa")
students=[]

for i in range(5):
    nombre=input(f"Nombre del estudiante {i+1}:")
    notas=[]
    for j in range(3):
        nota=float(input(f"Nota {j+1} de {nombre}:"))
        notas.append(nota)
    students.append({"nombre": nombre, "notas": notas})

promedios=[]
for estudiante in students:
    promedio = sum(estudiante["notas"]) / 3
    promedios.append(promedio)

todos_menor_70 = True
for promedio in promedios:
    if promedio >= 70:
        todos_menor_70 = False
        break

if todos_menor_70:
    print("Todos los estudiantes tienen promedio menor a 70, se aplicara la curva")
    for estudiante in students:
        nuevas_notas = []
        for nota in estudiante["notas"]:
            nueva = min(nota + 5, 100)
            nuevas_notas.append(nueva)
        estudiante["notas"] = nuevas_notas

print("Tabla final de calificaciones:")
print("Nombre        Promedio")
for estudiante in students:
    promedio = sum(estudiante["notas"]) / 3
    print(f"{estudiante["nombre"]}, {promedio:.2f}")