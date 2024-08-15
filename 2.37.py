def analizar_tendencias(hashtags, tendencias, umbral):
    frecuencia_hashtags = {}
    for hashtag in hashtags:
        if hashtag in frecuencia_hashtags:
            frecuencia_hashtags[hashtag] += 1
        else:
            frecuencia_hashtags[hashtag] = 1
    
    tendencias_dict = dict(tendencias)
    
    hashtags_frecuentes = [hashtag for hashtag, frecuencia in frecuencia_hashtags.items()
                           if hashtag in tendencias_dict and tendencias_dict[hashtag] > umbral]
    
    return hashtags_frecuentes

hashtags = ["#verano", "#moda", "#viajes", "#verano", "#moda", "#tecnologia"]
tendencias = [("#verano", 120), ("#moda", 80), ("#tecnologia", 150)]
umbral = 100

hashtags_filtrados = analizar_tendencias(hashtags, tendencias, umbral)

print(hashtags_filtrados)
