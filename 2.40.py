def ranking_estudiantes(estudiantes):
    promedios = {}
    
    for estudiante_id, materias in estudiantes.items():
        total_calificaciones = 0
        total_materias = 0
        
        for calificaciones in materias.values():
            total_calificaciones += sum(calificaciones)
            total_materias += len(calificaciones)
        
        promedio_general = total_calificaciones / total_materias
        promedios[estudiante_id] = promedio_general
    
    ranking = sorted(promedios.items(), key=lambda item: item[1], reverse=True)
    
    return ranking

estudiantes = {
    101: {"matemáticas": [85, 90, 78], "ciencias": [88, 85, 80]},
    102: {"matemáticas": [92, 88, 84], "ciencias": [75, 80, 85]},
    103: {"matemáticas": [78, 85, 88], "ciencias": [90, 95, 92]}
}

ranking = ranking_estudiantes(estudiantes)

print(ranking)
