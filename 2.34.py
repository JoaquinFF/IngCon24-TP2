from collections import Counter

def analizar_encuestas(encuestas):
    resultados_frecuencia = {}
    
    for pregunta, respuestas in encuestas.items():
        frecuencia = Counter(respuestas)
        resultados_frecuencia[pregunta] = dict(frecuencia)
    
    return resultados_frecuencia

encuestas = {
    "¿Cómo califica el servicio?": [5, 4, 5, 3, 5, 4],
    "¿Recomendaría nuestro producto?": [1, 1, 0, 1, 1, 0]
}

frecuencias = analizar_encuestas(encuestas)

print(frecuencias)
