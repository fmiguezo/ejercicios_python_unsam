# Ejercicio 6.14: Búsqueda binaria


def busqueda_binaria(lista, x):
    """Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x esta en lista
    """
    pos = -1  # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == x:
            pos = medio  # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1  # descarto mitad derecha
        else:  # if lista[medio] < x:
            izq = medio + 1  # descarto mitad izquierda
    return pos


def donde_insertar(lista, x):
    pos = busqueda_binaria(lista, x)
    if pos != -1:
        return pos
    else:
        izq = 0
        der = len(lista) - 1
        while izq <= der:
            medio = (izq + der) // 2
            if lista[medio] > x:
                der = medio - 1  # descarto mitad derecha
                if der >= medio:
                    pos = der
                else:
                    pos = medio
            else:  # if lista[medio] < x:
                izq = medio + 1  # descarto mitad izquierda
                if izq <= medio:
                    pos = medio
                else:
                    pos = izq
    return pos


donde_insertar([0, 2, 4, 6], 3)
