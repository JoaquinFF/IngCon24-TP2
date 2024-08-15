def promedio_calificaciones(registro, matricula):
    if matricula in registro:
        estudiante = registro[matricula]
        calificaciones = estudiante["calificaciones"]
        
        # Calcular el promedio de las calificaciones
        promedio = sum(calificaciones.values()) / len(calificaciones)
        return promedio
    else:
        return "Matrícula no encontrada"

estudiantes = {
    101: {"nombre": "Ana", "edad": 16, "calificaciones": {"matemáticas": 85, "ciencias": 90}},
    102: {"nombre": "Luis", "edad": 17, "calificaciones": {"matemáticas": 78, "ciencias": 88}}
}

matricula = 101
promedio = promedio_calificaciones(estudiantes, matricula)
print(f"El promedio de calificaciones del estudiante con matrícula {matricula} es: {promedio}")
