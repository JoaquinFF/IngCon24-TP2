def estadisticas_ventas(ventas_mensuales):
    total_ventas = sum(ventas_mensuales)
    
    promedio_mensual = total_ventas / len(ventas_mensuales)
    
    mes_max_ventas = ventas_mensuales.index(max(ventas_mensuales)) + 1  # +1 para ajustar al formato 1-based
    
    estadisticas = {
        'total_ventas': total_ventas,
        'promedio_mensual': promedio_mensual,
        'mes_con_mayores_ventas': mes_max_ventas
    }
    
    return estadisticas

ventas_mensuales = [2000, 2500, 3000, 2800, 3500, 4000, 4200, 3800, 3600, 3900, 4100, 4500]

estadisticas = estadisticas_ventas(ventas_mensuales)

print(estadisticas)
