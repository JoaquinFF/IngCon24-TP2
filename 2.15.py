def calcular_promedio(*args):
    promedio = sum(args) / len(args)
    return promedio

promedio = calcular_promedio(85, 90, 78, 92)

print(f"El promedio de las notas es: {promedio:.2f}")
