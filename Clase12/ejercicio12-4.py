# comparaciones_ordenamiento.py
# Ejercicio 12.4: experimento con 3 métodos

import random

# generar lista
def generar_lista(N):
    lista = [0] * N
    for i in range(N):
        lista[i] = random.randint(0, 1000)
    return lista


# -------------------------------- #
# ordenamiento por selección


def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
    Pre: los elementos de la lista deben ser comparables.
    Post: la lista está ordenada."""
    # posición final del segmento a tratar
    n = len(lista) - 1
    # mientras haya al menos 2 elementos para ordenar
    contador = 0
    while n > 0:
        # posición del mayor valor del segmento
        p = buscar_max(lista, 0, n)
        contador += n - 0
        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        # reducir el segmento en 1
        n = n - 1
    return contador


def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
    lista de elementos comparables.
    La lista no debe ser vacía.
    a y b son las posiciones inicial y final del segmento"""

    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max


# -------------------------------- #
# ordenamiento por inserción


def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
    Pre: los elementos de la lista deben ser comparables.
    Post: la lista está ordenada."""
    contador = 0
    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            reubicar(lista, i + 1)
            contador += i + 1
    return contador


def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
    dentro del segmento [0:p-1].
    Pre: p tiene que ser una posicion válida de lista."""
    v = lista[p]
    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1
    lista[j] = v


# -------------------------------- #
# ordenamiento por burbujeo


def ord_burbujeo(lista):
    cambio = None
    n = len(lista)
    contador = 1
    while cambio != True:
        contador += 1
        cambio = True
        for i in range(1, n):
            if lista[i - 1] > lista[i]:
                lista[i - 1], lista[i] = lista[i], lista[i - 1]
                cambio = False
    return contador


# experimento
def experimento(N, k):
    sum_sel = 0
    sum_ins = 0
    sum_bur = 0
    for i in range(k):
        lista = generar_lista(N)
        sel = ord_seleccion(lista.copy())
        ins = ord_insercion(lista.copy())
        bur = ord_burbujeo(lista.copy())
        sum_sel += sel
        sum_ins += ins
        sum_bur += bur
    return (sum_sel / k, sum_ins / k, sum_bur / k)
