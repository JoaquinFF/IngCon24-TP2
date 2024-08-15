def hacer_reserva(reservas, fecha, nombre_huesped, habitacion, precio):
    if fecha in reservas:
        for _, habitacion_reservada, _ in reservas[fecha]:
            if habitacion_reservada == habitacion:
                return "La habitación ya está reservada en esta fecha."
    
    if fecha not in reservas:
        reservas[fecha] = []
    reservas[fecha].append((nombre_huesped, habitacion, precio))
    
    return "Reserva realizada con éxito."

reservas = {
    "2024-08-15": [("Juan", 101, 150), ("Ana", 102, 180)],
    "2024-08-16": [("Luis", 101, 150)]
}

resultado = hacer_reserva(reservas, "2024-08-15", "Carlos", 101, 160)
print(resultado)  # Debería imprimir "La habitación ya está reservada en esta fecha."

resultado = hacer_reserva(reservas, "2024-08-17", "Carlos", 101, 160)
print(resultado)  # Debería imprimir "Reserva realizada con éxito."

print(reservas)
