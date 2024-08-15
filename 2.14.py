def analizar_temperaturas(temperaturas):
    temperatura_media = sum(temperaturas) / len(temperaturas)
    
    temperatura_maxima = max(temperaturas)
    temperatura_minima = min(temperaturas)
    
    return temperatura_media, temperatura_maxima, temperatura_minima


temperaturas = [22.5, 23.0, 21.0, 19.5, 25.0, 26.5, 24.0]

media, maxima, minima = analizar_temperaturas(temperaturas)

# Imprimir los resultados
print(f"Temperatura media: {media:.2f}°C")
print(f"Temperatura máxima: {maxima}°C")
print(f"Temperatura mínima: {minima}°C")
