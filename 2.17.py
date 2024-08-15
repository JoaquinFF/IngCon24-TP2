def filtrar_empleados_por_salario(empleados, salario_minimo):
    empleados_filtrados = {}
    
    for id_empleado, datos in empleados.items():
        nombre, edad, salario = datos
        if salario > salario_minimo:
            empleados_filtrados[id_empleado] = datos
    
    return empleados_filtrados

empleados = {
    1: ("Ana", 30, 3000),
    2: ("Luis", 25, 2500),
    3: ("María", 35, 4000)
}

empleados_filtrados = filtrar_empleados_por_salario(empleados, 3000)

print(empleados_filtrados)
