def calcular_precios_paquetes(paquetes):
    precios_por_destino = {}
    
    for destino, precio_por_dia, duracion in paquetes:
        precio_total = precio_por_dia * duracion
        precios_por_destino[destino] = precio_total
    
    return precios_por_destino

paquetes = [
    ("Paris", 200, 5),
    ("Roma", 150, 4),
    ("Londres", 180, 3)
]

precios = calcular_precios_paquetes(paquetes)

print(precios)
