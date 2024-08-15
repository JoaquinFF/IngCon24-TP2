def producto_mas_caro(productos):
    mas_caro = None

    for producto in productos:
        if mas_caro is None or producto[1] > mas_caro[1]:
            mas_caro = producto
    return mas_caro

productos = [("laptop", 1200, 5), ("mouse", 25, 50), ("teclado", 100, 30)]

mas_caro = producto_mas_caro(productos)

print(mas_caro)
