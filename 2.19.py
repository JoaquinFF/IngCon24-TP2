def calcular_goles_totales(resultados):
    goles_anotados = 0
    goles_recibidos = 0
    
    for goles in resultados.values():
        goles_anotados += goles[0]
        goles_recibidos += goles[1]
    
    return goles_anotados, goles_recibidos

resultados = {
    "Equipo A": (3, 2),
    "Equipo B": (1, 1),
    "Equipo C": (4, 0)
}

total_goles_anotados, total_goles_recibidos = calcular_goles_totales(resultados)

print(f"Total de goles anotados: {total_goles_anotados}")
print(f"Total de goles recibidos: {total_goles_recibidos}")
