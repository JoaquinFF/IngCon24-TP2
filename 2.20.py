def configurar_app(**kwargs):
    configuraciones = {
        'modo_oscuro': False,
        'idioma': 'en',
        'notificaciones': True,
    }
    
    configuraciones.update(kwargs)
    
    return configuraciones

config = configurar_app(modo_oscuro=True, idioma="es", notificaciones=False)

print(config)
