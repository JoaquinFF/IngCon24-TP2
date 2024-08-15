def actualizar_inventario(inventario, tienda, **kwargs):
    if tienda not in inventario:
        return "La tienda no existe en el inventario."
    
    inventario_tienda = inventario[tienda]
    
    for producto, cantidad in kwargs.items():
        if producto in inventario_tienda:
            inventario_tienda[producto] += cantidad
        else:
            return f"El producto {producto} no existe en la tienda {tienda}."
    
    return inventario

inventario = {
    "Tienda A": {"producto_1": 50, "producto_2": 30},
    "Tienda B": {"producto_1": 20, "producto_2": 40}
}

estado_actual = actualizar_inventario(inventario, tienda="Tienda A", producto_1=10, producto_2=-5)

print(estado_actual)
