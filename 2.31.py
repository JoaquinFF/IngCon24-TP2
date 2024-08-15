def publicar(nombre_usuario, texto_publicacion, **kwargs):
    detalles_publicacion = {
        'usuario': nombre_usuario,
        'texto': texto_publicacion,
        'etiquetas': kwargs.get('etiquetas', []),
        'visibilidad': kwargs.get('visibilidad', 'privada'),
        'likes': kwargs.get('likes', 0)
    }
    return detalles_publicacion

publicacion = publicar(
    "Juan", 
    "Mi primer post!", 
    etiquetas=["#hola", "#primerPost"], 
    visibilidad="publica", 
    likes=100
)

print(publicacion)
