def actualizar_suscripcion(suscripciones, usuario, suscripcion, **kwargs):
    if usuario not in suscripciones:
        suscripciones[usuario] = []
    
    suscripciones[usuario].append(suscripcion)
    
    if kwargs:
        print(f"Opciones adicionales para {usuario}: {kwargs}")
    
    return suscripciones

suscripciones = {
    "Jose": ["mensual", "anual"],
    "Ana": ["mensual"]
}

estado_actual = actualizar_suscripcion(suscripciones, usuario="Luis", suscripcion="mensual", auto_renovacion=True)

print(estado_actual)
