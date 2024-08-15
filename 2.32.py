def simular_ventas(*ventas):
    total_ingresos = 0
    
    for venta in ventas:
        _, cantidad, precio_por_unidad = venta
        total_ingresos += cantidad * precio_por_unidad
    
    return total_ingresos

ingresos_totales = simular_ventas(
    ("Producto A", 10, 15.0),
    ("Producto B", 5, 25.0),
    ("Producto C", 3, 50.0)
)

print(ingresos_totales)
