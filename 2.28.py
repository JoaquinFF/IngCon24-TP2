def libros_posteriores_a_2000(biblioteca):
    libros_recientes = [
        titulo for titulo, info in biblioteca.items() if info['año'] > 2000
    ]
    return libros_recientes

biblioteca = {
    "El señor de los anillos": {"autor": "J.R.R. Tolkien", "año": 1954, "género": "Fantasía"},
    "Cien años de soledad": {"autor": "Gabriel García Márquez", "año": 1967, "género": "Realismo mágico"},
    "El código Da Vinci": {"autor": "Dan Brown", "año": 2003, "género": "Suspenso"}
}

libros_recientes = libros_posteriores_a_2000(biblioteca)

print(libros_recientes)
