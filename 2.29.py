def calcular_promedios(notas_estudiantes):
    promedios = {}
    
    for nombre, calificaciones in notas_estudiantes:
        promedio = round(sum(calificaciones) / len(calificaciones), 1)
        promedios[nombre] = promedio
    
    return promedios

notas_estudiantes = [
    ("Ana", [85, 90, 78]),
    ("Luis", [88, 92, 80]),
    ("María", [75, 85, 70])
]

promedios_estudiantes = calcular_promedios(notas_estudiantes)

print(promedios_estudiantes)
