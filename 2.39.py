def simular_mercado(precios_diarios, operaciones):
    saldo = 0
    acciones = 0
    precio_compra = 0

    for operacion, dia in operaciones:
        precio = precios_diarios[dia]
        if operacion == "compra":
            if acciones > 0:
                saldo += acciones * (precio - precio_compra)
            precio_compra = precio
            acciones += 1
        elif operacion == "venta":
            if acciones > 0:
                saldo += (precio - precio_compra)
                acciones -= 1
    
    return saldo

precios_diarios = [100, 105, 102, 110, 108]
operaciones = [("compra", 0), ("venta", 3), ("compra", 2), ("venta", 4)]

beneficio_o_perdida = simular_mercado(precios_diarios, operaciones)

print(beneficio_o_perdida)
