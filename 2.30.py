def configurar_perfiles(usuarios, **kwargs):
    perfiles = {}
    
    configuraciones = [f"{clave}={valor}" for clave, valor in kwargs.items()]
    
    for usuario in usuarios:
        perfiles[usuario] = configuraciones
    
    return perfiles

usuarios = ["Ana", "Luis", "María"]

configuraciones_perfiles = configurar_perfiles(
    usuarios, 
    idioma="es", 
    modo_oscuro=True, 
    notificaciones=False
)

print(configuraciones_perfiles)
